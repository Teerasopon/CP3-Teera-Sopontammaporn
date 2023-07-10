userNameInput = input("Username : ")
passWordInput = input("password : ")
if userNameInput == "admin" and passWordInput == "1234":
    print("Welcome to Shopping store")
    print("Pricelist")
    apple = 10
    banana = 20
    orange = 30
    print("apple = 10 bath")
    print("banana = 20 bath")
    print("orange = 30 bath")
    selectProduct = input("please select your product : ")
    if selectProduct == "apple":
        quatity1 = int(input("How many do you want? : "))
        sum1 = apple * quatity1
        print("Apple",quatity1,"Ea = ",sum1,"bath")
    elif selectProduct == "banana":
        quatity2 = int(input("How many do you want? : "))
        sum2 = banana * quatity2
        print("Banana",quatity2,"Ea = ",sum2,"bath")
    elif selectProduct == "orange":
        quatity3 = int(input("How many do you want? : "))
        sum3 = orange * quatity3
        print("Orange",quatity3,"Ea = ",sum3,"bath")
    else:
        print("Invalid")
else:
    print("Invalid")



