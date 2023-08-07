from selenium import webdriver  # webdriver module provides all WebDriver implementations
import warnings
import unittest, time, re  # unittest is the testing framework, provides module for organizing test cases
import requests, json           # Requests provides ability to hit API Json provides ability to encode & decode Json files
import csv
import HtmlTestRunner
import var, funct, confTest     # Custom class

class Rewild(confTest.RewildHeadlessBASE):
    # test the links under subcategory /get-to-know/[slug] and /wild-about/[slug] return 200s
    def test_newRoute(self):
        new_urls = []
        with open('../Rewild/files/newroute.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                new_urls.append(row[0])
                line_count += 1
            print(f'Processed {line_count} lines in CSV file.')
            # print(new_urls)

        routingFailedList = []
        for n in new_urls:
            r = requests.get(n)
            response_status_code = r.status_code
            if response_status_code == 200:
                pass
            else:
                routingFailedList.append(response_status_code)
                routingFailedList.append(n)


        if routingFailedList != []:
            print("FAIL - These individual urls did NOT have 200 Status code:")
            print(routingFailedList)
            raise Exception
        else:
            print("PASS - ALL individual urls returned 200 Status code")
            print(new_urls)

# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.RewildHeadlessBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.RewildHeadlessBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))