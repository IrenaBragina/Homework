def all_variants(text):
    len_text = len(text)
    for g in range(1,len_text + 1):
        for k in range (len_text - g + 1):
            yield text[k: k + g]

a = all_variants("abc")
for i in a:
    print(i)


