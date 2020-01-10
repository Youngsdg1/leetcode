nums = [12,12,2,11,22,20,11,13,3,21,1,13]
k = 3
def ky(nums, k):
    if len(nums)%k != 0:
        return False
    from collections import Counter
    dct = dict(Counter(nums))
    key= list(dct.keys())
    key.sort()
    for i in key:  # number
        if dct[i] > 0:  # 갯수가 남아 있다면
            for j in range(i+1,i+k):  # i 포함 k개 만큼 확인
                if j not in dct.keys():  # 있는 수인지
                    return False
                if dct[j]<dct[i]:  # 더 큰 수의 갯수가 작으면                    return False
                    return False
                dct[j]-=dct[i]  # 아니라면 
    return True
print(ky(nums, k))