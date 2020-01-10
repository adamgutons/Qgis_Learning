import os
from qgis.core import *
from osgeo import ogr

"""
driver = ogr.GetDriverByName("OpenFileGDB")

ds = driver.Open("/home/bedevere/Qgis_Python/RH_SampleData.gdb", 0)

print ds.GetLayerCount()

for i in range(ds.GetLayerCount()):
	lyr = ds.GetLayerByIndex(i)
	ds.CopyLayer(lyr, str(i))
	del lyr
"""

#### This little chunk copies a file geodatabase layer out to shapefile format... #######################

QgsApplication.setPrefixPath("/usr/bin/qgis", True)

# Create a reference to the QgsApplication.  Setting the
# second argument to False disables the GUI.
qgs = QgsApplication([], False)

qgs.initQgis()

uri = "/home/bedevere/Qgis_Python/RH_SampleData.gdb|layerid=1"
layer = QgsVectorLayer(uri, "layer_name_you_like", "ogr")

if not layer.isValid():
	print "Layer failed to load!"

field_list = layer.fields()	

for f in field_list:
	# displayName() returns the field name
	print f.displayName()

_writer = QgsVectorFileWriter.writeAsVectorFormat(layer,r"/home/bedevere/Qgis_Python/hoppla_new2.shp","utf-8",None,"ESRI Shapefile")

del layer
del _writer

quit = input()

del quit

##################################################################################################################

"""
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
"""

# Finally, exitQgis() is called to remove the
# provider and layer registries from memory

qgs.exitQgis()



"""
n = QgsApplication.prefixPath()

print(QgsProject.instance().homePath())
"""