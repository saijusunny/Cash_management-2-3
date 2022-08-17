
from calendar import c
from cgitb import enable, reset, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from textwrap import wrap
from tkinter import font
from tkinter.font import BOLD
from urllib.parse import parse_qs
from PIL import ImageTk, Image, ImageFile
from matplotlib.font_manager import json_dump
from numpy import choose, empty, place
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from pip import main
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import shutil
import csv
import json
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import Tk, Canvas

import customtkinter
import PIL.Image
from PIL import ImageGrab
from PIL import ImageTk, Image, ImageFile
import PIL.Image



# fbilldb = mysql.connector.connect(
#     host="localhost", user="root", password="", database="fbilling", port="3306"
# )
# fbcursor = fbilldb.cursor()

root=Tk()
root.geometry("1300x730")

root.title("Fin sYs")

p1 = PhotoImage(file = 'images/favicon.png')
root.iconphoto(False, p1)

#--------------------------------------------------------------------------------------------Images

imgr1 =PIL.Image.open("images\logs.png")
exprefreshIcon=ImageTk.PhotoImage(imgr1)

mnu =PIL.Image.open("images\menu bar.PNG")
mnus=ImageTk.PhotoImage(mnu)


srh =PIL.Image.open("images\search.PNG")
srh_img=ImageTk.PhotoImage(srh)

logo =PIL.Image.open("images\logo-icon.png")
resized_image= logo.resize((50,50), Image.ANTIALIAS)
mai_logo= ImageTk.PhotoImage(resized_image)

#--------------------------------------------------------------------------------------------Create Sign In customer

def main_sign_in():
    try:
        main_frame_signup.destroy()
    except:
        pass
    try:
        main_frame_signin.destroy()
    except:
        pass
    Sys_top_frame=Frame(root, height=70,bg="#213b52")
    Sys_top_frame.pack(fill=X,)

    #---------------------------------------------------------------------------------------Top Menu
    tp_lb_nm=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=400)#-----------------------------Logo Name Frame
    tp_lb_nm.grid(row=1,column=1)

    label = Label(tp_lb_nm, image = mai_logo,height=70,bg="#213b52",border=0)
    label.grid(row=2,column=1)
    label = Label(tp_lb_nm, text="Fin sYs",bg="#213b52", fg="white",font=('Calibri 30 bold'),border=0)
    label.grid(row=2,column=2)
    def hid_nav():
        tabControl.hide(1)
    mnu_btn = Button(tp_lb_nm, image=mnus, bg="white", fg="black",command=hid_nav,border=0)
    mnu_btn.grid(row=2,column=4,padx=50)

    tp_lb_srh=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=700)#-------------------------Serch area Frame
    tp_lb_srh.grid(row=1,column=2)

    srh_top = Entry(tp_lb_srh, width=50, font=('Calibri 16'))
    srh_top.insert(0,"Password")
    # srh_top.bind("<Button-1>",sig_pass)
    srh_top.grid(row=2,column=1)

    srh_btn = Button(tp_lb_srh, image=srh_img, bg="white", fg="black",border=0)
    srh_btn.grid(row=2,column=4)

    tp_lb_nm=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=100)#----------------Notification
    tp_lb_nm.grid(row=1,column=3)
    tp_lb_nm=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=200)#----------------profile area name
    tp_lb_nm.grid(row=1,column=4)

    Sys_top_frame2=Frame(root, height=70,bg="#213b52")
    Sys_top_frame2.pack(fill=X,)
    
    global cnv
    cnv = Canvas(Sys_top_frame2, borderwidth=1,width=1355,height=645, bg="#2f516f")
    frame = Frame(cnv)
 
    hscrollbar = Scrollbar(Sys_top_frame2, orient="horizontal", command=cnv.xview)
    hscrollbar.grid(row=1, column=0, sticky="nsew")

    cnv.configure(xscrollcommand=hscrollbar.set)
    cnv.grid(row=0, column=0, sticky="nsew")
    
    cnv.create_window((5,4), window=frame, anchor="nw", tags="frame")

    tabsystem = ttk.Notebook(frame, width=100, height=100)
    s = ttk.Style()
    s.theme_use('default')
    s.configure('TNotebook.Tab', background="#213b52",foreground="white", width=20,justify=CENTER, padding=5)
    s.map('TNotebook.Tab',background=[("selected","#2f516f")])
            
    global tabControl
    tabControl = ttk.Notebook(tabsystem)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3=  ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6=  ttk.Frame(tabControl)
    tab7 = ttk.Frame(tabControl)
    tab8 = ttk.Frame(tabControl)
    tab9 =  ttk.Frame(tabControl)
    tab10=  ttk.Frame(tabControl)
    tab11 = ttk.Frame(tabControl)
    tab12=  ttk.Frame(tabControl)
    tab13 = ttk.Frame(tabControl)
    tab14 = ttk.Frame(tabControl)
    tab15 =  ttk.Frame(tabControl)
    
    tabControl.add(tab1,compound = LEFT, text ='Dashboard',)
    tabControl.add(tab2,compound = LEFT, text ='Bancking')
    tabControl.add(tab3,compound = LEFT, text ='Sales')
    tabControl.add(tab4,compound = LEFT, text ='Expenses')
    tabControl.add(tab5,compound = LEFT, text ='Payroll') 
    tabControl.add(tab6,compound = LEFT, text ='Report')
    tabControl.add(tab7,compound = LEFT, text ='Taxes')
    tabControl.add(tab8,compound = LEFT, text ='Accounting')
    tabControl.add(tab9,compound = LEFT, text ='My Account')
    tabControl.add(tab10,compound = LEFT, text ='Cash Management')
    tabControl.add(tab11,compound = LEFT, text ='Production')
    tabControl.add(tab12,compound = LEFT, text ='Quality Management')
    tabControl.add(tab13,compound = LEFT, text ='Project Management')
    tabControl.add(tab14,compound = LEFT, text ='Usage Decisions')
    tabControl.add(tab15,compound = LEFT, text ='Account & Payable')
    tabControl.pack(expand = 1, fill ="both")


    tabsystem.grid(row=0, column=0, sticky="ew")

    def frame_configure(event):
        global cnv
        cnv.configure(scrollregion=cnv.bbox("all"))

    frame.bind("<Configure>", frame_configure)

    

    Sys_mains_frame=Frame(tab1, height=750,bg="#2f516f")
    Sys_mains_frame.pack(fill=X)

    

#----------------------------------------------------------------------------------Sign in frame in signup section
def fun_sign_in():
    
    main_frame_signup.destroy()
    global main_frame_signin
    main_frame_signin=Frame(root, height=750)
    main_frame_signin.pack(fill=X,)

    sign_in=Label(main_frame_signin, text="Sign In",font=('Calibri 30 bold'), fg="black")
    sign_in.place(x=900, y=220)


    def sig_nm(event):
        if nm_ent.get()=="Username":
            nm_ent.delete(0,END)
        else:
            pass

    def sig_pass(event):
            if pass_ent.get()=="Password":
                pass_ent.delete(0,END)
            else:
                pass
    nm_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
    nm_ent.insert(0,"Username")
    nm_ent.bind("<Button-1>",sig_nm)
    nm_ent.place(x=820,y=300)

    pass_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
    pass_ent.insert(0,"Password")
    pass_ent.bind("<Button-1>",sig_pass)
    pass_ent.place(x=820,y=350)

    but_sign2 = customtkinter.CTkButton(master=main_frame_signin,command=lambda:main_sign_in(),text="Log In",bg="#213b52")
    but_sign2.place(relx=0.69, rely=0.58)

    #----------------------------------------------------------------------------------------left canvas
    lf_signup= Canvas(main_frame_signin,width=1500, height=1500)
    lf_signup.place(x=-700,y=0)

    lf_signup.create_oval(1400,1400,-800,-1700,fill="#213b52")

    label = Label(main_frame_signin, image = exprefreshIcon,bg="#213b52", width=500, justify=RIGHT)
    label.place(x=0,y=150)

    lft_lab=Label(main_frame_signin, text="New here ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=250, y=40)
    lft_lab=Label(main_frame_signin, text="Join here to start a business with FinsYs!",font=('Calibri 16 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=150, y=80)

    btn2 = Button(main_frame_signin, text = 'Sign Up', command=lambda:func_sign_up(), bg="white", fg="black",borderwidth = 3,height=1,width=10)
    btn2.place(x=275,y=130)


#-----------------------------------------------------------------------------------Sign Up Section
def func_sign_up():
    global main_frame_signup
    main_frame_signin.destroy()

    main_frame_signup=Frame(root, height=750)
    main_frame_signup.pack(fill=X,)

    lf_signup= Canvas(main_frame_signup,width=1500, height=1500)
    lf_signup.place(x=500,y=0)

    lf_signup.create_oval(1400,1400,150,-1700,fill="#213b52")

    #--------------------------------------------------------------------------------sign up section
    sign_in=Label(main_frame_signup, text="Sign Up",font=('Calibri 30 bold'), fg="black")
    sign_in.place(x=260, y=100)

    def nme(event):
        if fst_nm.get()=="Firstname":
            fst_nm.delete(0,END)
        else:
            pass

    def nme1(event):
        if lst_nm.get()=="Lastname":
            lst_nm.delete(0,END)
        else:
            pass
        
    def nme2(event):
        if sys_em.get()=="Email":
            sys_em.delete(0,END)
        else:
            pass
        
        
    def nme3(event):
        if sys_usr.get()=="Username":
            sys_usr.delete(0,END)
        else:
            pass
        
    def nme4(event):
        if sys_pass.get()=="Password":
            sys_pass.delete(0,END)
        else:
            pass
    
    def nme5(event):
        if sys_cf.get()=="Confirm Password":
            sys_cf.delete(0,END)
        else:
            pass
    
    

    fst_nm = Entry(main_frame_signup, width=25,text="Firstname", font=('Calibri 16'))
    fst_nm.insert(0,"Firstname")
    fst_nm.bind("<Button-1>",nme)
    fst_nm.place(x=200,y=200)

    lst_nm = Entry(main_frame_signup,  width=25, font=('Calibri 16'))
    lst_nm.insert(0,"Lastname")
    lst_nm.bind("<Button-1>",nme1)
    lst_nm.place(x=200,y=250)

    sys_em = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_em.insert(0,"Email")
    sys_em.bind("<Button-1>",nme2)
    sys_em.place(x=200,y=300)

    sys_usr = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_usr.insert(0,"Username")
    sys_usr.bind("<Button-1>",nme3)
    sys_usr.place(x=200,y=350)

    sys_pass = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_pass.insert(0,"Password")
    sys_pass.bind("<Button-1>",nme4)
    sys_pass.place(x=200,y=400)

    sys_cf = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_cf.insert(0,"Confirm Password")
    sys_cf.bind("<Button-1>",nme5)
    sys_cf.place(x=200,y=450)

    # sig_up =PIL.Image.open("images/register.png")
    # sign_up=ImageTk.PhotoImage(sig_up)

    # label = Label(main_frame_signup, image = sign_up,bg="#213b52", width=500, justify=RIGHT)
    # label.place(x=200,y=150)
    
    button_sign = customtkinter.CTkButton(master=main_frame_signup,text="Sign Up",bg="#213b52")
    button_sign.place(relx=0.2, rely=0.7) 

    lft_lab=Label(main_frame_signup, text="One of us ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=900, y=40)
    lft_lab=Label(main_frame_signup, text="click here for work with FinsYs.",font=('Calibri 16 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=820, y=80)

    btn_signup = Button(main_frame_signup, text='Sign In', command=fun_sign_in, bg="white", fg="black",borderwidth = 3,height=1,width=10)
    btn_signup.place(x=920,y=130)


main_frame_signin=Frame(root, height=750)
main_frame_signin.pack(fill=X,)

sign_in=Label(main_frame_signin, text="Sign In",font=('Calibri 30 bold'), fg="black")
sign_in.place(x=900, y=220)

def sig_nm(event):
        if nm_ent.get()=="Username":
            nm_ent.delete(0,END)
        else:
            pass

def sig_pass(event):
        if pass_ent.get()=="Password":
            pass_ent.delete(0,END)
        else:
            pass
nm_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
nm_ent.insert(0,"Username")
nm_ent.bind("<Button-1>",sig_nm)
nm_ent.place(x=820,y=300)

pass_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
pass_ent.insert(0,"Password")
pass_ent.bind("<Button-1>",sig_pass)
pass_ent.place(x=820,y=350)

button = customtkinter.CTkButton(master=main_frame_signin,command=main_sign_in,text="Log In",bg="#213b52")
button.place(relx=0.69, rely=0.58)

#----------------------------------------------------------------------------------------left canvas
lf_signup= Canvas(main_frame_signin,width=1500, height=1500)
lf_signup.place(x=-700,y=0)

lf_signup.create_oval(1400,1400,-800,-1700,fill="#213b52")

label = Label(main_frame_signin, image = exprefreshIcon,bg="#213b52", width=500, justify=RIGHT)
label.place(x=0,y=150)

lft_lab=Label(main_frame_signin, text="New here ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
lft_lab.place(x=250, y=40)
lft_lab=Label(main_frame_signin, text="Join here to start a business with FinsYs!",font=('Calibri 16 bold'), fg="white", bg="#213b52")
lft_lab.place(x=150, y=80)

btn2 = Button(main_frame_signin, text = 'Sign Up', command = func_sign_up, bg="white", fg="black",borderwidth = 3,height=1,width=10)
btn2.place(x=275,y=130)

root.mainloop()


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #--------------------------------------------------------------------------------------------------------------Content head
    # cmpny_name_frm=Frame(frame,bg="#213b52",width=1300,height=60)
    # cmpny_name_frm.pack(pady=20)

    # cmp_name=Label(frame, text="Clown",bg="#213b52", fg="White",width=69, anchor="center",font=('Calibri 24 bold'))
    # cmp_name.place(x=60,y=27)
    # #-------------------------------------------------------------------------------------------------------Content bottam
    # das_btm_frm=Frame(frame,bg="#2f516f")
    # das_btm_frm.pack(pady=10)
    # #----------------------------------------------------------------------------------------------------Profit And Loss
    # das_btm1=Frame(das_btm_frm,bg="#213b52",height=500,width=420)
    # das_btm1.grid(row=1,column=1,padx=10,pady=10)

    # cmp_name=Label(das_btm1, text="PROFIT AND LOSS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    # cmp_name.grid(row=1,column=1)
    # # cmp_name=Label(das_btm1, text="__________________________________________________",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    # # cmp_name.place(x=10,y=30)

    # figlast = plt.figure(figsize=(8, 4), dpi=50)

    # x="Income"
    # y=10 
    # plt.barh(x,y, label="Undefined", color="blue") 
    # plt.legend()
  
    # plt.ylabel("")
    # axes=plt.gca()
    # axes.xaxis.grid()

    # x="Expense"
    # y=100
    # plt.barh(x,y, color="red") 
    # plt.legend()
 
    # plt.ylabel("")
    # axes=plt.gca()
    # axes.xaxis.grid()
              

    # canvasbar = FigureCanvasTkAgg(figlast, master=das_btm1)
    # canvasbar
    # canvasbar.draw()
    # canvasbar.get_tk_widget().grid(row=2,column=1,padx=5,pady=135)
  

    # #--------------------------------------------------------------------------------------------------------card2

    # das_btm2=Frame(das_btm_frm,bg="#213b52",height=500,width=420)
    # das_btm2.grid(row=1,column=2,padx=10,pady=10)

    # cmp_name=Label(das_btm2, text="Expenses:2000",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    # cmp_name.grid(row=1,column=1)

    # stockListExp = ['AMZN' , 'AAPL', 'JETS', 'CCL', 'NCLH']
    # stockSplitExp = [15,25,40,10,10]

    # fig = Figure(figsize=(4.3, 4.65)) # create a figure object
    # ax = fig.add_subplot(111) # add an Axes to the figure

    # ax.pie(stockSplitExp, radius=1, labels=stockListExp,autopct='%0.2f%%', shadow=True,)

    # chart1 = FigureCanvasTkAgg(fig,das_btm2)
    # chart1.get_tk_widget().grid(row=2,column=1)
  
    # #----------------------------------------------------------------------------------------------------Card 3
    # das_btm3=Frame(das_btm_frm,bg="#213b52",height=500,width=420)
    # das_btm3.grid(row=1,column=3,padx=10,pady=10)
    # # cmp_name=Label(das_btm3, text="Banknbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb Accounts",bg="#213b52", fg="White",font=('Calibri 16 bold'))
    # # cmp_name.grid(row=1,column=1)

    # das_btm4=Frame(das_btm_frm,bg="#213b52",height=500,width=420)
    # das_btm4.grid(row=2,column=1,padx=10,pady=10)

    # #--------------------------------------------------------------------------------------------------card5
    # das_btm5=Frame(das_btm_frm,bg="#213b52",height=500,width=420)
    # das_btm5.grid(row=2,column=2,padx=10,pady=10)

    # cmp_name=Label(das_btm5, text="PROFIT AND LOSS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    # cmp_name.grid(row=1,column=1)
    # # cmp_name=Label(das_btm5, text="__________________________________________________",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    # # cmp_name.place(x=10,y=30)

    # figlast = plt.figure(figsize=(8, 4), dpi=50)

    # x="Unpaid"
    # y=10 
    # plt.barh(x,y, label="Undefined", color="blue") 
    # plt.legend()
  
    # plt.ylabel("")
    # axes=plt.gca()
    # axes.xaxis.grid()

    # x="Paid"
    # y=100
    # plt.barh(x,y, color="red") 
    # plt.legend()
 
    # plt.ylabel("")
    # axes=plt.gca()
    # axes.xaxis.grid()
              

    # canvasbar = FigureCanvasTkAgg(figlast, master=das_btm5)
    # canvasbar
    # canvasbar.draw()
    # canvasbar.get_tk_widget().grid(row=2,column=1,padx=5,pady=135)

    # #------------------------------------------------------------------------------------------------------------------Card6

    # das_btm6=Frame(das_btm_frm,bg="#213b52",height=500,width=420)
    # das_btm6.grid(row=2,column=3,padx=10,pady=10)

    # cmp_name=Label(das_btm6, text="PROFIT AND LOSS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    # cmp_name.grid(row=1,column=1)
    # # cmp_name=Label(das_btm6, text="__________________________________________________",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    # # cmp_name.place(x=10,y=30)

    # figlast = plt.figure(figsize=(8, 4), dpi=50)

    # x="Income"
    # y=10 
    # plt.barh(x,y, label="Undefined", color="blue") 
    # plt.legend()
  
    # plt.ylabel("")
    # axes=plt.gca()
    # axes.xaxis.grid()

    # canvasbar = FigureCanvasTkAgg(figlast, master=das_btm6)
    # canvasbar
    # canvasbar.draw()
    # canvasbar.get_tk_widget().grid(row=2,column=1,padx=5,pady=135)
    
