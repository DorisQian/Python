'''
I believe that many of you have dealt with such a problem. One day you are working in the text editor, saving the document and closing it. And the next day you are re-reading the text and realizing that one of the previous versions was better but there is no way to get it back. This thing can be easily handled by the version control system (for example, git), but it’s used mostly by the developers and not the ordinary people who work with texts. In this mission you’ll help the latter by creating a text editor prototype that supports the version control system, which will allow to save different versions of the text and restore any one of them.
Your task is to create 2 classes: Text and SavedText. The first will works with texts (adding, font changing, etc.), the second will control the versions and save them.

Class Text should have the next methods:
write(text) - adds (text) to the current text;
set_font(font name) - sets the chosen font. Font is applied to the whole text, even if it’s added after the font is set. The font is displayed in the square brackets before and after the text: "[Arial]...example...[Arial]". Font can be specified multiple times but only the last variant is displays;
show() - returns the current text and font (if is was set);
restore(SavedText.get_version(number)) - restores the text of the chosen version.

Class SavedText should have the next methods:
save_text(Text) - saves the current text and font. The first saved version has the number 0, the second - 1, and so on;
get_version(number) - this method works with the 'restore' method and is used for choosing the needed version of the text.

In this mission you can use the Memento design pattern.

Example:

text = Text()
saver = SavedText()
    
text.write("At the very beginning ")
saver.save_text(text)
text.set_font("Arial")
saver.save_text(text)
text.write("there was nothing.")
text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
text.restore(saver.get_version(0))
text.show() == "At the very beginning "

Input: information about the text and saved copies.

Output: the text after all of the commands.

How it is used: To save the object’s previous states with the ability to return to them, in case something goes wrong.

Precondition: No more than 10 saved copies.
验证没过，自己assert没问题
'''


class Text:
	text = ''

	def write(self, texts):
		if ']' in self.text:
			index = self.text.index(']')
			fonts = self.text[:index + 1]
			current = self.text.rstrip(fonts)
			self.text = current + texts + fonts
		else:
			self.text += texts
		return self.text

	def set_font(self, font):
		if '[' in self.text:
			index = self.text.index(']')
			fonts = self.text[:index + 1]
			self.text.replace(fonts, '[%s]' % font)
		else:
			self.text = ('[{0}]' + self.text + '[{0}]').format(font)

	def show(self):
		print(self.text)
		return self.text

	def restore(self, version):
		self.text = version
		return self.text


class SavedText:
	version = []

	def save_text(self, texts):
		self.version.append(texts.text)
		#print(self.version)

	def get_version(self, number):
		self.text = self.version[number]
		return self.text


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	'''
    text = Text()
    saver = SavedText()
    
    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")


	text_1 = Text()
	saver_1 = SavedText()
	text_1.write("At the very beginning ")
	saver_1.save_text(text_1)
	text_1.set_font("ComicSans")
	text_1.write("there was nothing.")
	text_1.restore(saver_1.get_version(0))
	assert text_1.show() =="At the very beginning "
	'''
	text_2 = Text()
	saver_2 = SavedText()
	text_2.write("Tomorrow at 7:15 PM.")
	saver_2.save_text(text_2)
	text_2.set_font("ComicSans")
	text_2.write(" Sorry. 7:15 AM.")
	saver_2.save_text(text_2)
	text_2.write(" Near the stadium.")
	text_2.restore(saver_2.get_version(1))
	assert text_2.show() == "[ComicSans]Tomorrow at 7:15 PM. Sorry. 7:15 AM.[ComicSans]"
