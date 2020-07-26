import Classfy
import Viewer
import Recognise

print("test 1.0.1")

#初始化爬虫的网址源码，存储为csv形式并读出
#Recognise.BeginChartReading("http://www.baidu.com")
#Viewer.PrintPatchResultBefore()
names = ''
names = input()
Recognise.BaiduPacher(names)