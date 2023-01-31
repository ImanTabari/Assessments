def solution(N, K):
    k = K
    count = 0
    for n in range(N, 0, -1):
        if k-n >= 0:
            k -= n
            count += 1
    if k == 0:
        return count
    return -1