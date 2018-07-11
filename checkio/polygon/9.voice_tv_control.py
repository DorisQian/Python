'''
Technologies are developing very fast - only 50 years ago a simple black and white TV was almost a great treasure! And now even the big cool color TV with remote control is the usual thing. Let's try to improve our TV and add to it voice control! At least we will write the simple prototype with Python. It will use the next commands:

first_channel() - turn on the first channel from the list.
last_channel() - turn on the last channel from the list.
turn_channel(N) - turn on the N channel. Pay attention that the channels numbers start from 1, not from 0.
next_channel() - turn on the next channel. If the current channel is the last - turn on the first channel.
previous_channel() - turn on the previous channel. If the current channel is the first - turn on the last channel.
current_channel() - return the name of the current channel.
is_exist(N/'name') - get 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' is exist in the list or "No" in the other case.

The default channel which is turn on before all commands is №1. 
Your task is to create class VoiceCommand and methods which has described above. 
In this mission you could use the Iterator design pattern.

Example:

CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = VoiceCommand(CHANNELS)

controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
controller.is_exist(4) == "No"
controller.is_exist("BBC") == "Yes"

Input: voice commands.

Output: channel name or result of is_exist method.

How it is used: For work with iterable objects.

Precondition: All commands and channel names are correct.
'''

class VoiceCommand(object):
	
	def __init__(self, channels):
		self.channels = channels
		self._current = self.channels[0]

	def first_channel(self):
		self._current = self.channels[0]
		return self._current

	def last_channel(self):
		self._current = self.channels[-1]
		return self._current

	def turn_channel(self, id):
		self._current = self.channels[id - 1]
		return self._current

	def next_channel(self):
		index = self.channels.index(self._current)
		if index == len(self.channels) - 1:
			self._current = self.channels[0]
		else:
			self._current = self.channels[index + 1]
		return self._current

	def previous_channel(self):
		index = self.channels.index(self._current)
		if index == 0:
			self._current = self.channels[-1]
		else:
			self._current = self.channels[index - 1]
		return self._current

	def current_channel(self):
		return self._current

	def is_exist(self, channel):
		if isinstance(channel, int):
			if 0 < channel <= len(self.channels):
				return 'Yes'
			else: return 'No'
		elif isinstance(channel, str):
			if channel in self.channels:return 'Yes'
			else: return 'No'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)
    
    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")