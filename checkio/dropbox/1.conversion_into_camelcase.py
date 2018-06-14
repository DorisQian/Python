'''
Your mission is to convert the name of a function (a string) from the Python format 
(for example "my_function_name") into CamelCase ("MyFunctionName"), where the first char 
of every word is in uppercase and all words are concatenated without any intervening characters.

Input: A function name as a string.

Output: The same string, but in CamelCase.

Example:

to_camel_case("my_function_name") == "MyFunctionName"
to_camel_case("i_phone") == "IPhone"
to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
to_camel_case("name") == "Name"

How it is used: To apply function names in the style in which they are adopted in a specific 
language (Python, JavaScript, etc.).

Precondition:
0 < len(string) <= 100
Input data won't contain any numbers.

你的任务是从Python格式转换函数的名字（一个字符串）
（例如“my_function_name”）转换为CamelCase（“MyFunctionName”），其中第一个字符
每个单词的大写字母都是大写字母，所有单词都连接在一起，没有任何中间字符。

输入：作为字符串的函数名称。
输出：相同的字符串，但在CamelCase中。

它是如何使用的：将函数名称应用到特定的函数中
语言（Python，JavaScript等）。

前提：
0 <len（string）<= 100
输入数据不会包含任何数字。
'''

def to_camel_case(name):
    re = name.replace('_', ' ').title()
    result = ''.join(re.split(' '))
    return result
    
if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")