import re

data = """
park 901211-1034555
kim 901231-1034456
hong 901211-10345556
"""

pat = re.compile("(\d{6})[-](\d{7})")
print(pat.sub("\g<1>-*******",data))
# park 901211-*******
# kim 901231-*******
# hong 901211-*******6


#match: 문자열의 처음부터 조건 만족하는지
p1 = re.compile('[a-z]+')
m = p1.match("python")
print(m)    # 조건에 부합하면 match 객체 돌려줌
            # <re.Match object; span=(0, 6), match='python'>
m2 = p1.match("3python")
print(m2)   # 조건에 부합하지 않아 None 리턴

if m:
    print(m.group())    #python
else:
    print('no match')

#search: 문자열 전체 중 만족하는 부분이 있는지
m3 = p1.search("python")
print(m3)   # 조건에 부합하면 match 객체 돌려줌
            # <re.Match object; span=(0, 6), match='python'>
m4 = p1.search("3pyth0n")
print(m4)   # <re.Match object; span=(1, 5), match='pyth'>
            # 앞의 한 부분만 돌려줌
m5 = p1.search("397460N")
print(m5)   # 조건에 부합하지 않아 None 리턴

#findall: 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴
result = p1.findall("life is too short")
print(result)   #['life', 'is', 'too', 'short']

#finditer: 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴
result2 = p1.finditer("life is too short")
print(result2)  #<callable_iterator object at 0x01C2D050>
#for r in result2: print(r)
for r in result2: print(r.start(), r.end(), r.span(), r.group())

#re모듈: 하기 두개는 같다!
q = re.compile('[0-9]+').match('123')
q2 = re.match('[0-9]+','123')


