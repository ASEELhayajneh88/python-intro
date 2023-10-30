print('hello word')
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
   
   
   
   
mypages={
    "mypages1":{
  'Title' : 'home page',
  'welcome' : 'hi to mypage',
  'content' : ['about,preview']
  },
    "mypages2":{
    'Title' : "good adventure",
    'welcome' : 'hi to mypage',
      'content' : ['about,preview']
  },
    "mypages3": {
    'Title' : 'home page',
  'welcome' : 'Thats great',
  'content' : ['about,preview']
  }
    }
for i in mypages:
    print (i, mypages[i])
    