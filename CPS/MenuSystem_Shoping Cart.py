'''
### Question: **Online Shopping Cart System**

**Description** 
Create a program to simulate an online shopping cart system that allows users to add items to their cart, remove items, apply discounts, and suggest alternative products if a requested product is unavailable.

---

**Predefined Data**

```python
# Predefined data: User accounts and product catalog
users = {
    "Tom": {"cart": [], "wallet_balance": 5000},
    "Jerry": {"cart": ["Item2"], "wallet_balance": 3000},
}

products = {
    "Item1": {"price": 1000, "stock": 5},
    "Item2": {"price": 500, "stock": 0},
    "Item3": {"price": 700, "stock": 3},
    "Item4": {"price": 1200, "stock": 2},
}
```

---

**Program Requirements**

1. **User Input**:
   - User's name
   - Operation: Add to Cart or Remove from Cart
   - Product name
   
2. **Cart Management**:
   - For "Add to Cart," check product availability and deduct stock.
   - For "Remove from Cart," update the cart and increase product stock.
   
3. **Checkout**:
   - Calculate the total cost of items in the cart.
   - Apply a discount (e.g., 10% for orders above ₹2000).
   - Check if the user’s wallet balance is sufficient. If not, suggest removing items to match their budget.
   
4. **Dynamic Suggestions**:
   - If the requested product is unavailable, suggest products in the same price range.
   - If the user’s cart exceeds their wallet balance, suggest removing specific items.
   
5. **Transaction Summary**:
   - Display the user’s cart, total cost, applied discounts, and updated wallet balance.

---

**Edge Cases to Handle**:
- User exceeds wallet balance.
- Product requested is out of stock.
- Attempt to remove an item not in the cart.
- Empty cart at checkout.

---

**Sample Input/Output**

**Sample Input 1**:
```
User Name: Tom
Operation: Add to Cart
Product Name: Item1
```

**Output**:
```
Transaction Successful.
Added Item: Item1
Updated Cart: ['Item1']
Remaining Stock of Item1: 4
Wallet Balance: ₹5000
```

**Sample Input 2**:
```
User Name: Jerry
Operation: Checkout
```

**Output**:
```
Transaction Summary:
Items in Cart: ['Item2']
Total Cost: ₹500
Discount: ₹0
Updated Wallet Balance: ₹2500
```

**Sample Input 3**:
```
User Name: Tom
Operation: Add to Cart
Product Name: Item2
```

**Output**:
```
"Requested product is out of stock. Suggested alternatives: 'Item3' priced at ₹700."
```

---
'''

# Online Shopping Cart System

# Predefined data: User accounts and product catalog
users = {
    "Tom": {"cart": [], "wallet_balance": 5000},
    "Jerry": {"cart": ["Item2","Item4","Item4","Item2"], "wallet_balance": 3000},
}

products = {
    "Item1": {"price": 1000, "stock": 5},
    "Item2": {"price": 500, "stock": 0},
    "Item3": {"price": 700, "stock": 0},
    "Item4": {"price": 1200, "stock": 2},
}

s_prod=sorted(products, key=lambda x: products[x]['price'])

def Add(usr_n):
    global users
    prod_n= input("Product Name: ")
    if prod_n in products:
        if products[prod_n]['stock']>0:
            users[usr_n]["cart"].append(prod_n)
            products[prod_n]['stock']-=1
            print("Transaction Successful.")
            print(f"Added Item: {prod_n}")
            print(f"Updated Cart: {users[usr_n]['cart']}")
            print(f"Remaining Stock of {prod_n}: {products[prod_n]['stock']}")
            print(f"Wallet Balance: ₹{users[usr_n]['wallet_balance']}")
            print()
        else:
            alt=s_prod.index(prod_n)
            if alt!=0:
                alt-=1
            else:
                alt+=1
            x=len(s_prod)
            i=0;rr=True
            while products[s_prod[alt]]['stock']==0:
                if alt!=0:
                    if rr:
                        alt-=1
                    else:
                        alt+=1
                    if i==x:
                        print()
                        print("Apologies for the inconvience, all products are out of stock")
                        print()
                        return
                    i+=1
                else:
                    alt=s_prod.index(prod_n)
                    alt+=1
                    rr=False
                    
            print()
            print(f"Requested product is out of stock. Suggested alternatives: {s_prod[alt]} priced at ₹{products[s_prod[alt]]['price']}.")
            print()
    else:
        print()
        print("### INVALID ITEM ###")
        print()

def Remove(usr_n):
    global users
    prod_n= input("Product Name: ")
    if prod_n in products:
        if prod_n in users[usr_n]['cart']:
            users[usr_n]["cart"].remove(prod_n)
            products[prod_n]['stock']+=1
            print("Transaction Successful.")
            print(f"Removed Item: {prod_n}")
            print(f"Updated Cart: {users[usr_n]['cart']}")
            print(f"Remaining Stock of {prod_n}: {products[prod_n]['stock']}")
            print(f"Wallet Balance: ₹{users[usr_n]['wallet_balance']}")
            print()
        else:
            print()
            print("### ITEM UNAVAILABLE IN CART ###")
            print()
    else:
        print()
        print("### INVALID ITEM ###")
        print()

def Checkout(usr_n):
    global users
    T_cost=sum([products[x]['price'] for x in users[usr_n]['cart']])
    if T_cost<=users[usr_n]['wallet_balance']:
        print("Transaction Summary:")
        print(f"Items in Cart: {users[usr_n]['cart']}")
        print(f"Total Cost: ₹{T_cost}")
        users[usr_n]['wallet_balance']-=T_cost
        users[usr_n]['cart']=[]
        print(f"Updated Wallet Balance: ₹{users[usr_n]['wallet_balance']}")
        print()
    else:
        prods=[(x,products[x]['price']) for x in users[usr_n]['cart']]
        prods.sort(key=lambda x: x[1])
        diff=T_cost-users[usr_n]['wallet_balance']
        x=0
        while True:
            if prods[x][1]>=diff:
                break
            elif x==len(prods)-1:
                break
            x+=1
        print()
        print(f"### INSUFFICIENT WALLET BALANCE: RECOMMEND REMOVING {prods[x][0]} priced at ₹{prods[x][1]} ###")
        print()

while True:
    try:
        print("### WELCOME TO SHAQUILA MALLS ###")
        print("Items Available:")
        for i in products:
            print(f"{i} : {products[i]['price']}rs (Stock: {products[i]['stock']})")
        print()
        usr_n= input("User Name: ")
        operation= input("Operation: ")
        if usr_n in users:
            match operation.lower():
                case "add to cart":
                    Add(usr_n)
                case "remove from cart":
                    Remove(usr_n)
                case "checkout":
                    Checkout(usr_n)
                case "exit":
                    print()
                    print("### THANK YOU FOR YOUR PATRONAGE ###")
                    print()
                    break
                case _:
                    print()
                    print("### INVALID OPERATION ###")
                    print()
        else:
            print()
            print("### USER NOT AVAILAIBLE ###")
            print()
    except:
        print("#### ERROR ####")
