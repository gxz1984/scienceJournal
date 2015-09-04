import scrapy
from scienceJournal.items import ArticleListItem


class PaperListSpider(scrapy.spiders.Spider):
    name = "paper_list"
    allowed_domains = ["http://www.sciencedirect.com/"]
    start_urls = [
        "http://www.sciencedirect.com/science/journal/00344257/%s" % i for i in range(71, 170)
    ]

    def parse(self, response):
        for sel in response.xpath('//ol[@class="articleList results"]'):
            item = ArticleListItem()
            item['article_list'] = sel.xpath('li/ul/li/h4/a/@href').extract()
            #author = sel.xpath('p/a/text()').extract()
            #email
            #authaffli
            #articleDates
            #highlights
            #abstract

            yield item
