'''
Sometimes you find yourself in a situation where among a huge number of files on your computer or in a 
separate folder you need to find files of a certain type - for example, images with the extension '.jpg' 
or documents with the extension '.txt', or even files that have the word 'butterfly' in their name. 
Doing this manually can be time-consuming. 'Matching' or patterns for searching files by a specific mask are 
just what you need for these sort of challenges.
This mission will help you understand how this works.

You need to find out if the given unix pattern matches the given filename.

Let me show you a couple of small examples of matching the filenames in the unix-shell. For example, 
* matches everything and *.txt matches all of the files that have txt extension. Here is a small table that 
shows symbols that can be used in patterns.

*	matches everything
?	matches any single character
Input: Two arguments. Both are strings.

Output: Bool.

Example:

unix_match('somefile.txt', '*') == True
unix_match('other.exe', '*') == True
unix_match('my.exe', '*.txt') == False
unix_match('log1.txt', 'log?.txt') == True
unix_match('log12.txt', 'log?.txt') == False
unix_match('log12.txt', 'log??.txt') == True

How it is used: in the unix-shell

Precondition: 0 < len(strings) < 100
'''
import re
def unix_match(filename: str, pattern: str) -> bool:
    #patten = re.compile(pattern.replace('*', '.'))
    #print(patten)
    pattern = pattern.replace('.', '\.').replace('*', '.+').replace('?', '.')
    print(pattern)
    match_list = re.findall(pattern, filename)
    match = ''.join(match_list)
    print(match)
    if match == filename:
        return True
    else:
        return False


if __name__ == '__main__':
    #print("Example:")
    #print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

