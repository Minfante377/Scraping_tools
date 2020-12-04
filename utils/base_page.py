from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utils.logger import Logger
import os


class BasePage():

    def __init__(self, url, name, headless=True):
        self.name = name
        self.url = url
        firefox_options = Options()
        if headless:
            firefox_options.add_argument("--headless")
        profile = webdriver.FirefoxProfile ()
        profile.set_preference ("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0;WOW64;Trident/7.0;rv: 11.0) like Gecko")
        profile.set_preference ('useAutomationExtension', False)
        profile.set_preference ('devtools.jsonview.enabled', False)
        profile.set_preference ("dom.webdriver.enabled", False)
        profile.update_preferences ()
        self.driver = webdriver.Firefox(firefox_options=firefox_options, firefox_profile=profile)
        self.result_dir = "{}/{}".format(os.getcwd(), self.name)
        self.logger = Logger(self.result_dir)

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
