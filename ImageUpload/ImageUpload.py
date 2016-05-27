
# import sublime*
import sublime, sublime_plugin
# import system or core
# import user-code

# method
def mkFormatImage(path):
	import sys
	sys.path.append(r'D:\server\python\Python33\Lib\site-packages')
	sys.path.append(r'C:\Users\Yao\AppData\Roaming\Sublime Text 3\Packages\ImageUpload')
	sys.path.append(r'C:\Users\Yao\AppData\Roaming\Sublime Text 3\Packages\ImageUpload\utils')

	from ImageUpload.utils.commonUtils import checkImage	
	import ImageUpload.utils.upload as uploader
	path= checkImage(path)
	qiniu_url= 'None'

	if not path:
		from ImageUpload.utils.clipboard import getClipboardImage
		path= getClipboardImage()

	if path:
		qiniu_url= uploader.upload(path, is_delete= True)

	return qiniu_url



# class for sublime
class ScreenShotUploadMarkdownCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		path= sublime.get_clipboard()
		formatUrl= mkFormatImage(path)
		sublime.set_clipboard(formatUrl)
		if formatUrl:
			from ImageUpload.utils.format import format_markdown_img
			formatUrl= format_markdown_img(formatUrl)
		self.view.insert(edit, self.view.sel()[0].begin(), formatUrl)