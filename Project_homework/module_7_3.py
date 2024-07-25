class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = []
        for i in file_names:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                string_ = file.read()
                string_ = string_.lower()
                for j in [',', '.', '=', '!', '?', ';', ':']:
                    string_ = string_.replace(j, '')
                string_ = string_.replace(' - ', ' ')
                list_ = string_.split()
                all_words[i] = list_
        return all_words

    def find(self, word):
        found = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                found[name] = words.index(word) + 1
        return found

    def count(self, word):
        count_ = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                count_[name] = words.count(word)
        return count_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
