# -*- coding: utf-8 -*-
import scrapy


class DetikCodesSpider(scrapy.Spider):
    name = 'detik_codes'
    allowed_domains = ['www.detik.com']
    start_urls = ['https://www.detik.com']

    def parse(self, response):
        data =[]

        # ul = response.css(".ul[@class='list_fokus']")
        # row_selector = "article"
        row_data = response.xpath('//ul/li/article/a/div/h2/span/text()')

        # for row in ul.xpath(row_selector):
        #     judul = row.xpath('.a/div/h2/span/text()').extract_first()
        print ("===========================================================")
        for row in row_data :
            print ("+++++++++++++++++++++++++++++++++++++++++++++++++++")
            print (">>>>>>>>>>>>>>>>>>>> "+str(row.extract()))
            
            judul = str(row.extract())
            data.append(
                {
                    'judul' : judul
                }
            )

        return data
