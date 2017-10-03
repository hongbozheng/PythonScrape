# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys

sys.path.append("/usr/local/lib/python2.7/site-packages")
import requests
import os
from datetime import datetime as dt
from bs4 import BeautifulSoup

start_page = 2
end_page = 23
country = 'Bangladesh'
folder = "afroIntroBlackGirls"
index = 1
countryCode = "BD"

def count(start=0, step=1):
    n = start
    i = 0
    pages = 1
    while i <= pages:
        yield n
        n += step
        i += 1


def getUrls():
    url= 'https://www.afrointroductions.com/en/results/search?pageno={pn}'
    # url = r"https://www.dateinasia.com/Search.aspx?pg={pn}&g=1&af=18&at=99&c=" + countryCode
    # url = r"https://www.dateinasia.com/Search.aspx?pg={pn}&g=1&af=18&at=99&c=JP"
    urls = (url.format(pn=x) for x in count(start=start_page, step=1))
    return urls

dirpath = '/Users/danny/Desktop/WesternFaces/' + folder




with requests.Session() as c:


    # urls = getUrls()
    # if not os.path.isdir(dirpath):
    #         os.mkdir(dirpath)
    #
    # start_time = dt.now()
    # for url in urls:
    #     print 'url: ' + str(url)
        url= 'https://www.afrointroductions.com/en/results/search?pageno=1'

        page = c.get(url)
        soupPage = BeautifulSoup(page.content,'html.parser')
        print soupPage
        # imgs = soupPage.findAll('img',{"alt":"S256"})
        imgs = soupPage.findAll('img', {"height": "136px"})

        print  'total images: ' + str(len(imgs))

        for img in imgs:
            pic_url = img['src']
            print 'Downloading image num: ' + str(index) + ' , address:' + str(pic_url) + ' to ' + folder
#             try:
#                 res = requests.get(pic_url, timeout=10)
#                 if str(res.status_code)[0] == "4":
#                     print("Fail download: ", pic_url)
#                     continue
#             except Exception as inst:
#                 print("Fail download2: ", pic_url)
#                 print(type(inst))  # the exception instance
#                 print(inst.args)  # arguments stored in .args
#                 print(inst)
#             filename = os.path.join(dirpath, str(index) + ".jpg")
#             with open(filename, 'wb') as f:
#                 f.write(res.content)
#                 index += 1
# print("Finish download %s images" % index)
# print "time used :", dt.now() - start_time


