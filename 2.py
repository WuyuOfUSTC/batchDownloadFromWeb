'''

1、path改成htmlDownload.py里面filename的地址
2、然后left最右边57358改成你当前要下载的目录编号
3、运行2.py
'''
import urllib.request
path='C:\\Users\\cloudfan\\PycharmProjects\\batchDownload\\1.txt'
left='https://dr15.sdss.org/sas/dr15/eboss/spectro/data/57358/'

file=open(path)
num=0
for line in file.readlines():

    key = '<tr><td><a href='
    if ((key in line)and(line[9]=='a')):
        num=num+1
        stringname=line[17:39]
        print(stringname)
        url=left+stringname
        print(url)

        urllib.request.urlretrieve(url, stringname)

file.close()