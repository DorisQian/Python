"""
You are given two strings and you have to find an index of the second occurrence of the second string in the first one.

Let's go through the first example where you need to find the second occurrence of "s" in a word "sims". It’s easy to find its first occurrence with a function index or find which will point out that "s" is the first symbol in a word "sims" and therefore the index of the first occurrence is 0. But we have to find the second "s" which is 4th in a row and that means that the index of the second occurrence (and the answer to a question) is 3.

Input: Two strings.

Output: Int or None

给你两个字符串，你必须在第一个字符串中找到第二个字符串的第二个索引。

让我们来看看第一个例子，你需要在“sims”中找到第二个“s”。用函数索引很容易找到它的第一次出现，或者找到哪个指出“s”是单词“sims”中的第一个符号，因此第一次出现的索引是0.但是我们必须找到第二个“ s“，这是连续的第四次，这意味着第二次发生的指数（和一个问题的答案）是3。

输入：两个字符串。

输出： Int或None

Example:

second_index("sims", "s") == 3
second_index("find the river", "e") == 12
second_index("hi", " ") is None
<<<<<<< HEAD
=======

>>>>>>> origin/original
"""

def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    
    if symbol in text:
        num = 0
        for str in text :
            if str != symbol:
                num += 1
            else:
                break
        if symbol in text[num+1:]:
            for str2 in text[num+1:] :
                if str2 != symbol:
                    num += 1
                else:
                    num += 1
                    break
            return num
        else:
            return None
    else:
        return None


if __name__ == '__main__':
    print(second_index("sims", "s"))
    print(second_index("find the river", "e"))
    print(second_index("hi", " "))
    print(second_index("hi mayor", " "))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"

