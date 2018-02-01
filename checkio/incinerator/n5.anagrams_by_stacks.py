'''
You have been given two anagrams as a string, separated by dash. You need to rearrange the letters to turn the first word into the second. The tools you have for this mission are two stacks and a one-letter buffer. The first stack is the beginning of a word; the second stack is where you will put the anagram. The word is placed in the stack, letter by letter. The first letter of the anagram is placed in the bottom stack and the last letter in the middle stack, until it is needed as the end of the anagram. You need to return the shortest sequence of actions to move and turn the word in the first stack into the anagram in the second. The first stack is labeled 1, the second is labeled 2, and the buffer as 0. The action is written as a string of two numbers which signify the original location of the letter and the new location. For example: 12 means that from the first stack, we take the last letter and place it at the end of the second stack. For the result, you need to get a string that lists the steps, separated by commas.

anagrams_by_stacks
Input: Two words separated by dash as a string.

Output: A sequence of actions as a string.

Example:

checkio("rice-cire") == "10,12,12,12,02"
checkio("tort-trot") == "12,12,12,12"
checkio("hello-holle") == "12,12,12,12,10,21,21,21,21,02,12,12,12,12"
checkio("anagram-mragana") == "12,10,12,02,12,12,12,12"
checkio("mirror-mirorr") == "12,12,10,12,12,02,10,21,21,21,21,21,02,12,12,12,10,21,21,21,02,12,12,12,12"
#It can be solved more the one way.
1
2
3
4
5
6
How it is used: Here you can play with stacks and how they work in games. We see stacks in everyday life, they’re in the books in our library, and the blank sheets of paper in our printer tray.

Precondition: 1 ≤ |word| < 10
Words contains only ASCII letters in lowercase.
'''
