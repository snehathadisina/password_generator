from tkinter import *
import string
import random              



def password_generator():
    small_letters=string.ascii_lowercase
    capital_letters=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

  
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_letters+numbers,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_letters+capital_letters+numbers,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(small_letters+capital_letters+numbers+special_charecters,password_length))




root=Tk()
#root.config(bg='gray20')
choice=IntVar()
Font=('arial',13,'bold')


title=Label(root,text='PASSWORD GENERATOR',font=('calibri',20,'bold'))
title.pack()
root.title("PASSWORD GENERATOR")
root.geometry("9000x6500")

Label1=Label(root,text='weak password consist of small letters and numbers',font=Font)
Label1.pack()

radioButton1=Radiobutton(root,text='Weak_Password',value=1,variable=choice,font=Font)
radioButton1.pack()

Label2=Label(root,text='medium password consist of small letters,capital letters,numbers',font=Font)
Label2.pack()

radioButton2=Radiobutton(root,text='Medium_Password',value=2,variable=choice,font=Font)
radioButton2.pack()

Label3=Label(root,text='strong password consist of small letters,capital letters,numbers and special charecters',font=Font)
Label3.pack()

radioButton3=Radiobutton(root,text='Strong_Password',value=3,variable=choice,font=Font)
radioButton3.pack()

lengthLabel=Label(root,text='Enter Password Length',font=Font)
lengthLabel.pack()

length_Box=Spinbox(root,from_=5,to_=12,width=5,font=Font)
length_Box.pack()

generateButton=Button(root,text='Generate',font=Font,command=password_generator)
generateButton.pack()

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.pack()

root.mainloop()










