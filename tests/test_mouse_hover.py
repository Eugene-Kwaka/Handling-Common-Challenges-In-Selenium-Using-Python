import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    product_item = driver.find_element(By.XPATH, '//*[@id="mz-product-listing-image-37213259-0-0"]/div/div[1]/img')
    # Create a sequence of actions through the ActionsChains class
    actions = ActionChains(driver)
    # Perform triggers the actions
    actions.move_to_element(product_item).perform()
    # find the add_to_cart element we want to click on the product element
    add_to_cart = driver.find_element(By.CSS_SELECTOR, 'button[title="Add to Cart"]')
    # The mouse will click the add_to_cart element to complete the sequence.
    actions.click(add_to_cart)
    print("Item moved to the cart")

    driver.close()
    
    
    
    
    


