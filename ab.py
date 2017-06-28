
from steganography.steganography import *
'''
i=1
j=1
while(i<11) :
    secret=Steganography.decode("secret%d.jpg"%(j))
    print("message%d"%(i))
    print(secret)
    i=i+1
    j=j+1  '''
from datetime import datetime
t=datetime.now()
print(t)
print t.strftime("%H")
print("enter image\n")
ori=raw_input("enter\n")
out="output.jpg"
text=raw_input("enter message\n")
Steganography.encode(ori,out,text)
secret=Steganography.decode("out")
print(secret)