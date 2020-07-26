import requests
import pandas as pd
import random
import os


global line
line = 0
def BeginChartReading(url):
    print(url + "-------> Pached")
    strhtml = requests.get(url)
    strhtml.encoding='utf-8'
    print (strhtml.headers['content-type'])
    global line
    dataframe = pd.DataFrame({'url':url,'url_text':strhtml.text},index=[line])
    line=line+1
    dataframe.to_csv("PatchWebdatabin.csv",encoding='utf-8',index=False,sep=',')

def BaiduPacher(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    defSearchurl = "http://www.baidu.com/s?ie=UTF-8&wd="
    
    SearchInitUrl = defSearchurl + name                      #合成网址
    strhtml = requests.get(SearchInitUrl,headers = headers)  #请求网址内容

    strhtml.encoding='utf-8'
    print (strhtml.text)
    target_dir = "patched_html/" + name  #存储目标目录
    mkdir(target_dir)
    saveHtml("Result-" + str(random.randint(100000000,900000000)),strhtml.text,target_dir)
    
    return

def BingPacher(name):
    return

def Search360Pacher(name):
    return

def OtherWebSearchPacher(name,configs,websearchurls):
    return

def PatchConfigs(config):
    return

def UpdateRecognise(UpdateConfig,urls,texts,User):
    return



def StrogeData(Mode,Charset,Text,dirs):
    return

def saveHtml(file_name,file_content,data_dir):
    b1 = bytes( file_content,encoding =  "utf8")
    with open(data_dir +file_name.replace('/','_')+'.html','wb') as f:
        f.write(b1)


def mkdir(path):                                
    nowpath = os.getcwd()
    folder = os.path.exists(nowpath +"\\"+ path)
    if not folder:                                  #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(nowpath +"\\"+ path)            #makedirs 创建文件时如果路径不存在会创建这个路径
        print ("---  new folder...  ---")
        print ("---  OK  ---")
    else:
        print ("---  There is this folder!  ---")
    
