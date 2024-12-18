
pin="2045"
balance="50000"
pin_in=input("enter your pin")
if (pin==pin_in):
    while True:
        print("1.withdrawl /n 2.credit amount /n 3.balance check")
        option=int(input("select any one option"))
        if(option == 1):
            amount = int(input("enter debit amount"))
            if(balance >= amount):
                balance = balance - amount
                print("your amount successfully debited, remaining balance =",balance)
                repeat = input("do you want to repeat transaction? yes or no")
                if(repeat == "no"):
                    break
            else:
                print("insufficient balance")
                repeat = input("do you want to repeat transaction? yes or no")
                if (repeat == "no"):
                    break


        elif(option == 2):

            amount = int(input("enter your credit amount"))
            balance = balance + amount
            print("your amount successfully credited, total balance=", balance)
            repeat = input("do you want to repeat transaction? yes or no")
            if (repeat == "no"):
                break

        elif(option == 3):
            print("your total balance= ",balance)

            repeat = input("do you want to repeat transaction? yes or no")
            if (repeat =="no"):
                break
        else:
            print("wrong input")
            repeat = input("do you want to repeat transaction? yes or no")
            if (repeat == "no"):
                break
    else:
        print(("wrong pin"))