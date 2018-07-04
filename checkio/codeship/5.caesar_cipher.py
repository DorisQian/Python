'''
! When we received an encrypted text we've noticed that there are some extra symbols!
Your mission is to decrypt a secret message (which consists of text, the whitespace characters and special chars like "!", "&", "?" etc.) using Caesar cipher where each letter is replaced by another that stands at a fixed distance. For example ("a b c", 3) == "d e f". Also you should ignore/delete all special characters. So the message like this ("!d! [e] &f*", -3) will be decrypted just as "a b c" and nothing more.

example

Input: A Secret message as a string (lowercase letters only, white spaces and special characters)

Output: The same string, but decrypted into a normal text

Example:

to_decrypt("!d! [e] &f*", -3) == "a b c"
to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"

How it is used: For cryptography and to save important information.

Precondition:
0 < len(text) < 50
-26 < delta < 26

！ 当我们收到加密文本时，我们注意到有一些额外的符号！
你的任务是使用凯撒密码解密秘密信息（包括文本，空白字符和特殊字符，如“！”，“＆”，“？”等），其中每个字母被替换为另一个字母 
距离。 例如（“a b c”，3）==“d e f”。 你也应该忽略/删除所有特殊字符。 所以像这样的消息（“！d！[e]＆f *”，-3）将被解密，
就像“a b c”一样，仅此而已。

例

输入：作为字符串的秘密消息（仅限小写字母，空格和特殊字符）
输出：相同的字符串，但解密为普通文本

它如何使用：用于密码学和保存重要信息。
'''

def to_decrypt(cryptotext, delta):
    text = ''.join([s for s in cryptotext if s.isalpha() or s == ' '])
    result = ''
    for s in text:
        if s.isalpha():
            asc = ord(s) + delta
            if asc > 122:
                result += chr(asc - 26)
            elif asc < 97:
                result += chr(asc + 26)
            else:
                result += chr(asc)
        else:
            result += s
    return result

if __name__ == '__main__':
    #print("Example:")
    #print(to_decrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_decrypt("!d! [e] &f*", -3) == "a b c"
    assert to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
    assert to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
    assert to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
    assert to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"
    print("Coding complete? Click 'Check' to earn cool rewards!")