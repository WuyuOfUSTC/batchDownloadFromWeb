import requests

url='https://dr15.sdss.org/sas/dr15/eboss/spectro/data/'
filename='all.txt'


def get_web_html(url):

    res = requests.get(url)
    return res.text


x = get_web_html(url)
print(type(x))
with open(filename, 'w') as f:
    f.write(x)
    f.close()

setID=[]
with open(filename,'r') as f:
    for line in f.readlines():
        key = '<tr><td><a href='
        if ((key in line) and (line[9] == 'a')):
            stringname = line[17:22]
            setID.append(int(stringname))
    f.close()
print (setID)




