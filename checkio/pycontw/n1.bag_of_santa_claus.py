'''
When the New Year is coming, all the kids wait for a visit from Santa Claus. He comes with a huge bag of gifts, and you can choose any one of them. But how to make the best choice? Santa takes gifts out of the bag one at a time, and if you don't like it, he puts it back into the bag and doesn’t take it out again. This leads to some disappointing situations when the last thing from the bag is a doll, and you already refused a pirate hat because hoping to get a train set!

When this happened with John, his Dad told him - "Don't worry, I’ll teach you how to choose a better gift. Think about how many gifts are in the bag."

Your function will be called many times in the same environment. For each step you are given a value of the current gift, the quantity if gifts in the current bag and a number of the current gift (counted from 1). For each step you should make a choice to take a gift or not -- True or False.

Your function will be checked repeatedly for different bags containing anywhere from 10 to 1000 gifts. We will count only the best gifts from each bag as the second rate gifts are not for us. All calls are running in the same environment, so be careful with globals. You should choose 700+ the best gifts from 2000 bags.

Input: Three arguments.
current_gift - a value of the current gift as an float.
gifts_in_bag - the quantity of gifts in a bag as an integer.
gift_number - a number of the current gift as an integer (from 1 to gifts_in_bag).
Output: Do you accept the current gift or not as a boolean value.

Implementation examples (only to demonstrate the API):

def choose_good_gift(current_gift, gifts_in_bag, gift_number):
    from random import random
    # coin
    if random() > 0.5:
        return True
    else:
        return False
    
How to use: This code can recognize optimal situations and allow you to trigger certain events during those situations. For example, you could create a bot that crawls a website looking for concert tickets and automatically lets you know when your favorite band is playing in your city.

Precondition:
10 ≤ gifts_in_bag ≤ 1000
0 ≤ current_gift
Gifts are offered in the random order.
'''