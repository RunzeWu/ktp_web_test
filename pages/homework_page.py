#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/22 13:57
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : homework_page.py
# @Software : PyCharm
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from pages.index_page import IndexPage
from pages.locators.homework_locator import HomeworkLocator as hl
from pages.base import BasePage
from common.contants import test_file
from pages.login_page import LoginPage
from pages.main_page import MainPage


class HomeworkPage(BasePage):

    def click_upload_button(self):
        """
        点击上传文件
        :return:
        """
        return self.get_visible_element(hl.uploadHomework_button).click()

    def click_resubmit_button(self):
        """
        点击更新提交
        :return:
        """
        return self.get_visible_element(hl.re_upload_button_start).click()

    def click_resubmit_button_end(self):
        return self.get_visible_element(hl.re_upload_button_end).click()

    def click_confirm_resubmit_button(self):
        return self.get_visible_element(hl.confirm_resubmit_button_locator).click()

    def upload_file(self, file=test_file):
        self.upload_chrome(file)

    def click_submit_button(self):
        return self.get_visible_element(hl.submit_button_locator).click()

    def click_known(self):
        return self.get_visible_element(hl.known_locator).click()

    def click_leave_message_input(self):
        return self.get_visible_element(hl.leave_message_area_locator).click()

    def input_leave_message(self, message):
        return self.get_visible_element(hl.leave_message_input_locator).send_keys(message)

    def click_save_message_button(self):
        return self.get_visible_element(hl.save_message_button_locator).click()

    def return_page(self):
        return self.get_visible_element(hl.return_page_locator).click()

    def get_homework_status(self):
        self.return_page()
        status = self.get_visible_element(hl.homework_status_button).text
        self.driver.back()
        return status

    def move_to_element(self, locator):
        '''
        鼠标悬停操作
        locator=('id','xxx')
        driver.move_to_element(locator)
        '''

        element = self.get_visible_element(locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def upload_homework(self, leave_message=None):
        status = self.get_homework_status()
        # self.click_upload_button()

        if status == "已提交":
            self.click_resubmit_button()
            self.click_confirm_resubmit_button()

        time.sleep(2)
        self.move_to_element(hl.uploadHomework_button)

        self.upload_file()

        if leave_message is not None:
            self.click_leave_message_input()
            self.input_leave_message(leave_message)
            self.click_save_message_button()
            if status=="已提交":
                self.click_resubmit_button_end()
            else:
                self.click_submit_button()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    main_page = MainPage(driver)
    driver.get('https://www.ketangpai.com/')
    index_page.click_login_button()
    login_page.login("17751810779", "wrz19960529.")
    main_page.exit_class('wrz19960529.')
    time.sleep(3)
    main_page.join_class()
    main_page.click_homework()
    homework_page = HomeworkPage(driver)
    homework_page.upload_homework(leave_message="easy")
    b = homework_page.get_homework_status()
    print(b)