import re

# 출제문제(1) - 정규식
# 하기 단어들 중 at로 끝나는 세글자짜리 단어만 리스트로 반환해보세요
words = """
cat goat gloat spat at too kar stat brat zoo swat frat pat boo rat
moat vat mat tat wheat moo cheat fiat squat hat carat bat rabat
"""

p = re.compile("\s(.at)\s", re.M)
m = p.findall(words)
print(m)


# 출제문제(2) - 정규식
# 하기 age_list를 정규식을 통해 하기 딕셔너리 내용으로 출력되게 만들어보세요
# 출력 내용 => {'Janice': '22', 'Theon': '33', 'Gabriel': '44', 'Joey': '21'}

age_list = '''
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21
'''

ages = re.findall(r'\d{1,2}', age_list)     #['22', '33', '44', '21']
names = re.findall(r'[A-Z][a-z]*', age_list)#['Janice', 'Theon', 'Gabriel', 'Joey']

ageDict = {}
x = 0
for eachname in names:
    ageDict[eachname] = ages[x]
    x += 1

print(ageDict)  #{'Janice': '22', 'Theon': '33', 'Gabriel': '44', 'Joey': '21'}

# 준규쨩이 푼 방식! 멋지다!
p1 = re.compile('(?P<name>\S+)\s+is\s+(?P<age>\S+)')
r1 = p1.findall(age_list)

result = {}
for i in r1:
    result[i[0]] = i[1]

print(result)   # {'Janice': '22', 'Theon': '33', 'Gabriel': '44', 'Joey': '21'}

# ================================================================================

# 1. 아이디 유효성 검사
# 영문과 숫자만으로 아이디를 입력하는데 5자 미만이거나 16자 초과인 경우 "유효하지 않은 아이디입니다." 출력
# 5자 이상 15자 이하인 경우 유효한 아이디입니다." 출력
idd = input("아이디를 입력하세요>> ")
p = re.compile('\w{5,15}$')
m = p.match(idd)
if m == None:
    print("유효하지 않은 아이디입니다.")
else:
    print("유효한 아이디입니다.")


#2. "헬로 World"에서 영어를 *로 변환하고,
# 다음에 한글을 *로 변환하라.
p = re.compile('[a-zA-Z]')
m = p.sub('*', "헬로 World")
print(m)            # 헬로 *****
p1 = re.compile('[ㄱ-ㅣ가-힣]')
m1 = p1.sub('*', m)
print(m1)           # ** *****


# 3.
# 3-1. 첫 단어를 검색하여 crud중 어떤기능을 하는 sql문인지 출력한다.
# 3-2. sql문 a에서 name에 해당하는 부분을 target
#            member에 해당하는 부분을 table
#            python에 해당하는 부분을 id로 그루핑하고
#   a가 어떤 기능을 하는 sql문인지 자세히 출력한다.

def crud(sql):
    if sql == "select":
        print("read")
    elif sql == "delete":
        print("delete")
    elif sql == "insert":
        print("create")
    elif sql == "update":
        print("update")

a = 'select name from member where id = python'

p = re.compile('\w+')
m = p.match(a).group()
#print(m.group(1))    #select
crud(m)

def sentence(target, table, id):
    print(table+" 테이블에서 id가 "+id+"인 "+target+"을 찾아 리턴하는 sql문")

p1 = re.compile(r'\w+\s(?P<target>\w+)\s\w+\s(?P<table>\w+)\s(where)\s(id)\s[=]\s(?P<id>\w+)')
m1 = p1.search(a)
target = m1.group("target") #name
table = m1.group("table")   #member
id = m1.group("id")         #python
sentence(target,table,id)   #member 테이블에서 id가 python인 name을 찾아 리턴하는 sql문


# 4.정규식을 사용하여 80년도생, 90년도생, 남자, 여자가 각각 몇 명인지 구해보세요
string2 = """
950825-1234567
850612-2987654
930525-2876552
940808-2394945
841019-1102913
870718-1203913
910803-2113709
871001-1987121
951203-1655786
931213-1861930
900312-2908133
871032-1543922
911213-2877651
"""
p = re.compile('^\w{2}', re.M)
m = p.findall(string2)
dictAge = {'80년대생': 0, '90년대생': 0, '남성': 0, '여성': 0}
for i in m:
    a = int(i)
    if a >= 90:
        dictAge['90년대생'] += 1
    else:
        dictAge['80년대생'] += 1

p1 = re.compile('[-](\w)', re.M)
m1 = p1.findall(string2)
for i in m1:
    a = int(i)
    if a == 1:
        dictAge['남성'] += 1
    else:
        dictAge['여성'] += 1

print(dictAge)  #{'80년대생': 5, '90년대생': 8, '남성': 7, '여성': 6}


# 5. 정규식을 사용해 이메일만 골라내서 하나씩 프린트해보세요
string = """
purple smurf667@aol.com, send a message bill@billwaldon.com dishwasher blah
rem54mdds@sbcglobal.net monkey banana peel tommfs1982@hotmail.com
kakao switch christina-alvarez@gmail.net nintendo sony playstation
verdun.singh@stanford.edu university thomas tammy@reallybigknockers.net
disney netflix wavve donkey alexander@null.net pikachu pokemon
"""
emails = re.findall('\S+[@]\w+[.]\w+', string)

for i in emails:
    print(i)
