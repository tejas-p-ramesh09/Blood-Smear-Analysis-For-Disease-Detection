import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import argparse
import os
import pymysql
import matplotlib.pyplot as plt
import cv2
import numpy as np
import sys
import glob
import math
import time
import os
import itertools
#import requests
from PIL import Image
from numpy import average, linalg, dot

import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2
#from skimage.feature import greycomatrix, greycoprops
from sklearn.metrics.cluster import entropy
from PIL import Image, ImageStat
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from scipy.stats import kurtosis, skew

import math
import argparse


import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import math

import glob
from keras.models import Sequential, load_model

#import preprocess as pre
# import train as tr
import detect as pred
#import Predict as pred1
import pdfdemo as pdfgen
import chatgpt1 as search
import conditionaltest as dd

bgcolor="#87CEEB"
bgcolor1="#87CEEB"
fgcolor="black"

text_field_color = "#ffb3b3"
#---------------------------------------------------------------Login Function --------------------------------------
def clear():
        userentry.delete(0,END)
        passentry.delete(0,END)


def close():
        win.destroy()   


def login():
        if user_name.get()=="" or password.get()=="":
                messagebox.showerror("Error","Enter User Name And Password",parent=win) 
        else:
                try:
                        con = pymysql.connect(host="localhost",user="root",password="",database="blood") 
                        cur = con.cursor()

                        cur.execute("select * from user_information where username=%s and password = %s",(user_name.get(),password.get()))
                        row = cur.fetchone()

                        if row==None:
                                tm.showerror("Error" , "Invalid User Name And Password", parent = win)

                        else:
                                tm.showinfo("Success" , "Successfully Login" , parent = win)
                                close()
                                Home()
                        con.close()
                except Exception as es:
                        tm.showerror("Error" , f"Error Dui to : {str(es)}", parent = win)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def validate_characters(input_text):
        return input_text.isalpha() or input_text == ""

def Home():
        global window
        def clear():
                print("Clear1")
                txt.delete(0, 'end')
                txt1.delete(0, 'end')
                txt2.delete(0, 'end')
                txt3.delete(0, 'end')
                txt4.delete(0, 'end')
                txt5.delete(0, 'end')   
        def sel():
                selection = str(var.get())
                labelsel.config(text = selection) 
                print("selection==",selection)
        
        
                



        window = tk.Tk()
        var = IntVar()
        window.title("Blood Smear Analysis")

 
        window.geometry('1280x720')
        window.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)
        bg = PhotoImage(file = "new1.png")
        # Show image using label 
        label1 = Label( window, image = bg) 
        label1.place(x = 0, y = 0) 

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        validate_command = window.register(validate_characters)
        

        message1 = tk.Label(window, text="Blood Smear Analysis" ,bg=text_field_color  ,fg=fgcolor  ,width=40  ,height=2,font=('times', 24, 'italic bold underline')) 
        message1.place(x=650, y=50 ,anchor=CENTER)

        lbl = tk.Label(window, text="Enter Patient Name:",width=20  ,height=2  ,fg=fgcolor  ,bg=text_field_color ,font=('times', 15, ' bold ') ) 
        lbl.place(x=100, y=175)
        
        txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '),validate="key", validatecommand=(validate_command, "%P"))
        txt.place(x=400, y=185)

        R1 = Radiobutton(window, text="Male", variable=var, value=1,command=sel,fg=fgcolor  ,bg=text_field_color)
        R1.place(x=150, y=250)
        #R1.pack( anchor = W )
        R2 = Radiobutton(window, text="Female", variable=var, value=2,command=sel,fg=fgcolor  ,bg=text_field_color)
        R2.place(x=450, y=250)
       
        labelsel = tk.Label(window, text="",width=20  ,height=2  ,fg=fgcolor,font=('times', 15, ' bold ') ) 
        labelsel.place(x=650, y=250)

        lbl2 = tk.Label(window, text="Enter Age:",width=20  ,height=2  ,fg=fgcolor  ,bg=text_field_color ,font=('times', 15, ' bold ') ) 
        lbl2.place(x=100, y=325)
        
        txt2 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt2.place(x=400, y=340)

        lbl3 = tk.Label(window, text="Enter Doctor Name",width=20  ,height=2  ,fg=fgcolor  ,bg=text_field_color ,font=('times', 15, ' bold ') ) 
        lbl3.place(x=700, y=175)
        
        txt3 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '),validate="key",validatecommand=(validate_command, "%P"))
        txt3.place(x=1000, y=185)

        

        lbl4 = tk.Label(window, text="Select Blood Sample Folder",width=20  ,height=2  ,fg=fgcolor  ,bg=text_field_color ,font=('times', 15, ' bold ') ) 
        lbl4.place(x=700, y=250)
        
        txt4 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt4.place(x=1000, y=265)

        lbl5 = tk.Label(window, text="Enter text",width=20  ,height=2  ,fg=fgcolor  ,bg=text_field_color ,font=('times', 15, ' bold ') ) 
        lbl5.place(x=700, y=520)
        
        txt5 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        
        txt5.place(x=1000, y=535)
        
        

        def browse3():
                path=filedialog.askdirectory()
                print(path)
                txt4.delete(0, 'end')
                txt4.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select Input Image folder") 
        def searchCGPT():
                query=txt5.get()
                if query!="":
                        res=search.process(str(query))
                        tm.showinfo("Result", str(res))
                else:
                        tm.showinfo("Input error", "Enter Your Query")  


        
        
        def predictingresult():
                pname=txt.get()
                gen=labelsel.cget("text")
                print("gender==",gen)
                if int(gen)==1:
                        gen="Male"
                else:
                        gen="Female"
                age=txt2.get()
                dname=txt3.get()
                sym=txt4.get()
                if pname=="":
                        tm.showinfo("Input error", "Enter a patient Name")
                
                if gen=="":
                        tm.showinfo("Input error", "Enter Gender")
                if age=="":
                        tm.showinfo("Input error", "Enter Age")
                if is_number(age)==False:
                        tm.showinfo("Input error", "Enter Age in Number")
                if dname=="":
                        tm.showinfo("Input error", "Enter Doctor Name")
                
                if sym=="":
                        tm.showinfo("Input error", "Select the Blood smaples folder")

                if pname !="" and gen !="" and int(age)<100 !="" and dname !="" and sym !="":
                        dir_list = os.listdir(sym)
                        totalrbc=0
                        totalwbc=0
                        totalplatelets=0
                        for files in dir_list:
                                head, tail = os.path.split(sym+"/"+files)
                                print("head==",head)
                                print("tail==",tail)
                                rbc,wbc,platelets=pred.blood_cell_count(sym+"/"+files)
                                totalplatelets+=platelets
                                totalrbc+=rbc
                                totalwbc+=wbc
                        print("platelets==",totalplatelets)
                        print("totalrbc==",totalrbc)
                        print("totalwbc==",totalwbc)
                        totalplatelets1=int(totalplatelets)*15000
                        totalrbc1=int(totalrbc)*100000
                        totalwbc1=int(totalwbc)*1000
                        Detected_as=""
                        Treatment=""
                        #result=pred1.process("dataset.csv",int(totalplatelets1))
                        if totalplatelets1 > 0 or totalrbc1 >0 or totalwbc1 >0:
                                # Conditions to determine health status
                                Detected_as=dd.diagnose(gen, totalwbc1, totalplatelets1, totalrbc1,age)
                                print(f"Detected as: {Detected_as}")
                                if Detected_as=="Anemia":
                                        Treatment="Dietary Changes: Include iron-rich foods such as:\n Red meat, poultry, and fish, Leafy green vegetables (spinach, kale),\n Legumes and beans, Iron-fortified cereals "
                                if Detected_as=="Leukopenia":
                                        Treatment="Granulocyte Colony-Stimulating Factors (G-CSFs):\n Medications like filgrastim (Neupogen) or pegfilgrastim (Neulasta) \n stimulate WBC production in the bone marrow.Steroids or\n Immunosuppressive Agents: May be used for autoimmune \n conditions causing leukopenia."
                                if Detected_as=="Blood Cancer":
                                        Treatment="Primary Treatment: Uses drugs to kill cancer cells or stop their growth.\n Systemic Therapy: Delivered orally or \n intravenously to target cancer throughout the body.\n Combination Regimens: Often used with other therapies \n(e.g., radiation, targeted therapy)."
                                if Detected_as=="Normal":
                                        Treatment="Continue Your Regular Diet \n as usual"
                                image=cv2.imread('./output/' + tail)
                                cv2.imshow('Platelets: ' + str(totalplatelets) +' Total RBC: ' + str(totalrbc1) + ', WBC: ' + str(totalwbc1) + ', Total Platelets: ' + str(totalplatelets1)+',  Prediced as:  ' +str(Detected_as), image)
                                pdfgen.process(pname,age,gen,dname,totalrbc1,totalwbc1,totalplatelets1,Detected_as, Treatment)
                                tm.showinfo("Output", "Detected Disease is : "+str(Detected_as))
                                tm.showinfo("Recommended Treatment", "Treatment is : "+str(Treatment))
                        else:
                                 tm.showinfo("Error", "Invalid image selection ")


                
                        
                else:
                        
                        tm.showinfo("Input error", "Select Image Folder")



 

        #photo1 = PhotoImage(file ="logo.png") 
        Serachbtn = tk.Button(window, text="Search", command=searchCGPT  ,fg=fgcolor  ,bg=text_field_color  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        Serachbtn.place(x=1030, y=570)

        

        browse3btn = tk.Button(window, text="Upload", command=browse3  ,fg=fgcolor  ,bg=text_field_color  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse3btn.place(x=1030, y=300)

        clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=text_field_color  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
        clearButton.place(x=250, y=400)
         
        

        DCbutton = tk.Button(window, text="Prediction", command=predictingresult  ,fg=fgcolor   ,bg=text_field_color   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        DCbutton.place(x=850, y=400)



        quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=text_field_color  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitWindow.place(x=540, y=600)

        window.mainloop()
#--------------------------------------------------------------------------------------------------------------###########
def signup():
        # signup database connect 
        def action():
                if first_name.get()=="" or last_name.get()=="" or age.get()=="" or city.get()=="" or add.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="":
                        tm.showerror("Error" , "All Fields Are Required" , parent = winsignup)
                elif password.get() != very_pass.get():
                        tm.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
                else:
                        try:
                                con = pymysql.connect(
                                        host="localhost",
                                        user="root",
                                        password="",
                                        database="blood"
                                )
                                cur = con.cursor()
                                cur.execute("select * from user_information where username=%s",user_name.get())
                                row = cur.fetchone()
                                if row!=None:
                                        tm.showerror("Error" , "User Name Already Exits", parent = winsignup)
                                else:
                                        cur.execute("insert into user_information(first_name,last_name,age,gender,city,address,username,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                                (
                                                first_name.get(),
                                                last_name.get(),
                                                age.get(),
                                                var.get(),
                                                city.get(),
                                                add.get(),
                                                user_name.get(),
                                                password.get()
                                                ))
                                        con.commit()
                                        con.close()
                                        tm.showinfo("Success" , "Registration Successfull" , parent = winsignup)
                                        clear()
                                        switch()
                                
                        except Exception as es:
                                tm.showerror("Error" , f"Error Dui to : {str(es)}", parent = winsignup)

        # close signup function                 
        def switch():
                winsignup.destroy()
 # start Signup Window   

        winsignup =  tk.Toplevel()
        winsignup.title("Blood Smear Analysis App")
        winsignup.configure(background=bgcolor)
        winsignup.maxsize(width=900 ,  height=600)
        winsignup.minsize(width=900 ,  height=600)
        #bg = PhotoImage(file = "bg.png")
        # Show image using label
        label1 = Label(winsignup)
        label1.place(x = 0, y = 0)


        #heading label
        heading = tk.Label(winsignup , text = "Signup" ,bg=bgcolor  ,fg=fgcolor, font = 'Verdana 20 bold')
        heading.place(x=80 , y=60)

        # form data label
        first_name = tk.Label(winsignup, text= "First Name :" ,bg=bgcolor  ,fg=fgcolor, font='Verdana 10 bold')
        first_name.place(x=80,y=130)

        last_name = tk.Label(winsignup, text= "Last Name :" ,bg=bgcolor  ,fg=fgcolor, font='Verdana 10 bold')
        last_name.place(x=80,y=160)

        age = tk.Label(winsignup, text= "Age :" ,bg=bgcolor  ,fg=fgcolor, font='Verdana 10 bold')
        age.place(x=80,y=190)

        Gender = tk.Label(winsignup, text= "Gender :" ,bg=bgcolor  ,fg=fgcolor, font='Verdana 10 bold')
        Gender.place(x=80,y=220)

        city = tk.Label(winsignup, text= "City :" ,bg=bgcolor  ,fg=fgcolor, font='Verdana 10 bold')
        city.place(x=80,y=260)

        add = tk.Label(winsignup, text= "Address :" ,bg=bgcolor  ,fg=fgcolor, font='Verdana 10 bold')
        add.place(x=80,y=290)

        user_name = tk.Label(winsignup, text= "User Name :" ,bg=bgcolor  ,fg=fgcolor, font='Verdana 10 bold')
        user_name.place(x=80,y=320)

        password = tk.Label(winsignup, text= "Password :" ,bg=bgcolor  ,fg=fgcolor, font='Verdana 10 bold')
        password.place(x=80,y=350)

        very_pass = tk.Label(winsignup, text= "Verify Password:" ,bg=bgcolor  ,fg=fgcolor, font='Verdana 10 bold')
        very_pass.place(x=80,y=380)

        # Entry Box ------------------------------------------------------------------

        first_name = tk.StringVar()
        last_name = tk.StringVar()
        age = tk.IntVar(winsignup, value='0')
        var= tk.StringVar()
        city= tk.StringVar()
        add = tk.StringVar()
        user_name = tk.StringVar()
        password = tk.StringVar()
        very_pass = tk.StringVar()


        first_name = tk.Entry(winsignup, width=40 ,bg="white" ,fg="black", textvariable = first_name)
        first_name.place(x=200 , y=133)


        
        last_name = tk.Entry(winsignup, width=40 ,bg="white" ,fg="black", textvariable = last_name)
        last_name.place(x=200 , y=163)

        
        age = tk.Entry(winsignup, width=40,bg="white" ,fg="black", textvariable=age)
        age.place(x=200 , y=193)

        
        Radio_button_male = ttk.Radiobutton(winsignup,text='Male', value="Male", variable = var).place(x= 200 , y= 220)
        Radio_button_female = ttk.Radiobutton(winsignup,text='Female', value="Female",variable = var).place(x= 200 , y= 238)


        city = tk.Entry(winsignup, width=40,bg="white" ,fg="black",textvariable = city)
        city.place(x=200 , y=263)


        
        add = tk.Entry(winsignup, width=40 ,bg="white" ,fg="black", textvariable = add)
        add.place(x=200 , y=293)

        
        user_name = tk.Entry(winsignup, width=40,bg="white" ,fg="black",textvariable = user_name)
        user_name.place(x=200 , y=323)

        
        password = tk.Entry(winsignup, width=40,bg="white" ,fg="black", textvariable = password)
        password.place(x=200 , y=353)

        
        very_pass= tk.Entry(winsignup, width=40 ,show="*" ,bg="white" ,fg="black", textvariable = very_pass)
        very_pass.place(x=200 , y=383)


        # button login and clear

        btn_signup = tk.Button(winsignup, text = "Signup" ,bg=bgcolor1  ,fg=fgcolor,font='Verdana 10 bold', command = action)
        btn_signup.place(x=200, y=413)


        btn_login = tk.Button(winsignup, text = "Clear" ,bg=bgcolor1  ,fg=fgcolor,font='Verdana 10 bold' , command = clear)
        btn_login.place(x=280, y=413)


        sign_up_btn = tk.Button(winsignup , text="Switch To Login" ,bg=bgcolor1  ,fg=fgcolor, command = switch )
        sign_up_btn.place(x=350 , y =20)


        winsignup.mainloop()
#---------------------------------------------------------------------------End Singup Window-----------------------------------        


#------------------------------------------------------------ Login Window -----------------------------------------

win = tk.Tk()

# app title
win.title("Blood Smear Analysis")
win.configure(background=bgcolor)


# window size
win.maxsize(width=900 ,  height=500)
win.minsize(width=900 ,  height=500)
#bg = PhotoImage(file = "bg.png")
  
# Show image using label
label1 = Label(win)
label1.place(x = 0, y = 0)


#heading label
heading = tk.Label(win , text = "Login" ,bg=bgcolor  ,fg=fgcolor, font = 'Verdana 25 bold')
heading.place(x=80 , y=150)

username = tk.Label(win, text= "User Name :" ,bg=bgcolor  ,fg=fgcolor, font='Verdana 10 bold')
username.place(x=80,y=220)

userpass = tk.Label(win, text= "Password :" ,bg=bgcolor  ,fg=fgcolor, font='Verdana 10 bold')
userpass.place(x=80,y=260)

# Entry Box
user_name = tk.StringVar()
password = tk.StringVar()
        
userentry = tk.Entry(win, width=40 ,bg="white" ,fg="black", textvariable = user_name)
userentry.focus()
userentry.place(x=200 , y=223)

passentry = tk.Entry(win, width=40, show="*" ,bg="white" ,fg="black",textvariable = password)
passentry.place(x=200 , y=260)


# button login and clear

btn_login = tk.Button(win, text = "Login" ,bg=bgcolor1  ,fg=fgcolor,font='Verdana 10 bold',command = login)
btn_login.place(x=200, y=293)


btn_login = tk.Button(win, text = "Clear" ,bg=bgcolor1  ,fg=fgcolor,font='Verdana 10 bold', command = clear)
btn_login.place(x=260, y=293)

# signup button

sign_up_btn = tk.Button(win , text="Switch To Sign up" ,bg=bgcolor1  ,fg=fgcolor, command = signup )
sign_up_btn.place(x=350 , y =293)
# passentry1 = tk.Text(win, width=40,bg="white" ,fg="black")
# msg="Software Developed by:- \n Tejas \n Venkat N \n Kavya \n Nireeksha \n Guided by:- Prof. Manasa C"
# passentry1.insert("end",msg)
# passentry1.place(x=200 , y=320)



win.mainloop()

