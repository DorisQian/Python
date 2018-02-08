'''
Everyone has tried solving a crossword puzzle at some point in their lives. We're going to mix things up by adding a cipher to the classic puzzle. A cipher crossword replaces the clues for each entry with clues for each white cell of the grid. These clues are integers ranging from 1 to 26, inclusive. The objective, as any other crossword, is to determine the proper letter for each cell. In a cipher crossword, the 26 numbers serve as a cipher for those letters: cells that share matching numbers are filled with matching letters, and no two numbers stand for the same letter. All resulting entries must be valid words.

For this task you should solve the cipher crossword. You are given a crossword template as a list of lists (2D array) with numbers (from 0 to 26), where 0 is a blank cell and other numbers are encrypted letters. You will be given a list of words for the crossword puzzle. You should fill that template with a given word and return the solved crossword as a list of lists with letters. Blank cells are replaced with whitespaces (0 => " ").

The words are placed in rows and columns with NO diagonals. The crossword contains six words with 5 letters each. These words are placed in a grid.

cipher-crossword
Input: The Cipher Crossword as a list of lists with integers. Words as a list of strings.

Output: The solution to the Crossword as a list of lists with letters.

Example:

checkio(
    [
        [21, 6, 25, 25, 17],
        [14, 0, 6, 0, 2],
        [1, 11, 16, 1, 17],
        [11, 0, 16, 0, 5],
        [26, 3, 14, 20, 6]
    ],
    ['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace']
) == [['h', 'e', 'l', 'l', 'o'],
      ['a', ' ', 'e', ' ', 'z'],
      ['b', 'i', 'm', 'b', 'o'],
      ['i', ' ', 'm', ' ', 'n'],
      ['t', 'r', 'a', 'c', 'e']]

How it is used: This is a type of restriction problem. You have rules and should try to find a combination that conforms to these rules. This concept can help you to solve scheduling conflicts and - a situation where you would encounter many variables and restrictions, among other things.

Precondition: 
|crossword| = 5x5
∀ x ∈ crossword : 1 ≤ x ≤ 26

每个人都试图在他们生活中的某个时刻解决纵横字谜。我们将通过添加一个密码来混合经典之谜。密码填字游戏用网格中的每个白色单元格的线索替换每个条目的线索。这些线索是从1到26的整数，包括端点。与任何其他填字游戏一样，目标是为每个单元确定正确的字母。在密码填字游戏中，这26个数字作为这些字母的密码：共享匹配号码的单元格填充了匹配的字母，没有两个数字代表同一个字母。所有结果条目必须是有效的单词。

对于这个任务，你应该解决密码填字游戏。给你一个填字模板列表（二维数组）的列表（二维数组）（从0到26），其中0是一个空白单元格和其他数字是加密的字母。你会得到一个填字游戏的列表。你应该用一个给定的单词来填充该模板，并将解决的填字词作为一个列表与字母返回。空白单元格被替换为空格（0 =>“”）。

单词被放置在没有对角线的行和列中。填字游戏包含六个单词，每个单词有五个字母。这些词被放置在一个网格中。

密填字游戏
输入：密码填字游戏列表与整数列表。单词作为字符串的列表。
输出：填字游戏的解决方案列表与字母列表。

如何使用：这是一种限制问题。你有规则，应该尝试找到符合这些规则的组合。这个概念可以帮助您解决日程安排冲突，以及您会遇到许多变量和限制等情况。
'''
