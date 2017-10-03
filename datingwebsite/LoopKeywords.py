# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys

sys.path.append("/usr/local/lib/python2.7/site-packages")
import requests
import os
from datetime import datetime as dt
from bs4 import BeautifulSoup

start_page = 1
end_page = 50
country = 'Ethiopia'
# folder = 'afroIntroBlackGirls' + country
folder = 'afroIntroBlackMan'
index = 1923
countryCode = "132"

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
    url= 'https://www.afrointroductions.com/en/results/search?pageno={pn}'
    urls = (url.format(pn=x) for x in count(start=start_page, step=1))
    return urls

dirpath = '/Users/danny/Desktop/WesternFaces/' + folder

# dirpath = '/Users/danny/PycharmProjects/spider/' + 'asiandatetop1000girls'


def getUrlsByKeywords(cc,index):
    c = requests.Session()

    LOGIN_URL ="https://www.afrointroductions.com/logon_do.cfm?cmloc=en"
    html = c.get(LOGIN_URL)
    soup = BeautifulSoup(html.content,'html.parser')
    # authenticity_token = soup.find('meta',{"name":"csrf-token"})['content']
    # print '**************',authenticity_token
    # payload = {
    #     "authenticity_token": authenticity_token,
    #     "user[email]": "dannyzhengtest2@gmail.com",
    #     "user[password]": "zheng123456",
    #     "user[remember_me]":"0",
    #     "user[remember_me]":"1",
    #     "commit": "Login"
    # }
    payload = {
        "Email": "dannyzhengtest@gmail.com",
        "password": "zheng123456",
    }

    p = c.post(LOGIN_URL,data=payload)

    search_url= "https://www.afrointroductions.com/en/results/search?searchtype=1"
    searchPayload= {
        "resulttype": "advanced",
        "gender": "254",
        "gender_w": "253",
        "age_min": "21",
        "age_max": "99",
        "countryLive": cc,
        "stateLive": "-1",
        "distanceUnit": "miles",
        "cityLive": "-1",
        "countrySearchType": "1",
         "hasPhoto": "1",
         "lastActive": "-1",
         "searchingFor": "711" ,
         "sortBy": "2",
    }
    searchP = c.post(search_url, data=searchPayload)
    urls = getUrls()
    if not os.path.isdir(dirpath):
            os.mkdir(dirpath)

    for url in urls:
        print 'url: ' + str(url)

        page = c.get(url)
        soupPage = BeautifulSoup(page.content,'html.parser')
        # imgs = soupPage.findAll('img',{"alt":"S256"})
        # imgs = soupPage.findAll('img', {"class": "responsive-image"})
        imgs = soupPage.findAll('img', {"height": "136px"})

        print  'total images: ' + str(len(imgs))
        for img in imgs:
            pic_url = img['src']
            # if ".jpg" not in pic_url:
            #     pic_url = img['data-src']
            print 'Downloading image num: ' + str(index) + ' , address:' + str(pic_url) + ' to ' + folder +  ' keyword: ' + keyword
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

start_time = dt.now()

keywords = ['108','67','86','81','114','132','157','189','218','219','223']

i = 0
for keyword in keywords:
    print 'keyword: ', keyword
    index = 1000*i + 996
    getUrlsByKeywords(keyword,index)
    i += 1

# print("Finish download %s images" % index)
print "time used :", dt.now() - start_time


