#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/22 20:45
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :test_join_class.py
# Software  :PyCharm Community Edition
import pytest
import time
from pages.main_page import MainPage
from pages.locators.main_locator import MainPageLocator as ml
from common.mylog import get_logger
from datas.invite_code import *

logger = get_logger("test_join_class")


@pytest.mark.usefixtures("login")
@pytest.mark.usefixtures("join_class_env")
class TestJoinClass:
    '''
    init conditions: login, in main_page, no class
    after all: join in origin class
    '''

    @pytest.mark.parametrize("value", inviteCode_correct)
    def test_join_with_correct_code(self,value,join_class_env):
        locator = value["locator"]
        main_page = join_class_env
        main_page.refresh()
        main_page.join_class_with_no_class()
        toast_info = main_page.get_toast_text((By.XPATH, "//span[contains(., '加入课堂成功')]"))

        try:
            assert "加入课堂成功" in toast_info
            logger.info("success")
        except:
            logger.error("Failed")
            raise


    @pytest.mark.parametrize("value", inviteCode_incorrect)
    def test_join_with_wrong_code(self, value, join_class_env):
        main_page = join_class_env
        main_page.refresh()
        code = value["code"]
        expected = value["expected"]
        locator = value["locator"]
        main_page.join_class_with_class(code)
        toast_info = main_page.get_toast_text(locator=locator)

        try:
            assert expected in toast_info
            logger.info("success")

        except:
            logger.error("Failed")
            raise




if __name__ == '__main__':
    pytest.main()