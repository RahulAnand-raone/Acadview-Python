#d = {'abc':1,'def':[1,2,3],'asw':"abc"}

# function is used to reuse the code

#def abc(a): 
#    print("hello",a)
#abc(input())

#def userInfo(name,age,info):
#    print("name:",name,"\n","age is:",age,"\n","length of info:",len(info))
#userInfo(input(),input(),input())

# make dictionary and take key value pair,it should contain all datatype in it eg

# difference between list comprehension and generator expression
   #slicing concept
#l=[1,2,3,4,5,6] 
#print(l[:])

#print(l[0:3])
#print(l[-5:-1])

#l = [1,2,3,4,5,6,7,8,9,10]
#l[1::2]
#l[0::2]


#l=[1,2,3,4,5,6]
#for i in range(len(l)):         # access index of list
#    print(i)

#for i in l:                    # will print actual valuse in list
 #   print(i)                


#l=[1,2,3,4,5,6]
#for i in range(len(l)):
#    print (l[i])

#for i in l:
#    print(i,end=" ")

#l=[1,2,3,4,5,6]
#for i in range(2,len(l),-1):
 #   print (l[i])

#for i in l:
  #  print(i,end=" ")

 
l=[1,2,3,4,5,6]
for i in range(0,len(l),2):
    print (l[i])
