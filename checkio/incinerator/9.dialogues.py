'''
The modern world is filled with means of communication - the social networks, messengers, phone calls, SMS etc. 
But sometimes in every communication channel a flaw can be detected and in the moments like that you think to 
yourself: "I should create my own messenger which won’t have problems like this one".
In this mission you’ll get your chance.
Your task is to create a Chat class which could help a Human(name) and Robot(serial_number) to make a conversation. 
This class should have a few methods:
connect_human() - connects human to the chat.
connect_robot() - connects robot to the chat.
show_human_dialogue() - shows the dialog as the human sees it - as simple text.
show_robot_dialogue() - shows the dialog as the robot perceives it - as the set of ones and zeroes. 
To simplify the task, just replace every vowel ('aeiouAEIOU') with "0", and the rest symbols 
(consonants, white spaces and special signs like ",", "!", etc.) with "1".
Dialog for the human should be displayed like this:
(human name) said: message text
(robot serial number): message text
For the robot:
(human name) said: 11100100011
(robot serial number) said: 100011100101
Interlocutors should have a send() method for sending messages to the dialog.
In this mission you could use the Mediator design pattern.

Example:

chat = Chat()
karl = Human("Karl")
bot = Robot("R2D2")
chat.connect_human(karl)
chat.connect_robot(bot)
karl.send("Hi! What's new?")
bot.send("Hello, human. Could we speak later about it?")
chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""


Input: Interlocutors and the text of messages.

Output: A dialog (the multiline string).

How it is used: For creating a connection and sending/receiving the information.

Precondition: 2 interlocutors.
'''

VOWELS = "aeiou"
all_msg = []


def loading(kind, message):
	all_msg.append((kind, message))


class Chat:
	def connect_human(self, human):
		self.human = human

	def connect_robot(self, robot):
		self.robot = robot

	def show_human_dialogue(self):
		message = ''
		for msg in all_msg:
			if msg[0] == 'man':
				message += '%s said: %s' % (self.human.name, msg[1]) + '\n'
			elif msg[0] == 'robot':
				message += '%s said: %s' % (self.robot.name, msg[1]) + '\n'
		print(message)
		return message.rstrip('\n')

	def show_robot_dialogue(self):
		message = ''
		for msg in all_msg:
			said = msg[1].lower()
			mark = ''
			for word in said:
				if word in VOWELS:
					mark += '0'
				else:
					mark += '1'
			if msg[0] == 'man':
				message += '%s said: %s' % (self.human.name, mark) + '\n'
			elif msg[0] == 'robot':
				message += '%s said: %s' % (self.robot.name, mark) + '\n'
		print(message)
		return message.rstrip('\n')


class Human:
	def __init__(self, name):
		self.name = name

	def send(self, message):
		self.man_message = message
		loading('man', self.man_message)


class Robot:
	def __init__(self, name):
		self.name = name

	def send(self, message):
		self.ro_message = message
		loading('robot', self.ro_message)

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing

	chat = Chat()
	karl = Human("Karl")
	bot = Robot("R2D2")
	chat.connect_human(karl)
	chat.connect_robot(bot)
	karl.send("Hi! What's new?")
	bot.send("Hello, human. Could we speak later about it?")
	
	assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""

	assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

	# print("Coding complete? Let's try tests!")

	chat = Chat()
	bob = Human('Bob')
	ann = Robot('Ann-1244c')
	chat.connect_human(bob)
	chat.connect_robot(ann)
	bob.send("Hi, Ann! Is your part of work done?")
	ann.send("Hi, Bob. Sorry, I need a few more hours. Could you wait, please?")
	bob.send("Ok. But hurry up, please. It's important.")
	ann.send("Sure, thanks.")

	assert chat.show_human_dialogue() == """Bob said: Hi, Ann! Is your part of work done?
Ann-1244c said: Hi, Bob. Sorry, I need a few more hours. Could you wait, please?
Bob said: Ok. But hurry up, please. It's important.
Ann-1244c said: Sure, thanks."""