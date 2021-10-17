#Q1
text = "a:b:c:d"
text2 = text.split(":")
text3 = '#'.join(text2)
print(text3)

#Q2
a = {'A':90, 'B':80}
a.setdefault('C', 70)
print(a['C'])               #70
print(a.get('D', 60))       #60

#Q4
