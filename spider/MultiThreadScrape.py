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
end_page = 43
s_age = 66
e_age = 70
s_state = 48
folder = 'OurTimeUSAWoman' + str(s_age) + '-' + str(e_age)
index = 69240
uniqueIndex = 20541
states = [ "US-AK", "US-AL",
                      "US-AR",
                      "US-AS",
                      "US-AZ",
                      "US-CA",
                      "US-CO",
                      "US-CT",
                      "US-DC",
                      "US-DE",
                      "US-FL",
                      "US-GA",
                      "US-GU",
                      "US-HI",
                      "US-IA",
                      "US-ID",
                      "US-IL",
                      "US-IN",
                      "US-KS",
                      "US-KY",
                      "US-LA",
                      "US-MA",
                      "US-MD",
                      "US-ME",
                      "US-MI",
                      "US-MN",
                      "US-MO",
                      "US-MS",
                      "US-MT",
                      "US-NC",
                      "US-ND",
                      "US-NE",
                      "US-NH",
                      "US-NJ",
                      "US-NM",
                      "US-NV",
                      "US-NY",
                      "US-OH",
                      "US-OK",
                      "US-OR",
                      "US-PA",
                      "US-PR",
                      "US-RI",
                      "US-SC",
                      "US-SD",
                      "US-TN",
                      "US-TX",
                      "US-UT",
                      "US-VA",
                      "US-VI",
                      "US-VT",
                      "US-WA",
                      "US-WI",
                      "US-WV",
                      "US-WY"]

e_state = len(states)

def count(start=0, step=1):
    n = start
    i = 0
    pages = end_page - start_page
    while i <= pages:
        yield n
        n += step
        i += 1


def getUrls():
    url = "https://www.ourtime.com/v3/search/results?start={pn}&sortCol=MyDefault&DisplayResultsStyle=true"
    urls = (url.format(pn=x) for x in count(start=start_page, step=1))
    return urls


dirpath = '/Users/danny/Desktop/MultifacesForOnePerson/' + folder

if not os.path.isdir(dirpath):
    os.mkdir(dirpath)


def postSearchform(session, state):
    print "state: ", state
    searchURL = "https://www.ourtime.com/v3/search/processlegacyasync"
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
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    }

    searchP = c.post(searchURL, data=searchpayload, headers=headers)
    print "searchP: ",searchP

def downloadImageByUrl(pic_url,uniqueIndex):
    print 'Downloading imageNum: {0}, address:{1} to {2}, state: {3}, statenum: {4}, uniqueFaceNum: {5}'.format(
        str(index), str(
            pic_url), folder, state, str(stateN), str(
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
        filename = os.path.join(dirpath, str(index) + '-' + name + '-' + state + '-'+ str(uniqueIndex) + ".jpg")
        with open(filename, 'wb') as f:
            f.write(res.content)


with requests.Session() as c:
    LOGIN_URL = "https://www.ourtime.com/v3/login/process"

    # html = c.get(LOGIN_URL)
    # soup = BeautifulSoup(html.content, 'html.parser')
    payload = {
        "username": "dannyzhengtest@gmail.com",
        "password": "zheng123456",
        "FromLocation": "/v3/logout",
        "chkKeepMeLoggedIn": "true"
    }
    p = c.post(LOGIN_URL, data=payload)
    print "loginpost: ",p

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
                a = div.find('a')
                profileurl = 'https://www.ourtime.com/' + a['href']
                name = a.string
                print name

                userPhotoDiv = div.find('div',{"class":"userphoto"})
                img = userPhotoDiv.find('img')
                imgurl = img['src']
                if userPhotoDiv.find('div',{"class":"photo-count"}):
                    page = c.get(profileurl).content
                    pic_urls = re.findall('"PhotoUrl":"(.*?)",', page, re.S)
                    print  "profile url: ", profileurl, " photos: ", len(pic_urls)
                    for pic_url in pic_urls:
                        downloadImageByUrl(pic_url,uniqueIndex)
                        index += 1
                else:
                    downloadImageByUrl(imgurl,uniqueIndex)
                    index += 1

                uniqueIndex +=1

print "Finish date :", dt.now(), "Images: ", index
print "time used :", dt.now() - start_time
