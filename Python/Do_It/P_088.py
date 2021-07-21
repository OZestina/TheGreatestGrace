#딕셔너리
    #연관배열(Associative array), 해시(Hash) 자료형
    #Key:Value 한 쌍
    #key는 변하지 않는 값 (값이 변하는 리스트는 올 수 없고, 튜플은 key로 이용 가능)

dic = {'name':'pey','phone':'0123456789',1:'hi','a':[3,4,5]}

dic['birth'] = '1117'
dic[3] = (1,2)  #3 Key 추가
dic[3] = (2,3)  #3 Key의 값 변경
print(dic)

del dic['a']    #'a' Key를 가진 쌍 삭제
print(dic)

#keys: Key 리스트 만들기
#리스트 형식이 아니더라도 iterate구문에 사용 가능 (for문 등)
#리스트화 가능
print(dic.keys())   #dict_keys(['name', 'phone', 1, 'birth', 3])
print(list(dic.keys())) #['name', 'phone', 1, 'birth', 3]

for i in dic.keys():
    print(i, dic[i])

#values: Value 리스트 만들기
print(dic.values())
print(list(dic.values()))

#items: K-V 쌍 얻기
print(dic.items())
print(list(dic.items()))

#get(k): Key로 Value 얻기
#get(key, 'default'): key가 없을 경우 default값 반환
print(dic.get('name'))  #pey
print(dic.get('color'))  #None  #key값이 없으면 None 출력(error 메시지 안뜸!)
print(dic.get('color', 0))  #0
print(dic.get('color', '투명'))  #투명

#in: 해당 key가 딕셔너리에 있는지 확인
#반환값 bool
print('name' in dic)    #True
print('color' in dic)   #False

#clear: K-V 쌍 모두 지우기
dic.clear()
print(dic)    #{}
