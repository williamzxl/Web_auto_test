# -*- coding: utf-8 -*-
import time
import unittest
import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


import fwInfo
from script import test_dsa
from script import test_imm
from script import test_uefi


class FlashFW(unittest.TestCase):
    global bmcip, immImage, uefiImage, dsaImage

    bmcip = fwInfo.yuanshan1_bmcip
    uefiImage = fwInfo.yuanshan_uefiImage

    immImage = fwInfo.immImage
    #immImage = fwInfo.Official_immImage
    dsaImage = fwInfo.dsaImage

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = bmcip
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_flash_imm(self):
        test_imm.test_flash_imm(self)

    def test_flash_uefi(self):
        test_uefi.test_flash_uefi(self)

    def test_flash_dsa(self):
        time.sleep(30)
        test_dsa.test_flash_dsa(self)

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

def suite():
    suite = unittest.TestSuite()
    suite.addTest(FlashFW("test_flash_imm"))
    suite.addTest(FlashFW("test_flash_uefi"))
    suite.addTest(FlashFW("test_flash_dsa"))
    return suite

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    result_name = immImage.split('\\')[3]

    testunit = unittest.TestSuite()
    testunit.addTest(FlashFW("test_flash_imm"))
    testunit.addTest(FlashFW("test_flash_uefi"))
    testunit.addTest(FlashFW("test_flash_dsa"))

    filename = r"C:\Users\Desktop\Web_Test\Yuanshan1_ManualScript\report\{}.html".format("Yuanshan1" +"_" + now)
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=result_name,
            description='Report_discription')
        runner.run(testunit)