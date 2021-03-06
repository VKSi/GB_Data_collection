from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from sothebysdiamonds import settings

from sothebysdiamonds.spiders.rings import RingsSpider


if __name__ == '__main__':
    jewelery = 'brooches'
    global link_to_name
    link_to_name = {}
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(RingsSpider, text=jewelery)

    process.start()
