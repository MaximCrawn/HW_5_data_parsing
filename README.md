# Scrapy Parser for hh.ru

Этот проект использует **Scrapy** для парсинга вакансий с сайта hh.ru (HeadHunter). Скрипт собирает информацию о вакансиях, включая название работы, зарплату и валюту, и сохраняет эти данные в базу данных MongoDB.

## Настройка

1. **Установите зависимости**:
   - Убедитесь, что у вас установлен Python 3.x.
   - Установите необходимые библиотеки с помощью `pip`:
     ```bash
     pip install scrapy pymongo
     ```

2. **Настройте MongoDB**:
   - Запустите локальный экземпляр MongoDB или используйте удаленный сервер.
   - В коде указана база данных `vacancies191124`, которая будет использоваться для хранения данных.

3. **Запуск парсинга**:
   - Создайте проект Scrapy с помощью команды:
     ```bash
     scrapy startproject jobparser
     ```
   - Добавьте файл с пауком для парсинга данных с сайта hh.ru.
   - Включите настройки для MongoDB в вашем `settings.py`:
     ```python
     ITEM_PIPELINES = {
         'jobparser.pipelines.JobparserPipeline': 1,
     }
     ```

4. **Класс Pipeline**:
   - В файле `pipelines.py` определен класс `JobparserPipeline`, который:
     - Обрабатывает данные зарплаты (минимальная и максимальная зарплата, валюта).
     - Сохраняет результаты в базу данных MongoDB.
   
   Пример обработки зарплаты:
   - Если зарплата не указана: `min_salary` и `max_salary` будут `None`.
   - Если зарплата в диапазоне (от - до): извлекаются минимальная и максимальная зарплата, а также валюта.

5. **Пример обработки данных**:
   В процессе обработки вакансий парсер извлекает название вакансии и зарплату:
   - Преобразует данные о зарплате в числовые значения.
   - Определяет валюту (рубль, доллар, евро, фунт).


