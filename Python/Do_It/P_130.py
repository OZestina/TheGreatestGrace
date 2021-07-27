treeHit = 0
while treeHit <10:
    treeHit += 1
    print("나무를 %d번 찍었습니다" %treeHit)
    if treeHit == 10:
        print("tree falls")

prompt = """
1. add
2. del
3. list
4. quit

Enter number: """

number = 0
while number != 4:
    print(prompt, end="")
    number = int(input())

coffee = 10
while True:
    money = int(input("show me the money"))
    if money ==300:
        print("here's your coffee")
        coffee -= 1
    elif money >300:
        print("here's your coffee and your change %d" %(money-300))
        coffee -=1
    elif money < 0:
        print("shut up and take ma money")
    elif money == 0:
        print("(staring)")
    else:
        print("discount not available. take your money back.")
    if coffee ==0:
        print("sold out")
        break
