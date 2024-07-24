def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = dict({})
    count = 1
    for i in strings:
        strings_positions[(count, file.tell())] = i
        file.write(i + '\n')
        count += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
