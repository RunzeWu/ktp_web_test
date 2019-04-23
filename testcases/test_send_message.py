#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/23 11:16
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : test_send_message.py
# @Software : PyCharm
import pytest
from common.mylog import get_logger
from selenium.webdriver.common.by import By

logger = get_logger("test_send_message")


@pytest.mark.run
@pytest.mark.test_send_message
@pytest.mark.usefixtures("send_message")
@pytest.mark.usefixtures("login")
class TestSendMessage:

    def test_send_message(self, send_message):
        class_mate_page = send_message
        class_mate_page.click_teacher_talk_icon()
        message = "雨泽大佬你好帅testbyyysf"
        class_mate_page.send_message(message)

        locator = (By.XPATH, "//div[@class='text'][contains(.,'{}')]".format(message))

        expected = class_mate_page.get_visible_element(locator).text

        try:
            assert expected == message
            logger.info("success")
        except:
            logger.error("Failed")
            raise


if __name__ == '__main__':
    pytest.main("-m test_send_message")
