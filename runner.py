from scrapy.utils.reactor import install_reactor

# Устанавливаем нужный реактор до импорта Scrapy и Twisted
install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")

from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from jobparser.spiders.hhru import HhruSpider

if __name__ == '__main__':
    # Настраиваем логирование
    configure_logging()

    # Создаем процесс для запуска краулера
    process = CrawlerProcess(get_project_settings())

    # Запускаем краулер
    process.crawl(HhruSpider)
    process.start()
