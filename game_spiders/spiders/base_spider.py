import scrapy


class BaseSpider(scrapy.Spider):
    name = "quotes"
    urls = []
    keywords = []
    crawl_id = None
    max_depth = 10

    def start_requests(self):
        current_depth = 1
        while self.urls and current_depth < self.max_depth:
            yield scrapy.Request(url=self.urls.pop(), callback=self.parse)

    def parse(self, response, **kwargs):
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
                'url': response.url,
            }
