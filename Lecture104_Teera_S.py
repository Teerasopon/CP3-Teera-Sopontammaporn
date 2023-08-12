class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added to Cart",self.name,self.lastname,"'s cart")

customer1 = Customer()
customer1.name = "Teera"
customer1.lastname = "Sopontammaporn"
customer1.addCart()

customer2 = Customer()
customer2.name = "A"
customer2.lastname = "AA"
customer2.addCart()

customer3 = Customer()
customer3.name = "B"
customer3.lastname = "BB"
customer3.addCart()

customer4 = Customer()
customer4.name = "C"
customer4.lastname = "CC"
customer4.addCart()