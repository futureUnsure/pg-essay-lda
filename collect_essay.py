import scrapy
from links import links
import pdb
import lxml

class EssaySpider(scrapy.Spider):
    name = "essays"
    '''start_urls = [
        "http://www.paulgraham.com/articles.html"
    ]'''
    def start_requests(self):

        #links = response.xpath('//table[2]//a//@href').extract()
        #Omitting Lisp chapters
        LISP1 = "http://lib.store.yahoo.net/lib/paulgraham/acl1.txt"
        LISP2 = "http://lib.store.yahoo.net/lib/paulgraham/acl2.txt"
        if (LISP1 in links): links.remove(LISP1)
        if (LISP2 in links): links.remove(LISP2)

        for link in links:
            yield scrapy.Request('http://paulgraham.com/'+link, callback=self.parse)


    def parse(self, response):
        filename = response.url.split('/')[-1].split('.')[0] + '.txt'
        #items = response.xpath('//font/')[0].extract()
        #Remove date
        #try:
        #    del items[0]
        #except:
        #    self.log("Could not parse: {}".format(response.url))
        #text = ''.join(items)
        html_response = response.xpath('//font')[0].extract_unquoted()
        text = lxml.html.fromstring(html_response).text_content()
        with open(filename, 'w') as f:
            f.write(text)

        
