'''
Your task in this mission is to truncate a sentence to a length, that does not exceed a given number of characters.

If the given sentence already is short enough you don't have to do anything to it, but if it needs to be truncated the omission must be indicated by concatenating an ellipsis ("...") to the end of the shortened sentence.

The shortened sentence can contain complete words and spaces.
It must neither contain truncated words nor trailing spaces.
The ellipsis has been taken into account for the allowed number of characters, so it does not count against the given length.

Input: Two arguments:

one-line sentence as a string
max length of the truncated sentence as an int
Output: The shortened sentence plus the ellipsis (if required) as a one-line string.

Examples:

cut_sentence("Hi my name is Alex", 4) == "Hi..."
cut_sentence("Hi my name is Alex", 8) == "Hi my..."
cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"
cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"

Precondition:
line.startswith(' ') == False
0 < len(line) ≤ 79
0 < length ≤ 76
all(char in string.ascii_letters + ' ' for char in line)

你在这个任务中的任务是截短一个句子，长度不超过给定数量的字符。

如果给定的句子已经足够短，则不必做任何事情，但是如果需要截断，则必须通过将省略号（“...”）连接到缩短的句子的末尾来指示省略。

缩短的句子可以包含完整的单词和空格。
它不能包含截短的单词和尾部空格。
省略号已被考虑到允许的字符数，所以它不计算给定的长度。

输入：两个参数：

单行句作为一个字符串
截断句子的最大长度为int
输出：缩短的句子加上省略号（如果需要）作为单行字符串。
'''


def cut_sentence(line, length):
    if len(line) <= length:
        return line
    else:
        line_list = line.split(' ')
        count = 0
        result_list = []
        for li in line_list:
            count += len(li) + 1
            result_list.append(li)
            if count - 1 > length:
                result_list.remove(li)
                return ' '.join(result_list) + '...'
            if count - 1 == length:
                return ' '.join(result_list) + '...'
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cut_sentence("Hi my name is Alex",10) == "Hi my name..."
    assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    print('Done! Do you like it? Go Check it!')