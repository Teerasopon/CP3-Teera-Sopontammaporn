def vatCalculate(totalprice):
    result=totalprice*1.07
    return result
x = int(input("total price : "))
print("price indlude vat : ",vatCalculate(x))