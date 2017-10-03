# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys

sys.path.append("/usr/local/lib/python2.7/site-packages")
import requests
import os
from datetime import datetime as dt
from bs4 import BeautifulSoup

start_page = 0
end_page = 115
s_age = 35
e_age = 45
s_state = 1
e_state = 52
folder = 'MatchWomanUSA' + str(s_age) + '-' + str(e_age)
index = 1


def count(start=0, step=1):
    n = start
    i = 0
    pages = end_page - start_page
    while i <= pages:
        yield n
        n += step
        i += 1


def getUrls():
    # url = r"https://www.dateinasia.com/Search.aspx?pg={pn}&g=1&af=18&at=99&c=" + countryCode
    url = "http://www.match.com/SearchReskin/Page/?lid=108&pn={pn}&sb=OriginalOrder&st=QuickSearch"
    urls = (url.format(pn=x) for x in count(start=start_page, step=1))
    return urls


dirpath = '/Users/danny/Desktop/WesternFaces/' + folder

if not os.path.isdir(dirpath):
    os.mkdir(dirpath)


def postSearchform(session, state):
    print "state: ", state
    postUrl = "http://www.match.com/SearchReskin/Refine/?lid=3"
    searchPayload = {
        "statecodes": state,
        "countrycodes": 1,
        "searchby": "1",
        "onlinenow": "0",
        "photosonly": "1",
        "m_lage_a0": s_age,
        "m_uage_a1": e_age,
        "availableforim": "0",
        "gendercode":1,
        "themrelationship": 2,
        "sortby-dd": "1",
        "searchbyrdo": "1",
        "st": "QuickSearch",
        "sb": "OriginalOrder"
    }
    searchP = session.post(postUrl, data=searchPayload)
    print searchP


with requests.Session() as c:
    url1 = "http://www.match.com/SearchReskin/?dls=1&CLR=true&cl=1&po=1&r2s=1&ggs=4&lage=25&uage=99&pc="
    c.get(url1)
    start_time = dt.now()

    for state in range(s_state, 52):
        postSearchform(c, state)

        urls = getUrls()
        for url in urls:
            print 'url: ' + str(url)

            page = c.get(url)
            soupPage = BeautifulSoup(page.content, 'html.parser')
            # imgs = soupPage.findAll('img',{"alt":"S256"})
            # imgs = soupPage.findAll('img', {"class": "responsive-image"})
            imgs = soupPage.findAll('img', {"alt": ""})

            print  'total images: ' + str(len(imgs))

            for img in imgs:
                pic_url = img['src']
                if ".jpeg" not in pic_url:
                    continue
                print 'Downloading image num: ' + str(index) + ' , address:' + str(
                    pic_url) + ' to ' + folder + ' state: '+ str(state)
                try:
                    res = requests.get(pic_url, timeout=10)
                    if str(res.status_code)[0] == "4":
                        print("Fail download: ", pic_url)
                        continue
                except Exception as inst:
                    print("Fail download2: ", pic_url)
                    print(type(inst))  # the exception instance
                    print(inst.args)  # arguments stored in .args
                    print(inst)
                filename = os.path.join(dirpath, str(index) + ".jpg")
                with open(filename, 'wb') as f:
                    f.write(res.content)
                index += 1



# print("Finish download %s images" % index)
print "end at: ", dt.now()
print "time used :", dt.now() - start_time
