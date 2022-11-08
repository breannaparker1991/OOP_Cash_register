#DSC 510
#Week 11
#OOP cash register
#Author Breanna Parker
#11/7/22


import locale

class CashRegister:
  def __init__(self):
    self.items = 0
    self.price = float(0.00)
  
    
  def addItems(self,price): #keeps track of total number of items in cart
    self.price += price
    self.items += 1)
    
  def getTotal(self):  #returns total price
    return self.price
  
  def getCount(self):  #return the item count of the cart
    return self.items
  
  def clearCart(self):  #clears cart for another user or checkout
    self.items = 0
    self.price = float(0.00)

def main(): 
  user_name = input('What is your name?\n') #weclomes user
  print("Hello",user_name)
  locale.setlocale(locale.LC_ALL, 'en_US')
  user_name = CashRegister()  #user is using the cash register
  while True:
    line = input ("Would you like to add another food item to your cart? Choose y or n \n") 
    if line.lower()  == "y":
      price = float(input("please input the price of the item\n"))
      user_name.addItems(price)   #user adds prices to cart
    elif line.lower() == "n":
      print("Your total checkout price:", locale.currency(user_name.getTotal()) )
      # int(float(locale.currency(user_name.getTotal())))
      print("Your total item count", user_name.getCount())
      user_name.clearCart() #clears cart for another user/checkout
      break
    else:
        print("Error")

if __name__ == '__main__':
  main()