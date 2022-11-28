import os
import pytest
from selenium import webdriver
import tests.constants as self
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def test_download_files():
    options = ChromeOptions()
    options.browser_version = "107.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = os.environ.get("LT_USERNAME");
    lt_options["accessKey"] = os.environ.get("LT_ACCESS_KEY");
    lt_options["build"] = "Handling File Downloads";
    lt_options["project"] = "Handling File Downloads";
    lt_options["name"] = "Handling File Downloads";
    lt_options["w3c"] = True;
    lt_options["plugin"] = "python-python";
    options.set_capability('LT:Options', lt_options);
    
    # Specify the location I want the PDF file to be downloaded to.
    options.add_experimental_option("prefs", {"download.default_directory": "C:/SeleniumDownloadedFiles"})
    
    # LambdaTest Profile username
    user_name = os.environ.get('LT_USERNAME')
    # LambdaTest Profile access_key
    accesskey = os.environ.get('LT_ACCESS_KEY')
    remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(remote_url, options=options)
    
    # Download the PDF file.
    driver.get("https://www.lambdatest.com/selenium-playground/table-data-download-demo")
    pdf_button = driver.find_element(By.XPATH, '//*[@id="example_wrapper"]/div[1]/a[4]')
    pdf_button.click()
    print("successfully downloaded the pdf file to DownloadedFiles folder")
    
    
    driver.close()