#!/usr/bin/env python3

class MyString:
    
    def __init__(self, value = ""):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if type(value) == str:
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self.value.endswith("."):
            return True
        else:
            return False
    def is_question(self):
        if self.value.endswith("?"):
            return True
        else:
            return False
    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        else:
            return False

    def count_sentences(self):
        if not self.value:
            return 0
        sentence_endings = {'.', '!', '?'}
        count = 0
        in_sentence = False
        for char in self.value:
            if char in sentence_endings:
                if in_sentence:  # Counting one sentence per ending mark
                    count += 1
                    in_sentence = False
            elif char.isalpha() or char.isdigit():  # Any alphanumeric character means we're inside a sentence
                in_sentence = True
        return count