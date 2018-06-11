l=[1,2,3,4,5]
l.append(6) #to insert 1 value in list

l.extend([7,8,9]) #add list in list

l+[10,11,12]  # add list 

l.insert(0,0)  #add element from oth index

l.pop()  #del last element from the list

l.pop(1) #delete 1st index from the list

l.clear #to empty the list

l.sort(reverse=True) #sort in reverse order

l[-1::-1] #to sort in reverse

a=[1,2,3]
b=a #copy element
b==a #check if true or not
c=b.copy #copy element of b ,in case of change in b, c will not change
b[1]=3 #change the element in b
print a #it will also be changed when you changes b
d=c.copy()
d==c # 
d is c #

#code to print square of elements
a=[0,1,2,3,4,5,6,7,8,9,10]
for i in range(len(a)):
    a[i]=i*i
    print(a[i])

print([i**2 for i in range(10)]) #to print square of elements in range 0-10

#conditions for if elif and else statement

a=10
if a>10:
	print("if block")
elif a==10:
	print("elif block")
else:
	print("else block")

#output= elif block
	
#code to input student marks nd categorige his grade acoording to marks
l=[]
for i in range(int(input("How many students data do you want to enter:\n"))):
    a=input("Enter name:\n")
    b=int(input("Enter marks:\n"))
    grade=''
    if b>=81 and b<=100:
        grade="A+"
    elif b>=70 and b<=80:
        grade=-"A"
    else
        grade="R"
    l.append([a,grade])
    print(l)

#to print ascii value
#ord("a")
#chr(97)
#code to change to ascii value
a='abcdefghijklmnopqrstuvwxyz'
l=list(a)
for i in l:
    print(ord(i))



#2nd method
import string
for i in string.ascii_lowercase:
    print(ord(i))

#code to print in order of ([1,'a'],[1,'b'],[1,'c'],......)

[print([i,j]) for i in [1,2,3,4,5] for j in ['a','b','c']]

#code to print even no. in range 
l=[x for x in range(0,20) if x%2==0]
print(l)

#
dict_comp={x:chr(65+x) for x in range(1,11)}
print(dict_comp)

#
set_comp={x**3 for x in range(10) if x%2==0}
print(set_comp)

#has attribute
hasattr(str,'__iter__') #True
hasattr(str,'__iter')   #False


#generator expression
from sys import getsizeof
my_comp=[x*5 for x in range(1000)]
my_gen=[x*5 for x in range(1000)]
print(getsizeof(my_comp))
print(getsizeof(my_gen))


#to sort duplicate element nd calculate length nd show output as[0,len(l)]
#for hw
