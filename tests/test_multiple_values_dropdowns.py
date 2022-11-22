import os
import pytest
from selenium import webdriver
import tests.constants as self
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def test_multiple_values_dropdown():
    options = ChromeOptions()
    options.browser_version = "107.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = "himanshujlambdatest";
    lt_options["accessKey"] = "7A6pDWfFCavmJajP7466YAnCaH5pndMtfG0TnsSbfaPzUeJmu3";
    lt_options["build"] = "Handling Multiple Values Selection in Dropdowns";
    lt_options["project"] = "Handling Multiple Values Selection in Dropdowns";
    lt_options["name"] = "Handling Multiple Values Selection in Dropdowns";
    lt_options["selenium_version"] = "4.0.0";
    lt_options["w3c"] = True;
    options.set_capability('LT:Options', lt_options);
    
    # LambdaTest Profile username
    user_name = os.environ.get('LT_USERNAME')
    # LambdaTest Profile access_key
    accesskey = os.environ.get('LT_ACCESS_KEY')
    remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(remote_url, options=options)
    driver.get("https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo")
    
    # Find the multiselect dropdown element in the page
    dropdown = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[3]/div/div/div[2]/div[2]/div[2]/select')
    # if dropdown.get_attribute("multiple"):
    #     print("multiple select options can be chosen")
    # else:
    #     print("only one select option can be selected")
   
    
    # Using the webdriver Select class to select multiple values
    multi_select = Select(dropdown)
    
    multi_select.select_by_index(0)
    multi_select.select_by_value("AZ")
    multi_select.select_by_visible_text("Iowa")
    print("All selected values using the SELECT Class in the dropdown are: \n")
    for option in multi_select.all_selected_options:
        print(option.get_attribute('innerText'))
    
    # # Using actionChains class to select multiple values in the dropdown
    # dropdown_element= Select(dropdown)
    # option1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[3]/div/div/div[2]/div[2]/div[2]/select/option[5]')
    # option2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[3]/div/div/div[2]/div[2]/div[2]/select/option[10]')
    # option3 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[3]/div/div/div[2]/div[2]/div[2]/select/option[33]')
    # ActionChains(driver).key_down(Keys.CONTROL).click(option1).key_up(Keys.CONTROL).perform()
    # ActionChains(driver).key_down(Keys.CONTROL).click(option2).key_up(Keys.CONTROL).perform()
    # ActionChains(driver).key_down(Keys.CONTROL).click(option3).key_up(Keys.CONTROL).perform()
    # print("The values selected using ActionChains are: \n")
    # for opt in dropdown_element.all_selected_options:
    #     print(opt.get_attribute('innerText'))
    
    
    
    driver.close()