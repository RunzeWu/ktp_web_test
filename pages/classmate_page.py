#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/22 20:13
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :classmate_page.py
# Software  :PyCharm Community Edition
from pages.locators.classmate_locator import ClassmateLocator as cl
from pages.base import BasePage
from pages.index_page import IndexPage
from pages.login_page import LoginPage
from pages.class_page_locator import ClassPage
from pages.main_page import MainPage
from selenium import webdriver

class ClassmatePage(BasePage):

    def click_teacher_talk_icon(self):
        self.move_to_element(cl.mouse_needed_move_locator)
        return self.get_visible_element(cl.message_icon_locator).click()

    def send_message(self, msg):
        self.get_visible_element(cl.message_input_locator).send_keys(msg)
        self.get_visible_element(cl.message_submit_locator).click()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    index = IndexPage(driver)
    login = LoginPage(driver)
    class_page = ClassPage(driver)
    main_page = MainPage(driver)
    driver.get("https://www.ketangpai.com/")
    index.click_login_button()
    login.login("17751810779","wrz19960529.")
    main_page.go_into_class()
    class_page.click_classmate()
    classmate = ClassmatePage(driver)
    classmate.click_teacher_talk_icon()
    classmate.send_message("雨泽大佬你好帅test")