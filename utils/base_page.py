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
        self.get_url(self.url)

    def get_url(self, url):
        self._log_info("Navigating to {}".format(url))
        self.driver.get(url)

    def click(self, class_name=None, xpath=None, _id=None, name=None, link_text=None,
              partial_link_text=None):

        element = self._find_element(class_name, xpath, _id, name, link_text, partial_link_text)
        element.click()

    def send_keys(self, text, submit=False, class_name=None, xpath=None, _id=None, name=None,
                  link_text=None, partial_link_text=None):

        element = self._find_element(class_name, xpath, _id, name, link_text, partial_link_text)
        element.send_keys(text)
        if submit:
            element.submit()

    def get_text(self, class_name=None, xpath=None, _id=None, name=None, link_text=None,
                 partial_link_text=None):

        element = self._find_element(class_name, xpath, _id, name, link_text, partial_link_text)
        return element.text

    def _find_element(self, class_name, xpath, _id, name, link_text, partial_link_text):
        if not class_name and not xpath and not _id and not name and \
            not link_text and not partial_link_text:

            self.logger.log_info("I cant find the element withouth info")
            return
        elif class_name:
            element = self.driver.find_element_by
        elif xpath:
            element = self.driver.find_element_by_xpath(xpath)
        elif _id:
            element = self.driver.find_element_by_id(_id)
        elif name:
            element = self.driver.find_element_by_name(name)
        elif link_text:
            element = self.driver.find_element_by_link_text(link_text)
        else:
            element = self.driver.find_element_by_partial_link_text(partial_link_text)
        return element

    def _log_info(self, data):
        self.logger.log_info(data)

    def _log_error(self, data):
        self.logger.log_error(data)
