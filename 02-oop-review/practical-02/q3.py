# Language class has no attributes, but has a method called good_morning.
# The Maori, Japanese & German class inherit from Language class. When you
# execute the following code, what is happening & why is it happening?
# Refactor the code to display the expected output.

class Language:
    def good_morning(self):
        raise NotImplementedError

class Maori(Language):
    pass

class Japanese(Language):
    pass

class German(Language):
    pass

def main():
    maori = Maori()
    japanese = Japanese()
    german = German()
    for lang in (maori, japanese, german):
        lang.good_morning()

if __name__ == '__main__':
    main()

# Expected output:

# Morena
# おはようございます
# Guten Morgen

