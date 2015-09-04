# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SciencejournalItem(scrapy.Item):
    # define the fields for your item here like:
    journal_name = scrapy.Field()
    volume = scrapy.Field()
    pages = scrapy.Field()
    title = scrapy.Field()          # paper article
    author = scrapy.Field()         # author
    email = scrapy.Field()
    authaffli = scrapy.Field()      # affiliate to which institute or university
    articleDates = scrapy.Field()   # the paper dates
    highlights = scrapy.Field
    abstract = scrapy.Field()
    keywords = scrapy.Field()
    pdf_url = scrapy.Field()
    #pass


class ArticleListItem(scrapy.Item):
    article_list = scrapy.Field()
