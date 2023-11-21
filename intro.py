# import numbers
# print('hello word')
# sintacs in py
# data type in py
# 1- string
# name='ahmad'
# " "
# ''
# name2=""" hi
# ahmad """ # # as comment+you can down in line 
# print(name2)
#2- numbe - int:1,2,3,,4,5>
# numb2=1

# print(numb2)
# print(type(numb2))
#3- float: 1.2,2.2>
# 4- boolean: true, false
#5- list:[1,2,3,4,5,,6,7,8,9,0,>]
# index:0,1,2,3,4,5,6,7,8,9,0
#6 - tuple:(1,2,3,4,5,6,7,8,9,0>)
#tuple is unchangeable
# tb= (1,2,3,4,5,,6,7,8,,9,0)
# print(tb)
#7-  dictonary:{key:value}
# person = {'name':'aseel','age':'22'}
# print(person)
# x=2
# y=1
# if x == y:
#     print('i am if')
# elif x>y:
#     print('i')
       
# operator in py
# 1-arthmatic:+,-,*,%.**
# x=10**5
# print(x)
# print(5=='5')
#2-assigment: =,+=,/
#3-comprision: ==,!=,<,>
#4-logical: and ,or,not
#5- identity: is,is not


#for in py
# for var in iterable:# iterable,list,tuple,string
# arr1=[5,3,2,6,7,8,9,0]
# for i in arr1:
#      if i==6:
#          print(i)
# home = {
#     'Title':'Home page',
#     'welcome':'Hello in home page ',
#     'Content':['About','preview']
# }

# for i in home:
#     print (i, home[i])
   
   
   
   
# mypages={
#     "mypages1":{
#   'Title' : 'home page',
#   'welcome' : 'hi to mypage',
#   'content' : ['about,preview']
#   },
#     "mypages2":{
#     'Title' : "good adventure",
#     'welcome' : 'hi to mypage',
#       'content' : ['about,preview']
#   },
#     "mypages3": {
#     'Title' : 'home page',
#   'welcome' : 'Thats great',
#   'content' : ['about,preview']
#   }
#     }


# for i in mypages:
#     print (i, mypages[i])
    
   
   
# chose1= input ('enter your choice:') 
# if chose1 != numbers:
#   print('wrong input')

# print(chose1)a
# if False:
#       print('a')
# else:
#       print('b')


#finction in py :is a block of code which only 
# def myfunction():
# print ('hello)
#myfunction()
# How to check if number is odd or even

# num= int(input("Enter number: "))

# if num % 2 == 0:
#     print(" is even")
# else:
#     print(" is odd")

# num=int(input("Enter any number: "))
# #check the prime number using num>1 condition
# if num>1:
#     for i in range(2,num):
#         if(num%i)==0:
#             print(num," is not a prime number")
#             break;
#     else:
#         print(num," is a prime number")



# def my_function(fname):
#  print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")




# def number(i):
#     if i % 2 == 0:

#         return "even"
#     else:

#         return "odd"
# i = int(input("Enter a number: "))
# result = i(i)
# print("The number is", result)1


#while loop
# i=0
# wileTest = True
# while wileTest:
    
#     if i == 5:
#        i+=1
#        continue
#     print(i)
#     i+=1
#     if i == 10:
#         break
  

# name= input('enter name')
# print(name)
# # person 

# allperson= []
# person= {}
# print('welcom to our app')
# while True:
#     print('1- add new person')
#     print('2-see all person')
#     print('3-Exit')
#     choice = input('enter your choice:')
    
#     if choice =='1':
        
#      name = input('enter your name :')
#      age= ('enter age :') 
#      age= input("Enter your age: ")
#     #  if age.isdigit():
#     #   print(age)
#     #  else:
#     #      if age.isalpha():
#     #        print("error. Please enter a number.")

#      job= input('enter job :')
#     while True: 
#      try:
#            age= int(input('enter age'))
#            break
#      except:
#         print('please enter number')  
    
#     person={
#         'name':name,
#         'age':age,
#         'job':job
        
#     }
#     allperson.append(person)
     
#     print ('added sucsefully')
    
#     elif choice =='2':                
#     counter = 1
#     for i in allperson:
#             print ('person',counter)
#             for key in i:
#              print('    ',key,':',i[key])  
#              print(i)
#             counter+=1
        
#     break
            
     
# list1=['a','d','b','d','e','1','2']
# list1.sort()
# print(list1)
# list1.reverse()
# print(list1)
# print(list1.count('2'))
# print(list1.__len__())
# list1.pop(1)


#method in dic: keys{}, values{},items{},get{}
# dic1={
#     "name":"ali",
#     "family":"hay",
#     "age":30,
# }
#key method: to get all keys in dic
# print ('key method',dic1.keys())
#value method: to get all keys in dic
# print ('value',dic1.values())
#item method: to get all keys in dic
# print('item:',dic1.items())
# get method:to get value of the key
# print('get:',dic1.get('name'))
# dic1()
# dic1={'name':'ahmad'}
# dic1['skills'].append('html')

# print('get method :',dic1)
# name=input('enter name')
# passo=input('enter pass')
# print (f"hello {name} your password is {passo}")


# print('welcome to app')
# i=0
# while True:
#     print( '__'*20)
#     print('1-create account')
#     print('2-login')
#     print('3-Exit')
#     print('4-show all person')
#     choice = input('enter your choice:')
    
#     if choice =='1':
#      name = input('enter your name :')
#     while True:
#         try:
#          age=int(input('enter age:'))
#          break
#         except Exception as e:
#             print(e)
#             continue
#     job=int(input('enter the person job:'))
#     person={
#         'name':name,
#       'age':age,
#       'job':job,
#     }
    
#     allperson.append(person)
#     print(allperson)
#     print('you added person successfully')
    
#     elif choice == '2':
#     counter=1
#     print('__'*20)
    
#     print('allperson')
#     for i in allperson:
#      print('person',counter)
     
# allperson= []
# person= {}           
# print('welcome to app')
# x=0
# while True:
#     print( '__'*20)
#     print('1-create account')
#     print('2-login')
#     print('3-Exit')
#     print('4-show all person')
#     print('5-Edit a person')
#     choice = input('enter your choice:')
    
#     if choice =='1':
#         name = input('enter your name :')
#         if allperson!=[]:
#             isExited= True
              
#             for i in allperson:
#                 if name ==i['name']:
#                    print('this user already exist  ')
#                    name=input('enter the user name')
#                    isExited=True                  

#                    break
#             else :
#                 isExited=False                   
                    
                    
            
#         while True:
#             try:
#                 age=int(input('enter age:'))
#                 break
#             except Exception as e:
#                 print('enter a valid age')
#                 continue
#         job=input('enter the user job:')
#         skills=[]
#         while True:
#              try:
#                 counter2=int(input('enter the number of skills:'))
#                 break
#              except Exception as e:
#                  print('enter a valid number')
#                  continue
#         for i in range (counter2):
#             skill=input('enter the skill number:',i+1,':')
#             skills.append(input())
            
#         while True:
                
#            password=input('enter the password')
#            numberChar=False
#            upperChar=False
#            lowerChar=False
#            if len(password)>=8:     
#             for i in password:
#                 if i.isdigit():
#                     numberChar=True
#                 elif i.isupper():
#                     upperChar=True
#                 elif i.islower():
#                     lowerChar=True
                
                    
#                     if upperChar and numberChar and lowerChar:
#                       print("Password is strong")
#                     break
#                 else:
                    
#                     print('the password is not strong')
#                     continue
                
#             else:
#                 list1=[upperChar,lowerChar,numberChar]
#                 list2=['upperChar','lowerChar','numberChar']
#                 list3=[]
#                 for i in range(len(list1)):
#                     if list1[i]:
#                         list3.append(list[i])
#                         i=1
#                 print('the password must be at least 8 characters long')
#                 break

#            person={
#             'name':name,
#             'age':age,
#             'job':job,
#             'password':password
#           }
#            allperson.append(person)
#            print(allperson)
#            print('you added person successfully')

#     elif choice == '2':
        
        
       
#          print('__'*20)
#          print('please enter your name and password')
#          name= input('enter the user name')
#          password=input('enter the password')
#          for i in allperson:
#              if i['name']==name and i['password']==password:
#                  print('welcome',name)
#                  break
             
#              else:
#                  print('wrong username or password')
#                  break
             
             
             
#     elif choice =='3':
#         print('thank you for using ')
#         break
#     elif choice=='4':
#         isAdmin=input('please enter the admin password')
#         if isAdmin=='admin':
            
#            counter=1
#            print('__'*20)
    
#            print('allperson:')
#            for i in allperson:
#             print('person',counter)
#             for key in 1:   
#                 print('   ',key,':',i[key])
#                 counter+=1
#             else:
#                 print('wrong password re enter the choice')
                 
#            else :
#                print('invalid option please try again')
                      
#         else:
#              print('wrong choice')          
#              x+=1
    
          
# def checkLetter(letter, word, guess_word):
 
#     for c in word:
#         if c == letter:
#             guess_word[word.index(c)] = c
#             word[word.index(c)] = '*'
 
#     return guess_word
 
 
# word = list('hello')
# guess_word = ['_' for x in word]
 
# print(guess_word)
# while '_' in guess_word:
#     guess = input('Letter: ')
#     print(checkLetter(guess, word, guess_word))
         
     





    
     
# print('welcome to hand man game')
# print('start guessing')
# word=('Aseel')
# guesses=''
# possible=8
# while possible>0 :
#     faild= 0
#     for char in word:
#         if char in guesses:
#             print(char,end="")
#         else:
#             print("_ ",end="")
#             faild+=1
#             if faild==0:
#                 print('win')
#                 break
#     guess = input("guess a character:")  
#     guesses += guess 
#     if guess not in word:
#         possible-=1
#         print('wrong')
#         if possible == 0:   
#             print('you lose')
# import random



                
# import random
# print ("welcome to play hangman!")
# ## A List Of Secret Words
# words = ['aseel','programming','full','hayajneh']
# word = random.choice(words)
# guesses = ''
# possible= 5
# while possible > 0:         
#     failed = 0             
#     for char in word:      
#         if char in guesses:    
#             print (char,end="")    
#         else:
#             print ("_",end=""),     
#             failed += 1    
#     if failed == 0:        
#         print ("\nYou won") 
#         break              
# guess = input("\nguess a character:") 
# guesses += guess                    
# if guess not in word:  
#         possible -= 1        
#         print("\nWrong")    
#         print("\nYou have", + possible, 'more guesses') 
#         if possible == 0:           
#             print ("\nYou Lose") 
        
# class person():
#     """ هون شرح لتظهر """
#     #multry attr>every attr is a var
#     def __init__(self,name,age,job,skills,password):
#         #ATTRibute name = self.varname
#         self.name=name
#         self.age=age
#         self.job=job
#         self.skills=skills
#         self.password=password
            
#     def nameAndage(self):
#         return f'name:{self.name}, age:{self.age}'
#     def callPerson(self,person):
#         """this method will used to call a person"""
#         return f'{self.name} is calling {person}'


#     def __str__(self):
#         return f'name:{self.name},age:{self.age},job:{self.job},skills:{self.skills}'
    
# def checkpass():
                
# person1=person('Aseel','23','student','python')
# person2=person('ali','23','eng','jave')
# print(person1)
# print(person2.nameAndage())
# print(person2.callPerson('amjad')
#Create menu item to restaurnet  whith id uniqe using A-Z ,a-z,0-9 and stored in dic.


        
                
                               
    
        
        


          










# class Restaurant:
#  def __init__(self): 
#        self.menudic={}
#        self.orderlist=[]
#        self.orderdic={}


#  def Additem(self):
#       id=input('Enter the id ')
#       if  id in self.menudic:
#        print( " the Id found")
#       else:
#         name=input('Enter the name:')
#         price=int(input('Enter the price'))
#         description=(input('enter the descripition:'))
#         self.menudic[id]={'name':name,'price':price,'description:':description}  
#         print('item has been added successfully')   
#  def print_dict(self):
#         print (self.menudic)
        
#  def search_item(self):
#         id=input('Enter the id to search :')
#         if id  in self.menudic:
#          print ("Name of the Item",self.menudic[id]['name'])
#          print ("Price of the Item",self.menudic[id]['price'])
#          print ("Description of the Item",self.menudic[id]['description:'])
#         else:
#          print ('Item is not available')

#  def delete_item(self):
#         if id in self.menudic:
#                 del self.menudic[id]
#                 print ('Item deleted successfully')
#         else:
#                 print ('Item is not available')
#  def placeorder(self):
#        item= input('Please enter IDS seperated by comma ').split(',')
#        name= input('Please enter your name: ')
#        phone= input('Please enter your phone: ')
#        address= input('Please enter your address: ')
    
#        for i in item :
#         if i not in self.menudic:
#          return f"item is not founf"
     
#        self.orderdic={'name':name,'phone':phone,'address:':address,'item':item}
#        self.orderlist.append(self.orderdic)
#        print("Order placed Successfully")
#        print(self.orderlist)
       

# def vieworders(self):
#     for order in self.orderlist:
#      print(order) 
                      
        
        
        
                     
         
# meal=Restaurant()
# while True:        
#  print('welcome to my little restaurent') 
#  print('__'*20)     
#  print('1-Add a menu item: ')
#  print('2-Search a menu item:  ')
#  print('3-Delete a menu item: ')
#  print('4-List all item: ')
#  print('5- Place an Order: ')
#  print('6- View Orders:')
#  print('7- Exit: ')
#  choice = input('enter your choice: ')
#  if choice=='1':
#         meal.Additem()
         
#  elif choice == '2':
#         meal.search_item()
            
#  elif choice == '3':
#         meal.delete_item()
        
#  elif choice == '4':
#         meal.print_dict()
#  elif choice == '5':
#         meal.placeorder()
#  elif choice == '6':
#         meal.vieworders()
        
#  elif choice == '7':
#         break
#  else:
#    print("Wrong Choice ")
         
         




























