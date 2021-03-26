import time #used in time.sleep() which is in def clear()
from os import system #used to clear screen
import re #regex, used to compile words together.
import copy #used where global can't be accessed
import random #used for RAD
from datetime import date #used for date in dashboard
import copy #used for when global isn't accessible 

#sleep 0.5
def sleep05():
    time.sleep(0.5)

#clear screen after 0.75 seconds
def clear090():
    time.sleep(0.90)
    system('cls')
    
#clear screen after 1.75 second
def clear():
    time.sleep(1.75)
    system('cls')

#what will be shown when you open up the app
def startup():
    print("   _             _              _       _         _                __                  ")
    print("  (_)           | |            ( )     (_)       | |              / _|                 ")
    print("   _   ___  ___ | |_  ___  _ __|/ ___   _  _ __  | |_  ___  _ __ | |_  __ _   ___  ___ ")
    print("  | | / _ \/ __|| __|/ _ \| '__| / __| | || '_ \ | __|/ _ \| '__||  _|/ _` | / __|/ _ \ ")
    print("  | ||  __/\__ \| |_|  __/| |    \__ \ | || | | || |_|  __/| |   | | | (_| || (__|  __/")
    print("  | | \___||___/ \__|\___||_|    |___/ |_||_| |_| \__|\___||_|   |_|  \__,_| \___|\___|")
    print(" _/ |                                                                                  ")
    print("|__/                                                                                   ")
    clear()



#conditions for password and username
specialchar = re.compile('[!@#$%^&*()]') #used for password and username
numbers = re.compile('[1234567890]') #used for password
lowercase = re.compile('[abcdefghijklmnopqrstuvwxyz]') #used for password
capital = re.compile('[ABCDEFGHIJKLMNOPQRSTUVWXYZ]') #used for username

#where user info will be stored.
userList = []
passList = []

def register():
    print("""
    === Register === 
    """)

    print("Your username should be comprised of:")
    print("Numerical value(s) or alphabetical character(s).")
    print("Special characters will not be prohibited.")

    run = True
    #username
    while run == True:
        print()
        print("Input username")
        userLog = input("Username: ")

        if specialchar.search(userLog) != None:    
            print ("Special characters are not prohibited.")
            clear()
            continue
        else:
            print("Valid username ✔️ ")
            pass
        
        if userLog not in userList:
            userList.append(userLog) #saves user to list if not in list
            clear()
            del userLog #used for if more accounts want to be created, removes variable on userLog.
            break
        else:
            print("Username is not available.") #When user puts in a username and it is not available, 
                                                #it will display "Valid username" because, the username passes all criterias however due to it already existing in the database, 
                                                #user will have to use a different username
            continue
        run = False #stops loop
    
    
    
    #password
    while run == True:
        global score
        print()
        print("=== Password ===")
        print("Your password must contain:")
        print("Minimum of 8 characters.")
        print("Atleast 1 numerical value and 1 special character.")
        print("Atleast 1 capital and 1 lowercase alphabetical character.")
        print("Cannot be a common password.")
        print()
        

        print()

        score = 0
        global passLog
        print("Input password")
        passLog = input("Password: ")
        clear()

        #condition 1
        if passLog == ("123456" or "123456789" or "picture1" or "password" or "12345678" or "111111" or "123123" or "12345" or "1234567890"):
            print("Invalid Password: Password cannot be a common password.")
            
        else:
            score = score+1

        #condition 2
        if len(passLog) <8:
            print("Invalid password: Password is less than 8 characters long.")
            
        else:
            score = score+1
        
        #condition 3
        if specialchar.search(passLog) == None:
            print("Invalid Password: Password does not contain atleast 1 special character ")
            
        else:
            score = score+1

        #condition 4
        if lowercase.search(passLog) == None:
            print("Invalid Password: Password does not contain atleast 1 lowercase alphabetical character")
            
        else:
            score = score+1

        #condition 5
        if capital.search(passLog) == None:
            print("Invalid Password: Password does not contain atleast 1 capital alphabetical character")
            
        else:
            score = score+1

        if score == 5:
            print("Valid password ✔️ ")
            passList.append(passLog)
            del passLog #used for if more accounts want to be created, removes variable on passLog.
            run = False
            clear()

            login()
    run = False
    
def login():
    run = True
    while run == True:
        print("""
    === Login ===
        """)
        userLog = input("Enter username: ")
        if userLog in (userList):
            print("Account found... Welcome", userLog)
            global userCopy
            userCopy = copy.deepcopy(userLog) #used for dashboard welcome screen
            break
        else:
            print("Account not found in database... Please register an account.")
            clear()
            register()
        run = False
    invalidPass = 0
    while run == True:
        
         #used for security. attempt on bruteforce attack, at 5
        passLog = input("Enter password: ")
        if passLog in passList:
            clear()
            dashboard() #go to dashboard if user credentials match up
            break #break is only used when conditions are met
        else:
            ()
        
        if passLog not in passList:
            print("Invalid password",invalidPass)
            invalidPass = invalidPass+1
        else:
            ()
        if invalidPass == 5:
            print("Suspicious activity has been detected...")
            clear()
            print("Closing application...")
            exit()
        else:
            ()

def menu():
    while True:
        print("""
    === Menu ===
        """)
        print("To get started select an option. e.g. 'Signup'. ")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        selector = input("Input: ").lower()


        if selector == "register":
            print("Entering signup screen...")
            clear()
            register()


        elif selector =="login":
            print("Entering login screen...")
            clear()
            login()
            

        elif selector =="exit":
            print("Exiting...")
            clear()
            exit()

        else:
            clear()
            print("Invalid input, please select from the list.")
            clear()
            continue


def dashboard():
    while True:
        print("""
    === Dashboard ===
        """)
        print("Welcome,",userCopy)
        print("Select an option. e.g. 'Signup'. ")
        print("1. Roll-A-Dice")
        print("2. Pizza")
        print("3. Logout")
        Dashselector = input("input: ").lower()

        if Dashselector == ("roll-a-dice"):
            print("Entering Roll-A-Dice screen...")
            clear()
            rolladice()

        elif Dashselector =="pizza":
            print("Entering pizza screen...")
            clear()
            pizza()

        elif Dashselector =="logout":
            print("Logging out...")
            clear()
            menu()
            
        else:
            clear()
            print("Invalid input, please select from the list.")
            clear()
            continue

def pizza():
    print("""
                                         ._
                                   ,(  `-.
                                 ,': `.   `.
                               ,` *   `-.   \ 
                             ,'  ` :+  = `.  `.
                           ,~  (o):  .,   `.  `.
                         ,'  ; :   ,(__) x;`.  ;
                       ,'  :'  itz  ;  ; ; _,-'
                     .'O ; = _' C ; ;'_,_ ;
                   ,;  _;   ` : ;'_,-'   i'
                 ,` `;(_)  0 ; ','       :
               .';6     ; ' ,-'~
             ,' Q  ,& ;',-.'
           ,( :` ; _,-'~  ;
         ,~.`c _','
       .';^_,-' ~
     ,'_;-''
    ,,~
    i'
    :

    """)
    print("Type 'back' to go back to dashboard.")
    backInput =input("Input: ").lower()
    if backInput == "back":
        clear()
        dashboard()
    else:
        ()

def rolladice():
    repeat = True
    while repeat:
        print("You rolled",random.randint(1,6))
        clear090()
        print("Do you want to roll again? Type 'yes' or 'no'")
        repeat = ("y" or "yes") in input().lower()
    else:
        clear()
        dashboard()




def captcha():
    print("""

                        *****************
                   ******               ******
               ****                           ****
            ****                                 ***
          ***                                       ***
         **           ***               ***           **
       **           *******           *******          ***
      **            *******           *******            **
     **             *******           *******             **
     **               ***               ***               **
    **                                                     **
    **       *                                     *       **
    **      **                                     **      **
     **   ****                                     ****   **
     **      **                                   **      **
      **       ***                             ***       **
       ***       ****                       ****       ***
         **         ******             ******         **
          ***            ***************            ***
            ****                                 ****
               ****                           ****
                   ******               ******
                        *****************

    
    """)

    print("What facial expression is this?")
    print("Happiness")
    print("Sadness")
    print("Anger")
    print("Confusion")
    print("Disgust")

    facex = input("Input: ").lower()
    if facex == "happiness":
        clear()
    else:
        print("You are a bot")
        sleep05()
        exit()
        
