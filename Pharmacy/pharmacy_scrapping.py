from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess
from pharmacy_clear_format import format_csv_result


class Pharmacy(Item):
    Name = Field()
    Price = Field()
    Link = Field()


class PharmacyCrawl(CrawlSpider):
    name = "Farmacias"

    #  Useragent in Scrapy
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) + \
        AppleWebKit/537.36 (KHTML, like Gecko) + \
            Chrome/139.0.7258.128 Safari/537.36",
        #  Limit the number of pages to visit.
        'CLOSESPIDER_PAGECOUNT': 20,
        'FEED_EXPORT_ENCODING': 'utf-8'
        # To display special characters.
    }

    #  To prevent getting information from another domain.
    allowed_domains = ['fahorro.com']

    start_urls = ['https://www.fahorro.com/vitaminas.html']

    download_delay = 5

    rules = (
        Rule(
            #  Defining tags and attributes where to use LinkExtractor.
            LinkExtractor(
                allow=r'p=',
                tags=('a'),
                attrs=('href'),
            ), follow=True, callback='parse_pharmacy'
        ),
    )

    #  Function to delete special characters from the product price.
    def clear_price(self, price):
        #  Replacing the characters no needed.
        new_price = price.replace('$', '')
        new_price = new_price.replace(',', '')

        if new_price[-1] == '.':
            #  if the last character from price is '.', replace.
            new_price = new_price.replace('.', '')

        return new_price

    def trim_products(self, nombre):
        #  Clean the whitespaces
        trimmed_text = nombre.strip()
        return trimmed_text

    def parse_pharmacy(self, response):
        sel = Selector(response)
        #  Tag where to search for the information of all the products.
        products = sel.xpath('//div[@class="product-item-info"]')
        for product in products:
            item = ItemLoader(Pharmacy(), product)
            # .//  Used to make relative searches.
            item.add_xpath('Name', './/strong[@class="product name product-item-name"]/a/text()', MapCompose(self.trim_products))
            item.add_xpath('Price', './/span[@class="price"]/text()',
                           MapCompose(self.clear_price))
            item.add_xpath('Link', './/a[@class="product-item-link"]/@href')

            yield item.load_item()


process = CrawlerProcess({
     'FEED_FORMAT': 'csv',
     #  Format and where to save the file with the data extracted.
     'FEED_URI': 'Nivel 2/farmacia_productos.csv'
     })

process.crawl(PharmacyCrawl)
process.start()

#  Function to clear the data extracted.
#  See pharmacy_clear_format.py to see the function details.
format_csv_result('Nivel 2/farmacia_productos.csv')
