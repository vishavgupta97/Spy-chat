print("enter a ,b,c\n")
a=raw_input()
b=raw_input()
c=raw_input()
if(a<b and a<c) :
    print("a is lowest")
elif(b<a and b<c):
    print("b is lowest")
else :
    print("c is lowest")
print("enter to check even or odd\n")
d=raw_input("enter\n")
d=int(d)
if(d%2==0) :
    print("even \n")
else :
    print("odd \n")
print("how many even numbers you want\n")
e=raw_input("kindly add \n")
e=int(e)
y=2
j=1
while(j<=e) :
    print(y)
    y=y+2
    j=j+1
print("enter to check prime or not\n")
p=raw_input("enter no\n")
p=int(p)
l=2
l=int(l)
n=1
while(l<p) :
   if(p%l==0):
       print("not prime\n")
       break
   else :
       l+=1
if(l==p) :
    print("prime \n")







