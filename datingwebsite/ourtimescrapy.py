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
end_page = 2353
s_age = 0
e_age = 0
s_state = 0

folder = 'AsianDateGirlsChina'
index = 1
uniqueIndex = 1


def count(start=0, step=1):
    n = start
    i = 0
    pages = end_page - start_page
    while i <= pages:
        yield n
        n += step
        i += 1


def getUrls():
    url="https://www.asiandate.com/Pages/Search/SearchResults.aspx?age_min=18&age_max=99&countryID=1000113&sortBy=4&pageNum={pn}"
    urls = (url.format(pn=x) for x in count(start=start_page, step=1))
    return urls


dirpath = '/Users/danny/Desktop/MultifacesForOnePerson/blackpeoplemeet/' + folder

if not os.path.isdir(dirpath):
    os.mkdir(dirpath)


def postSearchform(session, state):
    print "state: ", state
    searchURL = "https://www.blackpeoplemeet.com/v3/search/processlegacyasync"
    searchpayload = {
         "ShowZip":"false",
         "ZipCode":"" ,
        "Location":state,
        "MinAge":s_age,
         "MaxAge":e_age,
         "MinHeight":48,
         "MaxHeight":95,
         "LookingFor":-1,
         "Status":-1,
         "Smoking":-1,
         "BodyType":-1,
         "HasPhotos":1,
         "Ethnicity":-1,
         "Religion":-1,
         "Zodiac":-1,
         "Children":-1,
         "DisplayGallery":"true",
         "Sortby":"MyDefault",
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    searchP = c.post(searchURL,data=searchpayload,headers=headers)
    print "searchP: ",searchP

def downloadImageByUrl(session,pic_url):
    print 'Downloading imageNum: {0}, address:{1} to {2}, state: {3}, statenum: {4}, uniqueFaceNum: {5}'.format(
        str(index), str(
            pic_url), folder, state, str(stateN), str(
            uniqueIndex))
    try:
        res = session.get(pic_url, timeout=10)
        if str(res.status_code)[0] == "4":
            print("Fail download: ", pic_url)
    except Exception as inst:
        print("Fail download2: ", pic_url)
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)
    else:
        filename = os.path.join(dirpath, str(index) + '-' + name + '-' + state + '-' + str(uniqueIndex) + ".jpg")
        with open(filename, 'wb') as f:
            f.write(res.content)


with requests.Session() as c:
    LOGIN_URL = "https://www.blackpeoplemeet.com/v3/login/process"

    html = c.get(LOGIN_URL)
    soup = BeautifulSoup(html.content, 'html.parser')
    payload = {
        "username": "dannyzhengtest@gmail.com",
        "password": "zheng123456",
        "FromLocation": "/v3/logout",
        "chkKeepMeLoggedIn": "true"
    }
    p = c.post(LOGIN_URL, data=payload)
    print "loginpost: ", p

    start_time = dt.now()

    for stateN in range(s_state,e_state):
        print "***************************************new " \
              "state******************************************************************* " \
              "*****************************************************************************"
        state = states[stateN]
        postSearchform(c, state)
        urls = getUrls()
        for url in urls:
            print 'url: ' + str(url) + ' statenum: ' + str(stateN)

            page = c.get(url)
            soupPage = BeautifulSoup(page.content, 'html.parser')

            divs = soupPage.findAll('div', {"class": "results-item"})
            # print divs
            print len(divs)
            for div in divs:
                # print div

                namea = div.find('a',string=True)
                name = namea.string
                print name
                ahref = div.find('a')
                img = ahref.find('img')
                imgurl = img['src']

                profileurl = 'https://www.blackpeoplemeet.com/' + ahref['href']
                overlay = div.find('div', {'class': 'overlay'})  # if multi photos
                if overlay:
                    page = c.get(profileurl).content
                    pic_urls = re.findall('"PhotoUrl":"(.*?)",', page, re.S)
                    print  "profile url: ", profileurl, " photos: ", len(pic_urls)
                    for pic_url in pic_urls:
                        pic_url = pic_url[:-4] + 't.jpg'
                        downloadImageByUrl(c, pic_url)
                        index += 1
                else:
                    downloadImageByUrl(c, imgurl)
                    index += 1

                uniqueIndex +=1

print "Finish date :", dt.now(), "Images: ", index
print "time used :", dt.now() - start_time
