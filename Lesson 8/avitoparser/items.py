# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Compose

def clean_price(value):
    new_value = value.replace('\xa0', '')
    try:
        new_value = int(new_value)
    except:
        pass
    return new_value

def update_id(id):
    return id.split('/')[-1]




class AvitoparserItem(scrapy.Item):
    _id = scrapy.Field(output_processor=TakeFirst(),input_processor=MapCompose(update_id))
    name = scrapy.Field(output_processor=TakeFirst())
    link = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(clean_price))
    description = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(output_processor=TakeFirst())
    pass
