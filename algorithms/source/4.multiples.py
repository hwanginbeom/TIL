"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
#
# def d(n):
#     return n + sum([int(x) for x in str(n)])
# # str 을 91 이라고 들어오면 9 랑 1 이 들어온다.


result = sum([n for n in range(1, 1000) if n % 3 == 0 or n % 5 == 0])

sum2 = 0

for n in range(1, 1000):
    if n % 3 == 0:
        sum2 += n
    if n % 5 == 0:
        sum2 += n
    # if n % 15 == 0:
    #     sum2 -= n

print(result)
print(sum2)

# >>> result = [num * 3 for num in a if num % 2 == 0]


# res = [n for n in range(5000) if n not in sub]
# sum(res)

