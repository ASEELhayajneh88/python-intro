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

allperson= []
person= {}
print('welcom to our app')
while True:
    print('1- add new person')
    print('2-see all person')
    print('3-Exit')
    choice = input('enter your choice:')
    if choice =='1':
        
     name = input('enter your name :')
     age= ('enter age :')
     age= input("Enter your age: ")
     if age.isdigit():
      print(age)
     else:
         if age.isalpha():
           print("error. Please enter a number.")

     
     job= input('enter job :')
     
     person['name']= name
     person['age']= age
     person['job']= job
     allperson.append(person)
     
     print ('added sucsefully')
    elif choice == '2':
        counter = 1
        for i in allperson:
            print ('person',counter)
            for key in i:
             print('    ',key,':',i[key])  
             print(i)
        counter+=1
    elif choice=='3':
        
        break
            
     
     
  





    
