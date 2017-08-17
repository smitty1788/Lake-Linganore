import arcpy

arcpy.env.workspace = "G:\Lake Linganore\Data\Spatial Data\Depth"
arcpy.env.overwriteOutput = True	

# Local Variables
idw_tin = 'G:\Lake Linganore\Data\Spatial Data\Depth\idw_tin'
Station_Data_Project = 'G:\Lake Linganore\Data\Spatial Data\Depth\depth.gdb\Station_Data_Project'

arcpy.env.snapRaster = "idw_tin"
arcpy.env.extent = "1220186.0169933 633391.460174471 1226567.2507933 637462.982614471"
arcpy.env.cellSize = "3.28084000000002"
arcpy.env.mask = "idw_tin"

# From Station_Data_Project shp
# List only fields related to hypoxic measurements at various dates
dates = [f.name for f in arcpy.ListFields(Station_Data_Project, 'hyp*', 'All')]


# Calculate Hypoxic volume at any particular measurment date
def hypoxic_volume(date):
	
	output_krig = 'G:\Lake Linganore\Data\Spatial Data\Depth\Scratch.gdb\krig' + str(int(filter(str.isdigit, str(date))))
	
	output_tin = output_krig + '_tin'
	
	output_dif = output_krig + '_diff'
	
	Output_variance_of_prediction_raster = ""
	Output_Raster = ""
	
	arcpy.gp.Kriging_sa(Station_Data_Project, str(date), output_krig, "Spherical 9.129743", "3.28084000000002", "VARIABLE 2", Output_variance_of_prediction_raster)
	
	arcpy.RasterTin_3d(output_krig, output_tin, "", "1500000", "1")
	
	arcpy.SurfaceDifference_3d(idw_tin, output_tin, output_dif, "0", "0", Output_Raster, "10", "", "")
	
	arcpy.AddSpatialIndex_management(output_dif)
	

# Calculate hypoxic volumes for all measurement dates 	
for j in dates:
	hypoxic_volume(j)