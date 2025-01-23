#Set- B
#Question 1
income=int(input("Enter your income:"))
age=int(input("Enter your age:"))
emp=input("Are you currently employed? (yes/no):")
if income<50000:
    print("Your income is less than 50,000/-. You are not eligible to file taxes.")
elif age<18:
    print("Your age is less than 18 years. You are not eligible to file taxes.")
elif emp.lower()=="no":
    print("You are currently not employed. You are not eligible to file taxes.")
else:
    print("You are eligible to file taxes.")

#Question 2
day=int(input("Enter day:"))
month=int(input("Enter month:"))
year=int(input("Enter year:"))

if month==2:
    leap=False
    if year%4==0:
        if year%400==0:
            leap = True
        elif year%100==0:
            pass
        else:
            leap = True
    if leap: 
        if day<1 or day>29:
            print(f"Invalid day. Please enter a day between 1 and 29. (for the {month} month)")
        elif month<1 or month>12:
            print("Invalid month. Please enter a month between 1 and 12.")
        else:
            print("The date is valid")
    else:
        if day<1 or day>28:
            print(f"Invalid day. Please enter a day between 1 and 28. (for the {month} month)")
        elif month<1 or month>12:
            print("Invalid month. Please enter a month between 1 and 12.")
        else:
            print("The date is valid")
    
elif month in [1,3,5,7,8,10,12]:
    if day<1 or day>31:
        print(f"Invalid day. Please enter a day between 1 and 31. (for the {month} month)")
    elif month<1 or month>12:
        print("Invalid month. Please enter a month between 1 and 12.")
    else:
        print("The date is valid")
else:
    if day<1 or day>30:
        print(f"Invalid day. Please enter a day between 1 and 30. (for the {month} month)")
    elif month<1 or month>12:
        print("Invalid month. Please enter a month between 1 and 12.")
    else:
        print("The date is valid")
    
    
            
