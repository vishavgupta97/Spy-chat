from spy_infom import Spy,spy,friends,ChattingMessages
#Spy_infom.py is A File where Details of Default Spy Is Stored

from datetime import datetime
#(It Is Used for Timestamping To Store The Time Of Sending A Message With Date)

from steganography.steganography import *
#(This Library Is Imported To Hide A message Under The Image And To Read A Secret Message

from colorama import init,Fore,Style
#(It is Imported Here For Using Different Colors For Different Texts)

import  sys                           #(It is Imported To Print A Statement In a Single Line Without Going To a New Line
                                      #Just Like println for New line and print For Same line In JAVA)

import re
#This Library Is Imported To Validate Certain Characters entered By Users Is Correct Or Not

#--------------------------------------Following are Available Status Messages------------------------------------------

STATUS_MSGS=['Don\'t Disturb! Busy Now','Very Happy','Enjoying Holidays','In a Meeting','Songs are my life']

init()

print(Fore.BLACK+"Welcome To Spy Chat Application\n")           #First Line Of Chat application

#NOTE:(HERE MESSAGES ARE PRINTED IN BLACK COLORS AND ONE OF THE OBJECTIVE OF THIS APPLICATION IS FULLFILLED)

print("We Are Very Happy To Get Your Presence Here\n")

print"Do You Want To Continue As "+Fore.RED+"%s %s %s Or Not"%(spy.salutation,spy.first_name,spy.last_name)

question=Fore.BLACK+"Kindly Enter Y for Yes and N for No\n"

answer=raw_input(question)   #answer stores whether user is existing or new

print(Style.RESET_ALL)

def add_status():
    init()
    updated_status_message = None

    if spy.current_status_msg !=  None:

        print Fore.GREEN+"Your current status message is %s \n" % (spy.current_status_msg)

    else:

        print Fore.BLACK+"You don\'t have any status message currently \n"

    while(True) :

        default = raw_input(Fore.BLACK+"Do you want to select from the older status (y/n)? \n") #This will be in black

        if(default.upper()=="Y" or default.lower()=="n" ) :
            #(This condition must be Satisfied otherwise It will Be ITERATE

            break

        else :

            continue


    if default.upper() == "N":

        init()

        sys.stdout.write(Fore.BLACK+" ")

        while(True) :

            new_status_message = raw_input("What status message do you want to set? ")

            v1=r"([a-zA-Z]+)"

            if len(new_status_message) > 0 and re.search(v1,new_status_message):

                STATUS_MSGS.append(new_status_message)

                updated_status_message = new_status_message

                break

            else :

                print ("Kindly Enter Valid Entries Only\n")

                continue

                #(IF USERS WILL ENTER ANY OF THE INVALID ENTRIES IT WILL ITERATE AGAIN AND AGAIN)


    elif default.upper() == 'Y':
        init()
        item_position = 1

        print Fore.BLACK+"YOU HAVE FOLLOWING OLDER STATUS\n"

        print "KINDLY SELECT ONE FROM THE BELOW\n"

        for message in STATUS_MSGS:

            print "%d. %s " % (item_position, message)

            item_position = item_position + 1
        try :

            message_selection = int(raw_input("\nChoose from the above messages "))


        except ValueError :

            print ("Please Enter A Value Only And Try Again\n")


        if len(STATUS_MSGS) >= message_selection:

            updated_status_message = STATUS_MSGS[message_selection - 1]

    else:

        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:

        print 'Your updated status message is: %s' % (updated_status_message)

    else:

        print 'You current don\'t have a status update'

    return updated_status_message #(UPDATED MESSAGES WILL BE RETURNED AFTER SATISFYING ALL BOUNDARY CONDITION)



'''ALTERNATIVE WAY OF ABOVE METHOD CAN BE FOLLOWING
def add_status() :                       #definition for adding new status
    init()
    updated_status_msg=None

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
    return updated_status_msg  
    
    #THIS CAN ALSO BE USED INSTEAD OF ABOVE'''

def add_new_friend() :

    new_friend_detail=Spy('','','',0.00 ,0,'','') #NEW OBJECT new_friend_detail OF SPY CLASS IS CREATED FOR ADDING
                                                  #NEW FRIEND

    while True :

        v2=r"([a-zA-Z]+)"    #VALIDATING FIRST,LAST NAME IN SHORT USING re LIBRARIES

        new_friend_detail.first_name=raw_input("What is the First Name Of Your Friend\n")

        new_friend_detail.last_name=raw_input("What is the Last Name Of Your Friend\n")

        new_friend_detail.salutation=raw_input("Enter The appropriate Salutation for Your Friend\n")

        if re.search(v2,new_friend_detail.first_name) and re.search(v2,new_friend_detail.last_name) and re.search(v2,
        new_friend_detail.salutation) :

            break

        else :

            print "You Have Entered Some Invalid Entry\nKIndly Continue"

            continue #ITERATE AGAIN IF THERE IS MISSING SOMETHING

    while True:

        try :

            new_friend_detail.rating=float(raw_input("Enter Ratings\n"))

        except ValueError:

            print "kindly enter valid detail"

            continue

        if new_friend_detail.rating<0:

            print "rating can't negative"

            continue
        else :

            break

    while True :

        try :

            new_friend_detail.age=int(raw_input("Enter Age Of Your friend\n"))

        except ValueError :

            print("Kindly add valid entry")
            continue

        if new_friend_detail.age<0 :

            print  "age can't be negative"

            continue

        else :

            break
    while(True) :
        v3=r"([a-zA-Z]+)"

        new_friend_detail.interest=raw_input("Enter your friend Interest\n")

        new_friend_detail.hometown=raw_input("Enter His\Her Hometown\n")

        if re.search(v3,new_friend_detail.interest) and re.search(v3,new_friend_detail.hometown) :

            break

        else :
            print("Something Went Going")

            continue

    print("FRIEND SUCCESSFULLY ADDED\n NOW WE HAVE NEW FRIEND\n")

    friends.append(new_friend_detail)

    print("You Have Currently %d friends\n"%(len(friends)))

    return len(friends)  #RETURN NUMBER OF FRIENDS CURRENTLY WE HAVE

def selection_of_friend() :

    num=1

    print("Enter friend number to perform appropriate operation\n")

    print("PLEASE ENTER A VALID NUMBER ONLY TO PERFORM SUCCESSFUL OPERATION")    #ALERT TO SPY

    for friend in friends :

        print("%d. %s %s aged %d with rating %f is online\n"%(num,friend.first_name,friend.last_name,friend.age,friend.rating))

        num+=1

    while True:

        try :

            friend_numb=int(raw_input("Now Enter A Number\n"))

        except ValueError:

            print("Kindly Enter Valid Number Only")

            continue

        if friend_numb < 0:

            print "Sorry your response cannot be negative"

            continue

        else:

            break

    friend_selected=friend_numb-1

    return friend_selected        #RETURNING CHOICE OF USER FOR SELECTING A FRIEND

def send_a_secret_message() :     #This Function Is Used To Send a Secret Message To A Friend

    sys.stdout.write(Fore.BLACK+" ")

    message_to=selection_of_friend()     #Calling To A function that will return selected friend


    original_image=raw_input("What is The Name Of Image Under Which You Want To Hide A Message\n")

    while True:
        sys.stdout.write(Fore.Red+"  ")
        global text
        text=raw_input(Fore.CYAN+"\nWRITE TEXT MESSAGE THAT YOU WANT TO SEND\n")
        v3=r"([a-zA-Z]+" ")"
        if re.search(v3,text) :
            break
        else :
            print("Kindly Enter A Valid Message Only\n")
            continue
    if len(text)>100 :
        print(Fore.RED+"\nYOU HAVE ECEEDED THE LIMIT OF SENDING THE MESSAGE")
        print("SORRY WE ARE REMOVING YOU")
        del friends[selection_of_friend]

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

    #output_path=raw_input("What Is The Name of Image From Which You Want To Read A Text\n")

    secret_text=Steganography.decode("output.jpg")

    print ("The Text Message Is %s "%(secret_text))

    new_chat=ChattingMessages(secret_text,False)

    friends[sender].old_chats.append(new_chat)

    print("Very Very Thanks For Reading A message\n")

def read_history_of_chat() :

    chat_between=selection_of_friend()

    chat_between+=1

    print("You Have Selected Friend Number %d"%(chat_between))

    for chat in friends[chat_between].old_chats :

        init()

        if chat.sent_by_me :

            print(Fore.BLUE+"[%s] "+Fore.GREEN+" %s %s"%(chat.sending_time.strftime("%d %B %Y"),+Fore.CYAN+
                  "You said",chat.message))

#HERE PRINTING CHAT HISTORY USING DIFFERENT COLOR AND TIME USING BLUE COLOR,SATISFYING ONE OF THE APPLICATION OBJECTIVE

        else :

            print(Fore.BLUE+"[%s} "+Fore.RED+" %s said %s"%(chat.sending_time.strftime("%d %B %Y"),friends[chat_between].first_name

                        ,chat.message))

            #PRINTING CHAT HISTORY USING DIFFERENT COLORS AND CHAT USING DIFFERENT COLOR AND SPY NAME IN RED COLOR

def start_chat(spy):

    spy.first_name = spy.salutation + " " + spy.first_name +" " +spy.last_name

    if spy.age > 12 and spy.age < 50:

        init()

        print Fore.BLACK+"Authentication complete. Welcome "+Fore.RED+" %s "+Fore.BLACK+"of age %d " \
                            "and rating of %f"%(spy.first_name,spy.age,spy.rating)

        #PRINTING SPY NAME USING RED COLORS AND MESSAGES USING BLACK COLORS

        sys.stdout.write("Proud To Be Here\n") #USING SYS LIBRARY

        show_menu = True

        while show_menu:

            print("\tWHICH OPERATION DO YOU WANT TO PERFORM \n")

            print("\tKindly Select From Following Operatioons")

            print("\t1. Add A Status For Updation")

            print("\t2. Add A New Friend")

            print("\t3. Send A Secret Message To A Friend")

            print ("\t4. Read A Secret Message")

            print ("\t5. Read Older Chats From A User")

            print ("\t6. Closing The Application")

            menu_choice = raw_input("Kindly Add One Choice From Above\n")

            if len(menu_choice) > 0:

                menu_choice = int(menu_choice)

                if menu_choice == 1:

                    spy.current_status_msg = add_status()

                elif menu_choice == 2:

                    number_of_friends = add_new_friend()

                    print 'You have %d friends' % (number_of_friends)

                elif menu_choice == 3:

                    send_a_secret_message()

                elif menu_choice == 4:

                    read_a_message()

                elif menu_choice == 5:

                    read_history_of_chat()

                else:

                    show_menu = False

                    continue

    else:

        print "Sorry you are not of the correct age to be a spy"

if answer.upper() == "Y":

    start_chat(spy)

elif answer.lower()=="n" :

    spy = Spy('', '','',0.00,0,'','')

    spy.first_name = raw_input("Welcome to spy chat application, you must tell me your first name :\n ")

    spy.last_name=raw_input("Now Kindly Tell Me Your Last Name\n")

    if len(spy.first_name and spy.last_name) > 0 :
        spy.salutation = raw_input("Please Enter An Appropriate Salutation Which Is Suitable For You\n ")

        spy.age = raw_input("What is Your Age\n")

        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")

        spy.rating = float(spy.rating)

        start_chat(spy)

    else :

        print("Enter A Valid Spy Name Only")

else:

    print("Please Enter A Valid Character Only\n")







