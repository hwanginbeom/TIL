S= 'ababababababa'
pattern = 'aabba'


count = 0
for i in range(0, len(S) - len(pattern) +1):
    true_code = 0
    code = S[i:i + len(pattern)]
    for j in range(0,len(pattern)):
        value = code.find(pattern[j])
        if value != -1:
            true_code +=1
            code = code[0:value] +code[value+1:]

    else:
        if true_code == len(pattern):
            count+=1
print(count)
# a ='abcdef'
# value = 2
# print(a[0:value])

#     #         if S[i:i + len(pattern)][j] == pattern[j]:
# #             a=0
# #
# #     print(S[i:i+len(pattern)])
#
# # s = 'python is fun'
# # c = 'z'
# # print(s.find(c))