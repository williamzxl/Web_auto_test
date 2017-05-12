# -*- coding: utf-8 -*-
import time
import unittest,HTMLTestRunner

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

import fwInfo
from script import login


class FlashFW(unittest.TestCase):
    global bmcip, immImage, uefiImage, dsaImage
    bmcip = fwInfo.yuanshan1_bmcip
    uefiImage = fwInfo.yuanshan_uefiImage

    #immImage = fwInfo.immImage
    immImage = fwInfo.Official_immImage
    dsaImage = fwInfo.dsaImage

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = bmcip
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_flash_imm(self):
        '''self.immImage'''
        print("####################")
        print("Now begin to test flash IMM")
        print("####################")
        driver = self.driver
        login.login(self)
        print("Now login web gui")
        try:
            driver.find_element_by_id("dijit_MenuBarItem_0_text")
        finally:
            time.sleep(5)
            print("Web is ready now")
        driver.find_element_by_id("dijit_PopupMenuBarItem_2_text").click()
        driver.find_element_by_css_selector("#dijit_MenuItem_9_text > table > tbody > tr > td").click()
        driver.find_element_by_id("btnUpdateFwDlg_label").click()
        time.sleep(5)
        # .find_element_by_css_selector("input.dijitOffScreen").click()
        # driver.find_element_by_name("uploadedfile").clear()
        driver.find_element_by_name("uploadedfile").send_keys(immImage)
        try:
            driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        finally:
            time.sleep(10)
            print("Now upload imm image")
            driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        time.sleep(200)
        try:
            driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        finally:
            time.sleep(15)
            print("Wait to flash imm image finished,need 2 min 37 sec")
            driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        time.sleep(5)
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        time.sleep(180)
        # driver.find_element_by_xpath("(//input[@value=''])[5]").click()
        driver.find_element_by_id("restartIMMId_label").click()
        time.sleep(5)
        driver.find_element_by_id("commonPopupOk_label").click()
        print("Reatart imm,wait about 5 min")
        time.sleep(720)
        print("Finish test to flash imm fw")

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

def test_flash_imm(self):
    print("####################")
    print("Now begin to test flash IMM")
    print("####################")
    driver = self.driver
    login.login(self)
    print("Now login web gui")
    try:
        driver.find_element_by_id("dijit_MenuBarItem_0_text")
    finally:
        time.sleep(5)
        print("Web is ready now")
    driver.find_element_by_id("dijit_PopupMenuBarItem_2_text").click()
    driver.find_element_by_css_selector("#dijit_MenuItem_9_text > table > tbody > tr > td").click()
    driver.find_element_by_id("btnUpdateFwDlg_label").click()
    time.sleep(5)
    # .find_element_by_css_selector("input.dijitOffScreen").click()
    # driver.find_element_by_name("uploadedfile").clear()
    driver.find_element_by_name("uploadedfile").send_keys(immImage)
    try:
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    finally:
        time.sleep(10)
        print("Now upload imm image")
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    time.sleep(200)
    try:
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    finally:
        time.sleep(15)
        print("Wait to flash imm image finished,need 2 min 37 sec")
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    time.sleep(5)
    driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    time.sleep(160)
    # driver.find_element_by_xpath("(//input[@value=''])[5]").click()
    if driver.find_element_by_id("restartIMMId_label"):
        driver.find_element_by_id("restartIMMId_label").click()
        time.sleep(5)
    else:
        time.sleep(30)
        driver.find_element_by_id("restartIMMId_label").click()
        time.sleep(5)
    driver.find_element_by_id("commonPopupOk_label").click()
    print("Reatart imm,wait about 5 min")
    time.sleep(720)
    print("Finish test to flash imm fw")

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%M_%H.%M.%S", time.localtime(time.time()))
    result_name = immImage.split('\\')[3]
    testunit = unittest.TestSuite()
    testunit.addTest(FlashFW("test_flash_imm"))

    filename = r'C:\Users\Desktop\Web_Test\Yuanshan1_ManualScript\report\{}.html'.format("Yuanshan1" + "_" + now)
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=result_name,
            description='Report_discription')
        runner.run(testunit)
