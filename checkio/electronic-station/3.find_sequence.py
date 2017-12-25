"""
“There’s nothing here...” sighed Nikola.

“You’re kidding right? All treasure is buried treasure! It wouldn’t be treasure otherwise!” Said

Sofia. “Here, take these.” She produced three shovels from a backpack that seemed to appear out of thin air.

“Where did you get-”

“Don’t ask questions. Just dig!” She hopped on the shovel and began digging furiously.

CLUNK

“Hey we hit something.” Stephen exclaimed in surprise.

“It’s the treasure!” Sofia was jumping up and down in excitement.

The trio dug around the treasure chest and pulled it out of the hole and wiped the dirt off. Sofia tried grabbing the lid but it was locked. Nikola studied the locking mechanism.

“I’ve seen this type of lock before. It’s pretty simple. We just need to check whether there is a sequence of 4 or more matching numbers and output a bool.”

“Easy enough. Let’s open this sucker up!” Sofia was shaking in excitement.

You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

find-sequence
Input: A matrix as a list of lists with integers.

Output: Whether or not a sequence exists as a boolean.

Example:

checkio([
    [1, 2, 1, 1],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5]
]) == True
checkio([
    [7, 1, 4, 1],
    [1, 2, 5, 2],
    [3, 4, 1, 3],
    [1, 1, 8, 1]
]) == False
checkio([
    [2, 1, 1, 6, 1],
    [1, 3, 2, 1, 1],
    [4, 1, 1, 3, 1],
    [5, 5, 5, 5, 5],
    [1, 1, 3, 1, 1]
]) == True
checkio([
    [7, 1, 1, 8, 1, 1],
    [1, 1, 7, 3, 1, 5],
    [2, 3, 1, 2, 5, 1],
    [1, 1, 1, 5, 1, 4],
    [4, 6, 5, 1, 3, 1],
    [1, 1, 9, 1, 2, 1]
    ]) == True

How it is used: This concept is useful for games where you need to detect various lines of the same elements (match 3 games for example). This algorithm can be used for basic pattern recognition.

Precondition:
0 ≤ len(matrix) ≤ 10
all(all(0 < x < 10 for x in row) for row in matrix)

“这里什么也没有…”尼古拉叹息道。
“你是在开玩笑吧?所有的宝藏都是宝藏!否则就不会是珍宝了!”
索非亚。“这儿,把这些。她从背包里拿出了三个铁锹，似乎是凭空出现的。
“你在哪里- - - - - -”
“别问问题。只是挖!她跳上铲子，开始拼命地挖。
沉闷的
“嘿我们撞上什么东西了。斯蒂芬惊奇地叫道。
“这是宝藏!索菲亚激动得跳了起来。
三人在宝藏箱周围挖了个洞，把它从洞里拉出来，把泥土擦掉。索非亚试图抓住盖子，但它被锁住了。尼古拉研究了锁定机制。
“我以前见过这种锁。”这很简单。我们只需要检查是否有4个或更多匹配的序列，并输出一个bool。
“很容易。让我们打开这个吸管吧!索菲亚激动得浑身发抖。
给你一个矩阵的NxN(4≤N≤10)。您应该检查是否有一个4个或多个匹配数字的序列。序列可能是水平的，垂直的或对角的(nw - se或ne - sw对角线)。
发现,序列

输入:一个包含整数列表的矩阵。
输出:一个序列是否作为布尔值存在。

如何使用:这个概念对于需要检测相同元素的不同行(例如，匹配3个游戏)的游戏非常有用。该算法可用于基本模式识别。
"""
def checkio(matrix):
    #replace this for solution
    return True or False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
