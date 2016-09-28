# -*- coding: utf-8 -*-
import logging
import unittest
import time

from testconfig import config

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


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

    def click_link(self, link):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_element(link)

    def click_element(self, element):       
        self.wait_until_element_located(element)
        self.wait_unti_element_clickable(element)    
        self.driver.find_element_by_xpath(element).click()

    def get_text(self, element, text):
        element = self.elements[element]
        self.wait_until_element_located_and_has_text(element, text)

    def wait_until_element_located_and_has_text(self, xpath, text):
        for _ in range(10):
            try:
                self.wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath), text))
                return True
            except (TimeoutException, StaleElementReferenceException):
                time.sleep(1)
        else:
            self.assertEqual(self.driver.find_element_by_xpath(xpath).text, text)

    def set_text(self, element, value):
        element = self.elements[element]
        self.wait_until_element_located(element)
        self.driver.find_element_by_xpath(element).clear()
        self.driver.find_element_by_xpath(element).send_keys(value)
