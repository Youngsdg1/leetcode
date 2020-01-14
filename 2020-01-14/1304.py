# 합이 0이고 길이가 n 인 array 만들기


class Solution(object):
    def sumZero(self, n):
        ans = []
        for i in range(1, n//2+1):
            ans.append(-i)
            ans.append(i)
        if n % 2:
            ans.append(0)
        return ans