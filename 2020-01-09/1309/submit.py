class Solution(object):
    def freqAlphabets(self, s):
        res_word = []
        for i in range(len(s)):
            if s[i] == '#':
                res_word.pop()
                res_word.pop()
                res_word.append(chr(int(s[i-2])*10+int(s[i-1])+96))
            else:
                res_word.append(chr(int(s[i])+96))
        ans = "".join(res_word)
        return ans
# print(word)
# print(ord('a'))  # 97:a -> 1: a
# print(ord('A') == 65)  # False
# print(chr(97))
# print(ord('j'))