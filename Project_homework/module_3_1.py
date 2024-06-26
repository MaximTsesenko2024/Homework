calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.lower(), string.upper()


def is_contains(string, list_str):
    count_calls()
    res = False
    for i in list_str:
        if string.lower() == i.lower():
            res = True
            break
    return res


a = string_info('UrBan')
print(a)
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
