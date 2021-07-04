def solution(S, pattern):
    count = 0
    for i in range(0, len(S) - len(pattern) + 1):
        true_code = 0
        for j in range(0, len(pattern)):
            value = S[i:i + len(pattern)].find(pattern[j])
            if value != -1:
                true_code += 1
        else:
            if true_code == len(pattern):
                count += 1

    answer = count
    return answer