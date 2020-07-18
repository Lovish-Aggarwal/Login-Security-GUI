#import modules

from tkinter import *
import os

# Designing window for registration

#Screen Stores Regristration Details Of the user ans pass then to other funtion to check weather the entries are valid.

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("400x400")

    #As these values are neded in other funtions thus they are maded Global

    global username
    global password
    global username_entry
    global password_entry
    global email
    global email_entry
    username = StringVar()    
    password = StringVar()
    email = StringVar()

    global Security_entry
    global forget_answer
    forget_answer=StringVar()

    #GUI Part

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)    
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    email_lable = Label(register_screen, text="Email ID * ")
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()

    #This below section is specially for the Security Question input

    forget_lable=Label(register_screen, text="Security Question",bg="yellow")
    forget_lable.pack(pady=5)
    security_Question=Label(register_screen, text="Your Nickname at School ...*")
    security_Question.pack(pady=2)
    Security_entry = Entry(register_screen, textvariable=forget_answer)
    Security_entry.pack()

    #Passing the values to check the validation of entries

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()


# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
    
    global username_verify
    global password_verify
    

# A StringVar() is used to edit a widget's text
# set() and get() methods are used to set and retrieve the values of these variables.
    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    #GUI Part

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    #Button(login_screen, text="Forget Password", width=10, height=1, command = login_verify).pack()
    submit=Button(login_screen,text="Forget Password",font="comicsansnas 8 bold",command=forget_Section)
    submit.pack(padx="2",side=BOTTOM,pady=10)


#Implementing event on forgot button

#Takes Username And Anwer to the Secqurity Question ANd pass to Checker Funtion
def forget_Section():
    global Sec_Answer
    Sec_Answer=StringVar()
    global username_forget
    username_forget=StringVar()
    global forget_screen
    global Answer_Entry
    global username_forget_entry

    #GUI Part

    forget_screen = Toplevel(main_screen)
    forget_screen.title("Register Through Security Question")
    forget_screen.geometry("300x300")
    Label(forget_screen, text="Username * ").pack()
    username_forget_entry = Entry(forget_screen, textvariable=username_forget)
    username_forget_entry.pack(pady=5)
    Label(forget_screen,text="Answer the Following Security Question \n to Login",fg="red").pack()
    Label(forget_screen,text="").pack()
    Label(forget_screen,text="Youe Nickname at School...*").pack()
    Answer_Entry=Entry(forget_screen,textvariable=Sec_Answer)
    Answer_Entry.pack()

    #Passing the values for checking

    Try=Button(forget_screen,text="Login",font="comicsansnas 8 bold",command=Security_check)
    Try.pack(padx="2",side=BOTTOM,pady=10)


# Implementing Login Button 

def Security_check():
    username_forget_login=username_forget.get()
    Passcode=Sec_Answer.get()
    Answer_Entry.delete(0,END)
    username_forget_entry.delete(0,END)
    list_of_files = os.listdir()
    #Check if User name Exists
    if username_forget_login in list_of_files:
        
        file1 = open(username_forget_login, "r")
        verify = file1.read().splitlines()
        #Checks whether the Security Input is Correct
        if Passcode in verify:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()

# Implementing event on register button

def register_user():

    username_info = username.get()
    password_info = password.get()
    email_info = email.get()
    
    security_info=forget_answer.get()

    list_of_files = os.listdir()
    if username_info in list_of_files:
         Label(register_screen, text="Registration Failed : Username Exists Already",fg="red", font=("calibri", 11)).pack()
    #Above Funtion is to check for similar Usernames

    elif email_info in list_of_files:
         Label(register_screen, text="Registration Failed : Email Already Exist",fg="red", font=("calibri", 11)).pack()
    #Above Funtion is to Check for Similar Emails

    elif password_validator(password_info)==False:
        Label(register_screen, text="Registration Failed : Must use 1 capital Character",fg="red", font=("calibri", 11)).pack()
    #Above funtion is to Check whether the password is valid

    else:
        #if the above conditions are satisfied Means Registration is valid.
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(security_info)
        file.write(password_info)
        file.write('Email ID' +email_info +'\n')
        
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)
        email_entry.delete(0,END)
        Security_entry.delete(0,END)

        Label(register_screen, text="Registration Success",fg="green", font=("calibri", 11)).pack()

#Password Validator Funtion to check wether their is one CAPITAL LETTER in the Password

def password_validator(p):
    p=str(p)
    #print(p)
    uc=False
    for i in p:
        if(not uc):
                if(ord(i)>=65 and ord(i)<=90):
                    uc=True
                    break
    #print(uc)
    return(uc)

# Implementing event on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    #This is only GUI part
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    #This is only GUI part
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    #This is only GUI part
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    main_screen.destroy()

def delete_register_success():
    register_success_screen.destroy()
    register_screen.destroy() 


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()
