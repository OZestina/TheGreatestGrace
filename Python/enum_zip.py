# enumerate

l = [1, 2, 3]
for i, val in enumerate(l):
    print(i, val)

d = {1: 'key', 2: 'keys'}
for i, (k, v) in enumerate(d.items()):
    print(i, k, v)


# zip
# 요소 수가 다를 때는 가장 작은 수에 맞춘다
a = ['a', 's', 'd']
for x, y, z in zip(l, d, a):
    print(x, y, z)

new_d = {key: val for key, val in zip(l, a)}
print(new_d) #{1: 'a', 2: 's', 3: 'd'}
