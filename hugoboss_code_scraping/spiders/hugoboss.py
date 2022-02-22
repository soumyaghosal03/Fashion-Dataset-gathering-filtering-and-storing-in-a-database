import scrapy
#from ..items import HbossItem


#class HugobossSpider(scrapy.Spider):
     #name = 'hugoboss'
     #allowed_domains = ['hugoboss.com/de/herren-schuhe/']
     #start_urls = start_urls = ['https://www.hugoboss.com/de/herren-schuhe/?sz=60&start=60',
       #'https://www.hugoboss.com/de/herren-schuhe/?sz=60&start=120',
       #'https://www.hugoboss.com/de/herren-schuhe/?sz=60&start=180',
       #'https://www.hugoboss.com/de/herren-schuhe/?sz=60&start=240',
       #'https://www.hugoboss.com/de/herren-schuhe/?sz=60&start=300',
      # 'https://www.hugoboss.com/de/herren-schuhe/?sz=60&start=60']

     #custom_settings = {
     #   'FEED_URI': 'tmp/shoeprojectfinal.csv'
     #}

     #def parse(self, response):
        #item = HbossItem()
        #image_urls = response.xpath('//div/@data-originalimage').extract()
        #product_title = response.xpath(
         #   '//*[@class="product-tile__productInfoWrapper product-tile__productInfoWrapper--is-small font__subline"]/text()').extract()
        #price = response.css('.product-tile__offer .price-sales::text').getall()

        #item = {}
        #item["image_urls"] = image_urls
        #item["product_title"] = product_title
        #item["price"] = price
        #yield (item)


class HugobossSpider(scrapy.Spider):
    name = 'hugoboss'
    allowed_domains = ['hugoboss.com/de/herren-schuhe/?sz=60&start=60']
    start_urls = ['https://www.hugoboss.com/de/herren-t-shirts/',
      'https://www.hugoboss.com/de/herren-t-shirts/?sz=60&start=60',
      'https://www.hugoboss.com/de/herren-t-shirts/?sz=60&start=120',
      'https://www.hugoboss.com/de/herren-t-shirts/?sz=60&start=180',
      'https://www.hugoboss.com/de/herren-t-shirts/?sz=60&start=240',
      'https://www.hugoboss.com/de/herren-t-shirts/?sz=60&start=300']


    def parse(self, response):
        #Extracting the content using css selectors
        url = response.xpath('//div/@data-mouseoverimage').extract()
        product_title = response.xpath('//*[@class="product-tile__productInfoWrapper product-tile__productInfoWrapper--is-small font__subline"]/text()').extract()
        price = response.css('.product-tile__offer .price-sales::text').getall()
        #Give the extracted content row wise
        for item in zip(url,product_title,price):
            #create a dictionary to store the scraped info
            scraped_info = {
                'URL' : item[0],
                'Product Name' : item[1].replace("\n", '').replace("von", ""),
                'Price' : item[2]
            }

            #yield or give the scraped info to scrapy
            yield scraped_info


