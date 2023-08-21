import scrapy
from scrapy import Selector
from scrapy.dupefilters import BaseDupeFilter
from scrapy.http import HtmlResponse

from spider_books.items import BookItem
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


http://opac.gzlib.gov.cn/opac/search?q=嵌入式&searchWay=title&rows=50&searchWay0=marc&sortWay=loannum_sort&sortOrder=desc

http://opac.gzlib.gov.cn/opac/search?q=嵌入式&searchType=standard&isFacet=true&view=standard&searchWay=title&rows=10&hasholding=1&searchWay0=marc&logical0=AND&sortWay=loannum_sort&sortOrder=desc

关键字：
计算机组成原理， 电路分析基础，模拟电路，数字电路，C 语言程序设计，c++程序设计，
电工技术，电子制作，印刷电路板，硬件制造，单片机，嵌入式，ARM开发，stm32，FPGA，
物联网技术，传感器技术、OpenCV, 机器人操作系统，ROS。

每个类别按照借阅次数排名，爬前面120个.

需要分类号，书号，书名，出版社，出版时间，作者， 关键字（内容提要） 这几个信息

给结果字段进行排序
对结果根据id进行去重复
"""

keywords = ['计算机组成原理', '电路分析基础', '模拟电路', '数字电路',
            'C语言程序设计', 'c++程序设计', ' 电工技术', '电子制作',
            '印刷电路板', '硬件制造', '单片机', '嵌入式', 'ARM开发',
            'stm32', 'FPGA', '物联网技术', '传感器技术',
            'OpenCV', '机器人操作系统', 'ROS']
keywords2 = ['嵌入式', 'ARM开发']


# 删除字符串中的所有 \r\n, \t符号
def clean_str(org_str):
    return org_str.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '').strip()

BOOK_TYPE_DICT = {
    "1" : "图书"
}


class GzlibSpider(scrapy.Spider):
    name = "gzlib"
    allowed_domains = ["opac.gzlib.gov.cn"]
    # start_urls = ["http://opac.gzlib.gov.cn"]
    # start_urls = ["http://opac.gzlib.gov.cn/opac/search?q=嵌入式&searchWay=title&rows=120&searchWay0=marc&sortWay=loannum_sort&sortOrder=desc"]

    # 去重复
    custom_settings = {
        "DUPEFILTER_CLASS": "spider_books.middlewares.BookDupeFilter",
        'FEED_EXPORT_FIELDS': [
            'search_key', 'title', 'publisher', "author",
            "book_isbn", "keywords",
            "borrow_times", "category", "price",
            "summary", "link", "book_cover"
        ],
    }


    def start_requests(self):
        for keyword in keywords:
            url = f"http://opac.gzlib.gov.cn/opac/search?q={keyword}&searchWay=title&rows=120&searchWay0=marc&sortWay=loannum_sort&sortOrder=desc"
            # yield scrapy.Request(url=url, callback=self.parse)
            yield scrapy.Request(url=url, cb_kwargs=dict(keyword=keyword), callback=self.parse)

    def parse(self, response: HtmlResponse, **kwargs):
        search_key = kwargs['keyword']
        sel = Selector(response)
        list_items = sel.css("table.resultTable tr")
        for item in list_items:
            book_item = BookItem()
            book_type = item.css("div.bookmeta::attr(booktype)").extract_first()
            if book_type in BOOK_TYPE_DICT:
                book_item['category'] = BOOK_TYPE_DICT[book_type]
            else:
                book_item['category'] = book_type
            book_item['search_key'] = search_key

            book_item['book_id'] = item.css("div.bookmeta::attr(bookrecno)").extract_first()
            book_item['title'] = item.css("a.title-link::text").extract_first().strip()
            # div.bookmeta里的div.meneame的第1个兄弟span内容作为借阅次数borrow_times
            book_item['borrow_times'] = item.css("div.bookmeta div.meneame + span::text").extract_first().strip()

            book_detail_url = f"http://opac.gzlib.gov.cn/opac/book/{book_item['book_id']}"
            book_item['link'] = book_detail_url
            # yield book_item
            yield scrapy.Request(url=book_detail_url, callback=self.parse_book_detail, meta={'book_item': book_item})

    def parse_book_detail(self, response: HtmlResponse):
        book_item = response.meta['book_item']
        sel = Selector(response)
        # 封面
        img_path = sel.css("#bookcover_img::attr(src)").extract_first()
        book_item["book_cover"] = response.urljoin(img_path)

        info_list = sel.css("#bookInfoTable tr")

        for info in info_list:
            info_key = info.css("td.leftTD > div::text").extract_first()
            info_sel = info.css("td.rightTD")
            if info_key is None or info_sel is None:
                continue
            info_key = info_key.strip()

            if info_key.startswith("题名"):
                # 截取/后的内容作为author
                info_value = clean_str(info_sel.xpath('string()').extract_first())
                index = info_value.rfind('/')
                if index >= 0:
                    info_value = info_value[index + 1:]
                book_item['author'] = info_value
            elif info_key.startswith("ISBN"):
                info_value = clean_str(info_sel.xpath('string()').extract_first())
                if "价格：" in info_value:
                    values = info_value.split("价格：")
                    book_item['book_isbn'] = values[0]
                    book_item['price'] = values[1]
                else:
                    book_item['book_isbn'] = info_value
            elif info_key.startswith("出版"):
                book_item['publisher'] = clean_str(info_sel.xpath('string()').extract_first())
            elif info_key.startswith("主题词"):
                book_item['keywords'] = clean_str(info_sel.xpath('string()').extract_first())
            elif info_key.startswith("内容提要"):
                book_item['summary'] = clean_str(info_sel.xpath('string()').extract_first())

        yield book_item
