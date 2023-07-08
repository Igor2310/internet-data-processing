import scrapy
from items import CastoramaItem
from scrapy.loader import ItemLoader


class Castorama(scrapy.Spider):
    name = "castorama"
    allowed_domains = ["castorama.ru"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://www.castorama.ru/{kwargs.get('search')}"]

    def parse(self, response):
        links = response.xpath("//div[@class='category-products']//a[@class='product-card__img-link']")
        for link in links:
            yield response.follow(link, callback=self.castorama_parse)
        next_page = 'https://www.castorama.ru/'+response.xpath("//a[@class='next i-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def castorama_parse(self, response):
        loader = ItemLoader(item=CastoramaItem(), response=response)
        loader.add_value('_id', response.url)
        loader.add_xpath('name', "//h1/text()")
        loader.add_value('link', response.url)
        loader.add_xpath('price', "(//div[@class='current-price']//span[@class='price']/span/span/text())[1]")
        loader.add_xpath('photos', "//div[@class='product-media']//div[@class='js-zoom-container']/img/@data-src")
        yield loader.load_item()
