a=[1,3,4,2,2,2,2,2,6]

#append 리스트 맨 마지막에 요소 추가
a.append(0)
print(a)

#reverse 리스트 뒤집기 (단순 뒤집기)
a.reverse()
print(a)

#sort 정렬: 숫자,알파벳 순서로 정렬 가능. 데이터형이 섞이면 error
a.sort()                #오름차순
print(a)
a.sort(reverse=True)    #내림차순
print(a)

#index(n) n의 위치반환 (첫번째 n)
print(a.index(2))   #3
#print(a.index(7))   #없는 값은 error

#insert 리스트 요소 삽입 (원하는 인덱스에)
a.insert(0,5)   #insert(i,n) n인덱스에 m삽입
print(a)

#remove(x) 리스트 요소 제거 (리스트에서 첫번째로 나오는 x제거)
a.remove(2)
print(a)

#pop 요소 끄집어내기: 맨 마지막 요소를 반환하고, 해당 요소는 삭제
print(a.pop())  #0
print(a)        #[5, 6, 4, 3, 2, 1]

#count(x) 리스트 내 x의 개수 세기
print(a.count(2))  #4

#extend([x,y,z]) 리스트 확장: 리스트에 리스트 더하기
a.extend([8,9,10])
print(a)        #[5, 6, 4, 3, 2, 2, 2, 2, 1, 8, 9, 10]
a += [1,2,4]
print(a)        #[5, 6, 4, 3, 2, 2, 2, 2, 1, 8, 9, 10, 1, 2, 4]
