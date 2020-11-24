
#### 版本
* python 3.6
* airtest-selenium 1.0.3
* airtest 1.1.3
* BeautifulReport 0.1.2

#### 说明
* unittest 框架管理测试用例
* 使用airtest-selenium框架结合进行元素的定位和操作
* BeautifulReport 作为测试结果的报告
* 测试数据读取功能
* 报告邮件发送功能

#### 使用
* unittest 框架，在 test_cases 下对应模块的目录中添加用例
* unittest 框架，在 test_suite 下添加对应模块的用例组成用例集并调用auto_setup()函数方法进行路径初始化操作
* 在 test_images/hqwx 下添加图片识别算法录制的图像
* common 文件用于编写基本功能函数，如发邮件功能
* config 文件下存储整个工具的全局变量，如日志、报告、截图、浏览器驱动等路径
* data 存放Excel表或txt文件等需要读取的测试数据
* lib 自定义公用函数、方法
* 在 ./lib/basepage.py basepage object思想，用于定义页面基本类，这里只编写页面元素功能，目的是让页面元素和页面功能分开，页面数据和代码分开（实现数据驱动）
* 在./lib/datainfo.py 将表或者文本字段解析成dict（字典）、list（列表），方便数据读取
* 在./lib/mytest.py 基类：整个用例执行前的操作以及公共的方法
* 在./lib/readconfig.py config文件中.ini格式文件内容读取
* 直接运行 run.py 执行所有用例
* 报告、截图、日志生成在 ./report 目录下
* 用例成功的截图保存在 ./report/image 目录下，将截图嵌入到BR测试报告中整合起来
* 执行，运行run.py脚本，可以使用命令框：python run.py或者直接执行pycharm工具的执行操作按钮

#### 怎么写 case
* 元素属性有：ID、NAME、CLASS_NAME、TAG_NAME、CSS_SELECTOR、XPATH、LINK_TEXT、PARTIAL_LINK_TEXT等，利用调试工具获取
* airtest-selenium是对selenium进行了二次封装，也继承selenium的元素定位、页面交互等方法，功能更强大。同时也有图像点击识别函数airtest_touch进行图像识别定位功能
* 可以选择通过 airtest IDE工具先进行元素定位编写脚本或者进行录制，然后移植到 python case 中
* 初始化操作：每个 case 的均有前置和后置操作，根据项目情况设置
* 断言：对比结果可以放在每条 case 的后面，常用的assert等断言语句，有些根据功能需要跳过的，可以使用if/else或try/except来跳过某些不同情况下的用例，继续执行


> 注：airtest-selenium的用法请查看官方文档：
* https://airtest.doc.io.netease.com/tutorial/13_Selenium/（官方文档）
* https://github.com/AirtestProject/airtest-selenium/tree/master/airtest_selenium（airtest-selenium源码）
