# -*- coding: utf-8 -*-
import os
import time
import traceback
from airtest.core.helper import log
from BeautifulReport import BeautifulReport
from airtest.core.api import auto_setup
from common.configemail import send_email, new_report
from airtest.core.android.adb import *
from lib.del_all_report import del_all
from test_suite.hqwx_suite import suite
from airtest.report.report import simple_report
import logging
from config import globalparam


logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


def run_case():
    """
    用例执行并打印测试报告
    """
    test_suite = suite()
    # print("打印"+str(test_suite))

    # # 生成一整份用例报告
    # result = BeautifulReport(test_suite)
    # test_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # # report_name = 'UI自动化测试报告' + '{}'.format(time.strftime('%Y-%m-%d_%H_%M_%S'))  # 生成对应时间执行的报告名称
    # report_name = 'UI自动化测试报告'
    # result.report(filename=report_name, description=report_name + test_date, report_dir='./report',
    #               theme='theme_default')

    for i in test_suite:
        # 生成每份用例的BR报告
        result = BeautifulReport(i)
        test_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        report_name = 'Web端UI自动化测试报告' + '{}'.format(time.strftime('%Y-%m-%d_%H_%M_%S'))  # 生成对应时间执行的报告名称
        # report_name = 'Web端UI自动化测试报告'
        report_path = globalparam.report_path
        result.report(filename=report_name, description=report_name + test_date, report_dir=report_path,
                      theme='theme_default')

    # 生成airtest自带简单报告
    # simple_report(filepath='test_suite/hqwx_suite.py', logpath=log_dir, output=out_put)


def Send_email():
    '''
    发送邮件功能
    '''
    report_path = '../report'
    outFullName = "../report.zip"
    send_email(report_path=report_path, file_path=outFullName)


if __name__ == '__main__':
    run_case()
    # Send_email()  # 邮件发送
    # del_all()
