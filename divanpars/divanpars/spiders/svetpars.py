import scrapy



class SvetparsSpider(scrapy.Spider):
    name = "svetpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]
    # start_urls - это та ссылка, от которой начинается парсинг
    def parse(self, response):
        svetilniki = response.css('div._Ud0k')
        for svetilnik in svetilniki:
            yield {
                'name': svetilnik.css('div.lsooF span::text').get(),
                'price': svetilnik.css('div.pY3d2 span::text').get(),
                'url': svetilnik.css('a').attrib['href']
            }