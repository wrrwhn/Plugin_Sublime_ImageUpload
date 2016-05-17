
# import sublime*
import sublime, sublime_plugin
# import system or core
# import user-code

# method
def mkFormatShootImage():
	import os
	import sys
	sys.path.append(r'D:\server\python\Python33\Lib\site-packages')
	sys.path.append(r'C:\Users\Yao\AppData\Roaming\Sublime Text 3\Packages\ImageUpload')
	sys.path.append(r'C:\Users\Yao\AppData\Roaming\Sublime Text 3\Packages\ImageUpload\utils')

	from ImageUpload.utils.clipboard import getClipboardImage
	import ImageUpload.utils.upload as uploader

	tmp_path= getClipboardImage()
	if tmp_path:
		qiniu_url= uploader.upload(tmp_path, is_delete= True)
		return qiniu_url
	else:
		return 'None'

def mkFormatFullScreen():
	import os
	import sys
	sys.path.append(r'D:\server\python\Python33\Lib\site-packages')
	sys.path.append(r'C:\Users\Yao\AppData\Roaming\Sublime Text 3\Packages\ImageUpload')
	sys.path.append(r'C:\Users\Yao\AppData\Roaming\Sublime Text 3\Packages\ImageUpload\utils')

	from ImageUpload.utils.clipboard import saveScreenShoot
	import ImageUpload.utils.upload as uploader

	tmp_path= saveScreenShoot()
	if tmp_path:
		qiniu_url= uploader.upload(tmp_path, is_delete= True)
		return qiniu_url
	else:
		return 'None'


# class for sublime
class ShootImageUploadCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		formatUrl= mkFormatShootImage()
		sublime.set_clipboard(formatUrl)
		self.view.insert(edit, self.view.sel()[0].begin(), formatUrl)

class ShootImageUploadMarkdownCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		formatUrl= mkFormatShootImage()
		sublime.set_clipboard(formatUrl)
		if formatUrl:
			from ImageUpload.utils.format import format_markdown_img
			formatUrl= format_markdown_img(formatUrl)
		self.view.insert(edit, self.view.sel()[0].begin(), formatUrl)

class FullScreenUploadCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		formatUrl= mkFormatFullScreen()
		sublime.set_clipboard(formatUrl)
		self.view.insert(edit, self.view.sel()[0].begin(), formatUrl)

class FullScreenUploadMarkdownCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		formatUrl= mkFormatFullScreen()
		if formatUrl:
			from ImageUpload.utils.format import format_markdown_img
			formatUrl= format_markdown_img(formatUrl)
		sublime.set_clipboard(formatUrl)
		self.view.insert(edit, self.view.sel()[0].begin(), formatUrl)