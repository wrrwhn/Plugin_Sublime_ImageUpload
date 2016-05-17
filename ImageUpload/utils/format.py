from os import path

def format_markdown_img(url, key=None):
	formmat_str= "![{key}]({url})"
	if not key:
		key= path.basename(url)
	return formmat_str.format(key=key, url= url)