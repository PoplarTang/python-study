import scrapy
from scrapy import Selector

"""
http://opac.gzlib.gov.cn/opac/search?
q=嵌入式
&searchType=standard
&isFacet=true
&view=standard
&searchWay=title
&rows=10
&hasholding=1
&searchWay0=marc
&logical0=AND
&sortWay=loannum_sort
&sortOrder=desc

关键字：
计算机组成原理， 电路分析基础，模拟电路，数字电路，C 语言程序设计，c++程序设计，
电工技术，电子制作，印刷电路板，硬件制造，单片机，嵌入式，ARM开发，stm32，FPGA，
物联网技术，传感器技术、OpenCV, 机器人操作系统，ROS。

每个类别按照借阅次数排名，爬前面120个.

需要分类号，书号，书名，出版社，出版时间，作者， 关键字（内容提要） 这几个信息
"""


class GzlibSpider(scrapy.Spider):
    name = "gzlib"
    allowed_domains = ["opac.gzlib.gov.cn"]
    start_urls = ["http://opac.gzlib.gov.cn"]

    def parse(self, response):
        sel = Selector(response)

