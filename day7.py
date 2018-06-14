# pip-it is a pakage manager,to fetch module from site and install it.


#exception handling
class TransitionError(Exception):
    def __init__(self,prev,nex,msg):
        self.prev=prev
        self.next=nex
        self.msg=msg
try:
    raise(TransitionError(2,3*2,"Not Allowed"))
except TransitionError as error:
    print("kshdurgfyre",error.msg)

#try:
#   print(1/0)
#except ZeroDivisionError as e:
#    print(e)
#except ValueError as e:
#    print(e)
#finally:
#    print("This will always run")



#code to call api

#from requests import get
#n=int(input("How many quotes do you want to fetch:\n"))

#for i in range(n):
 #   try:
#        r=get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&j:")
#        print(r.json())
#        d=r.json()
 #       for key in d.keys():
  #          if key=="quoteAuthor":
   #             print("Author",d['quoteAuthor'])
    #            print("Quote:",d['quoteText'])
     #   print("-"*5)
   # except Exception as e:
        #d['quoteText']=d['quoteText'].replace('//','/')
        #print("Author:",d['quoteAuthor'])
       #print("Quote:",d['quoteText'])
       # print("-"*5)
