class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuations = {',', '.', '=', '!', '?', ';', ':', ' - '}
        for file_name in self.file_names:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    for punc in punctuations:
                        content = content.replace(punc, ' ')
                        words = content.split()
                    all_words[file_name] = words
        return all_words
    def find(self, word):
        all_words = self.get_all_words()
        word = word.lower()
        positions = {}

        for name, words in all_words.items():
            if word in words:
                positions[name] = words.index(word) + 1   # Индексация начинается с 1
            else:
                positions[name] = None

        return positions

    def count(self, word):
        all_words = self.get_all_words()
        word = word.lower()
        counts = {}
        for name, words in all_words.items():
            counts[name] = words.count(word)
        return counts


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))


# finder3 = WordsFinder('Rudyard Kipling - If.txt')
# print(finder3.get_all_words())
# print(finder3.find('if'))
# print(finder3.count('if'))
#

# finder4 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder4.get_all_words())
# print(finder4.find('captain'))
# print(finder4.count('captain'))








