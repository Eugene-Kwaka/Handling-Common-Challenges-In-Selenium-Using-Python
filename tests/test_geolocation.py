import os
import pytest
from selenium import webdriver
import tests.constants as self
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


def geolocation_test():
    options = ChromeOptions()
    options.browser_version = "107.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = "himanshujlambdatest";
    lt_options["accessKey"] = "7A6pDWfFCavmJajP7466YAnCaH5pndMtfG0TnsSbfaPzUeJmu3";
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
        latitude : 41.9521,
        longitude : -91.6853,
        accuracy : 100
    })
    
    driver.get("https://www.lambdatest.com/selenium-playground/geolocation-testing")
    location =  driver.find_element(By.CSS_SELECTOR, ".icon-geolocate")