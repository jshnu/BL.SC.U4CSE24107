#Create an ATM System
balance=0
p=1103
while True:
    try:
        pin=input("Enter your 4-digit pin: ")
        if int(pin)==p:
            print()
            print("### VALIDATION SUCCESSFULL ###")
            print()
            while True:
                print("Welcome to Bank of JIJI:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. PIN Change")
                print("5. Exit")
                print()
                ch=int(input("Enter your choice: "))
                match ch:
                    case 1:
                        print()
                        amt=int(input("Enter amount to be deposited: "))
                        balance+=amt
                        print("### Amount Successfully Deposited ###")
                        print()
                    case 2:
                        print()
                        amt=int(input("Enter amount to be withdrawn: "))
                        if amt<=balance:
                            balance-=amt
                            print("### Amount Successfully Withdrawn ###")
                        else:
                            print("### Insuffiecient Balance ###")
                        print()
                    case 3:
                        print()
                        print(f"Balance : {balance}rs")
                        print()
                    case 4:
                        print()
                        np=int(input("Enter new pin: "))
                        if len(str(np))==4:
                            p=np
                            print("### PIN Successfully Changed ###")
                        else:
                            print("### Invalid New PIN ###")
                        print()
                    case 5:
                        print()
                        print("### EXITTING MAIN MENU ###")
                        print()
                        break
                    case _:
                        print()
                        print("## INVALID CHOICE ##")
                        print()
        else:
            print()
            print("### INVALID PIN ###")
            print()
    except:
        if pin.lower()=="stop":
            print("### STOPPING EXECUTION ###")
            break
        print()
        print("### ERROR ###")
        print()
        
