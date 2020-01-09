import sys
sys.stdin = open('input.txt', 'r')
nums = [12, 345, 2, 6, 7896]
cnt = 0
for num in nums:
    if not len(str(num)) % 2:
        cnt += 1
print(cnt)