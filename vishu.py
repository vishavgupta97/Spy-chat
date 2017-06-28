#import new1
#print(new1.b)
from datetime import datetime
li=[]
spy={'name':"",'class':"",'roll':39}
li.append(spy)
li.append(spy)
for x in li :
    print x
print(len(li))
print(spy['roll'])
print(len(spy))
s='K'
if s.upper()=='K' :
    print("vishav gupta\n")
li1=[3,99]
li2=[9,10,15,99,88]
print cmp(li1,li2)#methods of list
print cmp(li2,li1)
li3=[4,'vishu']
print cmp(li1,li3)
print(datetime.now())
s=datetime.now()
print(s.time())
timedel=datetime.timedelta(7)
tday=datetime.now()
print(tday-timedel)
