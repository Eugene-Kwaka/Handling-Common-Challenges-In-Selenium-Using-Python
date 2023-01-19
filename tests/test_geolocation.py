import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_geolocation_test():
    options = ChromeOptions()
    options.browser_version = "108.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = os.environ.get('LT_USERNAME');
    lt_options["accessKey"] = os.environ.get('LT_ACCESS_KEY');
    lt_options["geoLocation"] = "US";
    lt_options["build"] = "Geolocation Testing";
    lt_options["project"] = "Geolocation Testing";
    lt_options["name"] = "Geolocation Testing";
    lt_options["w3c"] = True;
    lt_options["plugin"] = "python-python";
    options.set_capability('LT:Options', lt_options);
    
     # LambdaTest Profile username
    user_name = os.environ.get('LT_USERNAME')
    # LambdaTest Profile access_key
    accesskey = os.environ.get('LT_ACCESS_KEY')
    remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(remote_url, options=options)
    
    # Let's search for the Location specified in the Selenium Playground website.
    latitude = 41.9521
    longitude = -91.6853
    accuracy = 100
    
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
        "latitude ": latitude,
        "longitude" : longitude,
        accuracy : accuracy
    })
    
    driver.get("https://www.dennys.com/order")
    location =  WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="locationSearch"]')))
    location.send_keys(Keys.ENTER)
    # location.click()
    print("Test completed successfully")
