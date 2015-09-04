import scrapy
from scienceJournal.items import SciencejournalItem
import json


class SciSpider(scrapy.spiders.Spider):
    name = "sci_journal"
    allowed_domains = ["http://www.sciencedirect.com/"]
    myjson = open('data2_utf8.json', 'r')
    urls = json.load(myjson)
    #myjson = {"article_list": ["http://www.sciencedirect.com/science/article/pii/S0034425715300602", "http://www.sciencedirect.com/science/article/pii/S0034425715300584", "http://www.sciencedirect.com/science/article/pii/S0034425715300638", "http://www.sciencedirect.com/science/article/pii/S0034425715300675", "http://www.sciencedirect.com/science/article/pii/S0034425715300729", "http://www.sciencedirect.com/science/article/pii/S0034425715300596", "http://www.sciencedirect.com/science/article/pii/S0034425715300687", "http://www.sciencedirect.com/science/article/pii/S003442571530078X", "http://www.sciencedirect.com/science/article/pii/S0034425715300730", "http://www.sciencedirect.com/science/article/pii/S0034425715300778", "http://www.sciencedirect.com/science/article/pii/S003442571530064X", "http://www.sciencedirect.com/science/article/pii/S0034425715300663", "http://www.sciencedirect.com/science/article/pii/S0034425715300651", "http://www.sciencedirect.com/science/article/pii/S0034425715300699", "http://www.sciencedirect.com/science/article/pii/S0034425715300705", "http://www.sciencedirect.com/science/article/pii/S0034425715300626", "http://www.sciencedirect.com/science/article/pii/S0034425715300766", "http://www.sciencedirect.com/science/article/pii/S0034425715300808", "http://www.sciencedirect.com/science/article/pii/S0034425715300614"]}
    start_urls = urls['article_list']

    def parse(self, response):
        item = SciencejournalItem()
        pdf_url = response.xpath('//div[@id="page-area"]/div/div/ul/li/div/a/@href').extract()
        print(pdf_url, "========================")
        item['pdf_url'] = [pdf.encode('utf-8') for pdf in pdf_url]
        for sel in response.xpath('//div[@id="centerInner"]'):
            journal_name = sel.xpath('div/div/div[@class="title"]/a/span/text()').extract()
            volume = sel.xpath('div/div/p[@class="volIssue"]/a/text()').extract()
            pages = sel.xpath('div/div/p[@class="volIssue"]/text()').extract()
            title = sel.xpath('div/h1[@class="svTitle"]/text()').extract()
            author = sel.xpath('div/ul/li/a[@class="authorName svAuthor"]/text()').extract()
            email = sel.xpath('div/ul/li/a[@class="auth_mail"]/@href').extract()
            authaffli = sel.xpath('div/ul/li/span[@id="tn0005"]/text()').extract()
            articleDates = sel.xpath('div/dl/dd[1]/text()').extract()
            #highlights
            abstract = sel.xpath('div/div/p[@id="sp0005"]/text()').extract()
            keywords = sel.xpath('div/ul[@class="keyword"]/li/span/text()').extract()

            item['journal_name'] = [j.encode('utf-8') for j in journal_name]
            item['volume'] = [v.encode('utf-8') for v in volume]
            item['pages'] = [p.encode('utf-8') for p in pages]
            item['title'] = [t.encode('utf-8') for t in title]
            item['author'] = [a.encode('utf-8') for a in author]
            item['email'] = [e.encode('utf-8') for e in email]
            item['authaffli'] = [affli.encode('utf-8') for affli in authaffli]
            item['articleDates'] = [d.encode('utf-8') for d in articleDates]
            item['abstract'] = [abstr.encode('utf-8') for abstr in abstract]
            item['keywords'] = [keyws.encode('utf-8') for keyws in keywords]
            yield item
