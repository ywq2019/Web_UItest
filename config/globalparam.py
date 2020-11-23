# coding=utf-8

import os
from lib.readconfig import ReadConfig

# chrome浏览器驱动路径
executable_path = r"D:\PythonProject\Web_UItest\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"

# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path, 'config.ini'))

# 项目参数设置
prj_path = read_config.getValue('projectConfig', 'project_path')

# 日志路径
log_path = os.path.join(prj_path, 'report', 'log')

# 报告截图文件路径
img_path = os.path.join(prj_path, 'report', 'image')

# 测试报告路径
report_path = os.path.join(prj_path, 'report', 'testreport')

# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'testdata')

# 图像识别截图路径
test_images_path = os.path.join(prj_path, 'test_images', 'hqwx')
