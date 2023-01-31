def solution(s):
    result = []
    for i in range(len(s)):
        s2 = s[0:i]+s[i+1:]
        result.append(s2)
    r = result[0]
    for item in result:
        if item < r:
            r = item
    return r


s = "abcd"
i = 1
print(s[0:i]+s[i+1:])
print(solution("abc"))