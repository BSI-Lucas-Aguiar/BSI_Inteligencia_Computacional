# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Exercicio01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    filme_name = scrapy.Field()
    filme_direcao = scrapy.Field()

    pass
