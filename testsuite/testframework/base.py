# -*- coding: utf-8 -*-
import logging
import unittest
import time

from testconfig import config

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaseTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(BaseTest, self).__init__(*args, **kwargs)
        self.environment_url = config['main']['url']
        self.browser = config['main']['browser']

    def setUp(self):
        self._testID = self._testMethodName
        self._startTime = time.time()
        self._logger = logging.LoggerAdapter(logging.getLogger('portal_testsuite'),
                                             {'testid': self.shortDescription().split(':')[0] or self._testID})
        self.lg('Testcase %s Started at %s' % (self._testID, self._startTime))
        self.set_browser()
        self.driver.get(self.environment_url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 120)

    def tearDown(self):
        """
        Environment cleanup and logs collection.
        """
        self.driver.quit()
        if hasattr(self, '_startTime'):
            executionTime = time.time() - self._startTime
        self.lg('Testcase %s ExecutionTime is %s sec.' % (self._testID, executionTime))

    def lg(self, msg):
        self._logger.info(msg)

    def element_is_enabled(self, element):
        return self.driver.find_element_by_xpath(self.elements[element]).is_enabled()

    def element_is_displayed(self, element):
        return self.driver.find_element_by_xpath(self.elements[element]).is_displayed()

    def element_is_readonly(self, element):
        return self.driver.find_element_by_xpath(self.elements[element]).get_attribute("readonly")

    def wait_until_element_located(self, name):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, name)))

    def wait_unti_element_clickable(self, name):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, name)))

    def set_browser(self):
        if self.browser == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()

    def click(self, element):
        element = self.elements[element]
        self.click_element(element)

    def click_element(self, element):
        self.wait_until_element_located(element)
        self.wait_unti_element_clickable(element)
        self.driver.find_element_by_xpath(element).click()
        time.sleep(1)

    def get_text(self, element):
        element = self.elements[element]
        return self.get_element_text(element)

    def get_element_text(self, element):
        self.wait_until_element_located(element)
        return self.driver.find_element_by_xpath(element).text

    def get_value(self, element):
        element = self.elements[element]
        self.wait_until_element_located(element)
        return self.driver.find_element_by_xpath(element).get_attribute("value")

    def set_text(self, element, value):
        element = self.elements[element]
        self.wait_until_element_located(element)
        self.driver.find_element_by_xpath(element).clear()
        self.driver.find_element_by_xpath(element).send_keys(value)
