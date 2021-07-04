letters='zbgaj'
k=3

letters_list = []
for i in letters:
    letters_list.append(i)
sum_word = ''
letters_list2=letters_list[:-1]
for i in range( k-1 ):
    if k == len(letters):
        sum_word=letters
        break
    sum_word += max(letters_list2[:len(letters_list)-k])
    for j in range(0,len(letters_list2)):
        if letters_list2[j] == max(letters_list2[:len(letters_list)-k]):
            number = j
            break
    letters_list2 = letters_list2[j+1:]
else:
    sum_word = sum_word + letters[-1]
print(sum_word)
