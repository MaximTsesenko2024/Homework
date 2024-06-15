def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if root_word.lower() in other_words[i].lower() or other_words[i].lower() in root_word.lower():
            same_words.append(other_words[i])
    return same_words


word = input('Введите основное слово: ')
words = input('Введите список слов для проверки (через пробел): ')
List_words = words.split(' ')
print('Основное слово: ', word)
print('Проверяемая последовательность слов: ', List_words)
res = single_root_words(word, *List_words)
print(f'Онокоренные слова: {res} для слова: {word}')
res = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(f'Онокоренные слова: {res} для слова: rich')
res = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(f'Онокоренные слова: {res} для слова: Disablement')
