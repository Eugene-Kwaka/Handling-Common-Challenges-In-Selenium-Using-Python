import os
import pytest
from selenium import webdriver
import tests.constants as self
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions

def test_ajax_forms():
    options = ChromeOptions()
    options.browser_version = "107.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = "himanshujlambdatest";
    lt_options["accessKey"] = "7A6pDWfFCavmJajP7466YAnCaH5pndMtfG0TnsSbfaPzUeJmu3";
    lt_options["build"] = "Handling Ajax Forms";
    lt_options["project"] = "Handling Ajax Forms";
    lt_options["name"] = "Handling Ajax Forms";
    lt_options["w3c"] = True;
    lt_options["plugin"] = "python-python";
    options.set_capability('LT:Options', lt_options);
    
    # LambdaTest Profile username
    user_name = os.environ.get('LT_USERNAME')
    # LambdaTest Profile access_key
    accesskey = os.environ.get('LT_ACCESS_KEY')
    remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(remote_url, options=options)
    
    driver.get("")