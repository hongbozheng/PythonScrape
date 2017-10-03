# from scrapy.spiders.init import InitSpider
# from scrapy.http import Request, FormRequest
# # from scrapy.linkextractors.sgml import SgmlLinkExtractor
# from scrapy.spiders import Rule
#
# class MySpider(InitSpider):
#     name = 'myspider'
#     allowed_domains = ['www.ourtime.com']
#     login_page = 'https://www.ourtime.com/v3/login/process'
#     start_urls = ['http://www.ourtime.com//v3/profile?profile=E3DBD410C354ED6CACA0C235BB8ED21D&search=true&start=1&sortby=0#tab=photos&zoomPhoto=0',
#                   ]
#
#     # rules = (
#     #     Rule(SgmlLinkExtractor(allow=r'-\w+.html$'),
#     #          callback='parse_item', follow=True),
#     # )
#
#     def init_request(self):
#         """This function is called before crawling starts."""
#         print "init_request"
#         return Request(url=self.login_page, callback=self.login)
#
#     def login(self, response):
#         """Generate a login request."""
#         print "login"
#         return FormRequest.from_response(response,
#                     formdata={  "username": "rainzheng258@gmail.com",
#                                 "password": "zheng123456",
#                                 "FromLocation": "/v3/logout",
#                                 "chkKeepMeLoggedIn": "true",
#                             },
#                     callback=self.check_login_response)
#
#     def check_login_response(self, response):
#         """Check the response returned by a login request to see if we are
#         successfully logged in.
#         """
#         print "check_login_response"
#         if "Conniezheng" in response.body:
#             # self.log("Successfully logged in. Let's start crawling!")
#             print "Successfully logged in. Let's start crawling!"
#             # Now the crawling can begin..
#             self.initialized()
#         else:
#             self.log("Bad times :(")
#             print "bad times"
#             # Something went wrong, we couldn't log in, so nothing happens.
#
#
# if __name__ == '__main__':
#
#    s =  MySpider()
#    s.init_request()
#    s.parse()
#    print s.name



import scrapy

class MySpider(scrapy.Spider):

    name = 'myspider'
    start_urls = ['http://scrapinghub.com']

    def parse(self, response):
        print "parse"
        self.logger.info('Parse function called on %s', response.url)

if __name__ == '__main__':
  m = MySpider()
  print m.name
