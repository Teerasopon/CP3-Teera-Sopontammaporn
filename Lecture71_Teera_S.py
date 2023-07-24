menuList = []
priceList = []

def showBill():
    totalPrice = 0
    print("===== My Food =====")
    for n in range(len(menuList)):
        print(menuList[n],priceList[n])
        totalPrice = totalPrice + int(priceList[n])
    print("Total Price : ",totalPrice)


while True:
    menuName = input("Pleas Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList,priceList)
showBill()
