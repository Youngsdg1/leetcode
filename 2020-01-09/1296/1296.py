nums = [12,12,2,11,22,20,11,13,3,21,1,13]
k = 3
def ky(nums, k):
    if len(nums)%k != 0:
        return False
    from collections import Counter
    dct = dict(Counter(nums))
    key= list(dct.keys())
    key.sort()
    print(key)
    print(dct)
    for i in key:
        if dct[i] > 0:
            for j in range(i+1,i+k):
                if j not in dct.keys():
                    return False
                if dct[j]<dct[i]:
                    return False
                dct[j]-=dct[i]
    return True
print(ky(nums, k))