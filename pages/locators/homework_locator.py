#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/27 16:35
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : homework_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By


class HomeworkLocator:

    # 更新提交作业按钮//div[@class="sc-tj fl"]//a[@class="new-tj2 active"]
    re_upload_button_start = (By.XPATH, "//a[@class='new-tj1']")

    re_upload_button_end = (By.XPATH, '//div[@class="sc-tj fl"]//a[@class="new-tj2 active"]')

    resubmit_button_locator = (By.XPATH, "//a[@class='new-tj2 active']")

    # 上传作业
    uploadHomework_button = (By.XPATH, '//div[@class="webuploader-pick"]')

    # 未提交过作业用这个提交
    submit_button_locator = (By.XPATH, "//*[@id='viewer-handup']//a[contains(text(),'提交')]")

    # 提交后的“知道了”
    known_locator = (By.XPATH, "//a[contains(.,'知道了')]")

    # 留言input
    leave_message_area_locator = (By.XPATH,"//div[@class='work-message clearfix']//span[@class='s1']" \
                                  "[contains(.,'作业留言：')]/following-sibling::span")

    leave_message_input_locator = (By.XPATH, "//textarea[@id='comment']")

    save_message_button_locator = (By.XPATH, '//a[contains(.,"保存")]')

    return_page_locator = (By.XPATH, "//*[@id='return-course']/i")

    homework_status_button = (By.XPATH, '//a[@class="view-work"]')

    confirm_resubmit_button_locator = (By.XPATH,'//div[@class="btns"]//a[@class="sure active"]')

