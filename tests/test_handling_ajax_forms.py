import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions



def test_ajax_forms():
    options = ChromeOptions()
    options.browser_version = "107.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = os.environ.get("LT_USERNAME");
    lt_options["accessKey"] = os.environ.get("LT_ACCESS_KEY");
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
    
    driver.get("https://codepen.io/getform/pen/jRoexL")

    # Get into the iFrame 
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
    
    # Locate the Form
    form = driver.find_element(By.XPATH, '//*[@id="ajaxForm"]')
    # Identify the forms inputs and enter data through send_keys  
    email_element = form.find_element(By.XPATH, '//*[@id="exampleInputEmail1"]')
    email_element.send_keys('youremail@gmail.com')
    name_element = form.find_element(By.XPATH, '//*[@id="exampleInputName"]')
    name_element.send_keys('yourname')
    # Locate the dropdown 
    platform_element = Select(form.find_element(By.XPATH, '//*[@id="exampleFormControlSelect1"]'))
    platform_element.select_by_visible_text('Github')
    submit = form.find_element(By.XPATH, '//*[@id="ajaxForm"]/button')
    submit.click()
    
    # Wait for the ajax request to complete
    response = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ajaxForm"]/div[4]')))
    print(response.text)

    driver.quit()
        
   