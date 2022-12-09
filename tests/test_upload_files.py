import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_file_uploads():
    options = ChromeOptions()
    options.browser_version = "107.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = os.environ.get("LT_USERNAME");
    lt_options["accessKey"] = os.environ.get("LT_ACCESS_KEY");
    lt_options["build"] = "Handling File Upload";
    lt_options["project"] = "Handling File Upload";
    lt_options["name"] = "Handling File Upload";
    lt_options["w3c"] = True;
    lt_options["plugin"] = "python-python";
    options.set_capability('LT:Options', lt_options);
    
    # LambdaTest Profile username
    user_name = os.environ.get('LT_USERNAME')
    # LambdaTest Profile access_key
    accesskey = os.environ.get('LT_ACCESS_KEY')
    remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(remote_url, options=options)
    
    # Access website to automate file upload
    driver.get("http://demo.automationtesting.in/FileUpload.html")
    # locate the file upload button in the page using XPATH
    # file_upload = driver.find_element(By.XPATH, '//*[@id="input-4"]')
    file_upload = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-4"]')))
    # The Send Keys method will include the path for the file that will be uploaded.
    file_upload.send_keys(r"C:\Users\Eugene Kwaka\Desktop\SeleniumDoc.pdf")
    print("file uploaded successfully")
    
    driver.close()