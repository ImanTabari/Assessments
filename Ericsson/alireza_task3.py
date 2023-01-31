import math
def solution(T, R):
    t = ["" for x in T]
    for i in range(len(T)):
        if T[i][-1] >= "a" and T[i][-1] <= "z":
            t[i] = T[i][-1]
            T[i] = T[i][:-1]

    groups = list(set(T))

    result = []
    for i in range(len(T)):
        if R[i] != "OK":
            result.append(T[i])
    result = list(set(result))

    r = len(groups)-len(result)
    r = r/len(groups)
    r = r*100
    return math.floor(r)