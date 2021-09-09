import re

# | (or)
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)    #<re.Match object; span=(0, 4), match='Crow'>

# ^ (starts with)
print(re.search('^Life','Life is too short'))   #<re.Match object; span=(0, 4), match='Life'>
print(re.search('^Life','My Life'))             #None

# $ (ends with)
print(re.search('short$','Life is too short'))   #<re.Match object; span=(12, 17), match='short'>
print(re.search('short$','Life is too short, phthon')) #None

# \A (start with, re.M 옵션에서도 처음만!)

# \Z (end with, re.M 옵션에서도 맨 마지막만!)

# r \b (구분자) (whitespace)
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))  #<re.Match object; span=(3, 8), match='class'>
print(p.search('no subclass'))      #None

#r \B (구분자없음) (no whitespace)
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))  #None
print(p.search('no subclasses'))    #<re.Match object; span=(6, 11), match='class'>

#그루핑 with ()
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK? ABCABCABC')
print(m)                        #<re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group(0))               #ABCABCABC

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")    #이름 000-000-0000 형식
m = p.search("park 010-1111-2222")
print(m.group(1))                             #park
print(m.group(2))                             #010-1111-2222

#그루핑에 이름 짓기 (?P<그룹명> 그룹내용)
p = re.compile(r'(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)')
m = p.search("park 010-1111-2222")
print(m.group("name"))                        #park

p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())  #the the

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print(p.search('Paris in the the spring').group())  #the the

#전방탐색(Lookahead Assersions)
#   > 긍정적 전방탐색 (?= ) 정규식과 매치되어야 함
#   > 부정적 전방탐색 (?! ) 정규식과 매치되지 않아야 함
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())                    #http

p2 = re.compile(".*[.](?!bat$|exe$).*")

#문자열 바꾸기: sub('바꿀문자열','대상문자열', count=숫자)
#             subn('바꿀문자열','대상문자열')     => (바뀐내용, 바뀐횟수)
p = re.compile('(blue|white|red)')
m = p.sub('colour','blue socks and red shoes')
print(m)            #colour socks and colour shoes
m2 = p.subn('colour','blue socks and red shoes')
print(m2)            #('colour socks and colour shoes', 2)

p1 = re.compile('(blue|white|red)')
m1 = p1.sub('colour','blue socks and red shoes', count=1)
print(m1)            #colour socks and red shoes

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+[-]\d+[-]\d+))")
print(p.sub("\g<phone> \g<name>","park 010-1111-2222")) #010-1111-2222 park
print(p.sub("\g<2> \g<1>","park 010-1111-2222"))        #010-1111-2222 park

def hexrepl(match):
    value = int(match.group())
    return hex(value)
p = re.compile(r'\d+')
m = p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
print(m)        #Call 0xffd2 for printing, 0xc000 for user code.
