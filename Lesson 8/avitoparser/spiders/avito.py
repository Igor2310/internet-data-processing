from scrapy import Request
import scrapy
from scrapy_splash import SplashRequest
from items import AvitoparserItem
from scrapy.loader import ItemLoader


class AvitoSpider(scrapy.Spider):
    name = 'avitoparser'
    allowed_domains = ["avito.ru"]
    start_urls = ["https://www.avito.ru/all?q=%D0%BA%D0%BE%D1%82%D1%8F%D1%82%D0%B0"]

    def start_requests(self):
        if not self.start_urls and hasattr(self, "start_url"):
            raise AttributeError(
                "Crawling could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)"
            )
        for url in self.start_urls:
            yield SplashRequest(url)

    def parse(self, response):
        links = response.xpath("//h3[@itemprop='name']/../@href").getall()  # Извлекаем ссылку до конца
        for link in links:
            yield SplashRequest("https://avito.ru" + link, callback=self.parse_ads, args={'wait': 0.5})

    def parse_ads(self, response):
        loader = ItemLoader(item=AvitoparserItem(), response=response)
        loader.add_value('_id', response.url)
        loader.add_xpath('name', "//span[@class='title-info-title-text']/text()")
        loader.add_value('link', response.url)
        loader.add_xpath('price', "(//span[@data-marker='item-view/item-price']/text())[1]")
        loader.add_xpath('description',("//div[@data-marker='item-view/item-description']/p/text()"))
        loader.add_xpath('photos', "(//img)[1]/@src")
        yield loader.load_item()
