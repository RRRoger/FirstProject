# -*- coding: utf-8 -*-
import smtplib  # 加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

"""
    发邮件的方法, 支持发多个人, 支持html和纯文本格式
    author: Roger
"""

SMTP_IP = 'smtp.163.com'  # 邮箱服务器
SMTP_PORT = 25  # 端口

SENDER_INFO = {
    'sender': 'YOURMAIL@163.com',  # 发件人邮箱账号
    'password': '******',
    'sender_nickname': '',  # 如果不传则显示发件人的邮箱
}

# 收件人邮箱账号
RECEIVERS = [
    ('nickname', 'receiver1@163.com'),
    ('nickname', 'receiver2@163.com')
]

MAIL_INFO = {
    'subject': '今天天气不错',
    'mail_text': '今天天气不错',
    'mail_type': 'plain',
}

MAIL_INFO = {
    'subject': '今天天气不错',
    'mail_text': """<html><h1>你好</h1></html>""",
    'mail_type': 'html',
}


def get_smtp_server():
    return SMTP_IP, SMTP_PORT


def mail(sender_info, receivers, mail_info):
    smtp_ip, smtp_port = get_smtp_server()  # 获取连接信息

    subject = mail_info['subject']
    mail_text = mail_info['mail_text']
    mail_type = mail_info['mail_type']  # plain 纯文本; html, html,

    msg = MIMEMultipart(mail_text, mail_type, 'utf-8')

    sender_nickname = sender_info['sender_nickname']
    sender = sender_info['sender']
    password = sender_info['password']

    # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['From'] = formataddr([sender_nickname, sender])
    receiver_mails = []

    for nick_name, receive_mail in receivers:
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        receiver_mails.append(receive_mail)

    msg['To'] = ','.join(receiver_mails)
    msg['Subject'] = subject  # 邮件的主题，也可以说是标题

    #pdf类型附件
    part = MIMEApplication(open('/Users/chenpeng/Desktop/WechatIMG95928.jpeg','rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="WechatIMG95928.jpeg")
    msg.attach(part)

    res = True
    try:
        server = smtplib.SMTP(smtp_ip, smtp_port)  # 发件人邮箱中的SMTP服务器，端口是25

        """如果遇到以下错误
            smtplib.SMTPException: SMTP AUTH extension not supported by server
            
            在login之前，加入如下两行代码

            server.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
            server.starttls()
        """

        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(sender, receiver_mails, msg.as_string())
        server.quit()  # 关闭连接
    except smtplib.SMTPException, e:
        print e
        res = False
    return res


def send_mail():
    res = mail(SENDER_INFO, RECEIVERS, MAIL_INFO)
    if res:
        print 'OK'
    else:
        print 'FAIL'




send_mail()
