
def second_index(text:str, symbol:str):
	try:
		return (text.index(symbol, text.index(symbol) + 1))
	except ValueError:
		return None


if __name__ == '__main__':
	print(second_index("sims", "s"))
	print(second_index("find the river", "e"))
	print(second_index("hi", " "))
	print(second_index("hi mayor", " "))
    # These "asserts" are used for self-checking and not for an auto-testing
	assert second_index("sims", "s") == 3, "First"
	assert second_index("find the river", "e") == 12, "Second"
	assert second_index("hi", " ") is None, "Third"
	assert second_index("hi mayor", " ") is None, "Fourth"
	assert second_index("hi mr Mayor", " ") == 5, "Fifth"
