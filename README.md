# moedict
适用于Gboard的某二次元（？）百科网站词库（自定义短语）

## 使用

### 方法一：导入zip
* 在release下载最新的`gboard.zip`
* 打开Gboard设置-词典-个人词典-简体中文，点右上角导入，选择下载的zip文件，等待导入完成

### 方法二：导入db
*本方法需要root权限，且会覆盖你现有的个人词典，请确认你只需要使用这一个词库，并有基础的linux权限、用户和组的知识*

* 在release下载最新的`PersonalDictionary.db`
* 强行停止Gboard
* 使用任意支持root的文件管理器打开`/data/data/com.google.android.inputmethod.latin/databases`
* （建议）备份现有的`PersonalDictionary.db`和`PersonalDictionary.db-journal`
* 删除`PersonalDictionary.db`和`PersonalDictionary.db-journal`，然后把你下载的`PersonalDictionary.db`复制到这个目录，参考同目录下其他文件设置权限
* 打开Gboard，重新设置其为默认输入法，打开个人词典页面检查是否成功导入

## 来源

由 https://github.com/outloudvi/mw2fcitx 提供的萌百fcitx5词库，经转换而来

## License

代码使用`Unlicense`，词库文件遵循上游许可
