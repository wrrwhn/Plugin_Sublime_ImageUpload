
# 功能描述
- 流程
	- 使用截图工具截图
	- 切换至 sublime 3，并操作快捷键 [ctrl+ shift+ alt+ v]
	- 当前焦点处插入 `![fileName.png](qiniu.url/fileName.png)`
	- 并于剪贴板中插入文本 `qiniu.url/fileName.png`
- 限制
	- 限于 Windows 平台


# 使用
## 安装软件
- python 3.3 
	- 建议与 sublime 3 内置版本一致
	- 曾遇到过本地运行良好，搞到 sublime 中无法运行，就是忽略了 sublime 运行时是使用内置 python 运行的情况
- `pip install Pillow==2.7 `
	- 最新版本会出现获取截图文件异常情况
	- 所用功能仅于 Windows 环境可用
- `pip install qiniu`

## 拷贝程序
- 命令中运行 %appdata%
，并进入 Sublime Text 3\Packages
- 将 ImageUpload 文件夹拷贝至其中

## 快捷键
- 点击 Preferences/ `Key Bindings - User`
- 插入
```
[
	{ "keys": ["ctrl+alt+shift+v"], "command": "shoot_image_upload_markdown" }
]
```

## qiniu 配置
- 命令中运行 %appdata%，并进入 Sublime Text 3\Installed Packages
- 将 ImageUpload.sublime-settings 文件拷贝至其中
- 于其中修改对应个人 qiniu 服务配置

## 重启 Sublime 3
- 注：所谓的重启，即关闭再重新打开即可


# 参考
- http://blog.hickwu.com/sublime%E6%8F%92%E4%BB%B6%E5%BC%80%E5%8F%91%E6%89%8B%E8%AE%B0
- http://mux.alimama.com/posts/549#sublime.View
- http://www.sublimetext.com/docs/plugin-examples
