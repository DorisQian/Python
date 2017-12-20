"""
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the 
spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or 
diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. You are given a result of 
a game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure 
to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".

x-o-referee

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.

Example:

checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X"
checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"
How it is used: The concepts in this task will help you when iterating data types. They can also be used in game 
algorithms, allowing you to know how to check results.
Precondition:
There is either one winner or a draw.
len(game_result) == 3
all(len(row) == 3 for row in game_result)

井字,有时也被称为X和操作系统,是一个游戏的两名球员(X和O)轮流标记一个3×3的空间网格。成功地在水平、垂直或对角线(nw - se和ne - sw)
中分别放置三个标记的玩家获胜。

但我们不会玩这个游戏。你将成为这次比赛结果的裁判。你得到了一个游戏的结果，你必须决定游戏的结局是赢还是平局，谁将是赢家。如果X -
玩家赢了，确保返回“X”，如果O - player赢了。如果游戏是平局，返回D。

x-o-referee

游戏的结果是一个字符串列表，其中“X”和“O”是玩家的标记。“是空的细胞。”

输入:作为字符串列表的游戏结果(unicode)。

输出:“X”、“O”或“D”作为字符串。

如何使用:该任务中的概念将在迭代数据类型时帮助您。它们也可以用于游戏算法，让你知道如何检查结果。
先决条件:
要么一个赢，要么一个平局。

"""

def checkio(game_result):
    return "D" or "X" or "O"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

