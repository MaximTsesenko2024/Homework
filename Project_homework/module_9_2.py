first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]
print(first_result)
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(second_result)
third_result = {y: len(y) for x in (first_strings, second_strings) for y in x if not len(y) % 2}
print(third_result)
