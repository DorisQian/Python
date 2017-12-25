"""
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once. Two words are anagrams to each other if we can get one from another by rearranging the letters. Anagrams are case-insensitive and don't take account whitespaces. For example: "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not.

You are given two words or phrase. Try to verify are they anagrams or not.

Input: Two arguments as strings.

Output: Are they anagrams or not as boolean (True or False)

Example:

verify_anagrams("Programming", "Gram Ring Mop") == True
verify_anagrams("Hello", "Ole Oh") == False
verify_anagrams("Kyoto", "Tokyo") == True
    
How it is used: Anagramming can be a fun way to train your brain, but they have and another application. Psychologists use anagram-oriented tests, often called "anagram solution tasks", to assess the implicit memory. Anagrams are connected to pseudonyms, by the fact that they may conceal or reveal, or operate somewhere in between like a mask that can establish identity. In addition to this, multiple anagramming is a technique sometimes used to solve some kinds of cryptograms.

Precondition: 0 < |first_word| < 100;
0 < |second_word| < 100;
Words contain only ASCII latin letters and whitespaces.

字谜是一种文字游戏，其结果是重新排列单词或短语的字母，从而产生一个新的单词或短语，使用所有的原字母一次。两个字是字谜，如果我们可以通过重新排列字母来从另一个单词中得到一个单词。Anagrams不区分大小写，不考虑空格。例如:“Gram Ring Mop”和“Programming”是anagrams。但是“你好”和“Ole Oh”不是。
你有两个词或短语。试着验证他们是否字谜。

输入:两个参数作为字符串。

输出:是否为anagrams或not as boolean(True或False)

如何使用:Anagramming可以很有趣的训练你的大脑，但是他们有和另外一个应用。心理学家使用面向anagrama的测试(通常称为“anagram解决任务”)来评估内隐记忆。字谜被连接到假名，因为它们可能隐藏或揭示，或在介于两者之间的某个地方运作，就像一个可以建立身份的面具。除此之外，多个anagramming是一种用来解决某些密码的技术。
"""

def verify_anagrams(first_word, second_word):
    return True or False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"