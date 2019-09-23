# # if your python version <=2.7
# import urllib
#
# url = 'https://dr15.sdss.org/sas/dr15/eboss/spectro/data/57358/sdR-b1-00209282.fit.gz'
# print ("downloading with urllib")
# urllib.urlretrieve(url, "1.00209282.fit.gz")




#if your python version >=3.0
import urllib.request



url = 'https://dr15.sdss.org/sas/dr15/eboss/spectro/data/57358/sdR-b1-00209282.fit.gz'
url1='https://dr15.sdss.org/sas/dr15/eboss/spectro/data/57358/'+'sdR-b1-00209282.fit.gz'
print ("downloading with urllib")
urllib.request.urlretrieve(url1, "3.00209282.fit.gz")
