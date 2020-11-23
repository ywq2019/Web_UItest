# -*- encoding=utf8 -*-
from lib.mytest import Mytest
from airtest.core.api import *
from pages.TestDemo import TestDemoPage
from lib.log import Log


class TestDemo(Mytest):
    def setUp(self):
        """
        当前 case 的前置条件：执行 case 前的准备工作
        """
        pass

    def test_open_url(self):
        """
       这是一个demo
       """
        TestDemoPage.open_demo_page(self, url="https://www.baidu.com/")
        sleep(2.0)





