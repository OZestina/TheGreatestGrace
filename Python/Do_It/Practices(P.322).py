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
A = [20,55,67,82,45,33,90,87,100,25]
result = 0
for score in A:
    if score >= 50:
        result += score
print(result)

#Q5
def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-2) + fib(n-1)

def fib2(n):
    result = []
    for i in range(n+2):
        if n >= fib(i):
            result.append(fib(i))
        else:
            break
    return result
print(fib2(0))          #[0]
print(fib2(1))          #[0, 1, 1]
print(fib2(2))          #[0, 1, 1, 2]
print(fib2(3))          #[0, 1, 1, 2, 3]
print(fib2(4))          #[0, 1, 1, 2, 3]

