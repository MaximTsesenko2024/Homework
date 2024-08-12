def all_variants(text):
    i = 0
    j = 1
    while True:
        yield text[i:i+j]
        i += 1
        if i + j > len(text):
            i = 0
            j += 1
        if j > len(text):
            break


a = all_variants("abc")
for i in a:
    print(i)
