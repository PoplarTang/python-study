import scrapy
from scrapy import Selector

"""
# 初始化工程
scrapy startproject spider_books

# 创建爬虫
scrapy genspider douban movie.douban.com

# 运行爬虫
scrapy crawl douban -o douban.csv
"""

from spider_books.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        sel = Selector(response)
        list_items = sel.css("#content > div > div.article > ol > li")
        for item in list_items:
            movie_item = MovieItem()
            movie_item['title'] = item.css("span.title::text").extract_first()
            movie_item['rating_num'] = item.css("span.rating_num::text").extract_first()
            movie_item['link'] = item.css("a::attr(href)").extract_first()
            yield movie_item