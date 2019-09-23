'''
author:wuyu
data:2019/09/23
branch:dev
如果此时你要下载57358下面的所有数据，
1、修改url的后缀
2、filename随便写一个xx.txt
然后运行htmlDownload.py
然后打开2.py
'''
import requests

url='https://dr15.sdss.org/sas/dr15/eboss/spectro/data/57358/'
filename='4.txt'


def get_web_html(url):

    res = requests.get(url)
    return res.text


x = get_web_html(url)
with open(filename, 'w') as f:
    f.write(x)
    f.close()

