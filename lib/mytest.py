# -*- coding: utf-8 -*-

import base64
import os
import sys
import time
import unittest
from lib.log import Log
from airtest.core.api import *
from airtest_selenium.proxy import WebChrome
from config import globalparam

abs_dir = globalparam.img_path
success = "SUCCESS   "
fail = "FAIL   "
logger = Log()


class Mytest(unittest.TestCase):
    """
    基类：整个用例执行前的操作以及公共的方法
    """
    dr = WebChrome(globalparam.executable_path)
    logger = Log()

    @classmethod
    def setUpClass(cls):
        """
        整个用例执行的前置条件
        """
        cls.logger.info('############################### START ###############################')
        cls.dr.maximize_window()

    def setUp(self):
        pass

    def tearDown(self):
        """
        每个用例执行的后置条件
        """
        # 用例执行报错立即截图
        errors = self._outcome.errors
        for test, exc_info in errors:
            if exc_info:
                self.save_img('test')
                pass
            else:
                pass

    @classmethod
    def tearDownClass(cls):
        """
        整个用例执行的后置条件
        """
        cls.dr.quit()
        cls.logger.info('###############################  End  ###############################')

    @classmethod
    def save_img(self, img_name):
        """
        保存图片
        保存的图片同时可用于展示在报告里
        :param img_name: 要保存的图片的名称
        """

        img_path = abs_dir + '\{}-{}.png'.format(img_name, time.strftime('%Y-%m-%d_%H_%M_%S'))
        img_path = img_path.replace('\\', '/')  # 将反斜杠\替换成/
        print(img_path)
        # cls.dr.snapshot(filename=img_path)
        self.take_screenshot(self, file_path=img_path)
        img_path = img_path[img_path.index("/report"):]  # 截取图片路径后面部分，用来拼接成相对路径
        img_path = '..{}'.format(img_path)
        print("<img src='" + img_path + "' width=600 />")  # 把图片发送到 BR 报告里，BR 的特性

    def take_screenshot(self, file_path):
        """
        Get the current window screenshot.

        Usage:
        dr.take_screenshot('c:/test.png')
        """
        t1 = time.time()
        try:
            self.dr.get_screenshot_as_file(file_path)
            self.my_print(msg="{0} Get the current window screenshot,path: {1}, Spend {2} seconds".format(success,
                                                                                                          file_path,
                                                                                                          time.time() - t1))
        except Exception:
            self.my_print(msg="{0} Unable to get the current window screenshot,path: {1}, Spend {2} seconds".format(
                fail,
                file_path,
                time.time() - t1))
            raise

    def my_print(msg):
        logger.info(msg)
