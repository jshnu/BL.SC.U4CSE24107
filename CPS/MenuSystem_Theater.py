import random
import copy

price=250
def S_layout_gen():
    Seats=[["A" for j in range(6)] for i in range(6)] # A for Available and B for Booked seats
    r=random.randint(0,30)
    for i in range(r):
        r1=random.randint(0,5)
        r2=random.randint(0,5)
        Seats[r1][r2]="B"
    A=sum([i.count("A") for i in Seats])
    return Seats,A

def disp_seats(Seats):
    print("    ",end="")
    for i in range(6):
        print(i+1,end="    ")
    print()
    for i in range(len(Seats)):
        print(i+1,end=" ")
        print(Seats[i])


def B_Menu(X,Y):
    global mov
    Seats=X[0]
    A=X[1]
    try:
        print("1. Book a Single Seat")
        print("2. Book a Multiple Seats")
        print("3. Cancel")
        ch=int(input("Enter your choice: "))
        match ch:
            case 1:
                print()
                r=int(input("Enter the row no. of the seat: "))
                c=int(input("Enter the column no. of the seat: "))
                r-=1
                c-=1
                print()
                if Seats[r][c]=="A":
                    temp=copy.deepcopy(Seats)
                    temp[r][c]="O"
                    disp_seats(temp)
                    print()
                    print(f"Cost of booking: {price}rs")
                    print("Would you like to book the selected Seat? (Y/N)")
                    c1=input()
                    match c1.lower():
                        case "y":
                            Seats[r][c]="B"
                            A-=1
                            mov[Y][1]=(Seats,A)
                            del temp
                            print()
                            print("## BOOKING SUCCESSFULL ##")
                            print()
                            print("Are you finished with your business? (Y/N)")
                            cc=input()
                            if cc.lower()=="y":
                                print()
                                print("### THANK YOU FOR YOUR PATRONAGE ###")
                                return True
                            else:
                                print()
                                print("## RETURNING TO MAIN MENU ##")
                                print()
            case 2:
                print()
                nr=int(input("Enter number of seats to be booked: "))
                print()
                if nr>A:
                    print("## INSUFFICIENT SEAT AVAILABILITY ##")
                    print()
                    return B_Menu(X,Y)
                Ss=max([i.count("A") for i in Seats])
                if Ss<nr:
                    print("1. Same Row Seats (Not Available)")
                else:
                    print("1. Same Row Seats")
                print("2. Across Row Seats")
                c1=int(input("Enter your choice: "))
                match c1:
                    case 1:
                        if Ss<nr:
                            print()
                            print("## INSUFFICIENT SEAT AVAILABILITY FOR SAME ROW BOOKING ##")
                            print()
                            return B_Menu(X,Y)
                        while True:
                            print()
                            print("Enter X to Cancel")
                            r=input("Enter the row no. for the seats: ")
                            co=[]
                            for i in range(len(Seats)):
                                m1=0
                                m2=0
                                x=0
                                y=0
                                x1=0
                                for j in range(len(Seats[0])):
                                    if Seats[i][j]=="B":
                                        x1=j+1
                                        m1=0
                                    else:
                                        m1+=1
                                    if m2<m1:
                                        m2=m1
                                        x=x1
                                        y=j
                                co.append((m2,x,y))
                            if r.lower()=="x":
                                print()
                                break
                            r=int(r)-1
                            if co[r][0]<nr:
                                print()
                                print("## INSUFFICIENT SEAT AVAILABILITY FOR SAME ROW BOOKING ##")
                                print()
                            else:
                                temp=copy.deepcopy(Seats)
                                for j in range(co[r][1],co[r][1]+nr):
                                    temp[r][j]="O"
                                disp_seats(temp)
                                print()
                                print(f"Cost of booking: {price*nr}rs")
                                print("Would you like to book the selected Seat? (Y/N)")
                                c1=input()
                                match c1.lower():
                                    case "y":
                                        for j in range(co[r][1],co[r][1]+nr):
                                            Seats[r][j]="B"
                                        A-=nr
                                        mov[Y][1]=(Seats,A)
                                        del temp
                                        print()
                                        print("## BOOKING SUCCESSFULL ##")
                                        print()
                                        print("Are you finished with your business? (Y/N)")
                                        cc=input()
                                        if cc.lower()=="y":
                                            print()
                                            print("### THANK YOU FOR YOUR PATRONAGE ###")
                                            return True
                                        else:
                                            print()
                                            print("## RETURNING TO MAIN MENU ##")
                                            print()
                                            break
                    case 2:
                        cont=[]
                        for i in range(len(Seats)):
                            m1=0
                            m2=0
                            x=0
                            y=0
                            x1=0
                            for j in range(len(Seats[0])):
                                if Seats[i][j]=="B":
                                    x1=j+1
                                    m1=0
                                else:
                                    m1+=1
                                if m2<m1:
                                    m2=m1
                                    x=x1
                                    y=j
                            cont.append((m2,i,x,y))
                        cont.sort(reverse=True)
                        xx=nr
                        i=0
                        temp=copy.deepcopy(Seats)
                        while xx>0 and i<len(cont):
                            if xx>=cont[i][0]:
                                xx-=cont[i][0]
                                temp[cont[i][1]]=[temp[cont[i][1]][j] if j<cont[i][2] or j>cont[i][3] else "O" for j in range(len(temp))]
                                i+=1
                            else:
                                j=cont[i][2]
                                while xx!=0:
                                    if temp[cont[i][1]][j]=="A":
                                        temp[cont[i][1]][j]="O"
                                        xx-=1
                                    j+=1
                        if xx==0:
                            disp_seats(temp)
                            print()
                            print(f"Cost of booking: {price*nr}rs")
                            print("Would you like to book the selected Seat? (Y/N)")
                            c1=input()
                            match c1.lower():
                                case "y":
                                    xx=nr
                                    i=0
                                    while xx>0 and i<len(cont):
                                        if xx>=cont[i][0]:
                                            xx-=cont[i][0]
                                            Seats[cont[i][1]]=[Seats[cont[i][1]][j] if j<cont[i][2] or j>cont[i][3] else "O" for j in range(len(Seats))]
                                            i+=1
                                        else:
                                            j=cont[i][2]
                                            while xx!=0:
                                                if temp[cont[i][1]][j]=="A":
                                                    temp[cont[i][1]][j]="B"
                                                    xx-=1
                                                j+=1
                                    A-=nr
                                    mov[Y][1]=(Seats,A)
                                    del temp
                                    print()
                                    print("## BOOKING SUCCESSFULL ##")
                                    print()
                                    print("Are you finished with your business? (Y/N)")
                                    cc=input()
                                    if cc.lower()=="y":
                                        print()
                                        print("### THANK YOU FOR YOUR PATRONAGE ###")
                                        return True
                                    else:
                                        print()
                                        print("## RETURNING TO MAIN MENU ##")
                                        print()
                        else:
                            Rowcount=[(temp[i].count("A"),i) for i in range(len(temp))]
                            Rowcount.sort(reverse=True)
                            i=0
                            while xx>0:
                                if xx>=Rowcount[i][0]:
                                    xx-=Rowcount[i][0]
                                    temp[Rowcount[i][1]]=[j if j=="B" else "O" for j in temp[Rowcount[i][1]]]
                                else:
                                    j=0
                                    while xx!=0:
                                        if temp[Rowcount[i][1]][j]=="A":
                                            temp[Rowcount[i][1]][j]="B"
                                            xx-=1
                                            j+=1
                                i+=1
                            disp_seats(temp)
                            print()
                            print(f"Cost of booking: {price*nr}rs")
                            print("Would you like to book the selected Seat? (Y/N)")
                            c1=input()
                            match c1.lower():
                                case "y":
                                    xx=nr
                                    i=0
                                    while xx!=0:
                                        xx-=cont[i][0]
                                        Seats[cont[i][1]]=[Seats[cont[i][1]][j] if j<cont[0][2] or j>cont[0][3] else "B" for j in range(len(Seats))]
                                        i+=1
                                        if i==len(cont):
                                            break
                                    i=0
                                    while xx>0:
                                        if xx>=Rowcount[i][0]:
                                            xx-=Rowcount[i][0]
                                            Seats[Rowcount[i][1]]=[j if j=="B" else "O" for j in Seats[Rowcount[i][1]]]
                                        else:
                                            j=0
                                            while xx!=0:
                                                if Seats[Rowcount[i][1]][j]=="A":
                                                    Seats[Rowcount[i][1]][j]="B"
                                                    xx-=1
                                                j+=1
                                    A-=nr
                                    mov[Y][1]=(Seats,A)
                                    del temp
                                    print()
                                    print("## BOOKING SUCCESSFULL ##")
                                    print()
                                    print("Are you finished with your business? (Y/N)")
                                    cc=input()
                                    if cc.lower()=="y":
                                        print()
                                        print("### THANK YOU FOR YOUR PATRONAGE ###")
                                        return True
                                    else:
                                        print()
                                        print("## RETURNING TO MAIN MENU ##")
                                        print()
                    case _:
                        print()
                        print("## INVALID CHOICE ##")
                        print()
                        return B_Menu(X,Y)
            case 3:
                print()
                print("## CANCELLING REQUEST ##")
                print()
            case _:
                print()
                print("## INVALID CHOICE ##")
                print()
                return B_Menu(X,Y)
    except:
        print()
        print("## INVALID CHOICE ##")
        print()
        return B_Menu(X,Y)

l=["Jawaan","Animal","Moana 2","RRR","Bahubali","12th Fail","Barbie","Spiderman: No Way Home","Openheimer","Toy Story"]
mov=[]
mm=[]
for i in range (4):
    m=random.choice(l)
    while True:
        if m not in mm:
            mov.append([m,S_layout_gen()])
            mm.append(m)
            break
        else:
            m=random.choice(l)

while True:
    print("~ Weclome to Ciniplix ~")
    print("Movies Currently Screening:")
    for j in range(4):
        print(f"{j+1}. {mov[j][0]}")
    print()
    print("Enter 0 if you wish to leave the theater")
    print()
    ch=int(input("Which movie would you like to view (1-4): "))
    if ch in [1,2,3,4]:
        print()
        print(f"## Seat Layout for {mov[ch-1][0]} ##")
        disp_seats(mov[ch-1][1][0])
        print("No. of Seats avaiable: ",mov[ch-1][1][1])
        print()
        z=B_Menu(mov[ch-1][1],ch-1)
        if z:
            break
    elif ch==0:
        print()
        print("### THANK YOU FOR YOUR PATRONAGE ###")
        break
    else:
        print()
        print("## INVALID CHOICE ##")
        print()

            
            
    





