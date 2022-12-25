def to_upper(word):
    return word.upper()


word_lst = ['binoj', 'cinoj']
mp_obj = map(to_upper, word_lst)

for x in mp_obj:
    print(x)
