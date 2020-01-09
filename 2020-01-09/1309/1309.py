import sys
sys.stdin = open('input.txt', 'r')
word = input()

res_word = []
for i in range(1, len(word)-1):
    if word[i] == '#':
        res_word.pop()
        res_word.pop()
        res_word.append(chr(int(word[i-2])*10+int(word[i-1])+96))
    else:
        res_word.append(chr(int(word[i])+96))
ans = "".join(res_word)
print('"{}"'.format(ans))