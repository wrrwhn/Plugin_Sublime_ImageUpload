
# import sublime*
import sublime

# system or core
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import uuid
from os import path, remove


# method
def upload(local_file_path, upload_file_name=None, is_delete= True):
	'''local_file_path = local file path'''

	# read settings
	json= sublime.load_settings("ImageUpload.sublime-settings")
	access_key = json.get("access_key")
	secret_key = json.get("secret_key")
	def_host= json.get("def_host")
	bucket_name = json.get("bucket_name")

	# auth
	q = Auth(access_key, secret_key)

	# init
	file_basename, file_extension= path.splitext(local_file_path)

	# save name
	if not upload_file_name:
		key = str(uuid.uuid1())+ file_extension
	else:
		tmp_basename, tmp_extension= path.splitext(upload_file_name)
		key = tmp_basename+ file_extension

	# upload
	token = q.upload_token(bucket_name, key, 3600)
	ret, info = put_file(token, key, local_file_path)

	# check delete
	if is_delete:
		remove(local_file_path)

	return def_host+ key
