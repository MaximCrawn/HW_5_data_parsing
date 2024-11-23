import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem 


class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://hh.ru/search/vacancy?text=Python&from=suggest_post&salary=&ored_clusters=true&area=113&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line"]

    def parse(self, response:HtmlResponse):

        next_page = response.xpath("//a[@data-qa = 'number-pages-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//a[@data-qa = 'serp-item__title']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response:HtmlResponse):
        name = response.xpath(".//h1//../text()").getall()
        salary = response.xpath(".//span[contains(@data-qa,'vacancy-salary') or contains(@class,'magritte-text_typography')]/text()").getall()
        url = response.url
        yield JobparserItem(name=name, salary=salary, url=url)
