# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
分类号，书号，书名，链接，封面图
出版社，出版时间，作者，关键字, 内容提要 
"""

class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # 文献类型
    category = scrapy.Field()
    # 搜索词
    search_key = scrapy.Field()
    # 书id
    book_id = scrapy.Field()
    # ISBN
    book_isbn = scrapy.Field()
    # 书名
    title = scrapy.Field()
    # 借阅次数
    borrow_times = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 书链接
    link = scrapy.Field()
    # 书封面
    book_cover = scrapy.Field()
    # 出版社
    publisher = scrapy.Field()
    # 出版时间
    # publish_date = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 关键字
    keywords = scrapy.Field()
    # 内容提要
    summary = scrapy.Field()

class MovieItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    rating_num = scrapy.Field()