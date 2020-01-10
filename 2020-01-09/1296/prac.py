nums = [15,16,17,18,19,16,17,18,19,20,6,7,8,9,10,3,4,5,6,20]
k = 5

# def isPossibleDivide(nums, k):
#     if len(nums) % k:
#         return False
#     else:
#         for x in nums:
#             temp = [e+[x] for e in r]
#             r

#         return True

# 부분집합 만들었을 때 k개 안겹치는거 만큼 있는지. 있으면 True 없으면 False 리턴

# def perm(arr, cnt, empty, visited):
#     if cnt == k:
#         print(empty)
#     else:
#         for i in range(len(nums)):
#             if not visited[i]:
#                 visited[i] = 1
#                 empty.append(arr[i])
#                 perm(arr, cnt+1, empty, visited)
#                 empty.pop()
#                 visited[i] = 0

# perm(nums, 0, [], [0]*len(nums))

# def combination(idx, result, depth):
#     if depth == lenth:
#         print(result.strip())
#     else:
#         for x in range(idx, num+1):
#             combination(x+1, result+str(x)+' ', depth+1)

# num, lenth = map(int, input().split())
# combination(1, '', 0)

def setting(nums, k):
    q = len(nums) // k  # 뭉탱이 수
    q_child = len(nums) // q  # 한 뭉탱이에 들어가는 애들
    num_count = []
    count_over_two = 0
    for i in nums:
        num_count.append(nums.count(i))
        if nums.count(i) > 1:
            count_over_two += 1
    if len(nums) % k:
        return False
    elif len(set(nums)) < q:
            return False
    elif max(num_count) > q_child:
        return False
    elif count_over_two > q_child:
        return False
    else:
        return True

print(sorted(nums))
print(setting(nums, k))
