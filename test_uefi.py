# -*- coding: utf-8 -*-
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

import fwInfo
from script import login
import HTMLTestRunner


class FlashFW(unittest.TestCase):
    global bmcip, immImage, uefiImage, dsaImage
    bmcip = fwInfo.yuanshan1_bmcip
    uefiImage = fwInfo.yuanshan_uefiImage

    immImage = fwInfo.immImage
    dsaImage = fwInfo.dsaImage

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = bmcip
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_flash_uefi(self):
        print("####################")
        print("Now begin to test flash UEFI")
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
        time.sleep(5)
        driver.find_element_by_id("btnUpdateFwDlg_label").click()
        time.sleep(5)
        # .find_element_by_css_selector("input.dijitOffScreen").click()
        # driver.find_element_by_name("uploadedfile").clear()
        driver.find_element_by_name("uploadedfile").send_keys(uefiImage)
        try:
            driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        finally:
            time.sleep(10)
            print("Now upload UEFI image")
            driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        time.sleep(20)
        try:
            driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        finally:
            time.sleep(15)
            driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        print("Wait to flash UEFI image finished,need 1 min 37 sec")
        time.sleep(5)
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        time.sleep(110)
        # driver.find_element_by_xpath("(//input[@value=''])[4]").click()

        if driver.find_element_by_id("restartOSId_label"):
            print("Restart OS")
            time.sleep(10)
            driver.find_element_by_id("restartOSId_label").click()
        else:
            print("   ")
            time.sleep(10)
            driver.find_element_by_id("restartOSId_label").click()
        time.sleep(5)
        driver.find_element_by_id("commonPopupOk_label").click()
        time.sleep(5)
        driver.find_element_by_id("commonPopupClose_label").click()
        time.sleep(10)
        driver.find_element_by_id("dijit_MenuBarItem_0_text").click()
        time.sleep(5)
        driver.find_element_by_id("btnserverActionsListHealthSumm_label").click()
        time.sleep(5)
        driver.find_element_by_id("serverActionsListHealthSumm63_text").click()
        time.sleep(5)
        driver.find_element_by_id("commonPopupOk_label").click()
        time.sleep(5)
        driver.find_element_by_id("commonPopupClose_label").click()
        print("Reatart os,wait about 5 min")
        time.sleep(300)
        print("Finish test to flash UEFI fw")

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

def test_flash_uefi(self):
    print("####################")
    print("Now begin to test flash UEFI")
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
    time.sleep(5)
    driver.find_element_by_id("btnUpdateFwDlg_label").click()
    time.sleep(5)
    # .find_element_by_css_selector("input.dijitOffScreen").click()
    # driver.find_element_by_name("uploadedfile").clear()
    driver.find_element_by_name("uploadedfile").send_keys(uefiImage)
    try:
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    finally:
        time.sleep(10)
        print("Now upload UEFI image")
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    time.sleep(20)
    try:
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    finally:
        time.sleep(15)
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    print("Wait to flash UEFI image finished,need 1 min 37 sec")
    time.sleep(5)
    driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    time.sleep(110)
    # driver.find_element_by_xpath("(//input[@value=''])[4]").click()

    if driver.find_element_by_id("restartOSId_label"):
        print("Restart OS")
        time.sleep(10)
        driver.find_element_by_id("restartOSId_label").click()
    else:
        print("   ")
        time.sleep(10)
        driver.find_element_by_id("restartOSId_label").click()
    time.sleep(5)
    driver.find_element_by_id("commonPopupOk_label").click()
    time.sleep(5)
    driver.find_element_by_id("commonPopupClose_label").click()
    time.sleep(10)
    driver.find_element_by_id("dijit_MenuBarItem_0_text").click()
    time.sleep(5)
    driver.find_element_by_id("btnserverActionsListHealthSumm_label").click()
    time.sleep(5)
    driver.find_element_by_id("serverActionsListHealthSumm63_text").click()
    time.sleep(5)
    driver.find_element_by_id("commonPopupOk_label").click()
    time.sleep(5)
    driver.find_element_by_id("commonPopupClose_label").click()
    print("Reatart os,wait about 5 min")
    time.sleep(300)
    print("Finish test to flash UEFI fw")

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%M_%H.%M.%S", time.localtime(time.time()))
    result_name = immImage.split('\\')[3]
    testunit = unittest.TestSuite()
    testunit.addTest(FlashFW("test_flash_uefi"))

    filename = r'C:\Users\Desktop\Web_Test\Yuanshan1_ManualScript\report\{}.html'.format("Yuanshan1" + "_" +now)
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=result_name,
            description='Report_discription')
        runner.run(testunit)
