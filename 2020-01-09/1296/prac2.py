# 시간초과

def settings(nums, k):
    sorted_nums = sorted(nums)
    length = len(nums)
    if length % k:
        return False
    else:
        q = length // k  # 뭉탱이 수
        q_child = length // q  # 한 뭉탱이에 들어가는 애들
        num_group = [[] for _ in range(q)]
        for num in sorted_nums:
            for i in range(q):
                if num not in num_group[i] and len(num_group[i]) < q_child:
                    if not num_group[i]:  # 비어 있으면
                        num_group[i].append(num)
                        break
                    elif abs(num_group[i][-1] - num) == 1:
                        num_group[i].append(num)
                        break
            else:
                print(num_group)
                return False
        else:
            return True

nums = [12,12,2,11,22,20,11,13,3,21,1,13]
k = 3
print(settings(nums, k))