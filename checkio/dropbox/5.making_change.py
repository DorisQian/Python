'''
Nicola is taking a much needed vacation. He'll be backpacking around some lesser-known 
countries. Each has its own unique currency.

When making purchases, Nicola would like to use the minumum number of coins possible. 
For example, Outer Leftopia has coins with denomination 1, 3, and 5 shillings. He wants 
to buy a souvenir that costs 13 shillings. He can do that using two 5 shilling coins and 
one 3 shilling coin.

You can assume Nicola has access to an infinite number of coins of each denomination. 
(He has a large bank account and access to an ATM).

Input: Two arguments. The first argument is an int: the price of the purchase. The second 
is a list of ints: the denominations of available coins.

Output: int. The minimum number of coins Nicola can use to make the purchase. If the price 
cannot be made with the available denominations, return None.

Example:

checkio(8, [1, 3, 5]) == 2
checkio(12, [1, 4, 5]) == 3
    
How it is used: Besides helping Nicola make change, this is an example of a problem in combinatorial optimization.

Precondition: Inputs are all positive integers.


尼古拉正在度假。他会围着一些鲜为人知的背包背包国家。每个人都有自己独特的货币。

在购买时，Nicola希望尽可能使用最少数量的硬币。例如，外近视有硬币，面额为1,3和5先令。他要
购买一项花费13先令的纪念品。他可以用两个5先令硬币和一枚3先令硬币。

你可以假设尼古拉可以使用每种面额的无限数量的硬币。
（他有一个大的银行账户并可以使用ATM）。

输入：两个参数。第一个参数是int：购买价格。第二是一个整数列表：可用硬币的面额。
输出：int。尼古拉可以用来购买的最低数量的硬币。如果价格
不能用可用的面额进行，返回无。

它是如何使用的：除了帮助Nicola做出改变之外，这是组合优化问题的一个例子。

先决条件：输入都是正整数。
将price分成从1到price的price份，例如price为8，则计算给出的列表中，能凑成从1,2,3到8分别最少用几个，
其中，ey：8 - 5 = 3，即8可以用3的个数，加上一个5，只要取得3最小硬币数即可，而3又是，3-1 或者3-3，就是2的个数+1 或者直接一个3，
那最小一定是1个3，也就是1
'''

def checkio(price, denominations):
    price_num = [0] * (price + 1)
    for price in range(1, price + 1):
    	varis = []
    	for n in [coin for coin in denominations if coin <= price]:
    		varis.append(price_num[price - n] + 1)
    	if varis:
    		price_num[price] = min(varis)
    	else:
    		price_num[price] = -1
    if price_num[price] > 0:
    	return price_num[price]
    else:
    	return None

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(8, [1, 3, 5]) == 2
    assert checkio(12, [1, 4, 5]) == 3
    print('Done')
