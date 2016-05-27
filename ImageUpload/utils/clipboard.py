
# import
import sys
import os
# sys.path.insert(0, os.path.dirname("C:/Python27/Lib/site-packages"))


# method
def getLocalImage():
	'''grab clipboard[0] into the temp and return the temp file path'''
	# read from file
	# imgPath= 'd:/desk/'
	# imageList= ['logo.png', 'python.gif', '547fdf5d61748.jpg']
	imgPath= 'C:/Users/Yao/Desktop/'
	imageList= ['Another.png', '006fl9Dwjw1f1txyi2j60g305o05onpd.gif', 'psb.jpg']
	return imgPath+ imageList[2]

def saveScreenShoot(file_path=None, file_name=None, file_extension=None):
	'''save screen shot to settup/ default path'''
	# import
	from ImageUpload.utils.commonUtils import formatCurTime
	from os import sep
	from PIL import Image, ImageGrab
	
	# path/ name/ extension setup
	if not file_path:
		file_path= ""
	elif not file_path.endswith(sep):
		file_path+= sep
	if not file_name:
		file_name= formatCurTime()
	if not file_extension:
		file_extension= 'jpg'
	file_path= str.format('{0}{1}.{2}', file_path, file_name, file_extension)

	# save  
	im= ImageGrab.grab()
	if isinstance(im, Image.Image):
		im.save(file_path)
		return file_path
	else:
		return None

def getClipboardImage():
	'''return path of the shoot / list or none'''
	# image
	from PIL import Image, ImageGrab
	im= ImageGrab.grabclipboard()
	if isinstance(im, Image.Image):

		# get im fromat
		# print('\t-->', im.tile)

		# tmp save
		from ImageUpload.utils.commonUtils import mkdirIfNotExists, getTmpImagePath
		tmp_path= getTmpImagePath()
		if not mkdirIfNotExists(tmp_path):
			return None

		# save & return path
		try:
			tmp_path= im.save(tmp_path)
			print(result)
		except IOError:
			tmp_path= None
		finally:
			return tmp_path

	# image path list
	elif im:
		index= 0
		for fileName in im:
			try:
				im= Image.oepn(fileName)
				index += 1
			except IOError:
				pass
		return im
	else:
		return None

def getClipboardText():
	pass


