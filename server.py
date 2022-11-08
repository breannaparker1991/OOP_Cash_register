#DSC 510
#Week 11
#OOP cash register
#Author Breanna Parker
#11/7/22


# Your program should have two getter methods.
# getTotal – returns totalPrice
# getCount – returns the itemCount of the cart
# Your program must create an instance of the CashRegister class within your main function.
# Your program should have a loop in main which allows the user to continue to add items to the cart until they request to quit.
# The output should be formatted as currency. Be sure to investigate the locale class. You will need to call locale.setlocale and locale.currency.



class CashRegister:
  def __init__(self):
    self.items = 0
    self.price = 0.0
    
  def addItem(self,price,items): #keeps track of total number of items in cart
    self.price = price
    items = 0
    items = items + 1
    
  def getTotal():  #returns total price
    return self.price
  
  def getCount():  #return the item count of the cart
    return self.items
  

def main():
  user_name = input('What is your name?\n')
  print("Hello",user_name)
  user_name = CashRegister()
  while True:
    line = input ("Would you like to add another food item to your cart? Choose y or n \n")
    if line  == "y":
      price = input("please input the price of the item\n")
      user_name.addItem(price)
    elif line == "n":
      print(user_name.getTotal())
      print(user_name.getCount())
      break
    else:
        print("Error")

if __name__ == '__main__':
  main()