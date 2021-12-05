import requests
from decouple import config
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from game_spiders.spiders.spider_factory import start_batch_crawling


def main():
    django_api = config('DJANGO_API')
    process = CrawlerProcess(get_project_settings())
    response = requests.get(f"{django_api}/crawlers/").json()
    results = response['results']
    start_batch_crawling(process, results)
    while response["next"] is not None:
        response = requests.get(response["next"]).json()
        results = response['results']
        start_batch_crawling(process, results)


if __name__ == '__main__':
    configure_logging(get_project_settings())
    main()
