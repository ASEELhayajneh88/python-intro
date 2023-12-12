
import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter import messagebox
root= tk.Tk()
root.geometry('800x600+0+0')
root.title('Roaster and Coffee')

class Restaurant:
 def __init__(self): 
       self.menudic={}
       self.orderlist=[]
       self.orderdic={}


 def Additem(self):
      id=input('Enter the id ')
      if  id in self.menudic:
       print( " the Id found")
      else:
        name=input('Enter the name: ')
        price=int(input('Enter the price: '))
        description=(input('enter the descripition: '))
        self.menudic[id]={'name':name,'price':price,'description:':description}  
        print('item has been added successfully')   
 def print_dict(self):
        print (self.menudic)
        
 def search_item(self):
        id=input('Enter the id to search :')
        if id  in self.menudic:
         print ("Name of the Item",self.menudic[id]['name'])
         print ("Price of the Item",self.menudic[id]['price'])
         print ("Description of the Item",self.menudic[id]['description:'])
        else:
         print ('Item is not available')

 def delete_item(self):
        id=input("Enter the item id you want to delete ")
        if id in self.menudic:
               del self.menudic[id]
               print ("The item has been deleted from menu")
        else:
               print ("Item is not available")
               
      
     
                
 def placeorder(self):
       item= input('Please enter ID ')
       name= input('Please enter your name: ')
       phone= input('Please enter your phone: ')
       address= input('Please enter your address: ')
    
       for i in item :
        if i not in self.menudic:
         return f"item is not found"
     
       self.orderdic={'name':name,'phone':phone,'address:':address,'item':item}
       self.orderlist.append(self.orderdic)
       print("Order placed Successfully")
       print(self.orderlist)
       

def vieworders(self):
       
 for order in self.orderlist:
        print(order) 
                      
        
        
        
                     
         
meal=Restaurant()
while True:        
 print('welcome to my little restaurent') 
 print('__'*20)     
 print('1-Add a menu item: ')
 print('2-Search a menu item:  ')
 print('3-Delete a menu item: ')
 print('4-List all item: ')
 print('5- Place an Order: ')
 print('6- View Orders:')
 print('7- Exit: ')
 choice = input('enter your choice: ')
 if choice=='1':
        meal.Additem()
         
 elif choice == '2':
        meal.search_item()
            
 elif choice == '3':
        meal.delete_item()
        
 elif choice == '4':
        meal.print_dict()
 elif choice == '5':
        meal.placeorder()
 elif choice == '6':
        meal.vieworders()
        
 elif choice == '7':
        break
 else:
   print("Wrong Choice ")
   
   
   root.mainloop()
     