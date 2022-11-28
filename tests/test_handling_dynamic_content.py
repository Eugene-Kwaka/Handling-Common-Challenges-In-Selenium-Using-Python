# import os
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# # from selenium.webdriver import ActionChains

# def test_dynamic_content():
#     options = ChromeOptions()
#     options.browser_version = "107.0"
#     options.platform_name = "Windows 10"
#     lt_options = {};
#     lt_options["username"] = os.environ.get("LT_USERNAME");
#     lt_options["accessKey"] = os.environ.get("LT_ACCESS_KEY");
#     lt_options["build"] = "Handling Dynamic Content";
#     lt_options["project"] = "Handling Dynamic Content";
#     lt_options["name"] = "Handling Dynamic Content";
#     lt_options["w3c"] = True;
#     lt_options["plugin"] = "python-python";
#     options.set_capability('LT:Options', lt_options);
    