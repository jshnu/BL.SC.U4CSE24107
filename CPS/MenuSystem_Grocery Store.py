items={1:["Apples",30.0,50,45],2:["Oranges",30.0,40,35],3:["Rice",30.0,100,80],4:["Flour",30.0,20,15],5:["Sugar",30.0,120,105]}
Costprice_Networth=(items[1][3]+items[2][3]+items[3][3]+items[4][3]+items[5][3])*30
cost=0
sold=0
def Simulation(N):
    global cost, sold, items
    print(f"## DAY {N} ##")
    match N:
        case 1:
            pr= 1
        case 2:
            pr= 1
        case 3:
            pr= 1
        case 4:
            pr=0.9
        case 5:
            pr=0.85
        case 6:
            pr=0.80
        case 7:
            pr=0.75
        case _:
            pr=0.75
    while True:
        try:
            print()
            print("Items Available:")
            print(f"1. {items[1][0]} - {items[1][1]}kg")
            print(f"2. {items[2][0]} - {items[2][1]}kg")
            print(f"3. {items[3][0]} - {items[3][1]}kg")
            print(f"4. {items[4][0]} - {items[4][1]}kg")
            print(f"5. {items[5][0]} - {items[5][1]}kg")
            print()
            sel=int(input("Select Item (1-5): "))
            print()
            print(f"Item Selected: {items[sel][0]}")
            if sel in [1,2]:
                price=items[sel][2]*pr
            else:
                price=items[sel][2]
            print(f"Price: {price}rs/kg")
            print(f"Would you like to purchase this item? (Y/N)")
            ch=input()
            match ch.lower():
                case "y":
                    print()
                    p=float(input("How many kgs do you want: "))
                    if p<=items[sel][1]:
                        print(f"Total Cost: {p*price}rs")
                        print("Would you like to confirm purchase? (Y/N)")
                        c=input()
                        match c.lower():
                            case "y":
                                items[sel][1]-=p
                                cost+=p*items[sel][3]
                                sold+=p*price
                                print()
                                print("## PURCHASE COMPLETED ##")
                                print()
                            case "n":
                                print()
                                print("## PURCHASE CANCELLED ##")
                                print()
                            case _:
                                print()
                                print("## INVALID CHOICE ##")
                                print()
                        print("Are you finished shopping? (Y/N)")
                        c=input()
                        match c.lower():
                            case "y":
                                print()
                                print(f"## END OF DAY {N} ##")
                                print()
                                break
                    else:
                        print()
                        print("## INSUFFICIENT STOCK ##")
                        print()
                case "n":
                    print()
                    print("Are you finished shopping? (Y/N)")
                    c=input()
                    match c.lower():
                        case "y":
                            print()
                            print(f"## END OF DAY {N} ##")
                            print()
                            break
                case _:
                    print()
                    print("## INVALID ENTRY ##")
                    print()
        except:
            print()
            print("## INVALID ENTRY ##")
            print()


Simulation(1)      
Simulation(2)
Simulation(3)
Simulation(4)
Simulation(5)
Simulation(6)
Simulation(7)

print("## SIMULATION END ##")

print()
print("Stock Remaining:")
print(f"1. {items[1][0]} - {items[1][1]}kg")
print(f"2. {items[2][0]} - {items[2][1]}kg")
print(f"3. {items[3][0]} - {items[3][1]}kg")
print(f"4. {items[4][0]} - {items[4][1]}kg")
print(f"5. {items[5][0]} - {items[5][1]}kg")
print()
Costprice_of_remaining_items=sum([items[i][3]*items[i][1] for i in range(1,6)])
print(f"Cost price of remaining stock: {Costprice_of_remaining_items}rs")
print()
print(f"Cost price of sold items: {cost}rs")
print(f"Sold price of sold items: {sold}rs")
print()
if sold>=cost:
    print(f"Net Profit: {sold-cost}rs")
else:
    print(f"Net Loss: {cost-sold}rs")
