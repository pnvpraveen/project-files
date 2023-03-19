
#ATM program

name="praveen"
password="jai hind"
user_name=input("Enter the User Name:")
passwords=input("Enter the Password")

p='''
1.Credit
2.Debit
3.Mini Statement
4.Exit
'''
Amount=1000
if name==user_name and passwords==password:
    while True:
        print(p)
        option=int(input("enter the OPtion:"))
        if option==1:
            credit_amount=float(input("Enter the amount"))
            print("Amount after credit:",Amount+credit_amount)
        elif option==2:
            debit_amount=float(input("Enter the amount"))
            print("Amount after debit:",Amount-debit_amount)
        elif option==3:
            print("Amount:",Amount)
        elif option==4:
            break
else:
    print("incorrect user information")

