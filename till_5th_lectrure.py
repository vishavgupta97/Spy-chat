#import vishav                  #importing full file,runs also previous code in both cases
#from hello import x             #importing x from hello
print('vishav! what\'s up?')   #special character print
name=raw_input("raw input name\n")   #input function in python
print("length is with concatenation"+str(len(name))) #concatenation and length function,str function
print("your name is{0} and {1}".format("vishav","gupta"))#format function
a=3.99
print(type(a))#tells the type
age=raw_input("enter age\n")
age=int(age)
age1=27
if(age> age1 and age<34) : #if ,elif ,else use,and
    print("between 27 and 34\n")
elif(age>18 or age<age1) : #or,else if
    print("between 18 to 27")
elif(age<18):#not run always due to above elif
    print("less than 18\n")
else :
    print("above 34\n")
age1=float(age1)#changing to float
print("%f"%(age1))#use of place holderse
a=5
print("%d"%(a))
b=9.0009999999
print("after two place .%2f hhh"%(b))#two places
#print(vishav.l)#from vishav file
#print(x)# from hello.py
num=raw_input("enter number you want to reverse\n")
num=int(num)
rev=0
#use of while loop and hence reverse
while(num!=0) :
    rem=num%10
    rev=rem+rev*10
    num=num/10
print("reverse is %d"%(rev))
def fun() :            #function in python
    print("this is fun function\n")#definition
fun()#calling to function
order=['vishav','shimla',20]    #list in python name of list is order
i=1
#for loop is different in python
for z in order :
    print(str(i)+". "+str(z))
    i=i+1
order.append('JNV SHIMLA')#adding in last position of list
order.append(9.88)
x='g'
print("upper case is\t"+x.upper())#coverting g to G
print("length of list is \t"+str(len(order)))
count=0#used to print like 1.,2.
l=len(order)#l stores the length of list
while(count<l) :
    print(str(count)+"."+str(order[count]))#print like 0.,1.
    count+=1
#this is we studied upto 5th lecture
class A:
    def n(self):
        print("x")
    def __init__(self):
        print("vishav gupta\n")
w=A()
w.n()


