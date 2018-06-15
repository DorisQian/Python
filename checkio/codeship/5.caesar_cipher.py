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
'''

def to_decrypt(cryptotext, delta):
    #replace this for solution
    return cryptotext

if __name__ == '__main__':
    print("Example:")
    print(to_decrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_decrypt("!d! [e] &f*", -3) == "a b c"
    assert to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
    assert to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
    assert to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
    assert to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"
    print("Coding complete? Click 'Check' to earn cool rewards!")