# -*- coding: utf-8 -*-
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

import fwInfo
from script import login
import HTMLTestRunner


def test_flash_dsa(self):
    print("####################")
    print("Now begin to test flash DSA")
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
    driver.find_element_by_name("uploadedfile").send_keys(dsaImage)
    if driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label"):
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        print("1.Now upload DSA image,need about 250s")
    else:
        time.sleep(10)
        print("2.Now upload DSA image,need about 250s")
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    time.sleep(420)
    if driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label"):
        print("1.wait to flash dsa")
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    else:
        time.sleep(30)
        print("2.wait to flash dsa")
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    print("Wait to flash DSA image finished,need 120 sec")
    time.sleep(5)
    driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    time.sleep(5)
    driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    time.sleep(5)
    driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
    time.sleep(200)

    print("Finish test to flash DSA fw")

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

    def test_flash_dsa(self):
        print("####################")
        print("Now begin to test flash DSA")
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
        driver.find_element_by_name("uploadedfile").send_keys(dsaImage)
        if driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label"):
            driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
            print("1.Now upload DSA image,need about 250s")
        else:
            time.sleep(10)
            print("2.Now upload DSA image,need about 250s")
            driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        time.sleep(420)
        if driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label"):
            print("1.wait to flash dsa")
            driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        else:
            time.sleep(30)
            print("2.wait to flash dsa")
            driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        print("Wait to flash DSA image finished,need 120 sec")
        time.sleep(5)
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        time.sleep(5)
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        time.sleep(5)
        driver.find_element_by_id("updateServerFirmwareWizardbtnNext_label").click()
        time.sleep(200)

        print("Finish test to flash DSA fw")

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
    now = time.strftime("%Y-%m-%M_%H.%M.%S", time.localtime(time.time()))
    result_name = immImage.split('\\')[3]
    testunit = unittest.TestSuite()
    testunit.addTest(FlashFW("test_flash_dsa"))

    filename = r'C:\Users\Desktop\Web_Test\Yuanshan1_ManualScript\report\{}.html'.format("Yuanshan1" + "_" + now)
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=result_name,
            description='Report_discription')
        runner.run(testunit)
