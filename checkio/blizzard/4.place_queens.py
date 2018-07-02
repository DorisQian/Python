'''
Almost everyone in the world knows about the ancient game Chess and has at least a basic understanding of its rules. 
Ancient humans loved this game of skill and strategy and our Robots are attempting to examine all tricks to becoming 
Chess Grandmasters. Today they are trying to solve the 8-Queen problem as written in an old chess-manuscript.

Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and denoted 
with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. Each square of the 
chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", "d6"). For this mission 
we only need to concern ourselves with Queens. The Queen can move any number of squares along the rank, file, or diagonal axis.

You should place eight chess Queens on an 8×8 chessboard so that no two Queens threaten each other. For this challenge, 
we have already placed one or more Queens on the board, so you will need to finish the placement. In addition, each 
Queen may be considered as part of it’s army, meaning every Queen could possible be a threat to every other Queen on the board.

You are given a set of square coordinates where we have placed Queens already. You should finish this set and return 
the full set of the coordinates for all eight Queens. If it's not possible -- return an empty set.
Be careful - an initial position could possibly threaten another Queen right off the bat.

place-queens
Input: Placed Queens coordinates as a set of strings.

Output: Eight Queens coordinates as a set of strings or an empty set.

Example:

place_queens({"b2", "c4", "d6", "e8"})  # {"b2", "c4", "d6", "e8", "a5", "f3", "g1", "h7"},
place_queens({"b2", "c4", "d6", "e8", "a7", "g5"}) == set()

How it is used: This is a classical puzzle and combinatorial constraints problem. It can be useful if you need make 
a schedule for teachers and classes, or for sport games occurring in several different stadiums.

Precondition:
0 < placed < 8

几乎世界上每个人都知道古代棋类游戏，并且至少对其规则有一个基本的了解。古代人喜欢这种技巧和策略的游戏，
我们的机器人正试图检查所有技巧成为国际象棋大师。今天，他们正在努力解决写在旧国际象棋手稿中的8皇后问题。

国际象棋是一个双人战略游戏，在一个方格游戏板上玩，排列成8行（称为排名，用数字1到8表示）和8列（称为文件，用字母a到h表示）。
棋盘的每个方格都由唯一的坐标对 - 一个字母和一个数字（例如“a1”，“h8”，“d6”）标识。为了这个使命我们只需要关心皇后。
女王可以沿着等级，文件或对角轴移动任意数量的方块。

你应该把八个棋子放在一个8×8的棋盘上，这样两个皇后就不会相互威胁。对于这个挑战，我们已经在棋盘上放置了一个或多个皇后区，
所以你需要完成这个位置。此外，每个女王都可能被视为军队的一部分，这意味着每个女王都有可能成为对其他女王的威胁。

您将得到一组我们已经放置了皇后的平方坐标。您应该完成此设置并返回所有八个皇后区的全套坐标。如果不可能 - 返回一个空集。
小心 - 一个初始位置可能会立即威胁到另一位女王。

地方皇后
输入：放置的女王坐标作为一组字符串。
输出：八个皇后坐标作为一组字符串或一个空集。

如何使用：这是一个经典的拼图和组合约束问题。如果您需要制定老师和班级的时间表，或者在几个不同的体育场馆中进行体育比赛，
那么这会很有用。
    #cols = ['a','b','c','d','e','f','g', 'h']
    #rows = ['1', '2', '3', '4', '5', '6', '7', '8']
'''

from itertools import product
def place_queens(placed):
    threats = []
    cols = 'abcdefgh'
    rows = '12345678'
    positions = [s[0] + s[1] for s in product(cols, rows)]

    def threation(point):
        #copy_position = positions.copy()
        for po in point:
            for position in positions:
                if po in position and position not in threats:
                   threats.append(position)
                   #copy_position.remove(position)
        for i in range(1, 9):
            move = product((-i, i), repeat = 2)
            for m in move:
                col = chr(ord(point[0]) + m[0])
                row = int(point[1]) + m[1]
                if 'a' <= col <= 'h' and 1 <= row <= 8 and str(col) + str(row) not in threats:
                    threats.append(str(col) + str(row))
        # print(threats)
        return threats

    
    for p in placed:
        threats.append(p)
        threats = threation(p)
    copy_positon = positions.copy()
    for m in threats:
        copy_positon.remove(m)
    print(copy_positon)

    threats = []
    result = []
    while 
    now = copy_positon[0]
    copy_positon.remove(now)

    for re in copy_positon:
        threat = threation(re)
        for r in copy_positon:
            if r in threat and r != re:
                continue
            else:
                result.append(r)
    print(result)
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    from itertools import combinations
    COLS = "abcdefgh"
    ROWS = "12345678"

    THREATS = {c + r: set(
        [c + ROWS[k] for k in range(8)] +
        [COLS[k] + r for k in range(8)] +
        [COLS[k] + ROWS[i - j + k] for k in range(8) if 0 <= i - j + k < 8] +
        [COLS[k] + ROWS[- k + i + j] for k in range(8) if 0 <= - k + i + j < 8])
               for i, r in enumerate(ROWS) for j, c in enumerate(COLS)}

    def check_coordinate(coor):
        c, r = coor
        return c in COLS and r in ROWS

    def checker(func, placed, is_possible):
        user_set = func(placed.copy())
        if not all(isinstance(c, str) and len(c) == 2 and check_coordinate(c) for c in user_set):
            print("Wrong Coordinates")
            return False
        threats = []
        for f, s in combinations(user_set.union(placed), 2):
            if s in THREATS[f]:
                threats.append([f, s])
        if not is_possible:
            if user_set:
                print("Hm, how did you place them?")
                return False
            else:
                return True
        if not all(p in user_set for p in placed):
            print("You forgot about placed queens.")
            return False
        if is_possible and threats:
            print("I see some problems in this placement.")
            return False
        return True

    assert checker(place_queens, {"b2", "c4", "d6", "e8"}, True), "1st Example"
    assert checker(place_queens, {"b2", "c4", "d6", "e8", "a7", "g5"}, False), "2nd Example"
