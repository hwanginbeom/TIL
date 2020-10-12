def d(n):
    return n + sum([int(x) for x in str(n)])
# str 을 91 이라고 들어오면 9 랑 1 이 들어온다.

sub = [d(i) for i in range(5000)]
res = [n for n in range(5000) if n not in sub]
sum(res)


