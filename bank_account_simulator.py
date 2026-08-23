bank=[]
balance=500


def check():
    print("your balance:",balance)


def deposit(balance):
    amount=int(input("enter amount:"))
    balance=balance+amount
    print("your balance:",balance)
    return balance


def withdraw(balance):
    amount2=int(input("enter amount:"))
    if amount2<=balance and amount2>0:
        balance=balance-amount2
        print("your balance:",balance)
    elif amount2>balance:
        print("insufficient balance!")
    else:
        print("invalid amount!")
    return balance



print("====BANK ACCOUNT====")

choose=0
while choose != "4":
    print("1.check balance")
    print("2.deposit money")
    print("3.withdraw")
    print("4.exit")

    choose=input("choose an option:")
    if choose=="1":
        check()

    if choose=="2":
        balance=deposit(balance)

    if choose=="3":
       balance= withdraw(balance)    

print("thank you for using our bank.\n Goodbye!")

   


