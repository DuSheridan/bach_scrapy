import scrapy
from typing import List
from scrapy.crawler import CrawlerProcess

from game_spiders.spiders.base_spider import BaseSpider


def start_batch_crawling(crawl_process: CrawlerProcess, results: List):
    for crawler_info in results:
        url = crawler_info["url"]
        key_words = crawler_info["key_words"]
        crawl_id = crawler_info["id"]
        crawl_process.crawl(create_spider(url, key_words, crawl_id))


def create_spider(url, keywords, crawl_id):
    starting_urls = [url]
    some_keywords = keywords
    some_crawl_id = crawl_id

    class DynamicSpider(BaseSpider):
        url = starting_urls
        keywords = some_keywords
        crawl_id = some_crawl_id

    return DynamicSpider
