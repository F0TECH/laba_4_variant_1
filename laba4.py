import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        return string.ascii_uppercase

    def latters_num(self):
        return len(string.ascii_uppercase)


class EngAlphabet(Alphabet):
    _letters_num = 26

    def __init__(self):
        super().__init__("En", string.ascii_uppercase)

    def is_en_letter(self, letters):
        return letters in string.ascii_uppercase

    def latters_num(self):
        return self._letters_num

    @staticmethod
    def example():
        return "Dick"


a = EngAlphabet()
print(a.print())
print(a.latters_num())
print(a.is_en_letter("F"))
print(a.is_en_letter("Ф"))
print(a.example())