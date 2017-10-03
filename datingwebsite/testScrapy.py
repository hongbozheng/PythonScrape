import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

class LoginSpider(scrapy.Spider):
    name = 'www.ourtime.com'
    start_urls=['https://www.ourtime.com/v3/login/process']

    def parse(self, response):
        print "parse"
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                "username": "rainzheng258@gmail.com",
                "password": "zheng123456",
                "FromLocation": "/v3/logout",
                "chkKeepMeLoggedIn": "true"
            },
            callback=self.after_login
        )
    def after_login(self,response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return
        else:
            return Request(url="http://www.ourtime.com//v3/profile?profile=E3DBD410C354ED6CACA0C235BB8ED21D&search=true&start=1&sortby=0#tab=photos&zoomPhoto=0",clallback=self.parse_tastpage)
            # continue scraping with authenticated session...

    def parse_tastypage(self,response):
        hxs = HtmlXPathSelector(response)
        # yum = hxs.select()
        print  hxs

if __name__ == '__main__':
   l = LoginSpider()
   # print l.parse()