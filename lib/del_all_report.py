import os
from config import globalparam

def del_all():
    '''
    删除测试报告和报告截图
    '''
    fl = os.listdir(globalparam.img_path)
    for f in fl:
        if f.endswith('.png'):
            f_path = os.path.join(globalparam.img_path, f)
            os.remove(f_path)

    f2 = os.listdir(globalparam.report_path)
    for f in f2:
        if f.endswith('.html'):
            f_path = os.path.join(globalparam.report_path, f)
            os.remove(f_path)

    #删除日志
    f3 = os.listdir(globalparam.log_path)
    for f in f3:
        if f.endswith('.log'):
            f_path = os.path.join(globalparam.log_path, f)
            os.remove(f_path)

    print("delete report successfully")

if __name__ == '__main__':
    del_all()
    print("已成功删除")
