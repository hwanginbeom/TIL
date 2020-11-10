from operator import itemgetter

numbers=[]
N = int(input())

for _ in range(N):
    a, b= (input().split())
    a = int(a)
    numbers.append([a,b])

numbers.sort(key=itemgetter(0))
for i in range(N):
    print(numbers[i][0],numbers[i][1])
