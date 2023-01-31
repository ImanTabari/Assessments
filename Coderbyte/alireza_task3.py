def ArrayChallenge(arr) :
    s_arr = sorted(arr, reverse= True)
    right = [s_arr[0]]
    left = [s_arr[1]]
    result = []
    for i in range(2,len(s_arr)-1,2):
        if sum(right) < sum(left):
            right.append(s_arr[i]) 
            left.append(s_arr[i+1])
        else:
            right.append(s_arr[i+1]) 
            left.append(s_arr[i])
    if sum(right) != sum(left):
        return '-1'
    right.sort()
    left.sort()
    if right[0] < left[0]:
        result = right + left
    else: result = left +right
    return ','.join(map(str,result)) 

#arr = [1,8,11,16,20,21,22,35]
#arr = [1,2,1,5]
arr = [1,2,3,4]
print(ArrayChallenge(arr))       


