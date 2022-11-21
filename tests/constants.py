# import unittest
# import os
# # import pytest
# from selenium import webdriver
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options as ChromeOptions


# class CommonChallenges(unittest.TestCase):
#     def setUp(self):
#         options = ChromeOptions()
#         options.browser_version = "104.0"
#         options.platform_name = "Windows 10"
#         lt_options = {};
#         lt_options["username"] = os.environ.get("LT_USERNAME");
#         lt_options["accessKey"] = os.environ.get("LT_ACCESS_KEY");
#         lt_options["project"] = "HandlingSimpleAlerts";
#         lt_options["w3c"] = True;
#         lt_options["plugin"] = "python-python";
#         options.set_capability('LT:Options', lt_options);
#         # LambdaTest Profile username
#         user_name = os.environ.get('LT_USERNAME')
#         # LambdaTest Profile access_key
#         accesskey = os.environ.get('LT_ACCESS_KEY')
#         remote_url =  "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
#         self.driver = webdriver.Remote(remote_url, options=options)
        
# cc = CommonChallenges()
# cc.setUp()