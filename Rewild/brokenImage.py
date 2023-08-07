from selenium import webdriver  # webdriver module provides all WebDriver implementations
from selenium.webdriver.common.by import By
import warnings
import unittest, time, re
import requests
import csv
import HtmlTestRunner
import confTest     # Custom class
import urllib
from urllib import request, parse
from urllib.request import Request
from bs4 import BeautifulSoup

class Rewild(confTest.RewildBrowserBASE):

    # navigate to each page (can use sitemap.xml or csv file of links,
    # search page for img, grab img src, send http request, check status code == 200
    def test_brokenImage(self):
        driver = self.driver
        test_urls = []

        def url_grabber(file):
            with open(file, mode='r') as file:
                csv_reader = csv.reader(file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    test_urls.append(row[0])
                    line_count += 1
                print(f'Processed {line_count} lines in CSV file.')
                return test_urls

        if self.env == 'dev':
            csv_file = '../Rewild/files/sitelinks - dev.csv'
            url_grabber(csv_file)
        elif self.env == 'qa':
            csv_file= '../Rewild/files/sitelinks - qa.csv'
            url_grabber(csv_file)
        elif self.env == 'stage':
            csv_file = '../Rewild/files/sitelinks - stage.csv'
            url_grabber(csv_file)
        elif self.env == 'preview':
            csv_file = '../Rewild/files/sitelinks - preview.csv'
            url_grabber(csv_file)
        elif self.env == 'prod':
            # grabbing testlinks from a sitemap.xml link
            sitemap = 'https://rewild-dev.org/sitemap.xml'
            get_url = requests.get(sitemap)
            if get_url.status_code == 200:
                s = get_url.text
                soup = BeautifulSoup(s)
                line_count = 0
                for loc in soup.findAll('loc'):
                    test_urls.append(loc.text)
                    line_count += 1
                print(f'Processed {line_count} urls in sitemap.xml.')
            else:
                print(f'Unable to fetch sitemap: {sitemap}')

        agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'

        for t in test_urls:
            driver.get(t)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            image_list = driver.find_elements(By.TAG_NAME, 'img')
            print(f'Total number of images = {str(len(image_list))} on {t}')
            iBrokenImageCount = 0
            for img in image_list:
                time.sleep(.5)
                try:
                    img_link = img.get_attribute('src')
                    if img_link and img_link.isspace():
                        pass
                    else:
                        req = Request(img_link, headers={'User-Agent': agent})
                        status = request.urlopen(req).getcode()
                except urllib.error.URLError as e:
                    if hasattr(e, 'reason'):    # (e.g. conn. refused)
                        iBrokenImageCount += 1
                        print(f'FAIL: We failed to reach a server at {img_link}')
                        print('Reason: ', e.reason, 'Status code: ', status)
                    elif hasattr(e, 'code'):    # (e.g. 404, 501, etc)
                        iBrokenImageCount += 1
                        print(f'ERROR: The server couldn\'t fulfill the request at {img_link}')
                        print('Error code: ', e.code, 'Status code: ', status)
                except (RuntimeError, TypeError, NameError, ValueError) as e:
                    iBrokenImageCount += 1
                    print(f'ERROR encountered: - {status} - {e} - {img_link}')

            if iBrokenImageCount == 0:
                print('No broken images found.\n')
            else:
                print('FAIL - The page ' + t + ' has ' + str(iBrokenImageCount) + ' broken images\n')

# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.RewildBrowserBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.RewildBrowserBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))
