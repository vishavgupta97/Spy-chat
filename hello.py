print("vishav\n")
x=5
print('what\\\\\\\'s up?\n')
print("what's\"vishav \"up\n")
name=raw_input("what is yor name\n")
print("your name is "+name)
s="your name is\n "+name
print(len(s))
print(len("  "))
if(len(s)>0) :
    print("length is greater than 0")
else :
    print("length is less than 0")
age=raw_input("enter age\n")
print(type(age))
int(age)
rate=raw_input("enter ratings\n")
float(rate)
if (age>12 and age<47):
    print("nice to meet you")
else :
    print("not eligible")
print("your name is\n"+s+"your age is\n"+age)