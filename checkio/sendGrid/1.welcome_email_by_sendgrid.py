"""
To solve this mission you must use the SendGrid API Key (this video explains you how to create your own API Key). Check these Python examples.
It is all starts with your first email. Let’s try to send one.
Your mission is to create a function that sends a welcome email to a user. The function gets two arguments: email and name of the user.
Subject of the email should be "Welcome" and body simply "Hi, {name}" ({name} should be replaced by users name)
Input: Two arguments. email and username
Output: None. You should send an email. You don’t need to return anything.
send_email('a.lyabah@checkio.org', 'oduvan')
send_email('somebody@gmail.com', 'Some Body')

要解决这个任务，您必须使用SendGrid API键(这个视频解释了如何创建自己的API密钥)。检查这些Python示例。
这都是从你的第一封邮件开始的。让我们试着发送一个。
您的任务是创建一个向用户发送欢迎邮件的函数。这个函数有两个参数:电子邮件和用户名。
邮件的主题应该是“Welcome”，而body只是“Hi，{name}”({name}应该被用户名替换)
输入:两个参数。电子邮件和用户名
输出:没有。你应该发一封电子邮件。你不需要返回任何东西。


import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = 'Registrate your own key'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def send_email(email, name):
    pass

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.sina.com'
mail_user = 'doris_test'
mail_pwd = 'admin@123'

sender = 'doris_test@sina.com'
receiver = '1609047552@qq.com'

message = MIMEText('Hi,  関亍未来丶', 'plain', 'utf-8')
message['From'] = Header('doris_test@sina.com')
message['To'] = Header('関亍未来丶', 'utf-8')
message['Subject'] = Header('checkio sendGrid-1', 'utf-8')

server = smtplib.SMTP(mail_host, 25)
server.set_debuglevel(1)
server.login(mail_user, mail_pwd)
server.sendmail(sender, receiver, message.as_string())
server.quit()
