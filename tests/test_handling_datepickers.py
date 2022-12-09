import os
from selenium import webdriver
import tests.constants as self
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

        
# class DatePickers():
#     options = ChromeOptions()
#     options.browser_version = "107.0"
#     options.platform_name = "Windows 10"
#     lt_options = {};
#     lt_options["username"] = os.environ.get('LT_USERNAME');
#     lt_options["accessKey"] = os.environ.get('LT_ACCESS_KEY');
#     lt_options["build"] = "Handling Date Pickers";
#     lt_options["project"] = "Handling Date Pickers";
#     lt_options["name"] = "Handling Date Pickers";
#     lt_options["w3c"] = True;
#     lt_options["plugin"] = "python-python";
#     options.set_capability('LT:Options', lt_options)
#     # LambdaTest Profile username
#     user_name = os.environ.get('LT_USERNAME')
#     # LambdaTest Profile access_key
#     accesskey = os.environ.get('LT_ACCESS_KEY')
#     remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
#     driver = webdriver.Remote(remote_url, options=options)
    
#     def test_handling_jquey_datepicker(self):
#         driver = self.driver
#         # Handling JQuery DatePicker
#         driver.get('https://www.lambdatest.com/selenium-playground/jquery-date-picker-demo')
#         # # Switch to frame
#         # fr = driver.find_element(By.XPATH, '/html/body/iframe[1]')
#         # driver.switch_to.frame(fr);
#         # identify datepicker element in the frame
#         from_date = driver.find_element(By.XPATH, '//*[@id="from"]')
#         from_date.click()
#         print("I'm choosing the dates from..")
#         # Choose a date from the calendar
#         from_day = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[3]/a').click()
#         print("From date is:", from_day)
#         # Click the to_date element in the webpage.
#         to_date = driver.find_element(By.XPATH, '//*[@id="to"]')
#         to_date.click()
#         # Choose a day from the calendar
#         to_day = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[6]/a').click()
#         print("To date is:", to_day)
#         driver.close()
        
        
#     def test_bootstrap_datepicker(self):
#         driver = self.driver
#         # options = ChromeOptions()
#         # options.browser_version = "107.0"
#         # options.platform_name = "Windows 10"
#         # lt_options = {};
#         # lt_options["username"] = "Your LambdaTest Username";
#         # lt_options["accessKey"] = "Your LambdaTest Access Key";
#         # lt_options["build"] = "Handling Date Pickers";
#         # lt_options["project"] = "Handling Date Pickers";
#         # lt_options["name"] = "Handling Date Pickers";
#         # lt_options["w3c"] = True;
#         # lt_options["plugin"] = "python-python";
#         # options.set_capability('LT:Options', lt_options)
#         # LambdaTest Profile username
#         driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-date-picker-demo")
        
        
        
# jq = DatePickers()
# jq.test_handling_jquey_datepicker()


def test_handling_jquey_datepicker():
    options = ChromeOptions()
    options.browser_version = "107.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = os.environ.get('LT_USERNAME');
    lt_options["accessKey"] = os.environ.get('LT_ACCESS_KEY');
    lt_options["build"] = "Handling Date Pickers";
    lt_options["project"] = "Handling Date Pickers";
    lt_options["name"] = "Handling Date Pickers";
    lt_options["w3c"] = True;
    lt_options["plugin"] = "python-python";
    options.set_capability('LT:Options', lt_options)
    # LambdaTest Profile username
    user_name = os.environ.get('LT_USERNAME')
    # LambdaTest Profile access_key
    accesskey = os.environ.get('LT_ACCESS_KEY')
    remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(remote_url, options=options)
    # Handling JQuery DatePicker
    driver.get('https://www.lambdatest.com/selenium-playground/jquery-date-picker-demo')
    # # Switch to frame
    # fr = driver.find_element(By.XPATH, '/html/body/iframe[1]')
    # driver.switch_to.frame(fr);
    # identify datepicker element
    from_date = driver.find_element(By.XPATH, '//*[@id="from"]')
    from_date.click()
    print("I'm choosing the dates from..")
    # Choose a date from the calendar
    from_day = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[3]/a').click()
    print("From date is:", from_day.text)
    # Click the to_date element in the webpage.
    to_date = driver.find_element(By.XPATH, '//*[@id="to"]')
    to_date.click()
    # Choose a day from the calendar
    to_day = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[6]/a').click()
    print("To date is:", to_day.text)
    driver.close()