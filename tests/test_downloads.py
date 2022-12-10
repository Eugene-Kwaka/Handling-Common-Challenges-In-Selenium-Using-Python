import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    # prefs = {"download.default_directory": "C:\SeleniumDownloadedFiles"};
    # options.add_experimental_option("prefs", prefs);
    
    # LambdaTest Profile username
    user_name = os.environ.get('LT_USERNAME')
    # LambdaTest Profile access_key
    accesskey = os.environ.get('LT_ACCESS_KEY')
    remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(remote_url, options=options)
    
    # Download the PDF file.
    driver.get("https://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/")
    # pdf_button = driver.find_element(By.XPATH, '//*[@id="example_wrapper"]/div[1]/a[4]')
    pdf_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[6]/td[2]/a')))
    pdf_button.click()
    # print("successfully downloaded the pdf file to DownloadedFiles folder")
    print("Succussfully downloaded the pdf file")
    
    
    driver.close()
    