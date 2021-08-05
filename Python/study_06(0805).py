num = '123,456'
num = num.replace(',','')
print(int(num))

def comma(data):
    return int(data.replace(',',''))

num_list = ['123,456','456,789']

num_list2 = list(map(comma, num_list))
print(num_list2)


