"""
Almost everyone in the world knows about the ancient game Chess and has at least a basic understanding of its 
rules. It has various units with a wide range of movement patterns allowing for a huge number of possible 
different game positions (for example Number of possible chess games at the end of the n-th plies.) For this 
mission, we will examine the movements and behavior of chess pawns.

Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and 
denoted with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. 
Each square of the chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", 
"d6"). For this mission we only need to concern ourselves with pawns. A pawn may capture an opponent's piece on 
a square diagonally in front of it on an adjacent file, by moving to that square. For white pawns the front 
squares are squares with greater row than their.

A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. With this 
strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square. We have 
several white pawns on the chess board and only white pawns. You should design your code to find how many pawns 
are safe.

pawns

You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are 
safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.

Example:

safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
How it is used: For a game AI one of the important tasks is the ability to estimate game state. This concept will 
show how you can do this on the simple chess figures positions.

Precondition:
0 < pawns ≤ 8

世界上几乎每个人都知道古老的象棋，至少对它有一个基本的了解规则。它有各种各样的单位，有各种各样的运动模式，允许有大量的可能
不同的游戏位置(例如在n个plies结尾的可能的棋类游戏)。对于这个我们将考察棋子的运动和行为。

国际象棋是一种双人策略游戏，在棋盘上排列的棋盘上有八行(称为等级)用数字1到8)和8个列(称为文件，用字母a表示h)。
棋盘的每一个方格都由一个唯一的坐标对来标识——一个字母和一个数字(ex，“a1”，“h8”，“d6”)。对于这一任务，我们只需要关注卒。
棋子可以捕捉对手的棋子一个正方形对角线在它前面的一个相邻的文件，通过移动到那个正方形。白色的棋子在前面
正方形比它们的行更大。

典当通常是一个弱的单位，但是我们有8个可以用来建造一个兵防御墙。用这个
战略，一个兵为其他兵辩护。如果另一个兵能在那个方块上捕获一个单位，典当是安全的。我们有
棋盘上有几个白色的棋子，只有白色的棋子。你应该设计你的代码来找到多少个棋子
是安全的。

棋子

你得到了一组正方形坐标，我们在这里放置了白色的棋子。你应该数一下有多少个棋子
安全的。

输入:将pawns坐标放置为一组字符串。

输出:安全卒中的数量为整数。

规则：兵只能前进不能后退，直走斜吃，判断安全是看它后方的两个斜对角有没有旗子，有则安全

"""

def safe_pawns(pawns):
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

