import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.select import Select



def test_multiple_values_dropdown():
    options = ChromeOptions()
    options.browser_version = "107.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = os.environ.get("LT_USERNAME");
    lt_options["accessKey"] = os.environ.get("LT_ACCESS_KEY");
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
    dropdown = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/section[3]/div/div/div[2]/div[2]/div[2]/select')))

    # Using the webdriver Select class to select multiple values
    multi_select = Select(dropdown)
    driver.implicitly_wait(3)
    multi_select.select_by_index(0)
    driver.implicitly_wait(3)
    multi_select.select_by_value("AZ")
    driver.implicitly_wait(3)
    multi_select.select_by_visible_text("Iowa")
    print("All selected values using the SELECT Class in the dropdown are: \n")
    for option in multi_select.all_selected_options:
        print(option.get_attribute('innerText'))

    driver.close()
    
