import os
import scrapy
    
def getNonMargin(parentlist):
    for item in parentlist:
        if (float(item.re_first(r'margin-left:\s*(\d+)\s*px')) > 0):
            yield item

class UofCSpider(scrapy.Spider):
    name = "uofc_courselistlinks"

    def start_requests(self):
        urls = [
            'https://www.ucalgary.ca/pubs/calendar/current/course-desc-main.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        parentList = response.xpath('//*[@id="ctl00_ctl00_pageContent"]/tr/td/div/div/span')

        culledList = getNonMargin(parentList)

        for item in culledList:
            path = item.css('a::attr(href)').get()
            # yield f'https://www.ucalgary.ca/pubs/calendar/current/{path}'

            with open(f'{self.name}.txt', 'a') as f:
                f.write(f'"https://www.ucalgary.ca/pubs/calendar/current/{path}",\n')

        # courseLetters = response.css('span.page-title::text')[0].get().split(' ')[-1] # Like ACCT

        # courseList = response.xpath('//*[@id="ctl00_ctl00_pageContent"]/tr/td/div/table/tr[1]/td/table/tr')

        # for course in courseList:
        #     courseName = course.css('span::text')[0].get().strip() # Like 'Accounting'
        #     courseNumber = course.css('span::text')[1].get().strip() # Like '217'
        #     courseTitle = course.css('span::text')[2].get().strip() # Like 'Introductory Financial Accounting'

        #     yield {
        #         'courseName': courseName,
        #         'courseLetters': courseLetters,
        #         'courseNumber': courseNumber,
        #         'courseTitle': courseTitle,
        #     }

# mygen = getNonMargin(parentlist)
# for i in mygen:
#     i.css('a::attr(href)').get()