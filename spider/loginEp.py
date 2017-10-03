#!/bin/env python2
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import requests

from lxml import html

# from xml import etree

USERNAME = "<USERNAME>"
PASSWORD = "<PASSWORD>"

LOGIN_URL = "https://bitbucket.org/account/signin/?next=/"
URL = "https://bitbucket.org/dashboard/repositories"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    # tree = etree.HTML(html)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
    print authenticity_token
    # Create payload
    # payload = {
    #     "username": 'bobzheng258@gmail.com',
    #     "password": 'zheng123456',
    #     "csrfmiddlewaretoken": authenticity_token
    # }

    payload = {
        "username": "&lt;bobzheng258@gmail.com&gt;",
        "password": "&lt;zheng123456&gt;",
        "csrfmiddlewaretoken": "&lt;authenticity_token&gt;"
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    print tree
    # bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    # print(bucket_names)

if __name__ == '__main__':
    main()