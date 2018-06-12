#code to fetch no. from string and sum it
#r=input("Enter the string:")
#s=''.join(x for x in r if x.isdigit())
#a=[int(x) for x in s]
#b=sum(a)
#j=[int(i) for i in str(b)]
#k=sum(j)
#print(k)


#min()-extracts min value from the list
#max()-"        max value from list

#l=[1,2,3,4,5]
#min(l)

#abs()
#variable types:global,local,non-local
#pprint methods

#example of local variable
#def abc():
 #   a=print(a)
#abc()
#print(a)


#beautifulsoup fn for web scrapping
#import bs4 as bs
#from pprint import pprint
#import urllib.request
#sauce=urllib.request.urlopen('https://www.lpu.in').read()
#soup=bs.BeautifulSoup(sauce,'lxml')
#print(soup.title.text)

#for url in soup.find_all('a'):
 #   pprint(url.get('href'))

#code to extract no. from string nd add it

l=list(input())
n=[]
sum=0
for i in range(len(l)):
    if (l[i]).isdigit():
        n.append(l[i])
    else:
        if len(n)!=0:
            s="".join(n)
            sum+=int(s)
            n.clear()

if len(n)>0:
    s="".join(n)
    sum+=int(s)
    n.clear()

temp=0
while len(list(str(sum)))!=1:
    while sum!=0:
        temp+=sum%10
        sum=int(sum/10)
    sum=temp
    temp=0
print(sum)
    
