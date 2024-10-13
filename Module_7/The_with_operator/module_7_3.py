class WordsFinder:
    def __init__(self, *files):
        self.file_name = [name for name in files]

    def get_all_words(self):
        all_words = {}
        for name in self.file_name:
            with open(name, 'r', encoding='utf-8') as file:
                words = moderning(file.read())
                all_words.update({name: [word for word in words]})
        return all_words

    def find(self, word):
        word = word.lower()
        for name in self.file_name:
            with open(name, 'r', encoding='utf-8') as file:
                words = moderning(file.read())
            return {name: words.index(word) + 1}

    def count(self, word):
        word = word.lower()
        for name in self.file_name:
            with open(name, 'r', encoding='utf-8') as file:
                words = moderning(file.read())
            return {name: words.count(word)}

def moderning(text):
    text = text.lower()
    for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
        content = text.replace(char, ' ')
    return content.split()


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
