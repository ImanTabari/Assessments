from collections import Counter
def solution(A):
    a_dict = Counter(A)
    for item in a_dict:
        if a_dict[item] % 2 != 0:
            return False
    return True