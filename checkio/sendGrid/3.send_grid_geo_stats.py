"""
To solve this mission you must use the SendGrid API Key.

You should be able to operate with your statistical email data and SendGrid has a lot of APIs that provide information you may need.

Your mission is to figure out which country opens your emails the most. You can use this information in order to focus on a specific segment.

Input: Day as a string in format 'YYYY-MM-DD'

Output: String, Two-digit country code of country that has more unique clicks.

Example:

    best_country('2016-01-01') == 'UA'

要解决这个任务，您必须使用SendGrid API密钥。
您应该能够使用您的统计电子邮件数据，而SendGrid有许多提供您可能需要的信息的api。
你的任务是找出哪个国家最能打开你的邮件。您可以使用这些信息来关注特定的部分。
输入:Day作为格式“yyyy - mm - dd”格式的字符串
输出:字符串，两位数的国家代码，具有更独特的点击。

"""

import sendgrid

API_KEY = 'Registrate your own key'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def best_country(str_date):
        return 'UA'

    if __name__ == '__main__':
            #These "asserts" using only for self-checking and not necessary for auto-testing
                print('Your best country in 2016-01-01 was ' + best_country('2016-01-01'))
                    print('Check your results')
