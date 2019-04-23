#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/23 10:06
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : test_uploadhomework.py
# @Software : PyCharm
import pytest
from common.mylog import get_logger

logger = get_logger("test_upload")


@pytest.mark.run
@pytest.mark.test_upload
@pytest.mark.usefixtures("upload_file_env")
@pytest.mark.usefixtures("login")
class TestUploadFile:

    def test_upload_file(self, upload_file_env):
        homework_page = upload_file_env
        homework_page.upload_homework("easy")
        msg = homework_page.get_tips()

        try:
            assert msg == "作业提交成功"
            logger.info("success")
        except:
            logger.error("Failed")
            raise


if __name__ == '__main__':
    pytest.main("-m test_upload")

