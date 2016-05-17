

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