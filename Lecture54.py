def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCal():
    money = int(input("Price of product : "))
    vat = 7
    summary = money + (money * vat / 100)
    return summary

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

if login() :
    showMenu()
    choose = menuSelect()
    if choose == 1 :
        print(vatCal())
    elif choose == 2 :
        print(priceCalculator())
