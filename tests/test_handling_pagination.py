# import os
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# def test_pagination():
#     options = ChromeOptions()
#     options.browser_version = "106.0"
#     options.platform_name = "Windows 10"
#     lt_options = {};
#     lt_options["username"] = os.environ.get("LT_USERNAME");
#     lt_options["accessKey"] = os.environ.get("LT_ACCESS_KEY");
#     lt_options["build"] = "Handling - Pagination";
#     lt_options["project"] = "Pagination";
#     lt_options["name"] = "Handling Pagination";
#     lt_options["w3c"] = True;
#     lt_options["plugin"] = "python-python";
#     options.set_capability('LT:Options', lt_options);
#     # LambdaTest Profile username
#     user_name = os.environ.get('LT_USERNAME')
#     # LambdaTest Profile access_key
#     accesskey = os.environ.get('LT_ACCESS_KEY')
#     remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
#     driver = webdriver.Remote(remote_url, options=options)
#     driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/manufacturer/info&manufacturer_id=8")
#     # Find element that lists all the items in the page
#     element_list = driver.find_element(By.CSS_SELECTOR, "#entry_212439")
#     # Locate the individual items in the 1st page of the table. Look for a locator that all elements share.
#     items = element_list.find_elements(By. CSS_SELECTOR, "#entry_212439 > div > div:nth-child(n+1)")
#     # Print the number of items in the page
#     print(f"Number of items in the 1st Page: {len(items)}" + "\n")
#     # Locate the second item in the 1st page of the pagination table
#     second_item = element_list.find_element(By.CSS_SELECTOR, "#entry_212439 > div > div:nth-child(2)").text        
#     print("The Second item in the 1st Page is: " + "\n" + second_item)
    
#     # Loop through the page numbers
#     # The '>' element that when clicked takes us to the next page
#     # next_pages = driver.find_element(By.CSS_SELECTOR, "#entry_212440 > div > div.col-sm-6.text-left > ul > li:nth-child(6) > a").click()
    
#     # The last page in the pagination table. Since all the pagination elements share the page-link we are targeting the third pagination number 
#     last_pages = int(driver.find_elements(By.CLASS_NAME, "page-link"))[2]
#     for _ in range(1, last_pages):
#         last_item = element_list.find_element(By.CSS_SELECTOR, "#entry_212439 > div > div:nth-child(12)").text
#         print("The last item in the last pagination page is: " + last_item)
    
#     # # the class "activepageitem" is true when we are on a page in the pagination table
#     # activepageitem = True
    
#     # while activepageitem:
#     #     element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.By.CSS_SELECTOR, "#entry_212439")))
#     #     try:
#     #         driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div[1]/div[3]/div/div[1]/div[5]/div/div[1]/ul/li[5]/a').click()
#     #     # There will not be a next button at the end of the pagination table
#     #     except Exception as e:
#     #         print(e, "End of pagination table")
#     #         activepageitem = False
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     ###### THE SELENIUM PLAYGROUND TEST
#     # driver.get("https://www.lambdatest.com/selenium-playground/table-pagination-demo")
#     # # Find element that lists all the items in the table
#     # element_list = driver.find_element(By.ID, "table-id")
#     # print(element_list)
#     # # Locate the individual items in the 1 page. I set the n+26 because I want the number of items listed per page to be 25 out of n numbers
#     # items = element_list.find_elements(By.CSS_SELECTOR, "#table-id > tbody > tr:nth-child(n+26)")
#     # //*[@id="table-id"]/tbody/tr[1]
#     # # print the number of items in the page
#     # print(len(items))
