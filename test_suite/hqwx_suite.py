# -*- coding: utf-8 -*-
import unittest
import os
import sys
from airtest.core.api import auto_setup
from config import globalparam
from test_case.hqwx.test_demo import TestDemo


def suite():
    """
    return test suite
    """

    test_suite = unittest.TestSuite()

    # 添加执行case方法1
    Testcases = [TestDemo]
    for i in Testcases:
        auto_setup(basedir=globalparam.test_images_path)  # 初始化图像算法路径
        test_suite.addTest(unittest.makeSuite(i))
    return test_suite

    # 添加执行case方法2
    # test_suite.addTest(unittest.makeSuite(TestLive))  # 添加环球网校在线课堂回归用例
    # test_suite.addTest(unittest.makeSuite(TestMall))  # 添加环球网校官方课程回归用例
    # test_suite.addTest(unittest.makeSuite(TestDemo)) #调试使用
    # return test_suite
