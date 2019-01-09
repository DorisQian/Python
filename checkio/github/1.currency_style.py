'''
"Well, it's that time of the month again. Payroll checks for our employees, which require your signatures. And no forgetting to sign the big ones!"
-- Trading Places

Many countries use different conventions for the thousands separator and decimal mark. For example in the Netherlands one million one thousand two hundred and eighty one-hundredths is written as 1.001.200,80, but in the US this is written as 1,001,200.80. Use your coding skills to convert dollars in the first style (Netherlands, Germany, Russia, Turkey, Brazil, and others) to the second style (US, UK, Canada, China, Japan, Mexico, and others).

Only currency amounts in dollars should be converted: $1.234,50 to $1,234.50, $1.000 to $1,000, and $4,57 to $4.57. But don't convert your router's IP address 192.168.1.1. Also leave currency in the US style unchanged.

Input: A string containing dollar amounts to be converted.

Output: A string with converted currencies.

Example:

        checkio("Lot 192.001 costs $1.000,94.") == "Lot 192.001 costs $1,000.94."
        checkio("$1,23 + $2,34 = $3,57.") == "$1.23 + $2.34 = $3.57."

How it is used: This is an exercise in working with strings and using the Python standard library.

Precondition: 0 < len(text) ≤ 1000;
len(fractional_part_of_currency) in {0,2};
all(s[-1].isdigit() for s in currency_substrings);
all(s[0] == '$' for s in currency_substrings)

“那么现在是这个月的那个时候，工资单会检查我们的员工，这需要你的签名，而且不要忘了签名。
- 交易场所

许多国家对千位分隔符和小数点使用不同的约定。例如在荷兰，百万一千二百八十分之一写为1.001.200,80，而在美国则写为1,001,200.80。
用你的编码技巧把第一种方式（荷兰，德国，俄罗斯，土耳其，巴西等）的美元换成第二种方式（美国，英国，加拿大，中国，日本，
墨西哥等）。

只有以美元为单位的货币金额应该转换为：1.234,50美元到1,234.50美元，1.000美元到1,000美元以及4,57美元到4.57美元。
但不要转换你的路由器的IP地址192.168.1.1。同样留下美元风格的货币不变。

输入：包含要转换的美元金额的字符串。
输出：具有转换货币的字符串。

它是如何使用的：这是一个使用字符串和使用Python标准库的练习。
'''


def checkio(text):
    words = text.split(' ')
    result = []
    for w in words:
        if w.startswith('$'):
            if w.endswith(',') or w.endswith('.'):
                start = w[:-4].replace('.', ',')
                end = w[-4 : -1].replace(',', '.')
                e = w[-1]
                result.append(start + end + e)
            else:
                start = w[: -3].replace('.', ',')
                end = w[-3:].replace(',', '.')
                result.append(start + end)
        else:
            result.append(w)
    return ' '.join(result)
    

if __name__ == '__main__':    

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89" , "1st Example"
    assert checkio("$0,89") == "$0.89" , "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
                   "Euro Style = $12,345.67, US Style = $12,345.67" , "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
                   "Us Style = $12,345.67, Euro Style = $12,345.67" , "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
                   "$1,234, $5,678 and $9", "Dollars without cents"
