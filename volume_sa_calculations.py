import arcpy

arcpy.env.workspace = "G:\Lake Linganore"
arcpy.env.overwriteOutput = True

# Local Variables
volume = 'Data\Tab\Volume.csv'
LL_bathymetry = 'Data\Spatial Data\Depth\depth.gdb\IDW'

# Create List of depths to calculate volume/SA
# Depth ranges derived from min/max depths in Bathymetry raster 
depths = []
calc = 0

# Creates range of depths from 0 to 38 
while int(calc) <= 38:
    depths.append(calc)
    calc = int(calc) + 1

# Calculate Volume/SA for depths 0 to 38
for i in depths:
	
	arcpy.SurfaceVolume_3d(LL_bathymetry, volume, "ABOVE", str(i), "1", "0")
