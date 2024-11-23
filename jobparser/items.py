# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field()  # Название вакансии
    url = scrapy.Field()  # Ссылка на вакансию

    # Если вы хотите сохранять зарплату как целое поле
    salary = scrapy.Field()  # Зарплата

    # Поля для минимальной и максимальной зарплаты
    min_salary = scrapy.Field()  # Минимальная зарплата
    max_salary = scrapy.Field()  # Максимальная зарплата
    currency = scrapy.Field() 
