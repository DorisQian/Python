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
"""

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

