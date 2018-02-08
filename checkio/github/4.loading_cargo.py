'''
"Look Stephen, here's a list of the items that need to be loaded onto the ship. We're going to need a lot of batteries." Nikola handed him a notepad.

"What are the numbers next to the items?"

"That is the weight of each item."

"Er, why?"

"So you can see how much your trading cards and comic book collection will weigh us down during flight." Rang Sofias voice from the phone tube.

"What is she talking about?” asked Nikola “Ooooh, nevermind, that was sarcasm. It’s important because your load-stabilizing belt is broken and there is no way that we can find a new one right now. That’s why, when you carry the things on the list, you’ll have to redistribute their weights in order to get the minimal weight in each arm."

"Okay, so I have to figure out how many batteries I should hold in each hand to prevent them from breaking when they inevitably fall to the ground. Got it."

You have been given a list of integer weights. You should help Stephen distribute these weights into two sets, such that the difference between the total weight of each set is as low as possible.

Input data: A list of the weights as a list of integers.

Output data: The number representing the lowest possible weight difference as a positive integer.

Example:

checkio([10,10]) == 0
checkio([10]) == 10
checkio([5, 8, 13, 27, 14]) == 3
checkio([5,5,6,5]) == 1
checkio([12, 30, 30, 32, 42, 49]) == 9
checkio([1, 1, 1, 3]) == 0

How it is used: This is a combinatorial optimization version of the partition problem. The combinatorial optimization has wide usage and you often see it when you look at automated schedules or route calculating.

Precondition:
0 < len(weights) ≤ 10
all(0 < x < 100 for x in weights)

“看斯蒂芬，这里列出了需要装上船的物品清单，我们需要大量的电池。尼古拉递给他一个记事本。

“这些项目旁边的数字是什么？”

“这是每个项目的重量。”

“呃，为什么？”

“所以你可以看看你的交易卡和漫画收藏会在飞行中降低多少。”让索菲亚斯从电话筒里发出声音。

“她在说什么？”尼古拉问道，“噢，不要这么说，这很讽刺，这很重要，因为你的负荷稳定带已经坏了，现在没有办法找到新的东西，这就是为什么当你携带在名单上的事情，你将不得不重新分配他们的权重，以获得在每个手臂最小的重量。

“好的，所以我必须弄清楚每只手应该放多少个电池，以防止它们在不可避免地掉到地上时折断。

你已经得到了一个整数权重列表。你应该帮助斯蒂芬把这些权重分成两组，这样每组的总重量之间的差异越小越好。

输入数据：作为整数列表的权重列表。
输出数据：表示最小可能的重量差的数字，以正整数表示。

如何使用：这是分区问题的组合优化版本。组合优化具有广泛的用途，当您查看自动计划或路线计算时，您经常可以看到它。
'''


def checkio(data):

    #replace this for solution
    return 0


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"