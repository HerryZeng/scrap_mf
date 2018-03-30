# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.baidu.com/")
        driver.find_element_by_link_text(u"外媒:俄前间谍女儿苏醒并能讲话 俄希望英允许探视").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.close()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        driver.find_element_by_link_text(u"湖畔大学第四期学员名单来袭！ 柳青、李冰冰等入选").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_2 | ]]
        driver.close()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
