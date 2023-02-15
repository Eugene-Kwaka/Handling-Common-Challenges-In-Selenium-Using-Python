import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions


def test_dynamic_content():
    options = ChromeOptions()
    options.browser_version = "107.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = os.environ.get("LT_USERNAME");
    lt_options["accessKey"] = os.environ.get("LT_ACCESS_KEY");
    lt_options["build"] = "Handling Dynamic Content";
    lt_options["project"] = "Handling Dynamic Content";
    lt_options["name"] = "Handling Dynamic Content";
    lt_options["w3c"] = True;
    lt_options["plugin"] = "python-python";
    options.set_capability('LT:Options', lt_options);
    
    # LambdaTest Profile username
    user_name = os.environ.get('LT_USERNAME')
    # LambdaTest Profile access_key
    accesskey = os.environ.get('LT_ACCESS_KEY')
    remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(remote_url, options=options)
    
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    # locate the start_button 
    start_button = driver.find_element(By.XPATH, '//*[@id="start"]/button')
    start_button.click()
    # Waiting for the text to appear after clicking the start_button
    finish_element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]/h4')))
    print(finish_element.text)

    driver.close()
    