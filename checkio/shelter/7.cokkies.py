'''
This is pretty much a technical mission.

You have raw HTTP cookies. Your mission is to extract the value of a specific cookie by its name.

Input: Two arguments. Both are strings. The first one is the string of raw cookies, 
and the second one is the name of the cookie we are looking for.

Output: A string. Extracted value.

Example:

get_cookie('theme=light; sessionToken=abc123', 'theme') == 'light'
get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo') == 'true'

这几乎是一项技术任务。

你有原始的HTTP cookies。 您的任务是通过名称提取特定cookie的价值。

输入：两个参数。 两者都是字符串。 第一个是原始曲奇串，
第二个是我们正在寻找的cookie的名字。

输出：一个字符串。 提取值。
'''

def get_cookie(cookie, name):
    return 'value'


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert get_cookie('theme=light; sessionToken=abc123', 'theme') == 'light', 'theme=light'
    assert get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo') == 'true', 'ffo=true'
    print("Looks like you know everything. It is time for 'Check'!")
