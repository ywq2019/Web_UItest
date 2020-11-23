# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lib import basepage
from lib.log import Log


class TestDemoPage(basepage.Page):

    def open_demo_page(self, url):
        """打开环球网校官网"""
        self.dr.get(url)
        Log().info('open url')
