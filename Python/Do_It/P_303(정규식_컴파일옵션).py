import re

#re.DOTALL, re.S: .에 \n 포함
p = re.match('a.b','a\nb')
print(p)    #None
p2 = re.match('a.b','a\nb', re.DOTALL)  #re.S
print(p2)   #<re.Match object; span=(0, 3), match='a\nb'>

#re.IGNORECAS, re.I: 대소문자 구분 없이
p = re.match('[a-z]+','ABC')
print(p)    #None
p2 = re.match('[a-z]+','ABC', re.IGNORECASE)  #re.S
print(p2)   #<re.Match object; span=(0, 3), match='ABC'>

#re.MULTILINE, re.M: 여러 줄과 매치
data = """python one
life is too short
python two
you need python
python three"""
p = re.compile("^python\s\w+")
p1 = re.compile("^python\s\w+", re.MULTILINE)
print(p.findall(data))  #['python one']
print(p1.findall(data))  #['python one', 'python two', 'python three']

#re.VERBOSE, re.X: verbose(장황한) 모드 사용
#charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref = re.compile(r"""
&[#]                    # Start of a numeric entity reference
(
    0[0-7]+             # Octal form (8진수)
    |[0-9]+             # Decimal form (10진수)
    |x[0-9a-fA-F]+      # Hexadecimal form (16진수)
)
;                       #Trailing semicolon
""", re.VERBOSE)
