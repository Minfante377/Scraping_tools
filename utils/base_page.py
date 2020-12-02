from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.logger import Logger
import os


class BasePage():

    def __init__(self, url, name, headless=True):
        self.name = name
        self.url = url
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome("{}/drivers/chromedriver".format(os.getcwd()),
                                       chrome_options=chrome_options)
        self.result_dir = "{}/{}".format(os.getcwd(), self.name)
        self.logger = Logger(self.result_dir)
        self._log_info("Web driver starting on {}".format(self.url))

    def _log_info(self, data):
        self.logger.log_info(data)

    def _log_error(self, data):
        self.logger.log_error(data)
