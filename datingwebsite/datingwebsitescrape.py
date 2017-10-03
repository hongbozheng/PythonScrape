# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys

sys.path.append("/usr/local/lib/python2.7/site-packages")
import requests
import os
from datetime import datetime as dt
from bs4 import BeautifulSoup

start_page = 97
end_page = 109
s_age = 0
e_age = 0
s_state = 0
folder = 'AsiandateGirlsThailand'
index = 10109
uniqueIndex = 1336


def count(start=0, step=1):
    n = start
    i = 0
    pages = end_page - start_page
    while i <= pages:
        yield n
        n += step
        i += 1


def getUrls():
    url = "https://www.asiandate.com/Pages/Search/SearchResults.aspx?age_min=18&age_max=99&countryID=1000257&sortBy=4&pageNum={pn}"
    urls = (url.format(pn=x) for x in count(start=start_page, step=1))
    return urls


dirpath = '/Users/danny/Desktop/MultifacesForOnePerson/' + folder

if not os.path.isdir(dirpath):
    os.mkdir(dirpath)


def postSearchform(session, state):
    print "state: ", state
    searchURL = "https://www.ourtime.com/v3/search/processlegacyasync"
    searchpayload = {

    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    }

    # searchP = c.post(searchURL, data=searchpayload, headers=headers)
    # print "searchP: ",searchP

def downloadImageByUrl(pic_url):
    print 'Downloading imageNum: {0}, address:{1} to {2}, uniqueFaceNum: {3}'.format(
        str(index), str(
            pic_url), folder,  str(
            uniqueIndex))
    try:
        res = requests.get(pic_url, timeout=10)
        if str(res.status_code)[0] == "4":
            print("Fail download: ", pic_url)
    except Exception as inst:
        print("Fail download2: ", pic_url)
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)
    else:
        filename = os.path.join(dirpath, str(index) + '-' + name + '-' + str(uniqueIndex) + ".jpg")
        with open(filename, 'wb') as f:
            f.write(res.content)


with requests.Session() as c:
    LOGIN_URL = "https://www.asiandate.com/Pages/Security/Login.aspx?logout=1"

    # html = c.get(LOGIN_URL)
    # soup = BeautifulSoup(html.content, 'html.parser')
    payload = {
        "ctl00$ucContent$cntrlLogin$txtBoxLogin": "dannyzhengtest@gmail.com",
        "ctl00$ucContent$cntrlLogin$txtBoxPassword": "zheng123456",
        "ctl00$ucContent$cntrlLogin$btnLogin": "Login"
    }
    p = c.post(LOGIN_URL, data=payload)
    print "loginpost: ",p

    start_time = dt.now()


    urls = getUrls()
    for url in urls:
        print '************************newpage***************************'
        print 'url: ' + str(url)

        page = c.get(url)
        soupPage = BeautifulSoup(page.content, 'html.parser')

        ladys = soupPage.findAll('a',{'class':'b'})
        print len(ladys)
        # print photolist
        for lady in ladys:
            href = lady['href']
            print 'ladynameid: ' + href
            strs = href.split('/')
            nameid = strs[3][:-4]
            name = nameid[:-8]
            idstr = nameid[-7:]
            profile_url = 'https://www.asiandate.com/pages/lady/profile/profilepreview.aspx?LadyID=' + idstr
            print 'profile_url: ' + profile_url
            profilep = c.get(profile_url)
            profilesoup = BeautifulSoup(profilep.content,'html.parser')
            photolist = profilesoup.select('.thumbnail')
            for img in photolist:
                pic_url = img['href']
                if 'http' not in pic_url:
                    continue
                downloadImageByUrl(pic_url)
                index += 1

            uniqueIndex +=1

print "Finish date :", dt.now(), "Images: ", index
print "time used :", dt.now() - start_time
