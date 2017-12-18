You are given the current stock prices. You have to find out which stocks cost more.

Input: The dictionary where the market identifier code is a key and the value is a stock price.

Output: A string and the market identifier code.

Example:

best_stock({
    'CAC': 10.0,
    'ATX': 390.2,
    'WIG': 1.2
}) == 'ATX'
best_stock({
    'CAC': 91.1,
    'ATX': 1.01,
    'TASI': 120.9
}) == 'TASI'

Preconditions: All the prices are unique.

你得到了当前的股票价格。你得找出哪些股票更贵。
输入:市场标识码是关键字的字典，其值为股票价格。
输出:字符串和市场标识符代码。
先决条件:所有的价格都是独一无二的。

def best_stock(data):
    # your code here
    return 'GOOG'


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")

