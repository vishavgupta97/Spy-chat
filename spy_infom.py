
from datetime import datetime            #Importing Datetime To Store The Timing When We Have Send A Particular MSG...

class Spy :
                                         # THIS IS CONSTRUCTOR TO STORE SPY DETAILS
    def __init__(self,first_name,last_name,salutation,rating,age,interest,hometown):

        self.first_name=first_name

        self.last_name=last_name

        self.salutation=salutation

        self.rating=rating

        self.age=age

        self.interest=interest           # Which Is The Interested  Area of The Spy

        self.hometown=hometown

        self.is_online=True

        self.old_chats=[]                #This Is a list to store Chatting details

        self.current_status_msg=None     #None is like NULL Keyword in C++

class ChattingMessages :

    def __init__(self,message,sent_by_me):

        self.message=message

        self.sending_time=datetime.now()#Stores The time When we Have Send A Particular Message with help of Datetime

        self.sent_by_me=sent_by_me


spy=Spy('Vishav','Gupta','Mr.',5.99,20,'Programming','Shimla')     #Current Spy
#Here spy is the object of class spy

#------------------------FOLLOWING ARE FRIENDS OF THIS SPY---------------------------------------------------------------

friend_1=Spy('Adil','Thakur','Mr.',6.00,21,'Playing','Mumbai')

friend_2=Spy('Arushi','Sharma','Ms.',6.8,18,'Chatting','Sri Nagar')

friend_3=Spy('Surbhi','Gupta','Mrs.',5.99,30,'Travelling','Chandigarh')

friend_4=Spy('Amit','Mehta','Dr.',9.00,28,'Eating','Bhopal')


friends=[friend_1,friend_2,friend_3,friend_4] #LIST WHICH IS STORING OBJECTS OR DETAILS OF FRIENDS OF SPYsp