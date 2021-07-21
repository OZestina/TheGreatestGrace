# set: 집합자료형
    #중복을 허용하지 않는다
    #Unordered 순서가 없다 -> 인덱싱 불가!
    #리스트나 튜플로 변환 후에는 인덱싱 접근 가능

s = set()       # 빈거
print(s)        # set()
s2 = set([1, 2, 3])
print(s2)       # {1,2,3}
s3 = set("Hello")
print(s3)       # {'o', 'l', 'H', 'e'}
s4 = set(str(112))
print(s4)       #{'2', '1'}
s5 = set(["hello", "hi", "hi"])
print(s5)       #{'hello', 'hi'}

l2 = list(s2)
print(l2)       #[1, 2, 3]
t2 = tuple(s2)
print(t2)       #(1, 2, 3)

l3 = list(s3)
print(l3)       #['e', 'H', 'o', 'l']
t3 = tuple(s3)
print(t3)       #('e', 'H', 'o', 'l')

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
#교집합 &, intersection
print(s1&s2)                #{4, 5, 6}
print(s1.intersection(s2))  #{4, 5, 6}

#합집합 |, union
print(s1|s2)                #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))         #{1, 2, 3, 4, 5, 6, 7, 8, 9}

#차집합 -, difference
print(s1-s2)                #{1, 2, 3}
print(s1.difference(s2))    #{1, 2, 3}
print(s2-s1)                #{8, 9, 7}
print(s2.difference(s1))    #{8, 9, 7}

#add: 값 1개 추가
s1.add(8)
print(s1)   #{1, 2, 3, 4, 5, 6, 8}

#update: 값 여러개 추가
s2.update([3,2,4,5])
print(s2)   #{2, 3, 4, 5, 6, 7, 8, 9}

#remove: 특정 값 제거
s1.remove(3)
print(s1)   #{1, 2, 4, 5, 6, 8}
