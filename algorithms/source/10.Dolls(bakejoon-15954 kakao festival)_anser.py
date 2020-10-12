import sys

N, K = map(int, input().split())
prefered = list(map(int, input().split()))

min_std = float('inf')

while (K != (N + 1)):
    stride = 1
    full_range = ((N - K) // stride) + 1

    for i in range(full_range):
        do_list = prefered[i:(i + K)]
        mean = sum(do_list) / K
        var = sum([(x - mean) ** 2 for x in do_list]) / K
        std = var ** 0.5
        if (min_std >= std):
            min_std = std
    K += 1
sys.stdout.write(str(min_std))