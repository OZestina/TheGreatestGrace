# https://school.programmers.co.kr/learn/courses/4008/lessons/13246

# 1st try => success
dict_alpha = {}

my_str = input().strip()

for letter in my_str:
    if letter in dict_alpha:
        dict_alpha[letter] += 1
    else:
        dict_alpha[letter] = 1

max_v = dict_alpha[max(dict_alpha, key=dict_alpha.get)]
answer = []
for k in dict_alpha:
    if dict_alpha[k] == max_v:
        answer.append(k)
answer.sort()
print(''.join(answer))



# 2nd try (made it simple)
my_str = input().strip()

dic = {}
for letter in my_str:
    dic[letter] = dic[letter] + 1 if letter in dic else 1

max_v = max(dic.values())

answer = []
for k, v in dic.items():
    if v == max_v:
        answer.append(k)
print(''.join(sorted(answer)))



# 3nd try (다른 사람의 풀이 참고)
# 아 맞다 Counter!
from collections import Counter

my_str = input().strip()
max_value = max(Counter(my_str).values())
print(''.join(sorted([k for k, v in Counter(my_str).items() if v == max_value])))
