"""
Your mission here is to create a function that gets an tuple and returns a tuple with 3 elements - first, third and second to the last for the given tuple

Input: A tuple, at least 3 elements long.

Output: A tuple.

Example:

easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
easy_unpack((6, 3, 7)) == (6, 7, 3)

你的任务是创建一个函数，获取一个元组并返回一个包含3个元素的元组 - 第一个，第三个和倒数第二个

输入：一个元组，至少3个元素长。

输出：一个元组。

"""

def easy_unpack(elements):
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    # your code here

    return (elements[0],) + (elements[2],) + (elements[-2],)
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')
