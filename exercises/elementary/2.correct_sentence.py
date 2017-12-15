def correct_sentence(text: str) -> str:
    """Corrected sentence starting with a capital letter, ending with a dot."""
    print('.' * (not text.endswith('.')))
    return text.capitalize() + '.' * (not text.endswith('.'))

if __name__ == '__main__':
 #   print(correct_sentence("hi"))
 #   print(correct_sentence("greetings, friends"))
 #   print(correct_sentence("Greetings, friends"))
    print(correct_sentence("Greetings, friends."))
    #These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."


