from spy_infom import Spy,spy,friends,ChattingMessages

from datetime import datetime

from steganography.steganography import *

from colorama import init,Fore,Style   #It is Used For Coloring Purpose
init()
print (Fore.BLUE + "vishav")
print (Style.RESET_ALL)
#--------------------------------------Following are Available Status Messages------------------------------------------


STATUS_MSGS=['Don\'t Disturb! Busy Now','Very Happy','Enjoying Holidays','In a Meeting','Songs are my life']

init()

print(Fore.BLUE+"Welcome To Spy Chat Application\n")           #First Line Of Chat application

print("We Are Very Happy To Get Your Presence Here\n")

print("Do You Want To Continue As %s %s %s Or Not"%(spy.salutation,spy.first_name,spy.last_name))

question="Kindly Enter Y for Yes and N for No\n"

answer=raw_input(question)               #answer stores whether user is existing or new
print(Style.RESET_ALL)


def add_status() :                       #definition for adding new status

    init()

    if spy.current_status_msg is None :

        print(Fore.GREEN+"You Did Not have Any Status Message\n Kindly Add It")

    else :

        print("Your Current Status Message Is \n %s \n" % (spy.current_status_msg))    #spy has previous status

    add=raw_input("Do You Want To Add Status From Older Messages Or Want New \tPress Y or N\n\n")

 #if user enters something and it must be either Y or N only than if block will execute (BOUNDARY CONDITIONS FULLFILL)


    if(len(add)>0 and add.upper()=="Y" or add.upper()=="N") :

        if(add.upper()=="Y") :

            print("\n\n\t\tSELECT STATUS FROM FOLLOWING\n")

            status_num=1
            for x in STATUS_MSGS :

                print("\t\t%d. %s"%(status_num,x))

                status_num+=1

        num=int(raw_input("Enter The Number Correspondiong To The Status\n"))

        exact_num=num-1

        updated_status_msg=STATUS_MSGS[exact_num]

    elif(add.lower()=="n") :

        ques="What Is The Status That You Want To Update\n"

        ans=raw_input(ques)

        if(len(ans)>0) :

            updated_status_msg=ans

            STATUS_MSGS.append(updated_status_msg)

        else :

            print("you didn't enter something\n")

    else :

        print("Kindly Enter A Valid Character And Repeat The Same Procedure\n")

        add_status()         #RECURSSION BECAUSE USER DOES NOT ENTER CORRECT CHARACTER THAT IS Y OR N

    print (Style.RESET_ALL)

    return updated_status_msg

def add_new_friend() :

    new_friend_detail=Spy('','','',0.00 ,0,'','')

    new_friend_detail.first_name=raw_input("What is the First Name Of Your Friend\n")

    new_friend_detail.last_name=raw_input("What is the Last Name Of Your Friend\n")

    new_friend_detail.salutation=raw_input("Enter The appropriate Salutation for Your Friend\n")

    new_friend_detail.rating=float(raw_input("Enter Ratings\n"))

    new_friend_detail.age=int(raw_input("Enter Age Of Your friend\n"))

    new_friend_detail.interest=raw_input("Enter your friend Interest\n")

    new_friend_detail.hometown=raw_input("Enter His\Her Hometown\n")


#----------------------------------    FOLLOWING ARE BOUNDARY CONDITIONS    --------------------------------------------



    if(len(new_friend_detail.first_name)>0 and len(new_friend_detail.last_name)>0 and new_friend_detail.age>12) :


        if(len(new_friend_detail.hometown)>0 and new_friend_detail.age<50 and len(new_friend_detail)>0) :


            print("Very Nice\n")

            print("FRIEND SUCCESSFULLY ADDED\n NOW WE HAVE NEW FRIEND\n")

            friends.append(new_friend_detail)

        elif(new_friend_detail.age<12 or new_friend_detail.age>50) :

            print("spy age must be in Between 12 to 50 \nSorry We can't able to add you\n")

        else :

            print("Invalid Entries\n")

            print("kindly try again adding new friend\n")

            add_new_friend()



#-----------RECURSSION DUE TO INVALID ENTRIES SO THAT SPY CAN ADD A VALID ENTRIES---------------------------------------

    else :

        print("Something went wrong!!!kindly try again\n")

    print("You Have Currently %d friends\n"%(len(friends)))

    return len(friends)  #RETURN NUMBER OF FRIENDS CURRENTLY WE HAVE

def selection_of_friend() :

    num=1

    print("Enter friend number to perform appropriate operation\n\n")

    print("PLEASE ENTER A VALID NUMBER ONLY TO PERFORM SUCCESSFUL OPERATION\n")    #ALERT TO SPY

    for friend in friends :

        print("%d. %s %s aged %d with rating %f is online\n"%(num,friend.first_name,friend.last_name,friend.age,friend.rating))

        num+=1

    friend_numb=int(raw_input("Now Enter A Number\n"))

    friend_selected=friend_numb-1

    return friend_selected        #RETURNING CHOICE OF USER FOR SELECTING A FRIEND

def send_a_secret_message() :     #This Function Is Used To Send a Secret Message To A Friend

    message_to=selection_of_friend()     #Calling To A function that will return selected friend

    original_image=raw_input("What is The Name Of Image Under Which You Want To Hide A Message\n")

    init()

    text=raw_input(Fore.CYAN+"WRITE TEXT MESSAGE THAT YOU WANT TO SEND\n")

    print(Style.RESET_ALL)

    output_path=raw_input("What You Will Call Encrypted Message Under Image\n")

    Steganography.encode(original_image,text,output_path)     #This will hide A Message Under The Image

    new_chat=ChattingMessages(text,True)          #object of class ChattingMessages Is Created

    friends[message_to].old_chats.append(new_chat)     #!!!!!!Very Important Statement!!!!!!!!

#ABOVE STATEMENT WILL STORES TO WHICH FRIEND WHEN WE SEND A PARTICULAR MESSAGE AND THIS WILL ALSO STORES OUR CHATS ALSO

    print ("your secret image is ready\n")
    print("Your Message Is Successfully send To Your Friend\n")
    print("Thanks For Using Our Application for Chatting\n\n")


def read_a_message() :

    sender=selection_of_friend()        #Which Chat Do You Want To Read,Who is the SEnder

    output_path=raw_input("What Is The Name of Image From Which You Want To Read A Text\n")

    secret_text=Steganography.decode(output_path)

    print ("The Text Message Is %s "%(secret_text))

    new_chat=ChattingMessages(secret_text,False)

    friends[sender].old_chats.append(new_chat)

    print("Very Very Thanks For Reading A message\n")

def read_history_of_chat() :

    chat_between=selection_of_friend()

    print("You Have Selected Friend Number %d"%(chat_between))

    for chat in friends[chat_between].old_chats :

        if chat.sent_by_me :




