# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Compose


def clean_price(value):
    new_value = value.replace(' ', '')
    try:
        new_value = int(new_value)
    except:
        pass
    return new_value

def update_id(id):
    return id.split('.ru')[1].replace('/', '')

def update_photos(photos):
    return f'https://www.castorama.ru/{photos}'

def update_name(name):
    return name.strip()


class CastoramaItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(update_id))
    name = scrapy.Field(output_processor=TakeFirst(),input_processor=MapCompose(update_name))
    link = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst(),input_processor=MapCompose(clean_price))
    photos = scrapy.Field(output_processor=TakeFirst(),input_processor=MapCompose(update_photos))


    # price = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(clean_price))
    # photos = scrapy.Field(input_processor=Compose(get_photos_list))
