import string
      #code to sort a string according to lower case upper case nd no.
#  1st method

#s=list(input())
#s_upper=[]
#s_lower=[]
#s_odd_digits=[]
#s_even_digits=[]
#for i in s:
#    if i in string.ascii_lowercase:
#        s_lower.append(i)
#    elif i in string.ascii_uppercase:
#        s_upper.append(i)
#    elif i.isdigit() and int(i)%2==0:
#        s_even_digits.append(i)
#    elif i.isdigit() and int(i)%2!=0:
#        s_odd_digits.append(i)

#s_lower.sort()
#s_upper.sort()
#s_odd_digits.sort
#s_even_digits.sort()
#l=s_lower+s_upper+s_odd_digits+s_even_digits
#print("".join(l),sep="")



#second method
#def abc():
#    z=[]
#    y=[]
#    q=[]
#    x=input("Enter string:")
#    for i in x:
#        if(i.isdigit()):
#            z.append(i)
#        if(i.islower()):
#            y.append(i)
#            q.append(i)
#    b=sorted(z)
#    p=sorted(y)
#    m=sorted(q)
#    print("".join(p+m+b))
#abc()

                #to calculate gcd
#from fractions import gcd  
#gcd(20,4)

                #list comprehension

#nums=[1,2,3,4,5,6]
#nums_letters=[[n,l] for n in nums for l in letters]
#print(nums_letters)


