import os
from qgis.core import *
from osgeo import ogr


def copy_shps():

	input_gdb = raw_input("File geodatabase >> ")
	output_folder = raw_input("Shapefile folder >> ")

	print input_gdb


	QgsApplication.setPrefixPath("/usr/bin/qgis", True)

	# Create a reference to the QgsApplication.  Setting the
	# second argument to False disables the GUI.
	qgs = QgsApplication([], False)

	qgs.initQgis()


	driver = ogr.GetDriverByName("OpenFileGDB")

	ds = driver.Open(input_gdb)
	#ds = driver.Open("/home/bedevere/Qgis_Python/RH_SampleData.gdb")

	layer_idxs = ds.GetLayerCount()

	#layer = ds.GetLayer()


	for lyr in range(layer_idxs):
		uri = "%s|layerid=%s" % (input_gdb, lyr)
		#uri = "/home/bedevere/Qgis_Python/RH_SampleData.gdb|layerid=%s" % lyr
		ogr_layer = ds.GetLayer(lyr)
		try:
			layer = QgsVectorLayer(uri, "layer_name_you_like", "ogr")
		except:
			print "Layer is invalid!"
		layer_name = ogr_layer.GetName()
		writer = QgsVectorFileWriter.writeAsVectorFormat(layer,r"/home/bedevere/Qgis_Python/dump/%s_%s.shp" % (layer_name, lyr),"utf-8",None,"ESRI Shapefile")
		#layer = ds.GetLayer(lyr)
		#layer_name = layer.GetName()
		#print layer_name
		del writer
		del layer
		del ogr_layer

	# it seems like deleting the driver released the segmentation fault error this time...i bet b/c it held on to the file .gdb 
	# through ogr while qgis also used the same files to createa  layer...
	del driver
	del ds

	qgs.exitQgis()

copy_shps()


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

#qgs.exitQgis()



"""
n = QgsApplication.prefixPath()

print(QgsProject.instance().homePath())
"""