import os
import zipfile
from email.header import Header
from lib import logger
from common import get_conf
import mimetypes
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

mail_dict = get_conf('MAIL')
sender = mail_dict['sender']
receivers = mail_dict['receivers']
mail_host = mail_dict['mail_host']
mail_pass = mail_dict['mail_pass']
content = mail_dict['content']
subject = mail_dict['subject']

def set_message(sender, receivers, subject, content, file_path=None):
    '''
    设置发送的邮件内容
    '''
    try:
        message = MIMEMultipart()
        message.attach(MIMEText(content, 'plain', 'utf-8'))
        message['From'] = sender
        message['To'] = receivers
        message['Subject'] = Header(subject, 'utf-8')

        if file_path:
            if os.path.exists(file_path):

                # 读html文件内容做正文
                #                 # f = open(file_path, 'rb')
                #                 # mail_body = f.read()
                #                 # f.close()
                #                 # # 邮件正文是MIMEText
                #                 # body = MIMEText(mail_body,'html','utf-8')
                #                 # message.attach(body)

                # html附件
                # attr = MIMEText(open(file_path, 'r', encoding='utf-8').read())
                # attr['Content-Type'] = 'application/octet-stream'
                # attr['Content-Disposition'] = 'attachment;filename="report.html"'
                # message.attach(attr)

                # test_report文件夹附件
                data = open(file_path, 'rb')
                ctype, encoding = mimetypes.guess_type(file_path)
                if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream'
                maintype, subtype = ctype.split('/', 1)
                file_msg = MIMEBase(maintype, subtype)
                file_msg.set_payload(data.read())
                data.close()
                encoders.encode_base64(file_msg)  # 把附件编码
                file_msg.add_header('Content-Disposition', 'attachment', filename="测试报告.zip")  # 修改邮件头
                message.attach(file_msg)

            else:
                logger.log_error('{} does not exist'.format(file_path))

        return message

    except Exception as ex:
        logger.log_error(str(ex))
        return False


def send_email(sender=sender, receivers=receivers, mail_host=mail_host, mail_pass=mail_pass, subject=subject,
               content=content, file_path=None, report_path=None):
    '''
    发送邮件请求
    '''
    try:
        zip_dir(report_path, file_path)
        msg = set_message(sender, receivers, subject, content, file_path)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(mail_host)  # 连服务器
            smtp.login(sender, mail_pass)

            # smtp = smtplib.SMTP(mail_host, 465)
            # smtp.starttls()
            # smtp.connect()
            # mail_user = sender
            # smtp.login(mail_user, mail_pass)
        except:
            smtp = smtplib.SMTP_SSL(mail_host, 465)
            smtp.login(sender, mail_pass)  # 登录
        smtp.sendmail(sender, receivers.split(';'), msg.as_string())
        smtp.quit()
        logger.log_info('send email successfully')
        print('send email successfully')

    except Exception as ex:
        logger.log_error(str(ex))


# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = []
    f1 = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到f1
    for f in f1:
        if f.endswith('.html'):
            lists.append(f)  # 筛选出html文件保存到lists
            lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
            file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
            file_path = file_new.replace('\\', '/')  # 将反斜杠\替换成/
            print(file_path)
    return file_path


def zip_dir(dir_path, outFullName):
    """
    压缩指定文件夹
    :param dir_path: 目标文件夹路径
    :param outFullName:  压缩文件保存路径+XXXX.zip
    :return:
    """
    testcase_zip = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
    for path, dir_names, file_names in os.walk(dir_path):
        for filename in file_names:
            testcase_zip.write(os.path.join(path, filename))
    testcase_zip.close()
    print("打包成功")

if __name__ == '__main__':
    report_path = '../report'
    # send_email(file_path=new_report(report_path))  #发送html文件
    outFullName = "../report.zip"
    send_email(report_path=report_path, file_path=outFullName)  #发送测试报告文件夹
