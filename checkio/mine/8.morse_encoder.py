'''
Your task is to encrypt the text message using the Morse code. The input text will consist of letters (in uppercase and lowercase), numbers and whitespaces. There won't be any special characters ('&', '?', '#' etc.)
You need to use 3 spaces between words and 1 space between each letter of each word.

example

Input: The secret message as a string.

Output: The same string, but encrypted.

Example:

morse_encoder("some text") == "... --- -- .   - . -..- -"
morse_encoder("2018") == "..--- ----- .---- ---.."
morse_encoder("It was a good day") == ".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"

How it is used: For cryptography and spy work.

Precondition:
0 < len(text) < 50
Only English letters (in uppercase and lowercase), numbers and whitespaces.

您的任务是使用莫尔斯码对文本消息进行加密。 输入文本将由字母（大写和小写），数字和空格组成。 
不会有任何特殊字符（'＆'，'？'，'＃'等）
您需要在每个单词的每个字母之间在单词和1个空格之间使用3个空格。

'''

MORSE = {'a': '.-',    'b': '-...',  'c': '-.-.',
         'd': '-..',   'e': '.',     'f': '..-.',
         'g': '--.',   'h': '....',  'i': '..',
         'j': '.---',  'k': '-.-',   'l': '.-..',
         'm': '--',    'n': '-.',    'o': '---',
         'p': '.--.',  'q': '--.-',  'r': '.-.',
         's': '...',   't': '-',     'u': '..-',
         'v': '...-',  'w': '.--',   'x': '-..-',
         'y': '-.--',  'z': '--..',  '0': '-----',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.'
        }


def morse_encoder(text):
	#replace this for solution
	result = ''
	for word in text.lower().split(' '):
		for w in word:
			result += MORSE[w] + ' '
		result += ' ' * 2
	return result.rstrip(' ')


if __name__ == '__main__':
	print("Example:")
	print(morse_encoder('some text'))

	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert morse_encoder("some text") == "... --- -- .   - . -..- -"
	assert morse_encoder("2018") == "..--- ----- .---- ---.."
	assert morse_encoder("It was a good day") == ".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"
	print("Coding complete? Click 'Check' to earn cool rewards!")
