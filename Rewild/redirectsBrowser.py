from selenium import webdriver  # webdriver module provides all WebDriver implementations
import warnings
import unittest, time, re
import csv
import HtmlTestRunner
import confTest    # Custom class

class Rewild(confTest.RewildBrowserBASE):
    # check redirects by opening browser, waiting for redirect, verifying the url is as expected
    def test_redirects(self):
        driver = self.driver
        from_urls = []
        to_urls = []
        with open('../Rewild/files/Rewild - redirect breakdown - Mapped _team_ slugs.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                from_urls.append(row[0])
                to_urls.append(row[1])
                line_count += 1
            print(f'Processed {line_count} lines in CSV file.')
            # print(from_urls)
            # print(to_urls)

        # from_urls = ['https://www.globalwildlfe.org']
        # to_urls = ['https://www.rewild.org']
        redirectsPassedList = []
        redirectsFailedUrls = []
        redirectsExpectedUrls = []
        redirectsCurrentUrls = []
        redirectsFailedList = []

        for f, t in zip(from_urls, to_urls):
            driver.get('https://www.google.com')
            # open new window with execute_script()
            driver.execute_script("window.open('');")
            # switch to new window with switch_to.window()
            driver.switch_to.window(driver.window_handles[1])
            try:
                driver.get(f)
                time.sleep(11)
                if driver.current_url == t:
                    redirectsPassedList.append(f)
                else:
                    redirectsFailedUrls.append(f)
                    redirectsExpectedUrls.append(t)
                    redirectsCurrentUrls.append(driver.current_url)
                    print(f'FAILED redirect: {f} - Expected_url: {t} - Returned_url: {driver.current_url}')
                driver.close()
            except (RuntimeError, TypeError, NameError, ValueError) as e:
                print(f'ERROR encountered: - {e} - {f} - Expected_url: {t} - Returned_url: {driver.current_url}')
            except:
                if driver.current_url == t:
                    redirectsPassedList.append(f)
                else:
                    print(f'ERROR exception: {f} - Expected_url: {t} - Returned_url: {driver.current_url}')
            # switch back to old window with switch_to.window()
            driver.switch_to.window(driver.window_handles[0])

        for f, e, c in zip(redirectsFailedUrls, redirectsExpectedUrls, redirectsCurrentUrls):
            redirectsFailedList.append([(f, e, c)])

        if redirectsFailedList != []:
            print("ERROR - These individual urls did NOT redirect as expected:")
            print(f'(Initial URL, Expected URL, Returned URL)')
            print(redirectsFailedList)
            raise Exception
        else:
            print("PASS - ALL individual urls redirected as expected ")


# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.RewildBrowserBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.RewildBrowserBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))