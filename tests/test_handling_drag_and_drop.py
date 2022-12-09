import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver import ActionChains


def test_handling_simple_alert():
    options = ChromeOptions()
    options.browser_version = "106.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = os.environ.get("LT_USERNAME");
    lt_options["accessKey"] = os.environ.get("LT_ACCESS_KEY");
    lt_options["visual"] = True;
    lt_options["build"] = "Handling Drag & Drop";
    lt_options["project"] = "Handling Drag & Drop";
    lt_options["name"] = "Handling Drag & Drop";
    lt_options["w3c"] = True;
    lt_options["plugin"] = "python-python";
    options.set_capability('LT:Options', lt_options);
    # LambdaTest Profile username
    user_name = os.environ.get('LT_USERNAME')
    # LambdaTest Profile access_key
    accesskey = os.environ.get('LT_ACCESS_KEY')
    remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(remote_url, options=options)
    driver.get("https://www.lambdatest.com/selenium-playground/drag-drop-range-sliders-demo")
    
    # source = driver.find_element(By.CSS_SELECTOR, "input[value='5']")
    source = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='5']")))
    print("I am dragging the mouse from: ", source.get_attribute("value"))
    # target = driver.find_element(By.CSS_SELECTOR, "input[value='50']")
    target = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='50']")))
    print("I'm dropping the mouse at: ", target.get_attribute("value"))
    action = ActionChains(driver)
    action.drag_and_drop(source, target).perform()
    print("The mouse dragged from 5 to 50")
    driver.close()
    
    