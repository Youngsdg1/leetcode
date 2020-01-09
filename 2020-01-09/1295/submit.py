class Solution(object):
    def findNumbers(self, nums):
        cnt = 0
        for num in nums:
            if not len(str(num)) % 2:
                cnt += 1
        return cnt