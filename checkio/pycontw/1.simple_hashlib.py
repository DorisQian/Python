'''
In a correctly designed system, a plain password is not stored in the database. Instead, a hash of the password is stored. You are going to verify a password and you will need to use the same one-way function to calculate the hash and do a comparison.
在正确设计的系统中，普通密码不存储在数据库中。
而是存储密码的哈希值。
您将验证密码，您将需要使用相同的单向函数来计算哈希值并进行比较。
Input: Two arguments. A string to be hashed and a hash algorithm as a string (unicode utf8).
输入：两个参数。 要散列的字符串和散列算法作为字符串（unicode utf8）。
Output: Hexadecimal hash for for input string using given algorithm as a string.
输出：使用给定算法作为字符串的输入字符串的十六进制哈希

Example:

checkio('welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86bhe3d7'
checkio('happy spam', 'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'

Precondition:
algorithm in ("md5", "sha224", "sha256", "sha384", "sha512", "sha1")
0 ≤ len(hashed_string) ≤ 2**10
'''
import hashlib
def checkio(hashed_string, algorithm):
    return getattr(hashlib, algorithm)(hashed_string.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86b3d7'
    assert checkio('happy spam', 'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'