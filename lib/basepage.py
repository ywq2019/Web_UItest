# -*- encoding=utf8 -*-
from airtest_selenium.proxy import WebChrome
from config import globalparam


class Page(object):
    """
    This is a base page class for page Object.
    """

    def __init__(self):
        self.dr = WebChrome(globalparam.executable_path)
