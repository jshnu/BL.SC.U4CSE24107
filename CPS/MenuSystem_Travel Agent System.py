Data={1:["Bali",3500,[1500*2,1400*2,800],"2 Days",0],2:["Maldives",1500,[1000*1,900*1,600],"1 Day",0],
      3:["Japan",9500,[1600*5,1400*5,1000],"5 Days",0],4:["France",14000,[2000*4,1600*4,1200],"4 days",0],
      5:["Nepal",2500,[700*3,500*3,600],"3 Days",0],6:["Italy",12000,[1250*4,1050*4,900],"4 Day",0],
      7:["Germany",8000,[900*3,800*3,800],"3 Days",0],8:["China",10000,[950*4,850*4,1000],"4 Day",0],
      9:["Korea",8500,[1300*2,1100*2,900],"2 Days",0],10:["Sri Lanka",1200,[750*2,600*2,500],"2 Day",0]}
D=[2, 10, 5, 1, 7, 9, 8, 6, 3, 4]
#{Number:[<Country Name>,<Per Flight Ticket Price>, [<Price Breakdown: Stay,Food,Shopping>,<Minimum Stay Time>]]}

while True:
    try:
        print("#### WELCOME TO SYNTHAIR TRAVELS ####")
        print("Travel Destinations Available:")
        for i in range(1,len(Data)+1):
            if Data[i][4]==0:
                print(f"{i}. {Data[i][0]}")
            else:
                print(f"{i}. {Data[i][0]} [NOT AVAILABLE]")
        print()
        DD=int(input("Enter your desired destination (1-10): "))
        TB=int(input("Enter your total budget (in rs): "))
        NT=int(input("Enter number of tickets: "))
        if 0<DD<11:
            if Data[DD][4]==0:
                if TB>=0:
                    if NT>=0:
                        Af=True
                        B=True
                        print()
                        print(f"Destination: {Data[DD][0]}")
                        Tic=Data[DD][1]*NT
                        bud=sum(Data[DD][2])
                        print(f"Total Cost of flights: {Tic*2}rs")
                        print(f"Minimum recommended stay duration: {Data[DD][3]}")
                        print()
                        if Tic+bud<=TB:
                            print("Destination is Affordable in the Provided Budget")
                        elif Tic<=TB:
                            print("Destination is not recommendaded for the Provided Budget")
                            Af=False
                        else:
                            print("Destination is not Affordable in the Provided Budget")
                            B=False
                            Af=False
                        print("Approximate Price Breakdown for the Minimum Recommended Stay:")
                        print(f"Hotel Stay: {Data[DD][2][0]*NT}rs")
                        print(f"Food Expenses: {Data[DD][2][1]*NT}rs")
                        print(f"Shoppin Expenses: {Data[DD][2][2]*NT}rs")
                        print()
                        print(f"Recommended Budget for the Minimum Recommended Stay Duration: {(Tic+bud)*NT}rs")
                        print()
                        if not Af:
                            print("Would you like to see Alternative Destinations? (Y/N)")
                            P=input()
                            if P.lower()=="y":
                                i=0
                                while TB<=(Data[D[i]][1]+sum(Data[D[i]][2]))*NT:
                                    i+=1
                                print("Alternative Destination Suggestions:")
                                print()
                                if i<3:
                                    for i in range(3):
                                        print(f"Desitantion: {Data[D[i]][0]}")
                                        print(f"Recommended Budget: {Data[D[i]][1]+sum(Data[D[i]][2])}rs per person")
                                        print()
                                else:
                                    while i>=0:
                                        i-=1
                                        print(f"Desitantion: {Data[D[i]][0]}")
                                        print(f"Recommended Budget: {Data[D[i]][1]+sum(Data[D[i]][2])}rs per person")
                                        print()
                                if B:
                                    print("Would you like to proceed with the current Transaction? (Y/N)")
                                    PP=input()
                                    if PP.lower()=="y":
                                        BB=True
                                        print()
                                    elif PP.lower()=="n":
                                        BB=False
                                        print()
                                        print("### Returning TO Main Menu ###")
                                        print()
                                    else:
                                        print()
                                        print("### INVALID INPUT ###")
                                        print()
                            if P.lower()=="n" or BB==True:
                                print("Would you like to Book the Tickets? (Y/N)")
                            
                                P=input()
                                if P.lower()=="y":
                                    print("### PURCHASE COMPLETE ###")
                                    Data[DD][4]=1
                                    print()
                                    print("Would you like to exit? (Y/N)")
                                    c=input()
                                    if c.lower()=="y":
                                        print()
                                        print("### Thank You For Your Patronage ###")
                                        print()
                                        break
                                    else:
                                        print()
                                        print("### Returning TO Main Menu ###")
                                        print()
                                elif P.lower()=="n":
                                    print()
                                    print("### Returning TO Main Menu ###")
                                    print()
                            else:
                                print()
                                print("### INVALID INPUT ###")
                                print()
                                
                        else:
                            print("Would you like to Book the Tickets? (Y/N)")
                            
                            P=input()
                            if P.lower()=="y":
                                print("### PURCHASE COMPLETE ###")
                                Data[DD][4]=1
                                print()
                                print("Would you like to exit? (Y/N)")
                                c=input()
                                if c.lower()=="y":
                                    print()
                                    print("### Thank You For Your Patronage ###")
                                    print()
                                    break
                                else:
                                    print()
                                    print("### Returning TO Main Menu ###")
                                    print()
                            elif P.lower()=="n":
                                print()
                                print("### Returning TO Main Menu ###")
                                print()
                            else:
                                print()
                                print("### INVALID INPUT ###")
                                print()
                    else:
                        print()
                        print("### INVALID NUMBER OF TICKETS ###")
                        print()
                else:
                    print()
                    print("### INVALID BUDGET ###")
                    print()
            else:
                print()
                print("### DESTINATION NOT AVAIABLE ###")
                print()
        else:
            print()
            print("### DESTINATION NOT AVAIABLE ###")
            print()
        if DD==0:
            print()
            print("### Thank You For Your Patronage ###")
            print()
            break
        
    except:
        print()
        print("### INVALID INPUT ###")
        print()
