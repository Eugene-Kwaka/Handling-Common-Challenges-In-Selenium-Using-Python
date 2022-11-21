import os
import pytest
from selenium import webdriver
import tests.constants as self
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver import ActionChains

def test_mouse_hover():
    options = ChromeOptions()
    options.browser_version = "107.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = os.environ.get("LT_USERNAME");
    lt_options["accessKey"] = os.environ.get("LT_ACCESS_KEY");
    lt_options["build"] = "MouseHoverHandling";
    lt_options["project"] = "MouseHoverHandling";
    lt_options["name"] = "MouseHoverHandling";
    lt_options["selenium_version"] = "4.0.0";
    lt_options["w3c"] = True;
    options.set_capability('LT:Options', lt_options);
      
    # LambdaTest Profile username
    user_name = os.environ.get('LT_USERNAME')
    # LambdaTest Profile access_key
    accesskey = os.environ.get('LT_ACCESS_KEY')
    remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(remote_url, options=options)
    
    driver.get("https://ecommerce-playground.lambdatest.io/")
    # Find the element we want to hover 
    item_hover = driver.find_element(By.XPATH, '//*[@id="mz-product-listing-image-37213259-0-0"]/div/div[1]/img')
    # find the element we want to click on the hover element
    add_to_cart = driver.find_element(By.CSS_SELECTOR, 'button[title="Add to Cart"]')
    # Create a sequence of actions through the ActionsChains class
    # The mouse will move to the hover element then move to the click element to complete the sequence
    actions = ActionChains(driver)
    actions.move_to_element(item_hover)
    actions.click(add_to_cart)
    # Perform triggers the actions
    actions.perform()
    print("Item moved to the cart")

    driver.close()

# class MouseHover():
#     def test_mouse_hover(self):
#         options = ChromeOptions()
#         options.browser_version = "107.0"
#         options.platform_name = "Windows 10"
#         lt_options = {};
#         lt_options["username"] = os.environ.get("LT_USERNAME");
#         lt_options["accessKey"] = os.environ.get("LT_ACCESS_KEY");
#         lt_options["build"] = "MouseHoverHandling";
#         lt_options["project"] = "MouseHoverHandling";
#         lt_options["name"] = "MouseHoverHandling";
#         lt_options["selenium_version"] = "4.0.0";
#         lt_options["w3c"] = True;
#         options.set_capability('LT:Options', lt_options);
      
#         # LambdaTest Profile username
#         user_name = os.environ.get('LT_USERNAME')
#         # LambdaTest Profile access_key
#         accesskey = os.environ.get('LT_ACCESS_KEY')
#         remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
#         driver = webdriver.Remote(remote_url, options=options)
        
#         driver.get("https://ecommerce-playground.lambdatest.io/")
#         # Find the element we want to hover 
#         item_hover = driver.find_element(By.XPATH, '//*[@id="mz-product-listing-image-37213259-0-0"]/div/div[1]/img')
#         # find the element we want to click on the hover element
#         add_to_cart = driver.find_element(By.CSS_SELECTOR, 'button[title="Add to Cart"]')
#         # Create a sequence of actions through the ActionsChains class
#         # The mouse will move to the hover element then move to the click element to complete the sequence
#         actions = ActionChains(driver)
#         actions.move_to_element(item_hover)
#         actions.click(add_to_cart)
#         # Perform triggers the actions
#         actions.perform()
#         print("Item moved to the cart")
    
#         driver.close()
        
# he = MouseHover()
# he.test_mouse_hover()

