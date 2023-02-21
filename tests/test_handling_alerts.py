import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions


def test_handling_simple_alert():
    options = ChromeOptions()
    options.browser_version = "108.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = os.environ.get('LT_USERNAME');
    lt_options["accessKey"] = os.environ.get('LT_ACCESS_KEY');
    lt_options["build"] = "Handling Alerts";
    lt_options["project"] = "Handling Alerts";
    lt_options["name"] = "Handling Alerts";
    lt_options["w3c"] = True;
    lt_options["plugin"] = "python-python";
    options.set_capability('LT:Options', lt_options);
    
    # LambdaTest Profile username
    user_name = os.environ.get('LT_USERNAME')
    # LambdaTest Profile access_key
    accesskey = os.environ.get('LT_ACCESS_KEY')
    remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(remote_url, options=options)
    
    driver.get("https://www.lambdatest.com/selenium-playground/javascript-alert-box-demo")
    
    # Locate the button that prompts the alert
    alert_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/section[4]/div/div/div[2]/div[3]/p[3]/button')))
    alert_button.click()
    # Switch the webdriver's control to the alert pop-up
    alert_object = driver.switch_to.alert
    # Show the alert message
    print("This is the alert message: " + alert_object.text)
    #Enter text into the Alert using send_keys()
    driver.implicitly_wait(30)
    alert_object.send_keys('Eugene')
    print("Entered my name in the prompt box")
    # Use the alert.accept() method to accept the alert
    alert_object.accept()
    print("Alert pop-up accepted by clicking the 'OK' button")

    # End the driver session
    driver.quit()
    
