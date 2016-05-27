

# get format time
def formatCurTime(time_format=None):
	'''default format = %Y%m%d%H%M%S'''
	import time
	if not time_format:
		time_format= '%Y%m%d%H%M%S'
	return time.strftime(time_format)


# mkdir if not exits
def mkdirIfNotExists(file_path):
	from os import path, makedirs
	tmp_path, tmp_file= path.split(file_path)
	if not path.exists(tmp_path):
		try:
			makedirs(tmp_path)
		except OSError:
			return False
		else:
			return True
	else:
		return True


# get template image path
def getTmpImagePath(file_name=None, file_extension=None):
	from os import getenv, path
	import uuid
	if not file_name:
		file_name= str(uuid.uuid1())
	if not file_extension:
		file_extension= 'png'
	elif not file_extension.startswith('.'):
		file_extension= '.'+ file_extension

	return getenv('APPDATA')+ path.sep+ "markdown_tmp_image"+ path.sep+ file_name+ file_extension


# check path is image
def checkImageType(path):
	if path:
		types= ['gif', 'bmp', 'jpg', 'jpeg']
		for imgType in types:
			if path.lower().endswith('.'+ imgType):
				return imgType
	return None

# check path
def checkImage(path):
	'''check image type, then if not exists then download'''
	imgType= checkImageType(path)
	if imgType:
		import os.path
		if os.path.isfile(path):
			return path
		else:
			from urllib.request import urlopen
			file_path= getTmpImagePath(file_extension=imgType)
			img = urlopen(path)
			localFile = open(file_path, 'wb')
			localFile.write(img.read())
			localFile.close()
			return file_path
	else:
		return None