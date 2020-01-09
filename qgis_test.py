import os
from qgis.core import *
from osgeo import ogr

print os.getcwd()

driver = ogr.GetDriverByName("OpenFileGDB")

ds = driver.Open("/home/bedevere/Qgis_Python/RH_SampleData.gdb", 0)

print ds.GetLayerCount()

for i in range(ds.GetLayerCount()):
	lyr = ds.GetLayerByIndex(i)
	ds.CopyLayer(lyr, str(i))
	del lyr

"""
QgsApplication.setPrefixPath("/usr/bin/qgis", True)

# Create a reference to the QgsApplication.  Setting the
# second argument to False disables the GUI.
qgs = QgsApplication([], False)

qgs.initQgis()

path_to_ports_layer = os.path.join("/home", "bedevere", "Qgis_Python", "Sample_Data", "exercise_data", "projected_data", "farms_33S.shp")

vlayer = QgsVectorLayer(path_to_ports_layer, "Ports layer", "ogr")

if not vlayer.isValid():
	print "Layer failed to load!"

# return a container of QgsField objects for a vector layer.
field_list = vlayer.fields()

print field_list 

for f in field_list:
	# displayName() returns the field name
	print f.displayName()

# deleting the reference stopped the seg fault error...
del vlayer


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory

qgs.exitQgis()
"""



"""
n = QgsApplication.prefixPath()

print(QgsProject.instance().homePath())
"""