# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient, errors





class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', port=27017)
        self.mongo_base = client.vacancies191124

    def extract_salary_number(self, salary):
        if salary:
            salary = salary.replace(' ', '').replace('\xa0', '')
            try:
                return int(salary)
            except ValueError:
                print(f"Ошибка преобразования зарплаты: {salary}")
                return None


    def extract_currency(self, salary):
        if '₽' in salary:
            return 'рубль'
        elif '$' in salary:
            return 'доллар'
        elif '€' in salary:
            return 'евро'
        elif '£' in salary:
            return 'фунт'
        return None


    def process_item(self, item, spider):

        if isinstance(item.get('name'), list):
            item['name'] = ' '.join(item['name'])
        else:
            item['name'] = str(item.get('name'))

        salary = item.get('salary')
        if salary and isinstance(salary, list):
            try:
                if len(salary) >= 0 and salary[0] == 'Уровень дохода не указан':
                    item['min_salary'] = None
                    item['max_salary'] = None
                    item['currency'] = None
                    del item['salary']

                elif len(salary) >= 5 and salary[0].strip() == 'от' and salary[2].strip() == 'до':
                    item['min_salary'] = self.extract_salary_number(salary[1])
                    item['max_salary'] = self.extract_salary_number(salary[3])
                    item['currency'] = self.extract_currency(salary[5])
                    del item['salary']

                elif len(salary) >= 3 and salary[0].strip() == 'от':
                    item['min_salary'] = self.extract_salary_number(salary[1])
                    item['max_salary'] = None
                    item['currency'] = self.extract_currency(salary[3])
                    del item['salary']

                elif len(salary) >= 3 and salary[0].strip() == 'до':
                    item['min_salary'] = None
                    item['max_salary'] = self.extract_salary_number(salary[1])
                    item['currency'] = self.extract_currency(salary[3])
                    del item['salary']

                collection = self.mongo_base[spider.name]
                collection.insert_one(item)
            except errors.PyMongoError as e:
                self.logger.error(f"MongoDB insert error: {e}")
            except Exception as e:
                self.logger.error(f"Error processing item: {e}")
            except ValueError as e:
                print(f"Ошибка при обработке значений зарплаты: {e}")


        return item




        



