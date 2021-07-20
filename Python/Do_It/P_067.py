#문자열 관련 함수
a = "what is your hobby "
b = "hOBBy"
#count 특정 문자 개수 세기
print(a.count('b')) #2

#find 위치알려주기(1)
print(a.find('b'))  #15 (첫번째 문자의 인덱스값)
print(a.find('k'))  #-1 (문자가 없으면 -1 반환)

#index 위치알려주기(2)
print(a.index('b'))  #15 (첫번째 문자의 인덱스값)
#print(a.find('k')) #없는 문자면 error

#join 문자열 삽입
result = ".".join(a)    #사이사이에 넣는다
print(result)
result2 = ','.join(['a','b','c'])   #리스트 사용의 예 (사이에 넣고 합친다)
print(result2)

#upper 소문자->대문자
print(b.upper())

#lower 대문자->소문자
print(b.lower())

x = '  hi  '
#lstrip 왼쪽 공백 지우기
print(x.lstrip())   #왼쪽의 연속된 공백 모두 제거
#rstrip 오른쪽 공백 지우기
print(x. rstrip())   #오른쪽의 연속된 공백 모두 제거
#strip 오른쪽 공백 지우기
print(x.strip())   #양쪽의 연속된 공백 모두 제거

#replace 문자열 바꾸기
print(a.replace("what","game")) #찾는 단어가 없으면 원본 반환

#split 문자열 나누기
print(a.split())    #공백(스페이스,엔터,탭 등)을 기준으로 문자열 나눔, 리스트화
f = "a:b:c:d"
print(f.split(':')) #기호를 넣으면 해당 기호를 기준으로 나눔
