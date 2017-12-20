"""
You are massively sending thousands and thousands emails every day, meanwhile experimenting with subject lines and the message itself. SendGrid allows you to see statistics of your spam reports.

Your mission is to figure out how many spam reports you receive on a specific day.

Input: Day as a string in format 'YYYY-MM-DD'

Output: Int. The amount of spam reports

你每天都在发送成千上万封邮件，同时还在尝试着主题行和消息本身。SendGrid允许您查看垃圾邮件报告的统计信息。
你的任务是弄清楚你在某一天收到了多少垃圾邮件。
输入:Day作为格式“yyyy - mm - dd”格式的字符串
输出:Int .垃圾邮件报告数量
Example:

how_spammed('2014-5-5') == 16
"""

import sendgrid

API_KEY = 'Registrate your own key'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def how_spammed(str_date):
    return 1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('You had {} spam reports in 2016-01-01'.format(how_spammed('2016-01-01')))
    print('Check your results')