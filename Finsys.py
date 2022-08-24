import matplotlib.pyplot as plt
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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import re
from datetime import date,datetime, timedelta

from array import *
from forex_python.converter import CurrencyRates

from dateutil.relativedelta import relativedelta

finsysdb = mysql.connector.connect(
    host="localhost", user="root", password="", database="newfinsys", port="3306"
)
fbcursor = finsysdb.cursor(buffered=True)

root=Tk()
root.geometry("1366x768+0+0")

root.title("Fin sYs")

p1 = PhotoImage(file = 'images/favicon.png')
root.iconphoto(False, p1)

#-------------------------------------------------------------------------------------------------------------------------Images


pro_pic =PIL.Image.open("profilepic\propic.jpg")

prof_pics=ImageTk.PhotoImage(pro_pic)



imgr1 =PIL.Image.open("images\logs.png")
exprefreshIcon=ImageTk.PhotoImage(imgr1)

notic =PIL.Image.open("images/bell.png")
noti=ImageTk.PhotoImage(notic)

mnu =PIL.Image.open("images\menu bar.PNG")
mnus=ImageTk.PhotoImage(mnu)


srh =PIL.Image.open("images\search.PNG")
srh_img=ImageTk.PhotoImage(srh)

stn =PIL.Image.open("images/brightness-solid-24.png")
stn_img=ImageTk.PhotoImage(stn)


cash_fl =PIL.Image.open("images/bank-building-on-the-background-of-the-city-white-car-near-the-bank-free-vector.jpg")
resized_flow= cash_fl.resize((620,400))
cash_flow=ImageTk.PhotoImage(resized_flow)

logo =PIL.Image.open("images\logo-icon.png")
resized_image= logo.resize((50,50))
mai_logo= ImageTk.PhotoImage(resized_image)

sig_up =PIL.Image.open("images/register.png")
resized_sign_up= sig_up.resize((500,400))
sign_up=ImageTk.PhotoImage(resized_sign_up)


#------------------------------------------------------------------------------------------------------------Login Button Function

def main_sign_in():
    
        usr_nm=nm_ent.get()
        usr_pass=pass_ent.get()
        sql_log_sql='select * from auth_user where username=%s'
        vals=(nm_ent.get(),)
        fbcursor.execute(sql_log_sql,vals)
        check_logins=fbcursor.fetchone()
        
        if usr_nm=="" or usr_pass=="" or usr_nm=="Username" or usr_pass=="********":
            messagebox.showerror("Login Failed","Enter username and password")
        else:

            sql_log_sql='select * from auth_user where username=%s'
            vals=(nm_ent.get(),)
            fbcursor.execute(sql_log_sql,vals)
            check_login=fbcursor.fetchone()
            
            if check_login is None:
                messagebox.showerror("Login Failed","Create an account")
            else:
                if check_login[4]==usr_nm and check_login[1]==usr_pass:
                    
                    

                    pro_pic =PIL.Image.open("profilepic\propic"+str(check_logins[0])+".png")
                        # resized_pro_pic= pro_pic.resize((170,170))
                    prof_pics=ImageTk.PhotoImage(pro_pic)

                    dash_pro_pic =PIL.Image.open("profilepic\propic"+str(check_logins[0])+".png")
                    dash_resized_pro_pic= dash_pro_pic.resize((50,50))
                    dash_prof_pics=ImageTk.PhotoImage(dash_resized_pro_pic)
                    
                    try:
                        main_frame_signup.pack_forget()
                    except:
                        pass
                    try:
                        main_frame_signin.pack_forget()
                    except:
                        pass
                    Sys_top_frame=Frame(root, height=70,bg="#213b52")
                    Sys_top_frame.pack(fill=X,)

                    #---------------------------------------------------------------------------------------Top Menu
                    tp_lb_nm=LabelFrame(Sys_top_frame,bg="#213b52")#-----------------------------Logo Name Frame
                    tp_lb_nm.grid(row=1,column=1,sticky='nsew')
                    tp_lb_nm.grid_rowconfigure(0,weight=1)
                    tp_lb_nm.grid_columnconfigure(0,weight=1)

                    label = Label(tp_lb_nm, image = mai_logo,height=70,bg="#213b52",border=0)
                    label.grid(row=2,column=1,sticky='nsew')
                    label = Label(tp_lb_nm, text="Fin sYs",bg="#213b52", fg="white",font=('Calibri 30 bold'),border=0)
                    label.grid(row=2,column=2,sticky='nsew')
                
                    mnu_btn = Button(tp_lb_nm, image=mnus, bg="white", fg="black",border=0)
                    mnu_btn.grid(row=2,column=4,padx=50)

                    

                    tp_lb_srh=LabelFrame(Sys_top_frame,bg="#213b52")#-------------------------Serch area Frame
                    tp_lb_srh.grid(row=1,column=2,sticky='nsew')
                    tp_lb_srh.grid_rowconfigure(0,weight=1)
                    tp_lb_srh.grid_columnconfigure(0,weight=1)

                    def srh_fn(event):
                        if srh_top.get()=="Search":
                            srh_top.delete(0,END)
                        else:
                            pass

                    

                    #------------------------------------------------------settings 
                    def close_lst_2():
                            lst_prf2.place_forget()
                            set_btn4 = Button(tp_lb_srh, image=stn_img,command=settings, bg="#213b52", fg="black",border=0)
                            set_btn4.grid(row=2,column=5,padx=(0,30))
                            
                    def settings():
                        

                        # create a list box
                        stng = ("Accounts And Settings","Customize From Style","Chart Of Accounts")

                        stngs = StringVar(value=stng)
                        global lst_prf2
                        lst_prf2 = Listbox(root,listvariable=stngs,height=3 ,selectmode='extended',bg="black",fg="white")

                        lst_prf2.place(relx=0.70, rely=0.10)
                        lst_prf2.bind('<<ListboxSelect>>', )
                        set_btn.grid_forget()
                        set_btn2 = Button(tp_lb_srh, image=stn_img,command=close_lst_2, bg="#213b52", fg="black",border=0)
                        set_btn2.grid(row=2,column=5,padx=(0,30))

                    set_btn = Button(tp_lb_srh, image=stn_img,command=settings, bg="#213b52", fg="black",border=0)
                    set_btn.grid(row=2,column=5,padx=(0,30))

                    tp_lb_nm=LabelFrame(Sys_top_frame,bg="#213b52")#-----------------------------Notification
                    tp_lb_nm.grid(row=1,column=3,sticky='nsew')
                    tp_lb_nm.grid_rowconfigure(0,weight=1)
                    tp_lb_nm.grid_columnconfigure(0,weight=1)
                    srh_btn = Button(tp_lb_nm, image=noti, bg="#213b52", fg="black",border=0)
                    srh_btn.grid(row=0,column=0,padx=35)
                    
                    tp_lb_npr=LabelFrame(Sys_top_frame,bg="#213b52")#---------------------------profile area name
                    tp_lb_npr.grid(row=1,column=4,sticky='nsew')
                    tp_lb_npr.grid_rowconfigure(0,weight=1)
                    tp_lb_npr.grid_columnconfigure(0,weight=1)
                    dtl_sqls="select * from auth_user where username=%s"
                    dtl_sqls_val=(nm_ent.get(),)
                    fbcursor.execute(dtl_sqls,dtl_sqls_val,)
                    dtls=fbcursor.fetchone()

                    sql_pro_sql="select * from app1_company where id_id =%s"
                    sql_pro_sql_val=(dtls[0],)
                    fbcursor.execute(sql_pro_sql,sql_pro_sql_val,)
                    dtl_cmp_pro=fbcursor.fetchone()

                    label = Label(tp_lb_npr, text=str(dtl_cmp_pro[1])+"\nOnline",bg="#213b52", fg="white", anchor="center",width=10,height=2,font=('Calibri 16 bold'),border=0)
                    label.grid(row=0,column=1,sticky='nsew')
                    # label = Label(tp_lb_npr, text="Online",bg="#213b52", fg="white",width=15,font=('Calibri 12 bold'),border=0)
                    # label.grid(row=2,column=1,sticky='nsew')

                    
                    
                    def lst_frt():
                        lst_prf.place_forget()
                        srh_btn3 = Button(tp_lb_npr,image=dash_prof_pics, bg="White", fg="black",command=profile)
                        srh_btn3.grid(row=0,column=2,padx=15)
                    def lst_prf_slt(event):
                        def edit_profile():
                            def responsive_widgets_edit(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                                


                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/13
                                y2 = dheight/.53

                                dcanvas.coords("bg_polygen_pr",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )                              

                                
                                # dcanvas.coords("bg_polygen_pr",dwidth/16,dheight/.6,dwidth/1.07,dheight/9)
                                dcanvas.coords("my_pro",dwidth/2.3,dheight/12.5)
                                dcanvas.coords("pr_img",dwidth/2.3,dheight/5)
                                

                                dcanvas.coords("pr_hr_l",dwidth/16,dheight/6.5,dwidth/1.07,dheight/6.5)
                                dcanvas.coords("pr_hd",dwidth/20,dheight/2.2)
                                dcanvas.coords("pr_1_nm",dwidth/17.075,dheight/1.9)
                                dcanvas.coords("fr_name_ent",dwidth/17.075,dheight/1.75)
                                dcanvas.coords("pr_em_lb",dwidth/17.075,dheight/1.56)
                                dcanvas.coords("em_ent",dwidth/17.075,dheight/1.47)
                                dcanvas.coords("pr_crpass_lb",dwidth/17.075,dheight/1.33)
                                dcanvas.coords("pr_crpass_ent",dwidth/17.075,dheight/1.26)
                                dcanvas.coords("pr_re_pass_lb",dwidth/17.075,dheight/1.16)
                                dcanvas.coords("pr_re_pass_ent",dwidth/17.075,dheight/1.1)
                                dcanvas.coords("last_nm_lb",dwidth/1.92,dheight/1.9)
                                dcanvas.coords("lst_nm_ent",dwidth/1.92,dheight/1.75)
                                dcanvas.coords("usr_nm_lb",dwidth/1.92,dheight/1.56)
                                dcanvas.coords("usr_nm_ent",dwidth/1.92,dheight/1.47)
                                dcanvas.coords("pr_new_pass_lb",dwidth/1.92,dheight/1.33)
                                dcanvas.coords("pr_new_pass_ent",dwidth/1.92,dheight/1.26)

                                
                                #-------------------------------------------------------------------------company section
                                dcanvas.coords("cmp_hd",dwidth/20,dheight/1)
                                dcanvas.coords("cmp_nm_lb",dwidth/17.075,dheight/0.93)
                                dcanvas.coords("cmp_nm_ent",dwidth/17.075,dheight/0.89)
                                dcanvas.coords("cmp_cty_lb",dwidth/17.075,dheight/0.84)
                                dcanvas.coords("cmp_cty_ent",dwidth/17.075,dheight/0.81)
                                dcanvas.coords("cmp_pin_lb",dwidth/17.075,dheight/0.77)
                                dcanvas.coords("cmp_pin_ent",dwidth/17.075,dheight/.745)
                                dcanvas.coords("cmp_ph_lb",dwidth/17.075,dheight/.712)
                                dcanvas.coords("cmp_ph_ent",dwidth/17.075,dheight/.69)
                                dcanvas.coords("cmp_indest_lb",dwidth/17.075,dheight/.66)
                                dcanvas.coords("cmp_indest_ent",dwidth/17.075,dheight/.64)
                                dcanvas.coords("cmp_file_lb",dwidth/17.075,dheight/.615)
                                dcanvas.coords("cmp_file_ent",dwidth/17.075,dheight/.6)
                                

                                #--------------------------------------------------------------------------company right

                                dcanvas.coords("cmp_addr_lb",dwidth/1.92,dheight/0.93)
                                dcanvas.coords("cmp_addr_ent",dwidth/1.92,dheight/0.89)
                                dcanvas.coords("cmp_st_lb",dwidth/1.92,dheight/0.84)
                                dcanvas.coords("cmp_st_ent",dwidth/1.92,dheight/0.81)
                                dcanvas.coords("cmp_em_lb",dwidth/1.92,dheight/0.77)
                                dcanvas.coords("cmp_em_ent",dwidth/1.92,dheight/.745)
                                dcanvas.coords("cmp_lg_nm",dwidth/1.92,dheight/.712)
                                dcanvas.coords("cmp_lg_ent",dwidth/1.92,dheight/.69)
                                dcanvas.coords("cmp_typ_lb",dwidth/1.92,dheight/.66)
                                dcanvas.coords("cmp_typ_ent",dwidth/1.92,dheight/.64)
                                dcanvas.coords("btn_edit",dwidth/2.4,dheight/.57)
                            sql_pro="select * from auth_user where username=%s"
                            sql_pro_val=(nm_ent.get(),)
                            fbcursor.execute(sql_pro,sql_pro_val,)
                            edi_dtl=fbcursor.fetchone()

                            def update_profile():
                                first_name=fr_name_ent.get()
                                pro_email=em_ent.get()
                                last_name=lst_nm_ent.get()
                                pro_username=usr_nm_ent.get()
                                pro_new_pass=pr_new_pass_ent.get()

                                sql_signup='select * from auth_user'
                                fbcursor.execute(sql_signup)
                                check_none=fbcursor.fetchone()

                                if edi_dtl[4]==pro_username and edi_dtl[1]==pr_crpass_ent.get() and pro_new_pass=="" :
                                            passw=pr_crpass_ent.get()
                                    
                                            prof_edit="update auth_user set first_name=%s,last_name=%s,email=%s,username=%s,password=%s where id=%s" #adding values into db
                                            prof_edit_val=(first_name,last_name,pro_email,pro_username,passw,edi_dtl[0])
                                            fbcursor.execute(prof_edit,prof_edit_val)
                                            finsysdb.commit()

                                            #compnay
                                            cmp_name=cmp_nm_ent.get()
                                            cmp_cty=cmp_cty_ent.get()
                                            cmp_pin=cmp_pin_ent.get()
                                            cmp_phn=cmp_ph_ent.get()
                                            cmp_ind=cmp_indest_ent.get()
                                            cmp_addr=cmp_addr_ent.get()
                                            cmp_st=cmp_st_ent.get()
                                            cmp_em=cmp_em_ent.get()
                                            cmp_bname=cmp_lg_ent.get()
                                            cmp_typ=cmp_typ_ent.get()
                                            logo=cmp_file_ent.get()

                                            cmp_edit="update app1_company set cname=%s,caddress=%s,city=%s,state=%s,pincode=%s,cemail=%s,phone=%s,cimg=%s,bname=%s,industry=%s,ctype=%s where id_id =%s" #adding values into db
                                            cmp_edit_val=(cmp_name,cmp_addr,cmp_cty,cmp_st,cmp_pin,cmp_em,cmp_phn,logo,cmp_bname,cmp_ind,cmp_typ,edi_dtl[0])
                                            fbcursor.execute(cmp_edit,cmp_edit_val)
                                            finsysdb.commit()
                                            
                                        
                                else:
                                    # #username same password change
                                    if pr_new_pass_ent.get()=="":
                                        
                                        pro_new_passd=pr_crpass_ent.get()
                                        
                                    else:
                                        pro_new_passd=pr_new_pass_ent.get()
                                    if pro_new_pass==pr_re_pass_ent.get() and pr_re_pass_ent.get()==pro_new_pass:
                                            if pr_crpass_ent.get()==edi_dtl[1]:
                                                
                                                prof_edit="update auth_user set first_name=%s,last_name=%s,email=%s,username=%s,password=%s where id=%s" #adding values into db
                                                prof_edit_val=(first_name,last_name,pro_email,pro_username,pro_new_passd,edi_dtl[0])
                                                fbcursor.execute(prof_edit,prof_edit_val)
                                                finsysdb.commit()

                                                #compnay
                                                cmp_name=cmp_nm_ent.get()
                                                cmp_cty=cmp_cty_ent.get()
                                                cmp_pin=cmp_pin_ent.get()
                                                cmp_phn=cmp_ph_ent.get()
                                                cmp_ind=cmp_indest_ent.get()
                                                cmp_addr=cmp_addr_ent.get()
                                                cmp_st=cmp_st_ent.get()
                                                cmp_em=cmp_em_ent.get()
                                                cmp_bname=cmp_lg_ent.get()
                                                cmp_typ=cmp_typ_ent.get()
                                                logo=cmp_file_ent.get()

                                                cmp_edit="update app1_company set cname=%s,caddress=%s,city=%s,state=%s,pincode=%s,cemail=%s,phone=%s,cimg=%s,bname=%s,industry=%s,ctype=%s where id_id =%s" #adding values into db
                                                cmp_edit_val=(cmp_name,cmp_addr,cmp_cty,cmp_st,cmp_pin,cmp_em,cmp_phn,logo,cmp_bname,cmp_ind,cmp_typ,edi_dtl[0])
                                                fbcursor.execute(cmp_edit,cmp_edit_val)
                                                finsysdb.commit()
                                                
                                            else:
                                                messagebox.showerror("Updation Failed","Please check your current password")
                                    else:

                                            messagebox.showerror("Updation Failed","password and conform password does not match")
                                        
                                    
                                Sys_top_frame2.pack_forget()
                                Sys_top_frame.pack_forget()
                                Sys_mains_frame_pr_ed.grid_forget()
                                main_frame_signin.pack(fill=X,)

                            sql_pro_cmp="select * from app1_company where id_id=%s"
                            sql_pro_cmp_val=(pro_dtl[0],)
                            fbcursor.execute(sql_pro_cmp,sql_pro_cmp_val,)
                            edi_cmp_dtl=fbcursor.fetchone()

                            Sys_mains_frame_pr.place_forget()
                            global Sys_mains_frame_pr_ed
                            Sys_mains_frame_pr_ed=Frame(tab1, height=750)
                            Sys_mains_frame_pr_ed.grid(row=0,column=0,sticky='nsew')
                            Sys_mains_frame_pr_ed.grid_rowconfigure(0,weight=1)
                            Sys_mains_frame_pr_ed.grid_columnconfigure(0,weight=1)

                            pr_canvas_ed=Canvas(Sys_mains_frame_pr_ed,height=766,width=1340,scrollregion=(0,0,766,1650),bg="#2f516f",border=0)
                            pr_canvas_ed.bind('<Configure>', responsive_widgets_edit)
                            
                            pr_myscrollbar_ed=Scrollbar(Sys_mains_frame_pr_ed,orient="vertical",command=pr_canvas_ed.yview)
                            pr_canvas_ed.configure(yscrollcommand=pr_myscrollbar_ed.set)

                            pr_myscrollbar_ed.pack(side="right",fill="y")
                            pr_canvas_ed.pack(fill=X)

                            rth2 = pr_canvas_ed.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_pr"),smooth=True,)


                            grd1c=Label(pr_canvas_ed, text="MY PROFILE",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
                            win_inv1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=grd1c,tags=("my_pro"))

                            pr_img=Label(pr_canvas_ed,  image = prof_pics,bg="#213b52",width=170,height=170,  anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_img,tags=("pr_img"))

                            pr_canvas_ed.create_line(0,0, 0, 0,fill="gray",tags=("pr_hr_l") )
                            #----------------------------------------------------------------------------------------Personal info
                            pr_hd=Label(pr_canvas_ed, text="Personal Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                            win_pr = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_hd,tags=("pr_hd"))

                            fir_name=Label(pr_canvas_ed, text="First Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=fir_name,tags=("pr_1_nm"))

                            fr_name_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            fr_name_ent.delete(0,END)
                            fr_name_ent.insert(0,edi_dtl[5])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=fr_name_ent,tags=("fr_name_ent"))

                            pr_em_lb=Label(pr_canvas_ed, text="E-Mail",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_em_lb,tags=("pr_em_lb"))

                            em_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            em_ent.delete(0,END)
                            em_ent.insert(0,edi_dtl[7])
                            def validate(value):
            
                                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                                if re.fullmatch(pattern, value) is None:
                                                    
                                    return False

                                em_ent.config(fg="black")
                                return True

                            def on_invalid():
                                
                                em_ent.config(fg="red")

                            vcmdem_ent = (pr_canvas_ed.register(validate), '%P')
                            ivcmdem_ent = (pr_canvas_ed.register(on_invalid),)
                            em_ent.config(validate='focusout', validatecommand=vcmdem_ent, invalidcommand=ivcmdem_ent)                              
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=em_ent,tag=("em_ent"))

                            pr_crpass_lb=Label(pr_canvas_ed, text="Enter your Current Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_crpass_lb,tag=("pr_crpass_lb"))

                            pr_crpass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'),show="*")
                            
                            pr_crpass_ent.delete(0,END)
                            pr_crpass_ent.insert(0,edi_dtl[1])
                            
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_crpass_ent,tag=("pr_crpass_ent"))

                            pr_re_pass_lb=Label(pr_canvas_ed, text="Re-type new Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_re_pass_lb,tag=("pr_re_pass_lb"))

                            pr_re_pass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'),show="*")
                            def pas_val_fun1(value):
            
                                pattern = r'(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
                                if re.fullmatch(pattern, value) is None:
                                                    
                                    return False

                                pr_re_pass_ent.config(fg="black")
                                return True

                            def pass_inval_fun1():
                                pr_re_pass_ent.config(fg="red")

                            pas_val1 = (pr_canvas_ed.register(pas_val_fun1), '%P')
                            pass_inval1 = (pr_canvas_ed.register(pass_inval_fun1),)

                            pr_re_pass_ent.config(validate='focusout', validatecommand=pas_val1, invalidcommand=pass_inval1)

                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_re_pass_ent,tag=("pr_re_pass_ent"))


                            last_nm_lb=Label(pr_canvas_ed, text="Last Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=last_nm_lb,tag=("last_nm_lb"))

                            lst_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            lst_nm_ent.delete(0,END)
                            lst_nm_ent.insert(0,edi_dtl[6])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=lst_nm_ent,tag=("lst_nm_ent"))

                            usr_nm_lb=Label(pr_canvas_ed, text="Username",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=usr_nm_lb, tag=("usr_nm_lb"))

                            usr_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            usr_nm_ent.delete(0,END)
                            usr_nm_ent.insert(0,edi_dtl[4])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=usr_nm_ent,tag=("usr_nm_ent"))

                            pr_new_pass_lb=Label(pr_canvas_ed, text="Enter New Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_new_pass_lb,tag=("pr_new_pass_lb"))

                            pr_new_pass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'),show="*",)
                            def pas_val_fun2(value):
            
                                pattern = r'(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
                                if re.fullmatch(pattern, value) is None:
                                                    
                                    return False

                                pr_new_pass_ent.config(fg="black")
                                return True

                            def pass_inval_fun2():
                                pr_new_pass_ent.config(fg="red")

                            pas_val2 = (pr_canvas_ed.register(pas_val_fun2), '%P')
                            pass_inval2 = (pr_canvas_ed.register(pass_inval_fun2),)

                            pr_new_pass_ent.config(validate='focusout', validatecommand=pas_val2, invalidcommand=pass_inval2)
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_new_pass_ent,tag=("pr_new_pass_ent"))


                            # #------------------------------------------------------------------------------------------------COMPANY SECTION
                            cmp_hd=Label(pr_canvas_ed, text="Company Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                            win_pr = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_hd,tag=("cmp_hd"))

                            cmp_nm_lb=Label(pr_canvas_ed, text="Company Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_nm_lb,tag=("cmp_nm_lb"))

                            cmp_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_nm_ent.delete(0,END)
                            cmp_nm_ent.insert(0,edi_cmp_dtl[1])
                            
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_nm_ent,tag=("cmp_nm_ent"))

                            cmp_cty_lb=Label(pr_canvas_ed, text="City",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_cty_lb,tag=("cmp_cty_lb"))

                            cmp_cty_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_cty_ent.delete(0,END)
                            cmp_cty_ent.insert(0,edi_cmp_dtl[3])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_cty_ent,tag=("cmp_cty_ent"))

                            cmp_pin_lb=Label(pr_canvas_ed, text="Pincode",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_pin_lb,tag=("cmp_pin_lb"))

                            cmp_pin_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_pin_ent.delete(0,END)
                            cmp_pin_ent.insert(0,edi_cmp_dtl[5])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_pin_ent,tag=("cmp_pin_ent"))

                            cmp_ph_lb=Label(pr_canvas_ed, text="Phone Number",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_ph_lb,tag=("cmp_ph_lb"))

                            cmp_ph_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_ph_ent.delete(0,END)
                            cmp_ph_ent.insert(0,edi_cmp_dtl[7])
                            def validate_telb512(value):
            
                                    pattern = r'^[0-9]\d{9}$'
                                    if re.fullmatch(pattern, value) is None:
                                        
                                        return False
                                    cmp_ph_ent.config(fg="black")
                                    return True

                            def on_invalid_telb512():
                                    cmp_ph_ent.config(fg="red")
                                    
                            v_tel_cmd = (pr_canvas_ed.register(validate_telb512), '%P')
                            iv_tel_cmd = (pr_canvas_ed.register(on_invalid_telb512),)
                            cmp_ph_ent.config(validate='focusout', validatecommand=v_tel_cmd, invalidcommand=iv_tel_cmd)
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_ph_ent,tag=("cmp_ph_ent"))

                            cmp_indest_lb=Label(pr_canvas_ed, text="Your Industry",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_indest_lb,tag=("cmp_indest_lb"))

                            cmp_indest_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_indest_ent.delete(0,END)
                            cmp_indest_ent.insert(0,edi_cmp_dtl[10])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_indest_ent,tag=("cmp_indest_ent"))

                            # #----------------------------------------------------------------------------------------------------RIGHT SIDE
                            cmp_addr_lb=Label(pr_canvas_ed, text="Company Address",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_addr_lb,tag=("cmp_addr_lb"))

                            cmp_addr_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_addr_ent.delete(0,END)
                            cmp_addr_ent.insert(0,edi_cmp_dtl[2])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_addr_ent,tag=("cmp_addr_ent"))

                            cmp_st_lb=Label(pr_canvas_ed, text="State",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_st_lb,tag=("cmp_st_lb"))

                            cmp_st_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_st_ent.delete(0,END)
                            cmp_st_ent.insert(0,edi_cmp_dtl[4])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_st_ent,tag=("cmp_st_ent"))

                            cmp_em_lb=Label(pr_canvas_ed, text="Email",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_em_lb,tag=("cmp_em_lb"))

                            cmp_em_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_em_ent.delete(0,END)
                            cmp_em_ent.insert(0,edi_cmp_dtl[6])
                            def validateb2113(value):
            
                                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                                if re.fullmatch(pattern, value) is None:
                                                    
                                    return False

                                cmp_em_ent.config(fg="black")
                                return True

                            def on_invalidb2113():
                                
                                cmp_em_ent.config(fg="red")

                            vcmdb2113 = (pr_canvas_ed.register(validateb2113), '%P')
                            ivcmdb2113 = (pr_canvas_ed.register(on_invalidb2113),)
                            cmp_em_ent.config(validate='focusout', validatecommand=vcmdb2113, invalidcommand=ivcmdb2113) 

                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_em_ent,tag=("cmp_em_ent"))

                            cmp_lg_nm=Label(pr_canvas_ed, text="Legal Business Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_lg_nm,tag=("cmp_lg_nm"))

                            cmp_lg_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_lg_ent.delete(0,END)
                            cmp_lg_ent.insert(0,edi_cmp_dtl[9])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_lg_ent,tag=("cmp_lg_ent"))

                            cmp_typ_lb=Label(pr_canvas_ed, text="Company Type",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_typ_lb,tag=("cmp_typ_lb"))

                            cmp_typ_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_typ_ent.delete(0,END)
                            cmp_typ_ent.insert(0,edi_cmp_dtl[11])
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_typ_ent,tag=("cmp_typ_ent"))

                            cmp_file_lb=Label(pr_canvas_ed, text="File",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_file_lb,tag=("cmp_file_lb"))
                            def fil_ents(event):
                                sql_log_sql='select * from auth_user where username=%s'
                                vals=(nm_ent.get(),)
                                fbcursor.execute(sql_log_sql,vals)
                                check_logins=fbcursor.fetchone()
                                cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
                                logo_crp=cmp_logo.split('/',-1)
                                
                                im1 = Image.open(r""+cmp_logo) 
                                im1 = im1.save("profilepic/propic"+str(check_logins[0])+".png")

                                cmp_file_ent.delete("0",END)
                                cmp_file_ent.insert(0,logo_crp[-1])

                            cmp_file_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                            cmp_file_ent.delete(0,END)
                            cmp_file_ent.insert(0,edi_cmp_dtl[8])
                            cmp_file_ent.bind("<Button-1>",fil_ents)
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_file_ent,tag=("cmp_file_ent"))


                            btn_edit = Button(pr_canvas_ed, text='Update Profile', command=update_profile, bg="#213b52", fg="White",borderwidth = 3,height=2,width=30)
                            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=btn_edit,tag=("btn_edit"))

                        
                        selected_indices = lst_prf.curselection()
                        selected_langs = ",".join([lst_prf.get(i) for i in selected_indices])
                        lst_prf.place_forget()

                        def pr_responsive_widgets(event):
                                
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/13
                                y2 = dheight/.6

                                dcanvas.coords("bg_polygen_pr",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )                   
                
                                dcanvas.coords("my_pro",dwidth/2.3,dheight/13)
                                dcanvas.coords("pr_img",dwidth/2.3,dheight/5)

                                dcanvas.coords("pr_hr_l",dwidth/16,dheight/6.5,dwidth/1.07,dheight/6.5)
                                dcanvas.coords("pr_hd",dwidth/20,dheight/2.2)
                                dcanvas.coords("pr_1_nm",dwidth/17.075,dheight/1.9)
                                dcanvas.coords("fr_name_ent",dwidth/17.075,dheight/1.75)
                                
                                dcanvas.coords("pr_em_lb",dwidth/17.075,dheight/1.56)
                                dcanvas.coords("em_ent",dwidth/17.075,dheight/1.47)
                                dcanvas.coords("last_nm_lb",dwidth/1.92,dheight/1.9)
                                dcanvas.coords("lst_nm_ent",dwidth/1.92,dheight/1.75)
                                dcanvas.coords("usr_nm_lb",dwidth/1.92,dheight/1.56)
                                dcanvas.coords("usr_nm_ent",dwidth/1.92,dheight/1.47)

                                #-------------------------------------------------------------------------company section
                                dcanvas.coords("cmp_hd",dwidth/20,dheight/1.32)
                                dcanvas.coords("cmp_nm_lb",dwidth/17.075,dheight/1.22)
                                dcanvas.coords("cmp_nm_ent",dwidth/17.075,dheight/1.16)
                                dcanvas.coords("cmp_cty_lb",dwidth/17.075,dheight/1.07)
                                dcanvas.coords("cmp_cty_ent",dwidth/17.075,dheight/1.02)
                                dcanvas.coords("cmp_pin_lb",dwidth/17.075,dheight/.95)
                                dcanvas.coords("cmp_pin_ent",dwidth/17.075,dheight/.91)
                                dcanvas.coords("cmp_ph_lb",dwidth/17.075,dheight/.86)
                                dcanvas.coords("cmp_ph_ent",dwidth/17.075,dheight/.83)
                                dcanvas.coords("cmp_indest_lb",dwidth/17.075,dheight/.78)
                                dcanvas.coords("cmp_indest_ent",dwidth/17.075,dheight/.755)

                                #--------------------------------------------------------------------------company right

                                dcanvas.coords("cmp_addr_lb",dwidth/1.92,dheight/1.22)
                                dcanvas.coords("cmp_addr_ent",dwidth/1.92,dheight/1.16)
                                dcanvas.coords("cmp_st_lb",dwidth/1.92,dheight/1.07)
                                dcanvas.coords("cmp_st_ent",dwidth/1.92,dheight/1.02)
                                dcanvas.coords("cmp_em_lb",dwidth/1.92,dheight/.95)
                                dcanvas.coords("cmp_em_ent",dwidth/1.92,dheight/.91)
                                dcanvas.coords("cmp_lg_nm",dwidth/1.92,dheight/.86)
                                dcanvas.coords("cmp_lg_ent",dwidth/1.92,dheight/.83)
                                dcanvas.coords("cmp_typ_lb",dwidth/1.92,dheight/.78)
                                dcanvas.coords("cmp_typ_ent",dwidth/1.92,dheight/.755)
                                dcanvas.coords("btn_edit",dwidth/2.4,dheight/.71)

                        if selected_langs=="Profile":
                            # canvas.pack_forget()
                            # myscrollbar.pack_forget()
                            # Sys_mains_frame.pack_forget()
                            
                            sql_pro="select * from auth_user where username=%s"
                            sql_pro_val=(nm_ent.get(),)
                            fbcursor.execute(sql_pro,sql_pro_val,)
                            pro_dtl=fbcursor.fetchone()

                            sql_pro_cmp="select * from app1_company where id_id=%s"
                            sql_pro_cmp_val=(pro_dtl[0],)
                            fbcursor.execute(sql_pro_cmp,sql_pro_cmp_val,)
                            pro_cmp_dtl=fbcursor.fetchone()
                            
                            global Sys_mains_frame_pr
                            Sys_mains_frame_pr=Frame(tab1, height=750,bg="#2f516f",)
                            Sys_mains_frame_pr.grid(row=0,column=0,sticky='nsew')
                            Sys_mains_frame_pr.grid_rowconfigure(0,weight=1)
                            Sys_mains_frame_pr.grid_columnconfigure(0,weight=1)

                            pr_canvas=Canvas(Sys_mains_frame_pr,height=700,width=1340,scrollregion=(0,0,700,1300),bg="#2f516f",border=0)
                            pr_canvas.bind("<Configure>", pr_responsive_widgets)
                            
                            pr_myscrollbar=Scrollbar(Sys_mains_frame_pr,orient="vertical",command=pr_canvas.yview)
                            pr_canvas.configure(yscrollcommand=pr_myscrollbar.set)

                            pr_myscrollbar.pack(side="right",fill="y")
                            pr_canvas.pack(fill=X)

                            rth2 = pr_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",smooth=True,tags=("bg_polygen_pr"))

                            grd1c=Label(pr_canvas, text="MY PROFILE",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
                            win_inv1 = pr_canvas.create_window(0, 0, anchor="nw", window=grd1c,tags=("my_pro"))

                            pr_canvas.create_line(0,0, 0, 0,fill="gray",tags=("pr_hr_l") )
                            #----------------------------------------------------------------------------------------Personal info

            
                            pr_img=Label(pr_canvas, image = prof_pics,bg="#213b52",width=170,height=170, anchor="center",)
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=pr_img,tags=("pr_img"))

                            pr_hd=Label(pr_canvas, text="Personal Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                            win_pr = pr_canvas.create_window(0, 0, anchor="nw", window=pr_hd,tags=("pr_hd"))

                            fir_name=Label(pr_canvas, text="First Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=fir_name,tags=("pr_1_nm"))

                            fr_name_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            fr_name_ent.delete(0,END)
                            fr_name_ent.insert(0,pro_dtl[5])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=fr_name_ent,tags=("fr_name_ent"))

                            pr_em_lb=Label(pr_canvas, text="E-Mail",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=pr_em_lb,tags=("pr_em_lb"))

                            em_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            em_ent.delete(0,END)
                            em_ent.insert(0,pro_dtl[7])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=em_ent,tag=("em_ent"))

                            last_nm_lb=Label(pr_canvas, text="Last Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=last_nm_lb,tag=("last_nm_lb"))

                            lst_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            lst_nm_ent.delete(0,END)
                            lst_nm_ent.insert(0,pro_dtl[6])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=lst_nm_ent,tag=("lst_nm_ent"))

                            usr_nm_lb=Label(pr_canvas, text="Username",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=usr_nm_lb, tag=("usr_nm_lb"))

                            usr_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            usr_nm_ent.delete(0,END)
                            usr_nm_ent.insert(0,pro_dtl[4])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=usr_nm_ent,tag=("usr_nm_ent"))

                            #------------------------------------------------------------------------------------------------COMPANY SECTION
                            cmp_hd=Label(pr_canvas, text="Company Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                            win_pr = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_hd,tag=("cmp_hd"))

                            cmp_nm_lb=Label(pr_canvas, text="Company Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_nm_lb,tag=("cmp_nm_lb"))

                            cmp_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_nm_ent.delete(0,END)
                            cmp_nm_ent.insert(0,pro_cmp_dtl[1])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_nm_ent,tag=("cmp_nm_ent"))

                            cmp_cty_lb=Label(pr_canvas, text="City",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_cty_lb,tag=("cmp_cty_lb"))

                            cmp_cty_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_cty_ent.delete(0,END)
                            cmp_cty_ent.insert(0,pro_cmp_dtl[3])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_cty_ent,tag=("cmp_cty_ent"))

                            cmp_pin_lb=Label(pr_canvas, text="Pincode",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_pin_lb,tag=("cmp_pin_lb"))

                            cmp_pin_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_pin_ent.delete(0,END)
                            cmp_pin_ent.insert(0,pro_cmp_dtl[5])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_pin_ent,tag=("cmp_pin_ent"))

                            cmp_ph_lb=Label(pr_canvas, text="Phone Number",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_ph_lb,tag=("cmp_ph_lb"))

                            cmp_ph_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_ph_ent.delete(0,END)
                            cmp_ph_ent.insert(0,pro_cmp_dtl[7])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_ph_ent,tag=("cmp_ph_ent"))

                            cmp_indest_lb=Label(pr_canvas, text="Your Industry",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_indest_lb,tag=("cmp_indest_lb"))

                            cmp_indest_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_indest_ent.delete(0,END)
                            cmp_indest_ent.insert(0,pro_cmp_dtl[10])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_indest_ent,tag=("cmp_indest_ent"))

                            #----------------------------------------------------------------------------------------------------RIGHT SIDE
                            cmp_addr_lb=Label(pr_canvas, text="Company Address",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_addr_lb,tag=("cmp_addr_lb"))

                            cmp_addr_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_addr_ent.delete(0,END)
                            cmp_addr_ent.insert(0,pro_cmp_dtl[2])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_addr_ent,tag=("cmp_addr_ent"))

                            cmp_st_lb=Label(pr_canvas, text="State",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_st_lb,tag=("cmp_st_lb"))

                            cmp_st_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_st_ent.delete(0,END)
                            cmp_st_ent.insert(0,pro_cmp_dtl[4])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_st_ent,tag=("cmp_st_ent"))

                            cmp_em_lb=Label(pr_canvas, text="Email",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_em_lb,tag=("cmp_em_lb"))

                            cmp_em_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_em_ent.delete(0,END)
                            cmp_em_ent.insert(0,pro_cmp_dtl[6])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_em_ent,tag=("cmp_em_ent"))

                            cmp_lg_nm=Label(pr_canvas, text="Legal Business Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_lg_nm,tag=("cmp_lg_nm"))

                            cmp_lg_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_lg_ent.delete(0,END)
                            cmp_lg_ent.insert(0,pro_cmp_dtl[9])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_lg_ent,tag=("cmp_lg_ent"))

                            cmp_typ_lb=Label(pr_canvas, text="Company Type",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_typ_lb,tag=("cmp_typ_lb"))

                            cmp_typ_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                            cmp_typ_ent.delete(0,END)
                            cmp_typ_ent.insert(0,pro_cmp_dtl[11])
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_typ_ent,tag=("cmp_typ_ent"))


                            btn_edit = Button(pr_canvas, text='Edit Profile', command=edit_profile, bg="#213b52", fg="White",borderwidth = 3,height=2,width=30)
                            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=btn_edit,tag=("btn_edit"))
                        
                        elif selected_langs=="Log Out":
                            
                            Sys_top_frame2.pack_forget()
                            Sys_top_frame.pack_forget()
                            main_frame_signin.pack(fill=X,)
                        elif selected_langs== "Dashboard":
                            try:
                                
                                Sys_mains_frame_pr.grid_forget()
                            except:
                                pass
                            try:
                                Sys_mains_frame_pr_ed.grid_forget()
                            except:
                                pass
                            

                        else:
                            pass
                    def profile2():
                        lst_prf.place_forget()
                        srh_btn4 = Button(tp_lb_npr,image=dash_prof_pics, bg="White", fg="black",command=profile)
                        srh_btn4.grid(row=0,column=2,padx=15)
                    def profile():
                        # create a list box
                        langs = ("Dashboard","Profile","Log Out")

                        langs_var = StringVar(value=langs)
                        global lst_prf
                        lst_prf = Listbox(root,listvariable=langs_var,height=3 ,selectmode='extended',bg="black",fg="white")

                        lst_prf.place(relx=0.90, rely=0.10)
                        lst_prf.bind('<<ListboxSelect>>', lst_prf_slt)
                        srh_btn.grid_forget()
                        srh_btn2 = Button(tp_lb_npr,image=dash_prof_pics, bg="White", fg="black",command=profile2)
                        srh_btn2.grid(row=0,column=2,padx=15)
                
                    srh_btn = Button(tp_lb_npr,image=dash_prof_pics, bg="White", fg="black",command=profile)
                    srh_btn.grid(row=0,column=2,padx=15)

                    Sys_top_frame2=Frame(root, height=10,bg="#213b52")
                    Sys_top_frame2.pack(fill=X,)
                    
                    s = ttk.Style()
                    s.theme_use('default')
                    s.configure('TNotebook.Tab', background="#213b52",foreground="white", width=150,anchor="center", padding=5)
                    s.map('TNotebook.Tab',background=[("selected","#2f516f")])
                    def right_nav():
                        
                        tabControl.pack_forget()
                        btn_nav.place_forget()
                        tabControl2.pack(expand = 1, fill ="both")
                        btn_nav2.place(relx=0, rely=0)
                        try:
                            btn_nav3.place_forget()
                        except:
                            pass
                    def left_nav():
                        
                        tabControl2.pack_forget()
                        btn_nav2.place_forget()
                        tabControl.pack(expand = 1, fill ="both")
                        global btn_nav3
                        btn_nav3=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
                        btn_nav3.place(relx=0.97, rely=0)

                    tabControl = ttk.Notebook(Sys_top_frame2)
                    tab1 = ttk.Frame(tabControl)
                    tab2 = ttk.Frame(tabControl)
                    tab3=  ttk.Frame(tabControl)
                    tab4 = ttk.Frame(tabControl)
                    tab5 = ttk.Frame(tabControl)
                    tab6=  ttk.Frame(tabControl)
                    tab7 = ttk.Frame(tabControl)
                    tab8 = ttk.Frame(tabControl)
                    
                    
                    btn_nav=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
                    btn_nav.place(relx=0.97, rely=0)
                    tabControl.add(tab1,compound = LEFT, text ='Dashboard',)
                    tabControl.add(tab2,compound = LEFT, text ='Banking')
                    tabControl.add(tab3,compound = LEFT, text ='Sales')
                    tabControl.add(tab4,compound = LEFT, text ='Expenses')
                    tabControl.add(tab5,compound = LEFT, text ='Payroll') 
                    tabControl.add(tab6,compound = LEFT, text ='Report')
                    tabControl.add(tab7,compound = LEFT, text ='Taxes')
                    tabControl.add(tab8,compound = LEFT, text ='Accounting')
                    
                    tabControl.pack(expand = 1, fill ="both")


                    
                    tabControl2 = ttk.Notebook(Sys_top_frame2)
                    tab9 =  ttk.Frame(tabControl2)
                    tab10=  ttk.Frame(tabControl2)
                    tab11 = ttk.Frame(tabControl2)
                    tab12=  ttk.Frame(tabControl2)
                    tab13 = ttk.Frame(tabControl2)
                    tab14 = ttk.Frame(tabControl2)
                    tab15 =  ttk.Frame(tabControl2)

                    btn_nav2=Button(Sys_top_frame2,text="<<", command=left_nav, width=3, bg="#213b52",fg="white")
                    
                        
                    tabControl2.add(tab9,compound = LEFT, text ='My Account')
                    tabControl2.add(tab10,compound = LEFT, text ='Cash Management')
                    tabControl2.add(tab11,compound = LEFT, text ='Production')
                    tabControl2.add(tab12,compound = LEFT, text ='Quality Management')
                    tabControl2.add(tab13,compound = LEFT, text ='Project Management')
                    tabControl2.add(tab14,compound = LEFT, text ='Usage Decisions')
                    tabControl2.add(tab15,compound = LEFT, text ='Account & Payable')

                
                    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Dash Board}
                    tab1.grid_columnconfigure(0,weight=1)
                    tab1.grid_rowconfigure(0,weight=1)
                    
                    Sys_mains_frame=Frame(tab1,bg="#2f516f",)
                    Sys_mains_frame.grid(row=0,column=0,sticky='nsew')
                    
                    def responsive_wid(event):
                        dwidth = event.width
                        dheight = event.height
                        dcanvas = event.widget
                    
                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/13
                        y2 = dheight/6

                        dcanvas.coords("bg_polygen_dash",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )                    

                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/3.1
                        y1 = dheight/5
                        y2 = dheight/1.1

                        dcanvas.coords("bg_polygen_dash1",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        r1 = 25
                        x1 = dwidth/2.95
                        x2 = dwidth/1.529
                        y1 = dheight/5
                        y2 = dheight/1.1

                        dcanvas.coords("bg_polygen_dash2",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        r1 = 25
                        x1 = dwidth/1.49
                        x2 = dwidth/1.021
                        y1 = dheight/5
                        y2 = dheight/1.1

                        dcanvas.coords("bg_polygen_dash3",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/3.1
                        y1 = dheight/1.06
                        y2 = dheight/.59
                        
                        #-----------------------------------------second row
                        dcanvas.coords("bg_polygen_dash4",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        r1 = 25
                        x1 = dwidth/2.95
                        x2 = dwidth/1.529
                        y1 = dheight/1.06
                        y2 = dheight/.59

                        dcanvas.coords("bg_polygen_dash5",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        r1 = 25
                        x1 = dwidth/1.49
                        x2 = dwidth/1.021
                        y1 = dheight/1.06
                        y2 = dheight/.59

                        dcanvas.coords("bg_polygen_dash6",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        dcanvas.coords("head_lb",dwidth/2,dheight/8.4)
                    
                        
                        dcanvas.coords("prf_lb",dwidth/53,dheight/4.7)
                        
                        dcanvas.coords("prf_hr",dwidth/53,dheight/3.7,dwidth/3.15,dheight/3.7)
                        dcanvas.coords("net_prf",dwidth/53,dheight/3.2)
                        dcanvas.coords("graph",dwidth/53,dheight/2.2)
                        #--------------------------------------------------------------second
                        dcanvas.coords("exp_hd_lb",dwidth/2.9,dheight/4.7)
                        dcanvas.coords("exp_hr",dwidth/2.9,dheight/3.7,dwidth/1.54,dheight/3.7)
                        dcanvas.coords("graph_2",dwidth/2.9,dheight/2.2)
                        
                        #-----------------------------------------------------------third
                        dcanvas.coords("bnk_lb",dwidth/1.48,dheight/4.7)
                        dcanvas.coords("bank_hr",dwidth/1.48,dheight/3.7,dwidth/1.03,dheight/3.7)
                        dcanvas.coords("inv_lb4",dwidth/1.48,dheight/3.5)
                        dcanvas.coords("inv_lb5",dwidth/1.48,dheight/3)
                        dcanvas.coords("graph9",dwidth/1.48,dheight/2.2)
                        
                        #--------------------------------------------------------------forth
                        dcanvas.coords("incom_lb",dwidth/53,dheight/1.04)
                        
                        dcanvas.coords("incom_hr",dwidth/53,dheight/0.98,dwidth/3.15,dheight/0.98)

                    
                        dcanvas.coords("graph_4",dwidth/53,dheight/0.85)
                
                        #-------------------------------------------------------------fifth
                        dcanvas.coords("inv_lb",dwidth/2.9,dheight/1.04)
                        dcanvas.coords("invs_hr",dwidth/2.9,dheight/0.98,dwidth/1.54,dheight/0.98)
                        dcanvas.coords("inv_lb2",dwidth/2.9,dheight/0.95)
                        dcanvas.coords("inv_lb3",dwidth/2.9,dheight/0.90)
                        dcanvas.coords("graph_5",dwidth/2.9,dheight/0.85)
                        #-------------------------------------------------------------sixth
                        dcanvas.coords("sales_lb",dwidth/1.48,dheight/1.04)
                        dcanvas.coords("sales_hr",dwidth/1.48,dheight/0.98,dwidth/1.03,dheight/0.98)
                        
                        


                        dcanvas.coords("grapg_6",dwidth/1.48,dheight/0.85)
                            
                    Sys_mains_frame.grid_rowconfigure(0,weight=1)
                    Sys_mains_frame.grid_columnconfigure(0,weight=1)

                    canvas = Canvas(Sys_mains_frame,height=700,bg='#2f516f',scrollregion=(0,0,700,1200))
                    sr_Scroll = Scrollbar(Sys_mains_frame,orient=VERTICAL)
                    sr_Scroll.grid(row=0,column=1,sticky='ns')
                    sr_Scroll.config(command=canvas.yview)
                    canvas.bind("<Configure>", responsive_wid)
                    canvas.config(yscrollcommand=sr_Scroll.set)
                    canvas.grid(row=0,column=0,sticky='nsew')

                    

                    cmp_name=Label(canvas, text=dtl_cmp_pro[1],bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
                
                    win_inv1 = canvas.create_window(0, 0, anchor="center", window=cmp_name,tag=("head_lb"))

                    

                    
                    rth2 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash"),smooth=True,)
                    # #----------------------------------------------------------------------------------------------------------------grid 1
                    rth1 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash1"),smooth=True,)
                    #-------------------------------------------------------Income
                    sql_incomes="select sum(balance) from app1_accounts1 where cid_id=%s and acctype='Income'"
                    sql_incomes_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_incomes,sql_incomes_val,)
                    incom_dtls=fbcursor.fetchone()
                    
                    if incom_dtls[0]==None or incom_dtls[0]=='':
                        tot_inc=0.0
                    else:
                        tot_inc=incom_dtls[0]
                    
                
                    #-----------------------------------------------------expense
                    sql_pro="select sum(balance) from app1_accounts1 where cid_id=%s and acctype='Expenses'"
                    sql_pro_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_pro,sql_pro_val,)
                    exp_tot=fbcursor.fetchone()
                
                    if exp_tot[0]==None or exp_tot[0]=="":
                        total_exp=0.0
                    else:
                        total_exp=exp_tot[0]

                    prf_lb=Label(canvas, text="PROFIT AND LOSS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=prf_lb, tag=("prf_lb"))

                    canvas.create_line(0, 0, 0, 0,fill="gray", tag=("prf_hr") )
                    
                    try:
                        incomes=float(tot_inc)-float(total_exp)
                    except:
                        incomes=0.0
                
                    try:
                        if float(tot_inc) > float(total_exp):

                            net_prf=Label(canvas, text="NET INCOME: ₹"+str(incomes),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                        else:
                            net_prf=Label(canvas, text="NET LOSS: ₹"+str(incomes),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    except:
                        net_prf=Label(canvas, text="NET INCOME: ₹"+str(incomes),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=net_prf,tag=("net_prf"))

                    figlast = plt.figure(figsize=(8, 4), dpi=50) 


                    x="Income"
                    
                    y=tot_inc
                    plt.barh(x,y, label="Undefined", color="#92a1ae") 
                    plt.legend()
                
                    plt.ylabel("")
                    axes=plt.gca()
                    axes.xaxis.grid()

                    x="Expense"
            
                    try:
                        if exp_tot[0]==None or exp_tot[0]=="":
                            y=0.0
                        else:
                            y=exp_tot[0]
                    except:
                        y=0.0
                    plt.barh(x,y, color="#506579") 
                    plt.legend()
                
                    plt.ylabel("")
                    axes=plt.gca()
                    axes.xaxis.grid()
                    figlast.set_facecolor("#213b52")
                    axes.set_facecolor("#213b52")
                    
                            

                    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
                    canvasbar
                    canvasbar.draw()
                    canvasbar.get_tk_widget()
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph"))
                    # #----------------------------------------------------------------------------------------------------------------grid 2
                    
                    
                    
                    
                    rth2 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash2"),smooth=True,)

                    sql_pro="select sum(balance) from app1_accounts1 where cid_id=%s and acctype='Expenses'"
                    sql_pro_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_pro,sql_pro_val,)
                    exp_tots=fbcursor.fetchone()
                    

                    if exp_tots[0] is None:
                            ttl=0.0
                    else:
                            ttl=exp_tots[0]
                
                    try:
                        exp_hd_lb=Label(canvas, text="EXPENSES: ₹"+str(ttl),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    except:
                        exp_hd_lb=Label(canvas, text="EXPENSES: ₹0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=exp_hd_lb, tag=("exp_hd_lb"))
                    canvas.create_line(0, 0, 0, 0,fill="gray" ,tag=("exp_hr"))
                    fig, ax = plt.subplots(figsize=(8, 4), dpi=50)

                    sql_typ="select balance from app1_accounts1 where cid_id=%s and acctype='Expenses'"
                    sql_typ_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_typ,sql_typ_val,)
                    exp_typ=fbcursor.fetchall()

                    sql_typs="select name from app1_accounts1 where cid_id=%s and acctype='Expenses'"
                    sql_typs_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_typs,sql_typs_val,)
                    exp_typs=fbcursor.fetchall()
                    try:
                        labels = []
                        for i in exp_typs:
                                labels.append(i[0])
                        
                        
                        size = 0.3
                        
                        arr = np.asarray(exp_typ)
                        vals = np.array(arr)
                        
                        
                    
                        cmap = plt.colormaps["tab20c"]
                        outer_colors = cmap(np.arange(3)*4)
                        
                        # inner_colors = cmap([1, 2, 5, 6, 9, 10])

                        ax.pie(vals.sum(axis=1), radius=1,labels=labels, colors=outer_colors,wedgeprops=dict(width=size, edgecolor='w'))

                        ax.set(aspect="equal", title='Cost Of Sales')
                    
                        fig.set_facecolor("#213b52")
                        ax.set_facecolor("#92a1ae")
                        

                        canvasbar = FigureCanvasTkAgg(fig, master=canvas)
                        
                        canvasbar.draw()
                        canvasbar.get_tk_widget()
                        win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_2"))
                    except:
                        size = 0.3
                        
                        vals = np.array([[60.]])
                    
                        cmap = plt.colormaps["tab20c"]
                        outer_colors = cmap(np.arange(3)*4)
                        
                        # inner_colors = cmap([1, 2, 5, 6, 9, 10])

                        ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,wedgeprops=dict(width=size, edgecolor='w'))

                        ax.set(aspect="equal", title='Cost Of Sales')
                    
                        fig.set_facecolor("#213b52")
                        ax.set_facecolor("#92a1ae")
                        

                        canvasbar = FigureCanvasTkAgg(fig, master=canvas)
                        
                        canvasbar.draw()
                        canvasbar.get_tk_widget()
                        win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_2"))

                    # #----------------------------------------------------------------------------------------------------------------grid 3
                    rth3 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash3"),smooth=True,)

                    bnk_lb=Label(canvas, text="BANK ACCOUNTS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=bnk_lb,tag=("bnk_lb"))
                    canvas.create_line(910, 195, 1290, 195,fill="gray",tag=("bank_hr"))
                    sql_pro="select sum(debit), sum(credit) from app1_bankstatement where cid_id=%s"
                    sql_pro_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_pro,sql_pro_val,)
                    bank_stm=fbcursor.fetchone()
                    if bank_stm[0]==None or bank_stm[0]=="":
                        debit=0.0
                    else:
                        debit=bank_stm[0]
                    if bank_stm[1]==None or bank_stm[1]=="":
                        credit=0.0
                    else:
                        credit=bank_stm[1]
                 

                    inv_lb2=Label(canvas, text="DEBIT:₹"+str(debit),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=inv_lb2, tag=("inv_lb4"))
                    inv_lb3=Label(canvas, text="CREDIT:₹"+str(credit),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0,0 , anchor="nw", window=inv_lb3, tag=("inv_lb5"))

                    figlast = plt.figure(figsize=(8, 4), dpi=50) 
                    try:
                        x="Debit"
                        y=debit
                        plt.barh(x,y, label="Undefined", color="#92a1ae") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()

                        x="Credit"
                        y=credit
                        plt.barh(x,y, color="#506579") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()
                        figlast.set_facecolor("#213b52")
                        axes.set_facecolor("#213b52")
                    except:
                        x="Debit"
                        y=0
                        plt.barh(x,y, label="Undefined", color="#92a1ae") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()

                        x="Credit"
                        y=0
                        plt.barh(x,y, color="#506579") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()
                        figlast.set_facecolor("#213b52")
                        axes.set_facecolor("#213b52")

                    
                    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
                    canvasbar
                    canvasbar.draw()
                    canvasbar.get_tk_widget()
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph9"))
                    # #----------------------------------------------------------------------------------------------------------------grid 4
                    rth4 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash4"),smooth=True,)

                    sql_income="select sum(balance) from app1_accounts1 where cid_id=%s and acctype='Income'"
                    sql_income_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_income,sql_pro_val,)
                    incom_dtls=fbcursor.fetchone()

                    if incom_dtls[0]==None or incom_dtls[0]=='':
                        tot_incm=0.0
                    else:
                        tot_incm=incom_dtls[0]

                    incom_lb=Label(canvas, text="INCOME: ₹"+str(tot_incm),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=incom_lb,tag=("incom_lb"))
                    canvas.create_line(0, 0, 0, 0,fill="gray",tag=("incom_hr") )

                    sql_income_chart="select balance,name from app1_accounts1 where cid_id=%s and acctype='Income'"
                    sql_income_chart_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_income_chart,sql_income_chart_val,)
                    incom_chart=fbcursor.fetchall()
                    
                    try:
                        sizes = []
                        for i in incom_chart:
                            sizes.append(i[0])
                    except:
                        sizes=0
                    sql_lb_chart="select name from app1_accounts1 where cid_id=%s and acctype='Income'"
                    sql_lb_chart_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_lb_chart,sql_lb_chart_val,)
                    incom_chart_lb=fbcursor.fetchall()
                    try:
                        labels = []
                        for i in incom_chart_lb:
                            labels.append(i[0])
                    except:
                        pass
                    
                    
                    fig1, ax1 = plt.subplots(figsize=(8, 4), dpi=50)
                    patches, texts, autotexts =ax1.pie(sizes, autopct='%1.1f%%',labels=labels,
                    shadow=True, startangle=90)
                    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                    fig1.set_facecolor("#213b52")
                    ax1.set_facecolor("#92a1ae")
                
                    for text in texts:
                        text.set_color('white')
                    for autotext in autotexts:
                        autotext.set_color('black')

                    canvasbar = FigureCanvasTkAgg(fig1, master=canvas)
                    canvasbar
                    canvasbar.draw()
                    canvasbar.get_tk_widget()
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_4"))

                    # #----------------------------------------------------------------------------------------------------------------grid 5

                    sql_pro="select sum(amtrecvd), sum(baldue),min(invoicedate) from app1_invoice where cid_id=%s"
                    sql_pro_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_pro,sql_pro_val,)
                    exp_totl_inv=fbcursor.fetchone()

                    if exp_totl_inv[0]==None or exp_totl_inv[0]=='':
                        paid=0.0
                    else:
                        paid=exp_totl_inv[0]
                    if exp_totl_inv[1]==None or exp_totl_inv[1]=='':
                        unpaid=0.0
                    else:
                        unpaid=exp_totl_inv[1]

                    rth5 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash5"),smooth=True,)
                    inv_lb=Label(canvas, text="INVOICE",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=inv_lb, tag=("inv_lb"))

                    canvas.create_line(0, 0, 0, 0,fill="gray", tag=("invs_hr") )
                    inv_lb2=Label(canvas, text="UNPAID:₹"+str(unpaid),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=inv_lb2, tag=("inv_lb2"))
                    inv_lb3=Label(canvas, text="PAID:₹"+str(paid),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0,0 , anchor="nw", window=inv_lb3, tag=("inv_lb3"))

                    figlast = plt.figure(figsize=(8, 4), dpi=50)
                    try:
                        x="Unpaid"
                        y=unpaid 
                        plt.barh(x,y, label="Undefined", color="#92a1ae") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()

                        x="Paid"
                        y=paid
                        plt.barh(x,y, color="#506579") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()
                        figlast.set_facecolor("#213b52")
                        axes.set_facecolor("#213b52")
                    except:
                        x="Unpaid"
                        y=0 
                        plt.barh(x,y, label="Undefined", color="#92a1ae") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()

                        x="Paid"
                        y=0
                        plt.barh(x,y, color="#506579") 
                        plt.legend()
                    
                        plt.ylabel("")
                        axes=plt.gca()
                        axes.xaxis.grid()
                        figlast.set_facecolor("#213b52")
                        axes.set_facecolor("#213b52")

                    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
                    canvasbar
                    canvasbar.draw()
                    canvasbar.get_tk_widget()
                    win_inv1 = canvas.create_window(480, 780, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_5"))
                    #----------------------------------------------------------------------------------------------------------------grid 6
                    rth6 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash6"),smooth=True,)
                    

                    canvas.create_line(0, 0, 0, 0,fill="gray", tag=("sales_hr") )
                    
                    if exp_totl_inv[2]==None or exp_totl_inv[2]=='':
                        dates_start=date.today()
                    else:
                        dates_start=exp_totl_inv[2] 
                    

                    sql_pro="select invoicedate from app1_invoice where cid_id=%s"
                    sql_pro_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_pro,sql_pro_val,)
                    sal_totl_inv=fbcursor.fetchall()

                    sql_prof="select sum(grandtotal) from app1_invoice where cid_id=%s "
                    sql_prof_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_prof,sql_prof_val,)
                    sal_totl_invs2=fbcursor.fetchone()
                    

                    if sal_totl_invs2[0]==None or sal_totl_invs2[0]=='':
                        tot_sal=0.0
                    else:
                        tot_sal=sal_totl_invs2[0]

                    
                   

                    sales_lb=Label(canvas, text="SALES ₹"+str(tot_sal),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=sales_lb, tag=("sales_lb"))

                    
                    figlast = plt.figure(figsize=(8, 4), dpi=50)
                    try:
                        x = []
                        y = []
                        for i in sal_totl_inv:
                            x.append(i[0])
                    
                            sql_pros="select sum(grandtotal) from app1_invoice where cid_id=%s and invoicedate=%s "
                            sql_pros_val=(dtl_cmp_pro[0],i[0],)
                            fbcursor.execute(sql_pros,sql_pros_val,)
                            sal_totl_invs=fbcursor.fetchall()
                            
                            y.insert(-1,sal_totl_invs[0])
                        
                        
                        labels = x

                        plt.plot(x, y)
                        # You can specify a rotation for the tick labels in degrees or with keywords.
                        plt.xticks(x, labels, rotation='horizontal')
                        # Pad margins so that markers don't get clipped by the axes
                        plt.margins(0.2)
                        # Tweak spacing to prevent clipping of tick-labels
                        plt.subplots_adjust(bottom=0.15)
                        figlast.set_facecolor("#213b52")
                    
                    except:
                        x = [1,2]
                        y = [0,0]
                        
                        
                        
                        labels = x

                        plt.plot(x, y)
                        # You can specify a rotation for the tick labels in degrees or with keywords.
                        plt.xticks(x, labels, rotation='horizontal')
                        # Pad margins so that markers don't get clipped by the axes
                        plt.margins(0.2)
                        # Tweak spacing to prevent clipping of tick-labels
                        plt.subplots_adjust(bottom=0.15)
                        figlast.set_facecolor("#213b52")
                    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
                    canvasbar
                    canvasbar.draw()
                    canvasbar.get_tk_widget()
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("grapg_6"))
                    
                    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333Banking Section(Tab2)

                    tab_bank = ttk.Notebook(tab2)
                    tab2_1 =  ttk.Frame(tab_bank)
                    tab2_2=  ttk.Frame(tab_bank)
                    tab2_3 = ttk.Frame(tab_bank)

                    tab_bank.add(tab2_1,compound = LEFT, text ='Online Banking')
                    tab_bank.add(tab2_2,compound = LEFT, text ='Offline banking')
                    tab_bank.add(tab2_3,compound = LEFT, text ='Bank Reconvilation')

                    
                    tab_bank.pack(expand = 1, fill ="both")

                    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Sales Tab}
                    tab_sales = ttk.Notebook(tab3)
                    tab3_1 =  ttk.Frame(tab_sales)
                    tab3_2=  ttk.Frame(tab_sales)
                    tab3_3 = ttk.Frame(tab_sales)
                    tab3_4=  ttk.Frame(tab_sales)

                    
                        
                    tab_sales.add(tab3_1,compound = LEFT, text ='Sales Records')
                    tab_sales.add(tab3_2,compound = LEFT, text ='Invoices')
                    tab_sales.add(tab3_3,compound = LEFT, text ='Customers')
                    tab_sales.add(tab3_4,compound = LEFT, text ='Product & Services')
                
                    tab_sales.pack(expand = 1, fill ="both")

                    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Expenses Tab}
                    tab_exp = ttk.Notebook(tab4)
                    tab4_1 =  ttk.Frame(tab_exp)
                    tab4_2=  ttk.Frame(tab_exp)
                    tab_exp.add(tab4_1,compound = LEFT, text ='Expenses')
                    tab_exp.add(tab4_2,compound = LEFT, text ='Supliers')
                    tab_exp.pack(expand = 1, fill ="both")
                    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333{Pay Roll Tab}
                    tab_payroll = ttk.Notebook(tab5)
                    tab5_1 =  ttk.Frame(tab_payroll)
                    tab5_2=  ttk.Frame(tab_payroll)
                    
                    tab_payroll.add(tab5_1,compound = LEFT, text ='Employee')
                    tab_payroll.add(tab5_2,compound = LEFT, text ='Payslip')

                    tab_payroll.pack(expand = 1, fill ="both")

                    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Report Tab}

                    tab_report = ttk.Notebook(tab6)
                    tab6_1 =  ttk.Frame(tab_report)
                    tab6_2=  ttk.Frame(tab_report)
                    tab6_3 = ttk.Frame(tab_report)
                    tab6_4=  ttk.Frame(tab_report)

                    
                        
                    tab_report.add(tab6_1,compound = LEFT, text ='Profit & Loss')
                    tab_report.add(tab6_2,compound = LEFT, text ='Balance Sheet')
                    tab_report.add(tab6_3,compound = LEFT, text ='Accounts Receivables')
                    tab_report.add(tab6_4,compound = LEFT, text ='Accounts Payables')
                
                    tab_report.pack(expand = 1, fill ="both")

                    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Taxes}

                    tab_tax = ttk.Notebook(tab7)
                    tab7_1 =  ttk.Frame(tab_tax)
                    tab7_2=  ttk.Frame(tab_tax)

                    tab_tax.add(tab7_1,compound = LEFT, text ='GST')
                    tab_tax.add(tab7_2,compound = LEFT, text ='New')

                    tab_tax.pack(expand = 1, fill ="both")

                    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Accounting}
                    tab_account = ttk.Notebook(tab8)
                    tab8_1 =  ttk.Frame(tab_account)
                    tab8_2=  ttk.Frame(tab_account)

                    tab_account.add(tab8_1,compound = LEFT, text ='Chart Of Accounts')
                    tab_account.add(tab8_2,compound = LEFT, text ='Reconcile')
                
                
                    tab_account.pack(expand = 1, fill ="both")
                    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Cash Management}
                    tab_cash = ttk.Notebook(tab10)
                    
                    tab10_1 =  ttk.Frame(tab_cash)
                    tab10_2=  ttk.Frame(tab_cash)
                    tab10_3 = ttk.Frame(tab_cash)

                    tab_cash.add(tab10_1,compound = LEFT, text ='Cash Position')
                    tab_cash.add(tab10_2,compound = LEFT, text ='Cash Flow Analyzer')
                    tab_cash.add(tab10_3,compound = LEFT, text ='Check Cash Flow')

                    tab_cash.pack(expand = 1, fill ="both")

                    #`````````````````````````````````````````````````````````````````````````` Work Starting area
                    tab10_1.grid_columnconfigure(0,weight=1)
                    tab10_1.grid_rowconfigure(0,weight=1)


                    fin_cash_position=Frame(tab10_1,bg="#2f516f",)
                    fin_cash_position.grid(row=0,column=0,sticky='nsew')
                    
                    def res_wid_sal(event):
                        dwidth = event.width
                        dheight = event.height
                        dcanvas = event.widget
                        
                        
                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/13
                        y2 = dheight/2.5

                        dcanvas.coords("bg_polygen_sal",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )   
                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/2.2
                        y2 = dheight/.55

                        dcanvas.coords("bg_pol_graph",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )  

                        dcanvas.coords("head_lb_usd",dwidth/25,dheight/6.5)
                        dcanvas.coords("lv_name",dwidth/7.6,dheight/3.3)
                        dcanvas.coords("crcy_cmp",dwidth/1.3,dheight/7)
                        dcanvas.coords("chrt_type",dwidth/1.3,dheight/3.6)
                        dcanvas.coords("graph_sal",dwidth/35,dheight/2.1)
                        
     
                    fin_cash_position.grid_rowconfigure(0,weight=1)
                    fin_cash_position.grid_columnconfigure(0,weight=1)

                    cash_can = Canvas(fin_cash_position,height=700,bg='#2f516f',scrollregion=(0,0,700,1200))
                    sal_Scroll = Scrollbar(fin_cash_position,orient=VERTICAL)
                    sal_Scroll.grid(row=0,column=1,sticky='ns')
                    sal_Scroll.config(command=cash_can.yview)
                    cash_can.bind("<Configure>", res_wid_sal)
                    cash_can.config(yscrollcommand=sal_Scroll.set)
                    cash_can.grid(row=0,column=0,sticky='nsew')

                    #---------------------------------------------------------------------------Header File

                    rth2 = cash_can.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_sal"),smooth=True,)

                    rth2 = cash_can.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_pol_graph"),smooth=True,)

                    sql_sale="select paymdate from app1_payment where cid_id=%s and pmethod='Cash'"
                    sql_sale_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_sale,sql_sale_val,)
                    sales_graph=fbcursor.fetchall()
                    sal_date=[]
                    sal_pymt=[]
                    for i in sales_graph:
                            sal_date.append(i[0])
                    
                            sql_pros="select sum(payment) from app1_payment where cid_id=%s and paymdate=%s and pmethod='Cash'"
                            sql_pros_val=(dtl_cmp_pro[0],i[0],)
                            fbcursor.execute(sql_pros,sql_pros_val,)
                            sal_totl_invs=fbcursor.fetchone()
                            
                            sal_pymt.insert(-1,sal_totl_invs[0])
                   

                    def chart_tp_slt(event):
                        figfirst = plt.figure(figsize=(12, 6), dpi=105)
                        if chrt_tp.get()=="Bar":
                            try:
                                x= sal_date
                                y= sal_pymt
                            
                            except:
                                x=['0']
                                y=[0]
                                
                            plt.bar(x,y, label="Payment Amount", color="gray")
                            

                            plt.legend()
                            plt.xlabel("Total Amount")
                            plt.ylabel("Date")
                            axes=plt.gca()
                            axes.yaxis.grid()

                            figfirst.set_facecolor("#213b52")
                            axes.set_facecolor("#213b52")
                            
                            
                            
                        elif chrt_tp.get()=="Pie":
                            try:
                                labels= sal_date
                                sizes= sal_pymt
                            except:
                                labels=['0']
                                sizes=[100]
                           
                            figfirst, ax1 = plt.subplots(figsize=(12, 6), dpi=105)
                            patches, texts, autotexts =ax1.pie(sizes, autopct='%1.1f%%',labels=labels,
                            shadow=True, startangle=90)
                            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                            figfirst.set_facecolor("#213b52")
                            ax1.set_facecolor("#92a1ae")
                            
                        elif chrt_tp.get()=="Line":
                            
                            try:
                                x= sal_date
                                y= sal_pymt
                            except:
                                x=['0']
                                y=[0]
                            
                            
                            labels = x

                            plt.plot(x, y)
                  
                            plt.xticks(x, labels, rotation='horizontal')
                  
                            plt.margins(0.2)
                       
                            plt.subplots_adjust(bottom=0.15)
                            figfirst.set_facecolor("#213b52")
                          
                        elif chrt_tp.get()=="Doughnut":
                            figfirst, ax = plt.subplots(figsize=(12, 6), dpi=105)

                            size = 0.3
                            
                            
                            
                            size = 0.3
                            try:
                                vals=[]
                                sal_pymts= []
                                labels = sal_date
                                for i in sales_graph:
                                    
                                    sql_pros="select sum(payment) from app1_payment where cid_id=%s and paymdate=%s and pmethod='Cash'"
                                    sql_pros_val=(dtl_cmp_pro[0],i[0],)
                                    fbcursor.execute(sql_pros,sql_pros_val,)
                                    sal_totl_invs=fbcursor.fetchone()
                                    arr = np.asarray(sal_totl_invs)
                                    vals2s = np.array(arr)
                                    sal_pymts.insert(-1,list(vals2s))
                            

                                vals = np.array(sal_pymts)
                            
                            
                                cmap = plt.colormaps["tab20c"]
                                outer_colors = cmap(np.arange(3)*4)
                                
                            

                                ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,labels=labels, wedgeprops=dict(width=size, edgecolor='w'))

                                ax.set(aspect="equal", title='')
                            
                                figfirst.set_facecolor("#213b52")
                                ax.set_facecolor("#92a1ae")
                            except:
                                figfirst.set_facecolor("#213b52")
                                pass
                        elif chrt_tp.get()=="Bubble":
                            try:
                                x= sal_date
                                y= sal_pymt
                               
                                z=[]
                                lj='gray'
                                
                                for i in range(len(y)):
                                    z.insert(-1,lj)
                                
                                
                                    
                                browser_market_share = {
                                'browsers': x,
                                'market_share': y,
                                'color': z
                                }
                            
                               


                                class BubbleChart:
                                    def __init__(self, area, bubble_spacing=0):
                                        """
                                        Setup for bubble collapse.

                                        Parameters
                                        ----------
                                        area : array-like
                                            Area of the bubbles.
                                        bubble_spacing : float, default: 0
                                            Minimal spacing between bubbles after collapsing.

                                        Notes
                                        -----
                                        If "area" is sorted, the results might look weird.
                                        """
                                        area = np.asarray(area)
                                        r = np.sqrt(area / np.pi)

                                        self.bubble_spacing = bubble_spacing
                                        self.bubbles = np.ones((len(area), 4))
                                        self.bubbles[:, 2] = r
                                        self.bubbles[:, 3] = area
                                        self.maxstep = 2 * self.bubbles[:, 2].max() + self.bubble_spacing
                                        self.step_dist = self.maxstep / 2

                                        # calculate initial grid layout for bubbles
                                        length = np.ceil(np.sqrt(len(self.bubbles)))
                                        grid = np.arange(length) * self.maxstep
                                        gx, gy = np.meshgrid(grid, grid)
                                        self.bubbles[:, 0] = gx.flatten()[:len(self.bubbles)]
                                        self.bubbles[:, 1] = gy.flatten()[:len(self.bubbles)]

                                        self.com = self.center_of_mass()

                                    def center_of_mass(self):
                                        return np.average(
                                            self.bubbles[:, :2], axis=0, weights=self.bubbles[:, 3]
                                        )

                                    def center_distance(self, bubble, bubbles):
                                        return np.hypot(bubble[0] - bubbles[:, 0],
                                                        bubble[1] - bubbles[:, 1])

                                    def outline_distance(self, bubble, bubbles):
                                        center_distance = self.center_distance(bubble, bubbles)
                                        return center_distance - bubble[2] - \
                                            bubbles[:, 2] - self.bubble_spacing

                                    def check_collisions(self, bubble, bubbles):
                                        distance = self.outline_distance(bubble, bubbles)
                                        return len(distance[distance < 0])

                                    def collides_with(self, bubble, bubbles):
                                        distance = self.outline_distance(bubble, bubbles)
                                        idx_min = np.argmin(distance)
                                        return idx_min if type(idx_min) == np.ndarray else [idx_min]

                                    def collapse(self, n_iterations=50):
                                        """
                                        Move bubbles to the center of mass.

                                        Parameters
                                        ----------
                                        n_iterations : int, default: 50
                                            Number of moves to perform.
                                        """
                                        for _i in range(n_iterations):
                                            moves = 0
                                            for i in range(len(self.bubbles)):
                                                rest_bub = np.delete(self.bubbles, i, 0)
                                                # try to move directly towards the center of mass
                                                # direction vector from bubble to the center of mass
                                                dir_vec = self.com - self.bubbles[i, :2]

                                                # shorten direction vector to have length of 1
                                                dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))

                                                # calculate new bubble position
                                                new_point = self.bubbles[i, :2] + dir_vec * self.step_dist
                                                new_bubble = np.append(new_point, self.bubbles[i, 2:4])

                                                # check whether new bubble collides with other bubbles
                                                if not self.check_collisions(new_bubble, rest_bub):
                                                    self.bubbles[i, :] = new_bubble
                                                    self.com = self.center_of_mass()
                                                    moves += 1
                                                else:
                                                    # try to move around a bubble that you collide with
                                                    # find colliding bubble
                                                    for colliding in self.collides_with(new_bubble, rest_bub):
                                                        # calculate direction vector
                                                        dir_vec = rest_bub[colliding, :2] - self.bubbles[i, :2]
                                                        dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))
                                                        # calculate orthogonal vector
                                                        orth = np.array([dir_vec[1], -dir_vec[0]])
                                                        # test which direction to go
                                                        new_point1 = (self.bubbles[i, :2] + orth *
                                                                    self.step_dist)
                                                        new_point2 = (self.bubbles[i, :2] - orth *
                                                                    self.step_dist)
                                                        dist1 = self.center_distance(
                                                            self.com, np.array([new_point1]))
                                                        dist2 = self.center_distance(
                                                            self.com, np.array([new_point2]))
                                                        new_point = new_point1 if dist1 < dist2 else new_point2
                                                        new_bubble = np.append(new_point, self.bubbles[i, 2:4])
                                                        if not self.check_collisions(new_bubble, rest_bub):
                                                            self.bubbles[i, :] = new_bubble
                                                            self.com = self.center_of_mass()

                                            if moves / len(self.bubbles) < 0.1:
                                                self.step_dist = self.step_dist / 2

                                    def plot(self, ax, labels, colors):
                                        """
                                        Draw the bubble plot.

                                        Parameters
                                        ----------
                                        ax : matplotlib.axes.Axes
                                        labels : list
                                            Labels of the bubbles.
                                        colors : list
                                            Colors of the bubbles.
                                        """
                                        for i in range(len(self.bubbles)):
                                            circ = plt.Circle(
                                                self.bubbles[i, :2], self.bubbles[i, 2], color=colors[i])
                                            ax.add_patch(circ)
                                            ax.text(*self.bubbles[i, :2], labels[i],
                                                    horizontalalignment='center', verticalalignment='center')


                                bubble_chart = BubbleChart(area=browser_market_share['market_share'],
                                                        bubble_spacing=0.1)

                                bubble_chart.collapse()

                                figfirst, ax = plt.subplots(subplot_kw=dict(aspect="equal"),figsize=(12, 6), dpi=105)
                                bubble_chart.plot(
                                    ax, browser_market_share['browsers'], browser_market_share['color'])
                                ax.axis("off")
                                ax.relim()
                                ax.autoscale_view()
                                ax.set_title('')
                                figfirst.set_facecolor("#213b52")
                                ax.set_facecolor("#92a1ae")
                            except:
                                figfirst.set_facecolor("#213b52")
                                pass
                        can_sals2= FigureCanvasTkAgg(figfirst, master=cash_can)
                        can_sals2.draw()
                        can_sals2.get_tk_widget()
                            
                        win_inv1 = cash_can.create_window(40, 300, anchor="nw", window=can_sals2.get_tk_widget(), tag=("graph_sals"))

                    def crcy_typ(event):
                        c = CurrencyRates()
                        dt = datetime.today()
                    
                        if crcy_tps.get()=="$ USD":
                            valu_cr=c.get_rate( 'INR','USD', dt)
                            cmp_name.config(text="Today: $"+str(valu_cr)+" USD")
                            
                            pass
                        elif crcy_tps.get()=="₹ INR":
                            valu_cr=c.get_rate( 'INR','INR', dt)
                            cmp_name.config(text="Today: ₹"+str(valu_cr)+" INR")
                        
                            pass
                        
                        elif crcy_tps.get()=="€ EUR":
                            valu_cr=c.get_rate( 'INR','EUR', dt)
                            cmp_name.config(text="Today: €"+str(valu_cr)+" EUR")
                            
                            pass
                        else:
                            pass
                    cj = CurrencyRates()
                    dts = datetime.today()
                    val_cry=cj.get_rate( 'INR','USD', dts)
                    cmp_name=Label(cash_can, text="Today: $ "+str(val_cry)+" USD",bg="#213b52",justify=LEFT, fg="White", anchor="center",font=('Calibri 24 bold'))
                    win_inv1 = cash_can.create_window(0, 0, anchor="nw", window=cmp_name,tag=("head_lb_usd"))

                    lv_name=Label(cash_can, text="CASH POSITIOND",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
                    win_inv1 = cash_can.create_window(0, 0, anchor="center", window=lv_name,tag=("lv_name"))

                    crcy_tps= StringVar()
                    crcy_cmp = ttk.Combobox(cash_can,textvariable=crcy_tps,width=15,font=('Calibri 16'))
                    crcy_cmp['values'] = ('$ USD', '₹ INR','€ EUR')
                    crcy_cmp.bind('<<ComboboxSelected>>', crcy_typ)
                    crcy_cmp.current(0)
                    win_inv1 = cash_can.create_window(0, 0, anchor="nw", window=crcy_cmp, tag=("crcy_cmp"))

                    chrt_tp= StringVar()
                    chrt_type = ttk.Combobox(cash_can,textvariable=chrt_tp,width=15,font=('Calibri 16'))
                    
                    chrt_type['values'] = ('Bar','Pie', 'Line', 'Doughnut','Bubble')
                    chrt_type.bind('<<ComboboxSelected>>', chart_tp_slt)
                    chrt_type.current(0)
                
                    win_inv1 = cash_can.create_window(0, 0, anchor="nw", window=chrt_type, tag=("chrt_type"))

                    #----------------------------------------------------------------------graph section
                    try:
                        x= sal_date
                        y= sal_pymt
                    except:
                        x='0'
                        y=0
                    
                    
                    figfirst = plt.figure(figsize=(12, 6), dpi=105)
                    plt.bar(x,y, label="Payment Amount", color="gray")
                    plt.legend()
                    plt.xlabel("Date")
                    plt.ylabel("Payment Amount")
                    axes=plt.gca()
                    axes.yaxis.grid()

                    
                    figfirst.set_facecolor("#213b52")
                    axes.set_facecolor("#213b52")
                    
                    
                    can_sals= FigureCanvasTkAgg(figfirst, master=cash_can)
                    can_sals.draw()
                    can_sals.get_tk_widget()

                    win_inv1 = cash_can.create_window(0, 0, anchor="nw", window=can_sals.get_tk_widget(), tag=("graph_sal"))
                            
                    #****************************************************************************Cash Flow Analizer
                    tab10_2.grid_columnconfigure(0,weight=1)
                    tab10_2.grid_rowconfigure(0,weight=1)


                    fin_cash_analiz=Frame(tab10_2,bg="#2f516f",)
                    fin_cash_analiz.grid(row=0,column=0,sticky='nsew')
                    
                    def res_wid_anal(event):
                        dwidth = event.width
                        dheight = event.height
                        dcanvas = event.widget
                        
                        
                        
                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/13
                        y2 = dheight/4

                        dcanvas.coords("bg_polygen_anal",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )   

                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/3.5
                        y2 = dheight/1.8

                        dcanvas.coords("bg_polygen_anal2",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )   
                        
                        
                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/1.68
                        y2 = dheight/.22


                        dcanvas.coords("bg_polygen_anal3",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )  
                        dcanvas.coords("ptree1",dwidth/33,dheight/1.55)
                        dcanvas.coords("head_lb_usd",dwidth/25,dheight/6.5)
                        dcanvas.coords("lv_name",dwidth/7.6,dheight/3.3)
                        dcanvas.coords("lb_hdd",dwidth/2,dheight/7)
                        dcanvas.coords("anal_hr",dwidth/40,dheight/5.5,dwidth/1.03,dheight/5.5)
                        
                        
                        dcanvas.coords("cmb_lb",dwidth/12,dheight/3)
                        dcanvas.coords("cmb_bx",dwidth/25,dheight/2.8)
                        dcanvas.coords("button15",dwidth/1.5,dheight/2.2)
                        
                        dcanvas.coords("button25",dwidth/1.25,dheight/2.2)
                        
                        #table section
                        dcanvas.coords("r1x1",dwidth/6.8,dheight/1.50)
                        dcanvas.coords("r1c2",dwidth/3.1,dheight/1.50)
                        dcanvas.coords("r1c3",dwidth/2.4,dheight/1.50)
                        dcanvas.coords("r1c4",dwidth/1.955,dheight/1.50)
                        dcanvas.coords("r1c5",dwidth/1.65,dheight/1.50)
                        dcanvas.coords("r1c6",dwidth/1.425,dheight/1.50)
                        dcanvas.coords("r1c7",dwidth/1.255,dheight/1.50)
                        dcanvas.coords("r1c8",dwidth/1.1,dheight/1.50)

                        #---------------------------------second row

                        dcanvas.coords("r2c1",dwidth/6.8,dheight/1.38)
                        dcanvas.coords("r2c2",dwidth/3.6,dheight/1.42)
                        dcanvas.coords("r2c3",dwidth/2.688,dheight/1.42)
                        dcanvas.coords("r2c4",dwidth/2.15,dheight/1.42)
                        dcanvas.coords("r2c5",dwidth/1.785,dheight/1.42)
                        dcanvas.coords("r2c6",dwidth/1.18,dheight/1.42)
                        dcanvas.coords("r2c7",dwidth/1.525,dheight/1.42)
                        dcanvas.coords("r2c8",dwidth/1.329,dheight/1.42)

                        
                        #---------------------------------3rd row
                        dcanvas.coords("r3c1",dwidth/2.01,dheight/1.28)


                        #---------------------------------4th row
                        dcanvas.coords("r4c1",dwidth/6.8,dheight/1.2)

                        dcanvas.coords("r4c2",dwidth/3.6,dheight/1.227)
                        dcanvas.coords("r4c3",dwidth/2.688,dheight/1.227)
                        dcanvas.coords("r4c4",dwidth/2.15,dheight/1.227)
                        dcanvas.coords("r4c5",dwidth/1.785,dheight/1.227)
                        dcanvas.coords("r4c6",dwidth/1.525,dheight/1.227)
                        dcanvas.coords("r4c7",dwidth/1.329,dheight/1.227)
                        dcanvas.coords("r4c8",dwidth/1.18,dheight/1.227)

                        #---------------------------------5th row
                        dcanvas.coords("r5c1",dwidth/6.8,dheight/1.126)

                        dcanvas.coords("r5c2",dwidth/3.6,dheight/1.153)
                        dcanvas.coords("r5c3",dwidth/2.688,dheight/1.153)
                        dcanvas.coords("r5c4",dwidth/2.15,dheight/1.153)
                        dcanvas.coords("r5c5",dwidth/1.785,dheight/1.153)
                        dcanvas.coords("r5c6",dwidth/1.525,dheight/1.153)
                        dcanvas.coords("r5c7",dwidth/1.329,dheight/1.153)
                        dcanvas.coords("r5c8",dwidth/1.18,dheight/1.153)

                        #---------------------------------6th row
                        dcanvas.coords("r6c1",dwidth/6.8,dheight/1.06)

                        dcanvas.coords("r6c2",dwidth/3.6,dheight/1.083)
                        dcanvas.coords("r6c3",dwidth/2.688,dheight/1.083)
                        dcanvas.coords("r6c4",dwidth/2.15,dheight/1.083)
                        dcanvas.coords("r6c5",dwidth/1.785,dheight/1.083)
                        dcanvas.coords("r6c6",dwidth/1.525,dheight/1.083)
                        dcanvas.coords("r6c7",dwidth/1.329,dheight/1.083)
                        dcanvas.coords("r6c8",dwidth/1.18,dheight/1.083)

                        #---------------------------------7th row
                        dcanvas.coords("r7c1",dwidth/6.8,dheight/1.005)

                        dcanvas.coords("r7c2",dwidth/3.6,dheight/1.025)
                        dcanvas.coords("r7c3",dwidth/2.688,dheight/1.025)
                        dcanvas.coords("r7c4",dwidth/2.15,dheight/1.025)
                        dcanvas.coords("r7c5",dwidth/1.785,dheight/1.025)
                        dcanvas.coords("r7c6",dwidth/1.525,dheight/1.025)
                        dcanvas.coords("r7c7",dwidth/1.329,dheight/1.025)
                        dcanvas.coords("r7c8",dwidth/1.18,dheight/1.025)

                        #---------------------------------8th row
                        dcanvas.coords("r8c1",dwidth/6.8,dheight/.955)

                        dcanvas.coords("r8c2",dwidth/3.6,dheight/.973)
                        dcanvas.coords("r8c3",dwidth/2.688,dheight/.973)
                        dcanvas.coords("r8c4",dwidth/2.15,dheight/.973)
                        dcanvas.coords("r8c5",dwidth/1.785,dheight/.973)
                        dcanvas.coords("r8c6",dwidth/1.525,dheight/.973)
                        dcanvas.coords("r8c7",dwidth/1.329,dheight/.973)
                        dcanvas.coords("r8c8",dwidth/1.18,dheight/.973)

                        #---------------------------------9th row
                        dcanvas.coords("r9c1",dwidth/6.8,dheight/.909)

                        dcanvas.coords("r9c2",dwidth/3.6,dheight/.925)
                        dcanvas.coords("r9c3",dwidth/2.688,dheight/.925)
                        dcanvas.coords("r9c4",dwidth/2.15,dheight/.925)
                        dcanvas.coords("r9c5",dwidth/1.785,dheight/.925)
                        dcanvas.coords("r9c6",dwidth/1.525,dheight/.925)
                        dcanvas.coords("r9c7",dwidth/1.329,dheight/.925)
                        dcanvas.coords("r9c8",dwidth/1.18,dheight/.925)

                        #---------------------------------10th row
                        dcanvas.coords("r10c1",dwidth/6.8,dheight/.866)

                        dcanvas.coords("r10c2",dwidth/3.6,dheight/.881)
                        dcanvas.coords("r10c3",dwidth/2.688,dheight/.881)
                        dcanvas.coords("r10c4",dwidth/2.15,dheight/.881)
                        dcanvas.coords("r10c5",dwidth/1.785,dheight/.881)
                        dcanvas.coords("r10c6",dwidth/1.525,dheight/.881)
                        dcanvas.coords("r10c7",dwidth/1.329,dheight/.881)
                        dcanvas.coords("r10c8",dwidth/1.18,dheight/.881)

                        #---------------------------------11th row
                        dcanvas.coords("r11c1",dwidth/6.8,dheight/.828)

                        dcanvas.coords("r11c2",dwidth/3.6,dheight/.841)
                        dcanvas.coords("r11c3",dwidth/2.688,dheight/.841)
                        dcanvas.coords("r11c4",dwidth/2.15,dheight/.841)
                        dcanvas.coords("r11c5",dwidth/1.785,dheight/.841)
                        dcanvas.coords("r11c6",dwidth/1.525,dheight/.841)
                        dcanvas.coords("r11c7",dwidth/1.329,dheight/.841)
                        dcanvas.coords("r11c8",dwidth/1.18,dheight/.841)

                        #---------------------------------12th row
                        dcanvas.coords("r12c1",dwidth/6.8,dheight/.793)

                        dcanvas.coords("r12c2",dwidth/3.6,dheight/.805)
                        dcanvas.coords("r12c3",dwidth/2.688,dheight/.805)
                        dcanvas.coords("r12c4",dwidth/2.15,dheight/.805)
                        dcanvas.coords("r12c5",dwidth/1.785,dheight/.805)
                        dcanvas.coords("r12c6",dwidth/1.525,dheight/.805)
                        dcanvas.coords("r12c7",dwidth/1.329,dheight/.805)
                        dcanvas.coords("r12c8",dwidth/1.18,dheight/.805)

                        #---------------------------------13th row
                        dcanvas.coords("r13c1",dwidth/6.8,dheight/.760)

                        dcanvas.coords("r13c2",dwidth/3.6,dheight/.772)
                        dcanvas.coords("r13c3",dwidth/2.688,dheight/.772)
                        dcanvas.coords("r13c4",dwidth/2.15,dheight/.772)
                        dcanvas.coords("r13c5",dwidth/1.785,dheight/.772)
                        dcanvas.coords("r13c6",dwidth/1.525,dheight/.772)
                        dcanvas.coords("r13c7",dwidth/1.329,dheight/.772)
                        dcanvas.coords("r13c8",dwidth/1.18,dheight/.772)
                        #---------------------------------14th row
                        dcanvas.coords("r14c1",dwidth/6.8,dheight/.730)

                        dcanvas.coords("r14c2",dwidth/3.6,dheight/.741)
                        dcanvas.coords("r14c3",dwidth/2.688,dheight/.741)
                        dcanvas.coords("r14c4",dwidth/2.15,dheight/.741)
                        dcanvas.coords("r14c5",dwidth/1.785,dheight/.741)
                        dcanvas.coords("r14c6",dwidth/1.525,dheight/.741)
                        dcanvas.coords("r14c7",dwidth/1.329,dheight/.741)
                        dcanvas.coords("r14c8",dwidth/1.18,dheight/.741)

                        #---------------------------------15th row
                        dcanvas.coords("r15c1",dwidth/6.8,dheight/.703)

                        dcanvas.coords("r15c2",dwidth/3.6,dheight/.713)
                        dcanvas.coords("r15c3",dwidth/2.688,dheight/.713)
                        dcanvas.coords("r15c4",dwidth/2.15,dheight/.713)
                        dcanvas.coords("r15c5",dwidth/1.785,dheight/.713)
                        dcanvas.coords("r15c6",dwidth/1.525,dheight/.713)
                        dcanvas.coords("r15c7",dwidth/1.329,dheight/.713) 
                        dcanvas.coords("r15c8",dwidth/1.18,dheight/.713)

                        #---------------------------------16th row
                        dcanvas.coords("r16c1",dwidth/2.01,dheight/.677)


                        #---------------------------------17th row
                        dcanvas.coords("r17c1",dwidth/6.8,dheight/.654)

                        dcanvas.coords("r17c2",dwidth/3.6,dheight/.663)
                        dcanvas.coords("r17c3",dwidth/2.688,dheight/.663)
                        dcanvas.coords("r17c4",dwidth/2.15,dheight/.663)
                        dcanvas.coords("r17c5",dwidth/1.785,dheight/.663)
                        dcanvas.coords("r17c6",dwidth/1.525,dheight/.663)
                        dcanvas.coords("r17c7",dwidth/1.329,dheight/.663) 
                        dcanvas.coords("r17c8",dwidth/1.18,dheight/.663)

                        #---------------------------------18th row
                        dcanvas.coords("r18c1",dwidth/6.8,dheight/.633)

                        dcanvas.coords("r18c2",dwidth/3.6,dheight/.640)
                        dcanvas.coords("r18c3",dwidth/2.688,dheight/.640)
                        dcanvas.coords("r18c4",dwidth/2.15,dheight/.640)
                        dcanvas.coords("r18c5",dwidth/1.785,dheight/.640)
                        dcanvas.coords("r18c6",dwidth/1.525,dheight/.640)
                        dcanvas.coords("r18c7",dwidth/1.329,dheight/.640) 
                        dcanvas.coords("r18c8",dwidth/1.18,dheight/.640)

                        #---------------------------------19th row
                        dcanvas.coords("r19c1",dwidth/6.8,dheight/.6115)

                        dcanvas.coords("r19c2",dwidth/3.6,dheight/.619)
                        dcanvas.coords("r19c3",dwidth/2.688,dheight/.619)
                        dcanvas.coords("r19c4",dwidth/2.15,dheight/.619)
                        dcanvas.coords("r19c5",dwidth/1.785,dheight/.619)
                        dcanvas.coords("r19c6",dwidth/1.525,dheight/.619)
                        dcanvas.coords("r19c7",dwidth/1.329,dheight/.619) 
                        dcanvas.coords("r19c8",dwidth/1.18,dheight/.619)

                        #---------------------------------20th row
                        dcanvas.coords("r20c1",dwidth/6.8,dheight/.592)

                        dcanvas.coords("r20c2",dwidth/3.6,dheight/.599)
                        dcanvas.coords("r20c3",dwidth/2.688,dheight/.599)
                        dcanvas.coords("r20c4",dwidth/2.15,dheight/.599)
                        dcanvas.coords("r20c5",dwidth/1.785,dheight/.599)
                        dcanvas.coords("r20c6",dwidth/1.525,dheight/.599)
                        dcanvas.coords("r20c7",dwidth/1.329,dheight/.599) 
                        dcanvas.coords("r20c8",dwidth/1.18,dheight/.599)

                        #---------------------------------21th row
                        dcanvas.coords("r21c1",dwidth/6.8,dheight/.574)

                        dcanvas.coords("r21c2",dwidth/3.6,dheight/.581)
                        dcanvas.coords("r21c3",dwidth/2.688,dheight/.581)
                        dcanvas.coords("r21c4",dwidth/2.15,dheight/.581)
                        dcanvas.coords("r21c5",dwidth/1.785,dheight/.581)
                        dcanvas.coords("r21c6",dwidth/1.525,dheight/.581)
                        dcanvas.coords("r21c7",dwidth/1.329,dheight/.581) 
                        dcanvas.coords("r21c8",dwidth/1.18,dheight/.581)

                        #---------------------------------22th row
                        dcanvas.coords("r22c1",dwidth/6.8,dheight/.558)

                        dcanvas.coords("r22c2",dwidth/3.6,dheight/.564)
                        dcanvas.coords("r22c3",dwidth/2.688,dheight/.564)
                        dcanvas.coords("r22c4",dwidth/2.15,dheight/.564)
                        dcanvas.coords("r22c5",dwidth/1.785,dheight/.564)
                        dcanvas.coords("r22c6",dwidth/1.525,dheight/.564)
                        dcanvas.coords("r22c7",dwidth/1.329,dheight/.564) 
                        dcanvas.coords("r22c8",dwidth/1.18,dheight/.564)

                        #---------------------------------23th row
                        dcanvas.coords("r23c1",dwidth/6.8,dheight/.543)

                        dcanvas.coords("r23c2",dwidth/3.6,dheight/.549)
                        dcanvas.coords("r23c3",dwidth/2.688,dheight/.549)
                        dcanvas.coords("r23c4",dwidth/2.15,dheight/.549)
                        dcanvas.coords("r23c5",dwidth/1.785,dheight/.549)
                        dcanvas.coords("r23c6",dwidth/1.525,dheight/.549)
                        dcanvas.coords("r23c7",dwidth/1.329,dheight/.549) 
                        dcanvas.coords("r23c8",dwidth/1.18,dheight/.549)

                        #---------------------------------24th row
                        dcanvas.coords("r24c1",dwidth/6.8,dheight/.528)

                        dcanvas.coords("r24c2",dwidth/3.6,dheight/.534)
                        dcanvas.coords("r24c3",dwidth/2.688,dheight/.534)
                        dcanvas.coords("r24c4",dwidth/2.15,dheight/.534)
                        dcanvas.coords("r24c5",dwidth/1.785,dheight/.534)
                        dcanvas.coords("r24c6",dwidth/1.525,dheight/.534)
                        dcanvas.coords("r24c7",dwidth/1.329,dheight/.534) 
                        dcanvas.coords("r24c8",dwidth/1.18,dheight/.534)

                        #---------------------------------25th row
                        dcanvas.coords("r25c1",dwidth/2.01,dheight/.514)


                        #---------------------------------26th row
                        dcanvas.coords("r26c1",dwidth/6.8,dheight/.501)
                        dcanvas.coords("r26c2",dwidth/3.6,dheight/.506)
                        dcanvas.coords("r26c3",dwidth/2.688,dheight/.506)
                        dcanvas.coords("r26c4",dwidth/2.15,dheight/.506)
                        dcanvas.coords("r26c5",dwidth/1.785,dheight/.506)
                        dcanvas.coords("r26c6",dwidth/1.525,dheight/.506)
                        dcanvas.coords("r26c7",dwidth/1.329,dheight/.506) 
                        dcanvas.coords("r26c8",dwidth/1.18,dheight/.506)

                        #---------------------------------27th row
                        dcanvas.coords("r27c1",dwidth/6.8,dheight/.488)

                        dcanvas.coords("r27c2",dwidth/3.6,dheight/.493)
                        dcanvas.coords("r27c3",dwidth/2.688,dheight/.493)
                        dcanvas.coords("r27c4",dwidth/2.15,dheight/.493)
                        dcanvas.coords("r27c5",dwidth/1.785,dheight/.493)
                        dcanvas.coords("r27c6",dwidth/1.525,dheight/.493)
                        dcanvas.coords("r27c7",dwidth/1.329,dheight/.493) 
                        dcanvas.coords("r27c8",dwidth/1.18,dheight/.493)
                        #---------------------------------28th row
                        dcanvas.coords("r28c1",dwidth/6.8,dheight/.476)

                        dcanvas.coords("r28c2",dwidth/3.6,dheight/.4805)
                        dcanvas.coords("r28c3",dwidth/2.688,dheight/.4805)
                        dcanvas.coords("r28c4",dwidth/2.15,dheight/.4805)
                        dcanvas.coords("r28c5",dwidth/1.785,dheight/.4805)
                        dcanvas.coords("r28c6",dwidth/1.525,dheight/.4805)
                        dcanvas.coords("r28c7",dwidth/1.329,dheight/.4805) 
                        dcanvas.coords("r28c8",dwidth/1.18,dheight/.4805)

                        #---------------------------------29th row
                        dcanvas.coords("r29c1",dwidth/6.8,dheight/.465)

                        dcanvas.coords("r29c2",dwidth/3.6,dheight/.469)
                        dcanvas.coords("r29c3",dwidth/2.688,dheight/.469)
                        dcanvas.coords("r29c4",dwidth/2.15,dheight/.469)
                        dcanvas.coords("r29c5",dwidth/1.785,dheight/.469)
                        dcanvas.coords("r29c6",dwidth/1.525,dheight/.469)
                        dcanvas.coords("r29c7",dwidth/1.329,dheight/.469) 
                        dcanvas.coords("r29c8",dwidth/1.18,dheight/.469)

                        #---------------------------------30th row
                        dcanvas.coords("r30c1",dwidth/6.8,dheight/.454)

                        dcanvas.coords("r30c2",dwidth/3.6,dheight/.458)
                        dcanvas.coords("r30c3",dwidth/2.688,dheight/.458)
                        dcanvas.coords("r30c4",dwidth/2.15,dheight/.458)
                        dcanvas.coords("r30c5",dwidth/1.785,dheight/.458)
                        dcanvas.coords("r30c6",dwidth/1.525,dheight/.458)
                        dcanvas.coords("r30c7",dwidth/1.329,dheight/.458) 
                        dcanvas.coords("r30c8",dwidth/1.18,dheight/.458)

                        #---------------------------------31th row
                        dcanvas.coords("r31c1",dwidth/6.8,dheight/.443)

                        dcanvas.coords("r31c2",dwidth/3.6,dheight/.447)
                        dcanvas.coords("r31c3",dwidth/2.688,dheight/.447)
                        dcanvas.coords("r31c4",dwidth/2.15,dheight/.447)
                        dcanvas.coords("r31c5",dwidth/1.785,dheight/.447)
                        dcanvas.coords("r31c6",dwidth/1.525,dheight/.447)
                        dcanvas.coords("r31c7",dwidth/1.329,dheight/.447) 
                        dcanvas.coords("r31c8",dwidth/1.18,dheight/.447)

                        #---------------------------------32th row
                        dcanvas.coords("r32c1",dwidth/6.8,dheight/.433)

                        dcanvas.coords("r32c2",dwidth/3.6,dheight/.437)
                        dcanvas.coords("r32c3",dwidth/2.688,dheight/.437)
                        dcanvas.coords("r32c4",dwidth/2.15,dheight/.437)
                        dcanvas.coords("r32c5",dwidth/1.785,dheight/.437)
                        dcanvas.coords("r32c6",dwidth/1.525,dheight/.437)
                        dcanvas.coords("r32c7",dwidth/1.329,dheight/.437) 
                        dcanvas.coords("r32c8",dwidth/1.18,dheight/.437)

                        #---------------------------------33th row
                        dcanvas.coords("r33c1",dwidth/6.8,dheight/.424)

                        dcanvas.coords("r33c2",dwidth/3.6,dheight/.428)
                        dcanvas.coords("r33c3",dwidth/2.688,dheight/.428)
                        dcanvas.coords("r33c4",dwidth/2.15,dheight/.428)
                        dcanvas.coords("r33c5",dwidth/1.785,dheight/.428)
                        dcanvas.coords("r33c6",dwidth/1.525,dheight/.428)
                        dcanvas.coords("r33c7",dwidth/1.329,dheight/.428) 
                        dcanvas.coords("r33c8",dwidth/1.18,dheight/.428)

                        #---------------------------------34th row
                        dcanvas.coords("r34c1",dwidth/6.8,dheight/.415)

                        dcanvas.coords("r34c2",dwidth/3.6,dheight/.4185)
                        dcanvas.coords("r34c3",dwidth/2.688,dheight/.4185)
                        dcanvas.coords("r34c4",dwidth/2.15,dheight/.4185)
                        dcanvas.coords("r34c5",dwidth/1.785,dheight/.4185)
                        dcanvas.coords("r34c6",dwidth/1.525,dheight/.4185)
                        dcanvas.coords("r34c7",dwidth/1.329,dheight/.4185) 
                        dcanvas.coords("r34c8",dwidth/1.18,dheight/.4185)

                        #---------------------------------35th row
                        dcanvas.coords("r35c1",dwidth/6.8,dheight/.406)

                        dcanvas.coords("r35c2",dwidth/3.6,dheight/.4095)
                        dcanvas.coords("r35c3",dwidth/2.688,dheight/.4095)
                        dcanvas.coords("r35c4",dwidth/2.15,dheight/.4095)
                        dcanvas.coords("r35c5",dwidth/1.785,dheight/.4095)
                        dcanvas.coords("r35c6",dwidth/1.525,dheight/.4095)
                        dcanvas.coords("r35c7",dwidth/1.329,dheight/.4095) 
                        dcanvas.coords("r35c8",dwidth/1.18,dheight/.4095)
                        #---------------------------------36th row
                        dcanvas.coords("r36c1",dwidth/6.8,dheight/.3975)

                        dcanvas.coords("r36c2",dwidth/3.6,dheight/.401)
                        dcanvas.coords("r36c3",dwidth/2.688,dheight/.401)
                        dcanvas.coords("r36c4",dwidth/2.15,dheight/.401)
                        dcanvas.coords("r36c5",dwidth/1.785,dheight/.401)
                        dcanvas.coords("r36c6",dwidth/1.525,dheight/.401)
                        dcanvas.coords("r36c7",dwidth/1.329,dheight/.401) 
                        dcanvas.coords("r36c8",dwidth/1.18,dheight/.401)

                        #---------------------------------37th row
                        dcanvas.coords("r37c1",dwidth/6.8,dheight/.3895)

                        dcanvas.coords("r37c2",dwidth/3.6,dheight/.3925)
                        dcanvas.coords("r37c3",dwidth/2.688,dheight/.3925)
                        dcanvas.coords("r37c4",dwidth/2.15,dheight/.3925)
                        dcanvas.coords("r37c5",dwidth/1.785,dheight/.3925)
                        dcanvas.coords("r37c6",dwidth/1.525,dheight/.3925)
                        dcanvas.coords("r37c7",dwidth/1.329,dheight/.3925) 
                        dcanvas.coords("r37c8",dwidth/1.18,dheight/.3925)

                        #---------------------------------38th row
                        dcanvas.coords("r38c1",dwidth/6.8,dheight/.3818)

                        dcanvas.coords("r38c2",dwidth/3.6,dheight/.3848)
                        dcanvas.coords("r38c3",dwidth/2.688,dheight/.3848)
                        dcanvas.coords("r38c4",dwidth/2.15,dheight/.3848)
                        dcanvas.coords("r38c5",dwidth/1.785,dheight/.3848)
                        dcanvas.coords("r38c6",dwidth/1.525,dheight/.3848)
                        dcanvas.coords("r38c7",dwidth/1.329,dheight/.3848) 
                        dcanvas.coords("r38c8",dwidth/1.18,dheight/.3848)

                        #---------------------------------39th row
                        dcanvas.coords("r39c1",dwidth/6.8,dheight/.374)

                        dcanvas.coords("r39c2",dwidth/3.6,dheight/.377)
                        dcanvas.coords("r39c3",dwidth/2.688,dheight/.377)
                        dcanvas.coords("r39c4",dwidth/2.15,dheight/.377)
                        dcanvas.coords("r39c5",dwidth/1.785,dheight/.377)
                        dcanvas.coords("r39c6",dwidth/1.525,dheight/.377)
                        dcanvas.coords("r39c7",dwidth/1.329,dheight/.377) 
                        dcanvas.coords("r39c8",dwidth/1.18,dheight/.377)

                        #---------------------------------40th row
                        dcanvas.coords("r40c1",dwidth/6.8,dheight/.367)

                        dcanvas.coords("r40c2",dwidth/3.6,dheight/.370)
                        dcanvas.coords("r40c3",dwidth/2.688,dheight/.370)
                        dcanvas.coords("r40c4",dwidth/2.15,dheight/.370)
                        dcanvas.coords("r40c5",dwidth/1.785,dheight/.370)
                        dcanvas.coords("r40c6",dwidth/1.525,dheight/.370)
                        dcanvas.coords("r40c7",dwidth/1.329,dheight/.370) 
                        dcanvas.coords("r40c8",dwidth/1.18,dheight/.370)

                        #---------------------------------41th row
                        dcanvas.coords("r41c1",dwidth/6.8,dheight/.360)

                        dcanvas.coords("r41c2",dwidth/3.6,dheight/.3628)
                        dcanvas.coords("r41c3",dwidth/2.688,dheight/.3628)
                        dcanvas.coords("r41c4",dwidth/2.15,dheight/.3628)
                        dcanvas.coords("r41c5",dwidth/1.785,dheight/.3628)
                        dcanvas.coords("r41c6",dwidth/1.525,dheight/.3628)
                        dcanvas.coords("r41c7",dwidth/1.329,dheight/.3628) 
                        dcanvas.coords("r41c8",dwidth/1.18,dheight/.3628)

                        #---------------------------------42th row
                        dcanvas.coords("r42c1",dwidth/6.8,dheight/.3535)

                        dcanvas.coords("r42c2",dwidth/3.6,dheight/.356)
                        dcanvas.coords("r42c3",dwidth/2.688,dheight/.356)
                        dcanvas.coords("r42c4",dwidth/2.15,dheight/.356)
                        dcanvas.coords("r42c5",dwidth/1.785,dheight/.356)
                        dcanvas.coords("r42c6",dwidth/1.525,dheight/.356)
                        dcanvas.coords("r42c7",dwidth/1.329,dheight/.356) 
                        dcanvas.coords("r42c8",dwidth/1.18,dheight/.356)

                        #---------------------------------43th row
                        dcanvas.coords("r43c1",dwidth/6.8,dheight/.347)

                        dcanvas.coords("r43c2",dwidth/3.6,dheight/.3495)
                        dcanvas.coords("r43c3",dwidth/2.688,dheight/.3495)
                        dcanvas.coords("r43c4",dwidth/2.15,dheight/.3495)
                        dcanvas.coords("r43c5",dwidth/1.785,dheight/.3495)
                        dcanvas.coords("r43c6",dwidth/1.525,dheight/.3495)
                        dcanvas.coords("r43c7",dwidth/1.329,dheight/.3495) 
                        dcanvas.coords("r43c8",dwidth/1.18,dheight/.3495)
                        #---------------------------------44th row
                        dcanvas.coords("r44c1",dwidth/6.8,dheight/.341)

                        dcanvas.coords("r44c2",dwidth/3.6,dheight/.3433)
                        dcanvas.coords("r44c3",dwidth/2.688,dheight/.3433)
                        dcanvas.coords("r44c4",dwidth/2.15,dheight/.3433)
                        dcanvas.coords("r44c5",dwidth/1.785,dheight/.3433)
                        dcanvas.coords("r44c6",dwidth/1.525,dheight/.3433)
                        dcanvas.coords("r44c7",dwidth/1.329,dheight/.3433) 
                        dcanvas.coords("r44c8",dwidth/1.18,dheight/.3433)

                        #---------------------------------45th row
                        dcanvas.coords("r45c1",dwidth/6.8,dheight/.335)

                        dcanvas.coords("r45c2",dwidth/3.6,dheight/.3373)
                        dcanvas.coords("r45c3",dwidth/2.688,dheight/.3373)
                        dcanvas.coords("r45c4",dwidth/2.15,dheight/.3373)
                        dcanvas.coords("r45c5",dwidth/1.785,dheight/.3373)
                        dcanvas.coords("r45c6",dwidth/1.525,dheight/.3373)
                        dcanvas.coords("r45c7",dwidth/1.329,dheight/.3373) 
                        dcanvas.coords("r45c8",dwidth/1.18,dheight/.3373)

                        #---------------------------------46th row
                        dcanvas.coords("r46c1",dwidth/6.8,dheight/.329)

                        dcanvas.coords("r46c2",dwidth/3.6,dheight/.3313)
                        dcanvas.coords("r46c3",dwidth/2.688,dheight/.3313)
                        dcanvas.coords("r46c4",dwidth/2.15,dheight/.3313)
                        dcanvas.coords("r46c5",dwidth/1.785,dheight/.3313)
                        dcanvas.coords("r46c6",dwidth/1.525,dheight/.3313)
                        dcanvas.coords("r46c7",dwidth/1.329,dheight/.3313) 
                        dcanvas.coords("r46c8",dwidth/1.18,dheight/.3313)

                        #---------------------------------47th row
                        dcanvas.coords("r47c1",dwidth/6.8,dheight/.3235)

                        dcanvas.coords("r47c2",dwidth/3.6,dheight/.3255)
                        dcanvas.coords("r47c3",dwidth/2.688,dheight/.3255)
                        dcanvas.coords("r47c4",dwidth/2.15,dheight/.3255)
                        dcanvas.coords("r47c5",dwidth/1.785,dheight/.3255)
                        dcanvas.coords("r47c6",dwidth/1.525,dheight/.3255)
                        dcanvas.coords("r47c7",dwidth/1.329,dheight/.3255) 
                        dcanvas.coords("r47c8",dwidth/1.18,dheight/.3255)

                        #---------------------------------48th row
                        dcanvas.coords("r48c1",dwidth/6.8,dheight/.318)

                        dcanvas.coords("r48c2",dwidth/3.6,dheight/.320)
                        dcanvas.coords("r48c3",dwidth/2.688,dheight/.320)
                        dcanvas.coords("r48c4",dwidth/2.15,dheight/.320)
                        dcanvas.coords("r48c5",dwidth/1.785,dheight/.320)
                        dcanvas.coords("r48c6",dwidth/1.525,dheight/.320)
                        dcanvas.coords("r48c7",dwidth/1.329,dheight/.320) 
                        dcanvas.coords("r48c8",dwidth/1.18,dheight/.320)
                        #---------------------------------49th row
                        dcanvas.coords("r49c1",dwidth/6.8,dheight/.3125)

                        dcanvas.coords("r49c2",dwidth/3.6,dheight/.3145)
                        dcanvas.coords("r49c3",dwidth/2.688,dheight/.3145)
                        dcanvas.coords("r49c4",dwidth/2.15,dheight/.3145)
                        dcanvas.coords("r49c5",dwidth/1.785,dheight/.3145)
                        dcanvas.coords("r49c6",dwidth/1.525,dheight/.3145)
                        dcanvas.coords("r49c7",dwidth/1.329,dheight/.3145) 
                        dcanvas.coords("r49c8",dwidth/1.18,dheight/.3145)

                        #---------------------------------50th row
                        dcanvas.coords("r50c1",dwidth/6.8,dheight/.3075)

                        dcanvas.coords("r50c2",dwidth/3.6,dheight/.3093)
                        dcanvas.coords("r50c3",dwidth/2.688,dheight/.3093)
                        dcanvas.coords("r50c4",dwidth/2.15,dheight/.3093)
                        dcanvas.coords("r50c5",dwidth/1.785,dheight/.3093)
                        dcanvas.coords("r50c6",dwidth/1.525,dheight/.3093)
                        dcanvas.coords("r50c7",dwidth/1.329,dheight/.3093) 
                        dcanvas.coords("r50c8",dwidth/1.18,dheight/.3093)

                        #---------------------------------51th row
                        dcanvas.coords("r51c1",dwidth/6.8,dheight/.3025)

                        dcanvas.coords("r51c2",dwidth/3.6,dheight/.3043)
                        dcanvas.coords("r51c3",dwidth/2.688,dheight/.3043)
                        dcanvas.coords("r51c4",dwidth/2.15,dheight/.3043)
                        dcanvas.coords("r51c5",dwidth/1.785,dheight/.3043)
                        dcanvas.coords("r51c6",dwidth/1.525,dheight/.3043)
                        dcanvas.coords("r51c7",dwidth/1.329,dheight/.3043) 
                        dcanvas.coords("r51c8",dwidth/1.18,dheight/.3043)

                        #---------------------------------52th row
                        dcanvas.coords("r52c1",dwidth/6.8,dheight/.2975)

                        dcanvas.coords("r52c2",dwidth/3.6,dheight/.2993)
                        dcanvas.coords("r52c3",dwidth/2.688,dheight/.2993)
                        dcanvas.coords("r52c4",dwidth/2.15,dheight/.2993)
                        dcanvas.coords("r52c5",dwidth/1.785,dheight/.2993)
                        dcanvas.coords("r52c6",dwidth/1.525,dheight/.2993)
                        dcanvas.coords("r52c7",dwidth/1.329,dheight/.2993) 
                        dcanvas.coords("r52c8",dwidth/1.18,dheight/.2993)

                        #---------------------------------53th row
                        dcanvas.coords("r53c1",dwidth/6.8,dheight/.2928)

                        dcanvas.coords("r53c2",dwidth/3.6,dheight/.2945)
                        dcanvas.coords("r53c3",dwidth/2.688,dheight/.2945)
                        dcanvas.coords("r53c4",dwidth/2.15,dheight/.2945)
                        dcanvas.coords("r53c5",dwidth/1.785,dheight/.2945)
                        dcanvas.coords("r53c6",dwidth/1.525,dheight/.2945)
                        dcanvas.coords("r53c7",dwidth/1.329,dheight/.2945) 
                        dcanvas.coords("r53c8",dwidth/1.18,dheight/.2945)

                        #---------------------------------54th row
                        dcanvas.coords("r54c1",dwidth/6.8,dheight/.288)

                        dcanvas.coords("r54c2",dwidth/3.6,dheight/.2898)
                        dcanvas.coords("r54c3",dwidth/2.688,dheight/.2898)
                        dcanvas.coords("r54c4",dwidth/2.15,dheight/.2898)
                        dcanvas.coords("r54c5",dwidth/1.785,dheight/.2898)
                        dcanvas.coords("r54c6",dwidth/1.525,dheight/.2898)
                        dcanvas.coords("r54c7",dwidth/1.329,dheight/.2898) 
                        dcanvas.coords("r54c8",dwidth/1.18,dheight/.2898)

                        #---------------------------------55th row
                        dcanvas.coords("r55c1",dwidth/6.8,dheight/.2835)

                        dcanvas.coords("r55c2",dwidth/3.6,dheight/.2853)
                        dcanvas.coords("r55c3",dwidth/2.688,dheight/.2853)
                        dcanvas.coords("r55c4",dwidth/2.15,dheight/.2853)
                        dcanvas.coords("r55c5",dwidth/1.785,dheight/.2853)
                        dcanvas.coords("r55c6",dwidth/1.525,dheight/.2853)
                        dcanvas.coords("r55c7",dwidth/1.329,dheight/.2853) 
                        dcanvas.coords("r55c8",dwidth/1.18,dheight/.2853)

                        #---------------------------------56th row
                        dcanvas.coords("r56c1",dwidth/2.01,dheight/.2793)

                 

                        #---------------------------------57th row
                        dcanvas.coords("r57c1",dwidth/6.8,dheight/.2753)

                        dcanvas.coords("r57c2",dwidth/3.6,dheight/.2768)
                        dcanvas.coords("r57c3",dwidth/2.688,dheight/.2768)
                        dcanvas.coords("r57c4",dwidth/2.15,dheight/.2768)
                        dcanvas.coords("r57c5",dwidth/1.785,dheight/.2768)
                        dcanvas.coords("r57c6",dwidth/1.525,dheight/.2768)
                        dcanvas.coords("r57c7",dwidth/1.329,dheight/.2768) 
                        dcanvas.coords("r57c8",dwidth/1.18,dheight/.2768)

                        #---------------------------------58th row
                        dcanvas.coords("r58c1",dwidth/6.8,dheight/.2715)

                        dcanvas.coords("r58c2",dwidth/3.6,dheight/.2730)
                        dcanvas.coords("r58c3",dwidth/2.688,dheight/.2730)
                        dcanvas.coords("r58c4",dwidth/2.15,dheight/.2730)
                        dcanvas.coords("r58c5",dwidth/1.785,dheight/.2730)
                        dcanvas.coords("r58c6",dwidth/1.525,dheight/.2730)
                        dcanvas.coords("r58c7",dwidth/1.329,dheight/.2730) 
                        dcanvas.coords("r58c8",dwidth/1.18,dheight/.2730)

                        #---------------------------------59th row
                        dcanvas.coords("r59c1",dwidth/6.8,dheight/.2678)

                        dcanvas.coords("r59c2",dwidth/3.6,dheight/.2692)
                        dcanvas.coords("r59c3",dwidth/2.688,dheight/.2692)
                        dcanvas.coords("r59c4",dwidth/2.15,dheight/.2692)
                        dcanvas.coords("r59c5",dwidth/1.785,dheight/.2692)
                        dcanvas.coords("r59c6",dwidth/1.525,dheight/.2692)
                        dcanvas.coords("r59c7",dwidth/1.329,dheight/.2692) 
                        dcanvas.coords("r59c8",dwidth/1.18,dheight/.2692)

                        #---------------------------------60th row
                        dcanvas.coords("r60c1",dwidth/6.8,dheight/.2638)

                        dcanvas.coords("r60c2",dwidth/3.6,dheight/.2652)
                        dcanvas.coords("r60c3",dwidth/2.688,dheight/.2652)
                        dcanvas.coords("r60c4",dwidth/2.15,dheight/.2652)
                        dcanvas.coords("r60c5",dwidth/1.785,dheight/.2652)
                        dcanvas.coords("r60c6",dwidth/1.525,dheight/.2652)
                        dcanvas.coords("r60c7",dwidth/1.329,dheight/.2652) 
                        dcanvas.coords("r60c8",dwidth/1.18,dheight/.2652)

                        #---------------------------------61th row
                        dcanvas.coords("r61c1",dwidth/6.8,dheight/.2600)

                        dcanvas.coords("r61c2",dwidth/3.6,dheight/.2615)
                        dcanvas.coords("r61c3",dwidth/2.688,dheight/.2615)
                        dcanvas.coords("r61c4",dwidth/2.15,dheight/.2615)
                        dcanvas.coords("r61c5",dwidth/1.785,dheight/.2615)
                        dcanvas.coords("r61c6",dwidth/1.525,dheight/.2615)
                        dcanvas.coords("r61c7",dwidth/1.329,dheight/.2615) 
                        dcanvas.coords("r61c8",dwidth/1.18,dheight/.2615)

                        #---------------------------------62th row
                        dcanvas.coords("r62c1",dwidth/6.8,dheight/.2565)

                        dcanvas.coords("r62c2",dwidth/3.6,dheight/.2578)
                        dcanvas.coords("r62c3",dwidth/2.688,dheight/.2578)
                        dcanvas.coords("r62c4",dwidth/2.15,dheight/.2578)
                        dcanvas.coords("r62c5",dwidth/1.785,dheight/.2578)
                        dcanvas.coords("r62c6",dwidth/1.525,dheight/.2578)
                        dcanvas.coords("r62c7",dwidth/1.329,dheight/.2578) 
                        dcanvas.coords("r62c8",dwidth/1.18,dheight/.2578)

                        #---------------------------------63th row
                        dcanvas.coords("r63c1",dwidth/6.8,dheight/.2530)

                        dcanvas.coords("r63c2",dwidth/3.6,dheight/.2542)
                        dcanvas.coords("r63c3",dwidth/2.688,dheight/.2542)
                        dcanvas.coords("r63c4",dwidth/2.15,dheight/.2542)
                        dcanvas.coords("r63c5",dwidth/1.785,dheight/.2542)
                        dcanvas.coords("r63c6",dwidth/1.525,dheight/.2542)
                        dcanvas.coords("r63c7",dwidth/1.329,dheight/.2542) 
                        dcanvas.coords("r63c8",dwidth/1.18,dheight/.2542)

                        #---------------------------------64th row
                        dcanvas.coords("r64c1",dwidth/6.8,dheight/.2530)

                        dcanvas.coords("r64c2",dwidth/3.6,dheight/.2542)
                        dcanvas.coords("r64c3",dwidth/2.688,dheight/.2542)
                        dcanvas.coords("r64c4",dwidth/2.15,dheight/.2542)
                        dcanvas.coords("r64c5",dwidth/1.785,dheight/.2542)
                        dcanvas.coords("r64c6",dwidth/1.525,dheight/.2542)
                        dcanvas.coords("r64c7",dwidth/1.329,dheight/.2542) 
                        dcanvas.coords("r64c8",dwidth/1.18,dheight/.2542)
                        #---------------------------------65th row
                        dcanvas.coords("r65c1",dwidth/6.8,dheight/.2495)

                        dcanvas.coords("r65c2",dwidth/3.6,dheight/.2507)
                        dcanvas.coords("r65c3",dwidth/2.688,dheight/.2507)
                        dcanvas.coords("r65c4",dwidth/2.15,dheight/.2507)
                        dcanvas.coords("r65c5",dwidth/1.785,dheight/.2507)
                        dcanvas.coords("r65c6",dwidth/1.525,dheight/.2507)
                        dcanvas.coords("r65c7",dwidth/1.329,dheight/.2507) 
                        dcanvas.coords("r65c8",dwidth/1.18,dheight/.2507)

                        #---------------------------------66th row
                        dcanvas.coords("r66c1",dwidth/6.8,dheight/.2462)

                        dcanvas.coords("r66c2",dwidth/3.6,dheight/.2475)
                        dcanvas.coords("r66c3",dwidth/2.688,dheight/.2475)
                        dcanvas.coords("r66c4",dwidth/2.15,dheight/.2475)
                        dcanvas.coords("r66c5",dwidth/1.785,dheight/.2475)
                        dcanvas.coords("r66c6",dwidth/1.525,dheight/.2475)
                        dcanvas.coords("r66c7",dwidth/1.329,dheight/.2475) 
                        dcanvas.coords("r66c8",dwidth/1.18,dheight/.2475)

                        #---------------------------------67th row
                        dcanvas.coords("r67c1",dwidth/6.8,dheight/.2429)

                        dcanvas.coords("r67c2",dwidth/3.6,dheight/.2442)
                        dcanvas.coords("r67c3",dwidth/2.688,dheight/.2442)
                        dcanvas.coords("r67c4",dwidth/2.15,dheight/.2442)
                        dcanvas.coords("r67c5",dwidth/1.785,dheight/.2442)
                        dcanvas.coords("r67c6",dwidth/1.525,dheight/.2442)
                        dcanvas.coords("r67c7",dwidth/1.329,dheight/.2442) 
                        dcanvas.coords("r67c8",dwidth/1.18,dheight/.2442)

                        #---------------------------------68th row
                        dcanvas.coords("r68c1",dwidth/6.8,dheight/.2396)

                        dcanvas.coords("r68c2",dwidth/3.6,dheight/.2409)
                        dcanvas.coords("r68c3",dwidth/2.688,dheight/.2409)
                        dcanvas.coords("r68c4",dwidth/2.15,dheight/.2409)
                        dcanvas.coords("r68c5",dwidth/1.785,dheight/.2409)
                        dcanvas.coords("r68c6",dwidth/1.525,dheight/.2409)
                        dcanvas.coords("r68c7",dwidth/1.329,dheight/.2409) 
                        dcanvas.coords("r68c8",dwidth/1.18,dheight/.2409)

                        #---------------------------------69th row
                        dcanvas.coords("r69c1",dwidth/6.8,dheight/.2365)

                        dcanvas.coords("r69c2",dwidth/3.6,dheight/.2378)
                        dcanvas.coords("r69c3",dwidth/2.688,dheight/.2378)
                        dcanvas.coords("r69c4",dwidth/2.15,dheight/.2378)
                        dcanvas.coords("r69c5",dwidth/1.785,dheight/.2378)
                        dcanvas.coords("r69c6",dwidth/1.525,dheight/.2378)
                        dcanvas.coords("r69c7",dwidth/1.329,dheight/.2378) 
                        dcanvas.coords("r69c8",dwidth/1.18,dheight/.2378)

                        #---------------------------------70th row
                        dcanvas.coords("r70c1",dwidth/6.8,dheight/.2336)

                        dcanvas.coords("r70c2",dwidth/3.6,dheight/.2348)
                        dcanvas.coords("r70c3",dwidth/2.688,dheight/.2348)
                        dcanvas.coords("r70c4",dwidth/2.15,dheight/.2348)
                        dcanvas.coords("r70c5",dwidth/1.785,dheight/.2348)
                        dcanvas.coords("r70c6",dwidth/1.525,dheight/.2348)
                        dcanvas.coords("r70c7",dwidth/1.329,dheight/.2348) 
                        dcanvas.coords("r70c8",dwidth/1.18,dheight/.2348)

                        #---------------------------------71th row
                        dcanvas.coords("r71c1",dwidth/6.8,dheight/.2307)

                        dcanvas.coords("r71c2",dwidth/3.6,dheight/.2317)
                        dcanvas.coords("r71c3",dwidth/2.688,dheight/.2317)
                        dcanvas.coords("r71c4",dwidth/2.15,dheight/.2317)
                        dcanvas.coords("r71c5",dwidth/1.785,dheight/.2317)
                        dcanvas.coords("r71c6",dwidth/1.525,dheight/.2317)
                        dcanvas.coords("r71c7",dwidth/1.329,dheight/.2317) 
                        dcanvas.coords("r71c8",dwidth/1.18,dheight/.2317)


                    fin_cash_analiz.grid_rowconfigure(0,weight=1)
                    fin_cash_analiz.grid_columnconfigure(0,weight=1)

                    frm_analiz = Canvas(fin_cash_analiz,height=700,bg='#2f516f',scrollregion=(0,0,700,3000))
                    analiz_scrl = Scrollbar(fin_cash_analiz,orient=VERTICAL)
                    analiz_scrl.grid(row=0,column=1,sticky='ns')
                    analiz_scrl.config(command=frm_analiz.yview)
                    frm_analiz.bind("<Configure>", res_wid_anal)
                    frm_analiz.config(yscrollcommand=analiz_scrl.set)
                    frm_analiz.grid(row=0,column=0,sticky='nsew')

                    #----------------------------------------------------------------------------------heder 1
                    rth2 = frm_analiz.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_anal"),smooth=True,)

                    lv_name=Label(frm_analiz, text="CASH FLOW ANALYZER",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("lb_hdd"))
                    frm_analiz.create_line(0, 0, 0, 0,fill="gray", tag=("anal_hr") )


                    #----------------------------------------------------------------------------------heder 2
                    rth2 = frm_analiz.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_anal2"),smooth=True,)

                    lv_name=Label(frm_analiz, text="Report period",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("cmb_lb"))

                    chrt_ana= StringVar()
                    dat_type = ttk.Combobox(frm_analiz,textvariable=chrt_ana,width=20,font=('Calibri 16'))
                    
                    dat_type['values'] = ('Last 6 Months','All Dates','Custom', 'Today', 'This Month',)
                    dat_type.bind('<<ComboboxSelected>>', "chart_tp_slt")
                    dat_type.current(0)
                
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=dat_type, tag=("cmb_bx"))

                    button15 = customtkinter.CTkButton(master=frm_analiz,command=main_sign_in,text="Run Report",bg="#213b52")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=button15, tag=("button15"))

                    button25 = customtkinter.CTkButton(master=frm_analiz,command=main_sign_in,text="Back",bg="#213b52")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=button25, tag=("button25"))

                    
                    rth2 = frm_analiz.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_anal3"),smooth=True,)
                    #-----------------------------------------------------------------------------table section

                    dat_td=date.today()
                    
        
                    if dat_td.month==1:
                        daat_mnt="January"
                    elif dat_td.month==2:
                        daat_mnt="February"
                    elif dat_td.month==3:
                        daat_mnt="March"
                    elif dat_td.month==4:
                        daat_mnt="April"
                    elif dat_td.month==5:
                        daat_mnt="May"
                    elif dat_td.month==6:
                        daat_mnt="June"
                    elif dat_td.month==7:
                        daat_mnt="July"
                    elif dat_td.month==8:
                        daat_mnt="August"
                    elif dat_td.month==9:
                        daat_mnt="September"
                    elif dat_td.month==10:
                        daat_mnt="October"
                    elif dat_td.month==11:
                        daat_mnt="November"
                    elif dat_td.month==12:
                        daat_mnt="December"
                    else:
                        pass
                    #previous date
                    last_month = dat_td - relativedelta(months=1)

                    if last_month.month==1:
                        pr_mnt="January"
                    elif last_month.month==2:
                        pr_mnt="February"
                    elif last_month.month==3:
                        pr_mnt="March"
                    elif last_month.month==4:
                        pr_mnt="April"
                    elif last_month.month==5:
                        pr_mnt="May"
                    elif last_month.month==6:
                        pr_mnt="June"
                    elif last_month.month==7:
                        pr_mnt="July"
                    elif last_month.month==8:
                        pr_mnt="August"
                    elif last_month.month==9:
                        pr_mnt="September"
                    elif last_month.month==10:
                        pr_mnt="October"
                    elif last_month.month==11:
                        pr_mnt="November"
                    elif last_month.month==12:
                        pr_mnt="December"
                    else:
                        pass

                    #today month -2
                    mnt_2 = dat_td - relativedelta(months=2)

                    if mnt_2.month==1:
                        pr_mnt2="January"
                    elif mnt_2.month==2:
                        pr_mnt2="February"
                    elif mnt_2.month==3:
                        pr_mnt2="March"
                    elif mnt_2.month==4:
                        pr_mnt2="April"
                    elif mnt_2.month==5:
                        pr_mnt2="May"
                    elif mnt_2.month==6:
                        pr_mnt2="June"
                    elif mnt_2.month==7:
                        pr_mnt2="July"
                    elif mnt_2.month==8:
                        pr_mnt2="August"
                    elif mnt_2.month==9:
                        pr_mnt2="September"
                    elif mnt_2.month==10:
                        pr_mnt2="October"
                    elif mnt_2.month==11:
                        pr_mnt2="November"
                    elif mnt_2.month==12:
                        pr_mnt2="December"
                    else:
                        pass

                    #today month -3
                    mnt_3 = dat_td - relativedelta(months=3)

                    if mnt_3.month==1:
                        pr_mnt3="January"
                    elif mnt_3.month==2:
                        pr_mnt3="February"
                    elif mnt_3.month==3:
                        pr_mnt3="March"
                    elif mnt_3.month==4:
                        pr_mnt3="April"
                    elif mnt_3.month==5:
                        pr_mnt3="May"
                    elif mnt_3.month==6:
                        pr_mnt3="June"
                    elif mnt_3.month==7:
                        pr_mnt3="July"
                    elif mnt_3.month==8:
                        pr_mnt3="August"
                    elif mnt_3.month==9:
                        pr_mnt3="September"
                    elif mnt_3.month==10:
                        pr_mnt3="October"
                    elif mnt_3.month==11:
                        pr_mnt3="November"
                    elif mnt_3.month==12:
                        pr_mnt3="December"
                    else:
                        pass

                    #today month -4
                    mnt_4 = dat_td - relativedelta(months=4)

                    if mnt_4.month==1:
                        pr_mnt4="January"
                    elif mnt_4.month==2:
                        pr_mnt4="February"
                    elif mnt_4.month==3:
                        pr_mnt4="March"
                    elif mnt_4.month==4:
                        pr_mnt4="April"
                    elif mnt_4.month==5:
                        pr_mnt4="May"
                    elif mnt_4.month==6:
                        pr_mnt4="June"
                    elif mnt_4.month==7:
                        pr_mnt4="July"
                    elif mnt_4.month==8:
                        pr_mnt4="August"
                    elif mnt_4.month==9:
                        pr_mnt4="September"
                    elif mnt_4.month==10:
                        pr_mnt4="October"
                    elif mnt_4.month==11:
                        pr_mnt4="November"
                    elif mnt_4.month==12:
                        pr_mnt4="December"
                    else:
                        pass

                    #today month -5
                    mnt_5 = dat_td - relativedelta(months=5)

                    if mnt_5.month==1:
                        pr_mnt5="January"
                    elif mnt_5.month==2:
                        pr_mnt5="February"
                    elif mnt_5.month==3:
                        pr_mnt5="March"
                    elif mnt_5.month==4:
                        pr_mnt5="April"
                    elif mnt_5.month==5:
                        pr_mnt5="May"
                    elif mnt_5.month==6:
                        pr_mnt5="June"
                    elif mnt_5.month==7:
                        pr_mnt5="July"
                    elif mnt_5.month==8:
                        pr_mnt5="August"
                    elif mnt_5.month==9:
                        pr_mnt5="September"
                    elif mnt_5.month==10:
                        pr_mnt5="October"
                    elif mnt_5.month==11:
                        pr_mnt5="November"
                    elif mnt_5.month==12:
                        pr_mnt5="December"
                    else:
                        pass
                    
                    lv_name=Label(frm_analiz, text="",bg="#213b52", width=37, fg="White", anchor="center",font=('Calibri 13 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r1x1"))

                    lv_name=Label(frm_analiz, text=pr_mnt5,bg="#213b52", width=13, fg="White", anchor="center",font=('Calibri 13 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r1c2"))

                    lv_name=Label(frm_analiz, text=pr_mnt4,bg="#213b52", width=13, fg="White", anchor="center",font=('Calibri 13 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r1c3"))

                    lv_name=Label(frm_analiz, text=pr_mnt3,bg="#213b52", width=13, fg="White", anchor="center",font=('Calibri 13 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r1c4"))

                    lv_name=Label(frm_analiz, text=pr_mnt2,bg="#213b52", width=13, fg="White", anchor="center",font=('Calibri 13 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r1c5"))

                    lv_name=Label(frm_analiz, text=pr_mnt,bg="#213b52", width=13, fg="White", anchor="center",font=('Calibri 13 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r1c6"))

                    lv_name=Label(frm_analiz, text=daat_mnt,bg="#213b52", width=13, fg="White", anchor="center",font=('Calibri 13 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r1c7"))

                    lv_name=Label(frm_analiz, text="Total",bg="#213b52", width=18, fg="White", anchor="center",font=('Calibri 13 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r1c8"))
                    
                    #----------------------------------------------------------second row
                    lv_name=Label(frm_analiz, text="Beginning Cash Balance",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r2c1"))

                    

                    r2c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
               
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r2c2, tag=("r2c2"))
                    

                    r2c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)

                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r2c3, tag=("r2c3"))


                    r2c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)

                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r2c4, tag=("r2c4"))


                    r2c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)

                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r2c5, tag=("r2c5"))

                    
                    r2c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r2c7, tag=("r2c7"))

                    r2c8 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r2c8, tag=("r2c8"))

                    r2c6 = Entry(frm_analiz, width=18 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r2c6, tag=("r2c6"))

                    

                    #-----------------------------------------------------------------------------
                    today_gt2 = date.today()
                    firsty_gt2= today_gt2.replace(day=1)
                    last_monthy_gt2 = firsty_gt2 -relativedelta(months=6)
                    
                    end_todayy_gt2 = last_monthy_gt2
                    end_firsty_gt2 = end_todayy_gt2.replace(day=1)
                    end_monthy_gt2 = end_firsty_gt2 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt2='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype in ("Other Income","Income")'
                    sqly_gt2_val=(last_monthy_gt2,end_monthy_gt2,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt2,sqly_gt2_val)
                    mnty_gt2=fbcursor.fetchone()
                    


                    today25 = date.today()
                    first25 = today25.replace(day=1)
                    last_month25 = first25 -relativedelta(months=5)
                    
                    end_today25 = last_month25
                    end_first25 = end_today25.replace(day=1)
                    end_month25 = end_first25 -relativedelta(days=1)+relativedelta(months=1)

                    sql25='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype in ("Other Income","Income")'
                    sql25_val=(last_month25,end_month25,dtl_cmp_pro[0],)
                    fbcursor.execute(sql25,sql25_val)
                    mnt25=fbcursor.fetchone()

                    today24 = date.today()
                    first24 = today24.replace(day=1)
                    last_month24 = first24 -relativedelta(months=4)
                    
                    end_today24 = last_month24
                    end_first24 = end_today24.replace(day=1)
                    end_month24 = end_first24 -relativedelta(days=1)+relativedelta(months=1)

                    sql24='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype in ("Other Income","Income")'
                    sql24_val=(last_month24,end_month24,dtl_cmp_pro[0],)
                    fbcursor.execute(sql24,sql24_val)
                    mnt24=fbcursor.fetchone()

                    today32 = date.today()
                    first32 = today32.replace(day=1)
                    last_month32 = first32 -relativedelta(months=3)
                    
                    end_today32 = last_month32
                    end_first32 = end_today32.replace(day=1)
                    end_month32 = end_first32 -relativedelta(days=1)+relativedelta(months=1)

                    sql32='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype in ("Other Income","Income")'
                    sql32_val=(last_month32,end_month32,dtl_cmp_pro[0],)
                    fbcursor.execute(sql32,sql32_val)
                    mnt32=fbcursor.fetchone()

                    today22 = date.today()
                    first22 = today22.replace(day=1)
                    last_month22 = first22 -relativedelta(months=2)
                    
                    end_today22 = last_month22
                    end_first22 = end_today22.replace(day=1)
                    end_month22 = end_first22 -relativedelta(days=1)+relativedelta(months=1)

                    sql22='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype in ("Other Income","Income")'
                    sql22_val=(last_month22,end_month22,dtl_cmp_pro[0],)
                    fbcursor.execute(sql22,sql22_val)
                    mnt22=fbcursor.fetchone()

                    today21 = date.today()
                    first21 = today21.replace(day=1)
              

                    end_today21 = date.today()
                    end_first21 = end_today21.replace(day=1)
                    end_month21 = end_first21 -relativedelta(days=1)+relativedelta(months=1)

                    sql21='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype in ("Other Income","Income")'
                    sql21_val=(first21,end_month21,dtl_cmp_pro[0],)
                    fbcursor.execute(sql21,sql21_val)
                    mnt21=fbcursor.fetchone()

                    
                    
                    if mnty_gt2[0] is None:
                        val26=0.0
                    else:
                        val26=mnty_gt2[0] 
                    r2c2.delete(0,END)
                    r2c2.insert(0,"$"+str(val26))
                    # r2c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt25[0] is None:
                        val25="0.0"
                    else:
                        val25=mnt25[0] 
                    r2c3.delete(0,END)
                    r2c3.insert(0,"$"+str(val25))
                    # r2c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt24[0] is None:
                        val24="0.0"
                    else:
                        val24=mnt24[0] 
                    r2c4.delete(0,END)
                    r2c4.insert(0,"$"+str(val24))
                    # r2c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt32[0] is None:
                        val32="0.0"
                    else:
                        val32=mnt32[0] 
                    r2c5.delete(0,END)
                    r2c5.insert(0,"$"+str(val32))
                    # r2c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt22[0] is None:
                        val22="0.0"
                    else:
                        val22=mnt22[0] 
                    r2c6.delete(0,END)
                    r2c6.insert(0,"$"+str(val22))
                    # r2c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt21[0] is None:
                        val21="0.0"
                    else:
                        val21=mnt21[0] 
                    r2c7.delete(0,END)
                    r2c7.insert(0,"$"+str(val21))
                    # r2c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    # if mnttt2[0] is None:
                    #     valtt2="0.0"
                    # else:
                    #     valtt2=mnttt2[0] 
                    sum_tt_2=round(float(mnty_gt2[0])+float(mnt25[0])+float(mnt24[0])+float(mnt32[0])+float(mnt22[0])+float(mnt21[0]),2)
                    r2c8.delete(0,END)
                    r2c8.insert(0,"$"+str(sum_tt_2))
                    r2c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    

                    #----------------------------------------------------------3rd row
                    lv_name=Label(frm_analiz, text="Cash Inflows (Income):",bg="#506579", width=159, fg="white", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r3c1"))

                    

                    #----------------------------------------------------------4 th row
                    lv_name=Label(frm_analiz, text="Billable Expense Income",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r4c1"))

                    today6 = date.today()
                    first6 = today6.replace(day=1)
                    last_month6 = first6 -relativedelta(months=5)
                    
                    end_today6 = last_month6
                    end_first6 = end_today6.replace(day=1)
                    end_month6 = end_first6 -relativedelta(days=1)+relativedelta(months=1)

                    sql6='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Billable Expense Income" and acctype="Income"'
                    sql6_val=(last_month6,end_month6,dtl_cmp_pro[0],)
                    fbcursor.execute(sql6,sql6_val)
                    mnt6=fbcursor.fetchone()


                    today5 = date.today()
                    first5 = today5.replace(day=1)
                    last_month5 = first5 -relativedelta(months=4)
                    
                    end_today5 = last_month5
                    end_first5 = end_today5.replace(day=1)
                    end_month5 = end_first5 -relativedelta(days=1)+relativedelta(months=1)

                    sql5='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Billable Expense Income" and acctype="Income"'
                    sql5_val=(last_month5,end_month5,dtl_cmp_pro[0],)
                    fbcursor.execute(sql5,sql5_val)
                    mnt5=fbcursor.fetchone()

                    today4 = date.today()
                    first4 = today4.replace(day=1)
                    last_month4 = first4 -relativedelta(months=3)
                    
                    end_today4 = last_month4
                    end_first4 = end_today4.replace(day=1)
                    end_month4 = end_first4 -relativedelta(days=1)+relativedelta(months=1)

                    sql4='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Billable Expense Income" and acctype="Income"'
                    sql4_val=(last_month4,end_month4,dtl_cmp_pro[0],)
                    fbcursor.execute(sql4,sql4_val)
                    mnt4=fbcursor.fetchone()

                    today3 = date.today()
                    first3 = today3.replace(day=1)
                    last_month3 = first3 -relativedelta(months=2)
                    
                    end_today3 = last_month3
                    end_first3 = end_today3.replace(day=1)
                    end_month3 = end_first3 -relativedelta(days=1)+relativedelta(months=1)

                    sql3='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Billable Expense Income" and acctype="Income"'
                    sql3_val=(last_month3,end_month3,dtl_cmp_pro[0],)
                    fbcursor.execute(sql3,sql3_val)
                    mnt3=fbcursor.fetchone()

                    today2 = date.today()
                    first2 = today2.replace(day=1)
                    last_month2 = first2 -relativedelta(months=1)
                    
                    end_today2 = last_month2
                    end_first2 = end_today2.replace(day=1)
                    end_month2 = end_first2 -relativedelta(days=1)+relativedelta(months=1)

                    sql2='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Billable Expense Income" and acctype="Income"'
                    sql2_val=(last_month2,end_month2,dtl_cmp_pro[0],)
                    fbcursor.execute(sql2,sql2_val)
                    mnt2=fbcursor.fetchone()

                    today1 = date.today()
                    first1 = today1.replace(day=1)
              

                    end_today1 = date.today()
                    end_first1 = end_today1.replace(day=1)
                    end_month1 = end_first1 -relativedelta(days=1)+relativedelta(months=1)

                    sql1='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Billable Expense Income" and acctype="Income"'
                    sql1_val=(first1,end_month1,dtl_cmp_pro[0],)
                    fbcursor.execute(sql1,sql1_val)
                    mnt1=fbcursor.fetchone()

                    sqltt='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Billable Expense Income" and acctype="Income"'
                    sqltt_val=(last_month6,end_month1,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt,sqltt_val)
                    mnttt=fbcursor.fetchone()

                    r4c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    if mnt6[0] is None:
                        val6="0.0"
                    else:
                        val6=mnt6[0] 
                    r4c2.delete(0,END)
                    r4c2.insert(0,"$"+str(val6))
                    r4c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r4c2, tag=("r4c2"))

                    r4c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    if mnt5[0] is None:
                        val5="0.0"
                    else:
                        val5=mnt5[0] 
                    r4c3.delete(0,END)
                    r4c3.insert(0,"$"+str(val5))
                    r4c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r4c3, tag=("r4c3"))


                    r4c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    if mnt4[0] is None:
                        val4="0.0"
                    else:
                        val4=mnt4[0] 
                    r4c4.delete(0,END)
                    r4c4.insert(0,"$"+str(val4))
                    r4c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r4c4, tag=("r4c4"))


                    r4c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    if mnt3[0] is None:
                        val3="0.0"
                    else:
                        val3=mnt3[0] 
                    r4c5.delete(0,END)
                    r4c5.insert(0,"$"+str(val3))
                    r4c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r4c5, tag=("r4c5"))

                    r4c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    if mnt2[0] is None:
                        val2="0.0"
                    else:
                        val2=mnt2[0] 
                    r4c6.delete(0,END)
                    r4c6.insert(0,"$"+str(val2))
                    r4c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r4c6, tag=("r4c6"))


                    r4c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    if mnt1[0] is None:
                        val1="0.0"
                    else:
                        val1=mnt1[0] 
                    r4c7.delete(0,END)
                    r4c7.insert(0,"$"+str(val1))
                    r4c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r4c7, tag=("r4c7"))

                    r4c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    if mnttt[0] is None:
                        valtt="0.0"
                    else:
                        valtt=mnttt[0] 

                    r4c8.delete(0,END)
                    r4c8.insert(0,"$"+str(valtt))
                    r4c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r4c8, tag=("r4c8"))

                    #----------------------------------------------------------5 th row
                    
                    lv_name=Label(frm_analiz, text="Consulting Income",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r5c1"))

                    today65 = date.today()
                    first65 = today65.replace(day=1)
                    last_month65 = first65 -relativedelta(months=5)
                    
                    end_today65 = last_month65
                    end_first65 = end_today65.replace(day=1)
                    end_month65 = end_first65 -relativedelta(days=1)+relativedelta(months=1)

                    sql65='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Consulting Income" and acctype="Income"'
                    sql65_val=(last_month65,end_month65,dtl_cmp_pro[0],)
                    fbcursor.execute(sql65,sql65_val)
                    mnt65=fbcursor.fetchone()
                    


                    today55 = date.today()
                    first55 = today55.replace(day=1)
                    last_month55 = first55 -relativedelta(months=4)
                    
                    end_today55 = last_month55
                    end_first55 = end_today55.replace(day=1)
                    end_month55 = end_first55 -relativedelta(days=1)+relativedelta(months=1)

                    sql55='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Consulting Income" and acctype="Income"'
                    sql55_val=(last_month55,end_month55,dtl_cmp_pro[0],)
                    fbcursor.execute(sql55,sql55_val)
                    mnt55=fbcursor.fetchone()

                    today45 = date.today()
                    first45 = today45.replace(day=1)
                    last_month45 = first45 -relativedelta(months=3)
                    
                    end_today45 = last_month45
                    end_first45 = end_today45.replace(day=1)
                    end_month45 = end_first45 -relativedelta(days=1)+relativedelta(months=1)

                    sql45='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Consulting Income" and acctype="Income"'
                    sql45_val=(last_month45,end_month45,dtl_cmp_pro[0],)
                    fbcursor.execute(sql45,sql45_val)
                    mnt45=fbcursor.fetchone()

                    today35 = date.today()
                    first35 = today35.replace(day=1)
                    last_month35 = first35 -relativedelta(months=2)
                    
                    end_today35 = last_month35
                    end_first35 = end_today35.replace(day=1)
                    end_month35 = end_first35 -relativedelta(days=1)+relativedelta(months=1)

                    sql35='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Consulting Income" and acctype="Income"'
                    sql35_val=(last_month35,end_month35,dtl_cmp_pro[0],)
                    fbcursor.execute(sql35,sql35_val)
                    mnt35=fbcursor.fetchone()

                    today25 = date.today()
                    first25 = today25.replace(day=1)
                    last_month25 = first25 -relativedelta(months=1)
                    
                    end_today25 = last_month25
                    end_first25 = end_today25.replace(day=1)
                    end_month25 = end_first25 -relativedelta(days=1)+relativedelta(months=1)

                    sql25='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Consulting Income" and acctype="Income"'
                    sql25_val=(last_month25,end_month25,dtl_cmp_pro[0],)
                    fbcursor.execute(sql25,sql25_val)
                    mnt25=fbcursor.fetchone()

                    today15 = date.today()
                    first15 = today15.replace(day=1)
              

                    end_today15 = date.today()
                    end_first15 = end_today15.replace(day=1)
                    end_month15 = end_first15 -relativedelta(days=1)+relativedelta(months=1)

                    sql15='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Consulting Income" and acctype="Income"'
                    sql15_val=(first15,end_month15,dtl_cmp_pro[0],)
                    fbcursor.execute(sql15,sql15_val)
                    mnt15=fbcursor.fetchone()

                    sqltt5='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Consulting Income" and acctype="Income"'
                    sqltt_val5=(last_month65,end_month15,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt5,sqltt_val5)
                    mnttt5=fbcursor.fetchone()


                    r5c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    if mnt65[0] is None:
                        val65="0.0"
                    else:
                        val65=mnt65[0] 
                    r5c2.delete(0,END)
                    r5c2.insert(0,"$"+str(val65))
                    r5c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r5c2, tag=("r5c2"))

                    r5c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    if mnt55[0] is None:
                        val55="0.0"
                    else:
                        val55=mnt55[0] 
                    r5c3.delete(0,END)
                    r5c3.insert(0,"$"+str(val55))
                    r5c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r5c3, tag=("r5c3"))

                    r5c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)     
                    if mnt45[0] is None:
                        val45="0.0"
                    else:
                        val45=mnt45[0] 
                    r5c4.insert(0,"$"+str(val45))               
                    r5c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r5c4, tag=("r5c4"))


                    r5c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)  
                    if mnt35[0] is None:
                        val35="0.0"
                    else:
                        val35=mnt35[0] 
                    r5c5.delete(0,END)
                    r5c5.insert(0,"$"+str(val35))
                    r5c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")                 
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r5c5, tag=("r5c5"))

                    r5c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1) 
                    if mnt25[0] is None:
                        val25="0.0"
                    else:
                        val25=mnt25[0] 
                    r5c6.delete(0,END)
                    r5c6.insert(0,"$"+str(val25))
                    r5c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")                 
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r5c6, tag=("r5c6"))


                    r5c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1) 
                    if mnt15[0] is None:
                        val15="0.0"
                    else:
                        val15=mnt15[0] 
                    r5c7.delete(0,END)
                    r5c7.insert(0,"$"+str(val15))
                    r5c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r5c7, tag=("r5c7"))

                    r5c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1) 
                    if mnttt5[0] is None:
                        valtt5="0.0"
                    else:
                        valtt5=mnttt5[0]
                    r5c8.delete(0,END) 
                    r5c8.insert(0,"$"+str(valtt5)) 
                    r5c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")                
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r5c8, tag=("r5c8"))

                    #----------------------------------------------------------6 th row
                    lv_name=Label(frm_analiz, text="Product Sales",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r6c1"))

                    today66 = date.today()
                    first66 = today66.replace(day=1)
                    last_month66 = first66 -relativedelta(months=5)
                    
                    end_today66 = last_month6
                    end_first66 = end_today66.replace(day=1)
                    end_month66 = end_first66 -relativedelta(days=1)+relativedelta(months=1)

                    sql66='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Product Sales" and acctype="Income"'
                    sql66_val=(last_month66,end_month66,dtl_cmp_pro[0],)
                    fbcursor.execute(sql66,sql66_val)
                    mnt66=fbcursor.fetchone()
                    


                    today56 = date.today()
                    first56 = today56.replace(day=1)
                    last_month56 = first56 -relativedelta(months=4)
                    
                    end_today56 = last_month56
                    end_first56 = end_today56.replace(day=1)
                    end_month56 = end_first56 -relativedelta(days=1)+relativedelta(months=1)

                    sql56='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Product Sales" and acctype="Income"'
                    sql56_val=(last_month56,end_month56,dtl_cmp_pro[0],)
                    fbcursor.execute(sql56,sql56_val)
                    mnt56=fbcursor.fetchone()

                    today46 = date.today()
                    first46 = today46.replace(day=1)
                    last_month46 = first46 -relativedelta(months=3)
                    
                    end_today46 = last_month46
                    end_first46 = end_today46.replace(day=1)
                    end_month46 = end_first46 -relativedelta(days=1)+relativedelta(months=1)

                    sql46='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Product Sales" and acctype="Income"'
                    sql46_val=(last_month46,end_month46,dtl_cmp_pro[0],)
                    fbcursor.execute(sql46,sql46_val)
                    mnt46=fbcursor.fetchone()

                    today36 = date.today()
                    first36 = today36.replace(day=1)
                    last_month36 = first36 -relativedelta(months=2)
                    
                    end_today36 = last_month36
                    end_first36 = end_today36.replace(day=1)
                    end_month36 = end_first36 -relativedelta(days=1)+relativedelta(months=1)

                    sql36='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Product Sales" and acctype="Income"'
                    sql36_val=(last_month36,end_month36,dtl_cmp_pro[0],)
                    fbcursor.execute(sql36,sql36_val)
                    mnt36=fbcursor.fetchone()

                    today26 = date.today()
                    first26 = today26.replace(day=1)
                    last_month26 = first26 -relativedelta(months=1)
                    
                    end_today26 = last_month26
                    end_first26 = end_today26.replace(day=1)
                    end_month26 = end_first26 -relativedelta(days=1)+relativedelta(months=1)

                    sql26='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Product Sales" and acctype="Income"'
                    sql26_val=(last_month26,end_month26,dtl_cmp_pro[0],)
                    fbcursor.execute(sql26,sql26_val)
                    mnt26=fbcursor.fetchone()

                    today16 = date.today()
                    first16 = today16.replace(day=1)
              

                    end_today16 = date.today()
                    end_first16 = end_today16.replace(day=1)
                    end_month16 = end_first16 -relativedelta(days=1)+relativedelta(months=1)

                    sql16='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Product Sales" and acctype="Income"'
                    sql16_val=(first16,end_month16,dtl_cmp_pro[0],)
                    fbcursor.execute(sql16,sql16_val)
                    mnt16=fbcursor.fetchone()

                    sqltt6='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Product Sales" and acctype="Income"'
                    sqltt_val6=(last_month66,end_month16,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt6,sqltt_val6)
                    mnttt6=fbcursor.fetchone()

                    r6c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    if mnt66[0] is None:
                        val76="0.0"
                    else:
                        val76=mnt66[0] 
                    r6c2.delete(0,END)
                    r6c2.insert(0,"$"+str(val76))
                    r6c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r6c2, tag=("r6c2"))

                    r6c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    if mnt56[0] is None:
                        val36="0.0"
                    else:
                        val36=mnt56[0] 
                    r6c3.insert(0,"$"+str(val36))
                   
                    r6c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r6c3, tag=("r6c3"))

                    r6c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)  
                    if mnt46[0] is None:
                        val46="0.0"
                    else:
                        val46=mnt46[0] 
                    r6c4.delete(0,END)
                    r6c4.insert(0,"$"+str(val46))                  
                    r6c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r6c4, tag=("r6c4"))


                    r6c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)  
                    if mnt36[0] is None:
                        val56="0.0"
                    else:
                        val56=mnt36[0] 
                    r6c5.delete(0,END)
                    r6c5.insert(0,"$"+str(val56)) 
                    r6c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")                
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r6c5, tag=("r6c5"))

                    r6c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    if mnt26[0] is None:
                        val66="0.0"
                    else:
                        val66=mnt26[0] 
                    r6c6.delete(0,END)
                    r6c6.insert(0,"$"+str(val66))
                    r6c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r6c6, tag=("r6c6"))


                    r6c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1) 
                    if mnt16[0] is None:
                        val76="0.0"
                    else:
                        val76=mnt16[0] 
                    r6c7.delete(0,END)
                    r6c7.insert(0,"$"+str(val76)) 
                    r6c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r6c7, tag=("r6c7"))

                    r6c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1) 
                    if mnttt6[0] is None:
                        valtt6="0.0"
                    else:
                        valtt6=mnttt6[0] 
                    r6c8.delete(0,END)
                    r6c8.insert(0,"$"+str(valtt6)) 
                    r6c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")                 
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r6c8, tag=("r6c8"))

                    #----------------------------------------------------------7 th row
                    lv_name=Label(frm_analiz, text="Sales",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r7c1"))

                    today67 = date.today()
                    first67 = today67.replace(day=1)
                    last_month67 = first67 -relativedelta(months=5)
                    
                    end_today67 = last_month67
                    end_first67 = end_today67.replace(day=1)
                    end_month67 = end_first67 -relativedelta(days=1)+relativedelta(months=1)

                    sql67='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales" and acctype="Income"'
                    sql67_val=(last_month66,end_month66,dtl_cmp_pro[0],)
                    fbcursor.execute(sql67,sql67_val)
                    mnt67=fbcursor.fetchone()
                    


                    today57 = date.today()
                    first57 = today57.replace(day=1)
                    last_month57 = first57 -relativedelta(months=4)
                    
                    end_today57 = last_month57
                    end_first57 = end_today57.replace(day=1)
                    end_month57 = end_first57 -relativedelta(days=1)+relativedelta(months=1)

                    sql57='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales" and acctype="Income"'
                    sql57_val=(last_month57,end_month57,dtl_cmp_pro[0],)
                    fbcursor.execute(sql57,sql57_val)
                    mnt57=fbcursor.fetchone()

                    today47 = date.today()
                    first47 = today47.replace(day=1)
                    last_month47 = first47 -relativedelta(months=3)
                    
                    end_today47 = last_month47
                    end_first47 = end_today47.replace(day=1)
                    end_month47 = end_first47 -relativedelta(days=1)+relativedelta(months=1)

                    sql47='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales" and acctype="Income"'
                    sql47_val=(last_month47,end_month47,dtl_cmp_pro[0],)
                    fbcursor.execute(sql47,sql47_val)
                    mnt47=fbcursor.fetchone()

                    today37 = date.today()
                    first37 = today37.replace(day=1)
                    last_month37 = first37 -relativedelta(months=2)
                    
                    end_today37 = last_month37
                    end_first37 = end_today37.replace(day=1)
                    end_month37 = end_first37 -relativedelta(days=1)+relativedelta(months=1)

                    sql37='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales" and acctype="Income"'
                    sql37_val=(last_month37,end_month37,dtl_cmp_pro[0],)
                    fbcursor.execute(sql37,sql37_val)
                    mnt37=fbcursor.fetchone()

                    today27 = date.today()
                    first27 = today27.replace(day=1)
                    last_month27 = first27 -relativedelta(months=1)
                    
                    end_today27 = last_month27
                    end_first27 = end_today27.replace(day=1)
                    end_month27 = end_first27 -relativedelta(days=1)+relativedelta(months=1)

                    sql27='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales" and acctype="Income"'
                    sql27_val=(last_month27,end_month27,dtl_cmp_pro[0],)
                    fbcursor.execute(sql27,sql27_val)
                    mnt27=fbcursor.fetchone()

                    today17 = date.today()
                    first17 = today17.replace(day=1)
              

                    end_today17 = date.today()
                    end_first17 = end_today17.replace(day=1)
                    end_month17 = end_first17 -relativedelta(days=1)+relativedelta(months=1)

                    sql17='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales" and acctype="Income"'
                    sql17_val=(first17,end_month17,dtl_cmp_pro[0],)
                    fbcursor.execute(sql17,sql17_val)
                    mnt17=fbcursor.fetchone()

                    sqltt7='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales" and acctype="Income"'
                    sqltt_val7=(last_month67,end_month17,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt7,sqltt_val7)
                    mnttt7=fbcursor.fetchone()


                    r7c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    if mnt67[0] is None:
                        val67="0.0"
                    else:
                        val67=mnt67[0] 
                    r7c2.delete(0,END)
                    r7c2.insert(0,"$"+str(val67))
                    r7c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r7c2, tag=("r7c2"))

                    r7c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    if mnt57[0] is None:
                        val57="0.0"
                    else:
                        val57=mnt57[0] 
                    r7c3.delete(0,END)
                    r7c3.insert(0,"$"+str(val57))
                    r7c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r7c3, tag=("r7c3"))

                    r7c4 = Entry(frm_analiz, width=13,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    if mnt47[0] is None:
                        val47="0.0"
                    else:
                        val47=mnt47[0] 
                    r7c4.delete(0,END)
                    r7c4.insert(0,"$"+str(val47))
                    r7c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r7c4, tag=("r7c4"))


                    r7c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1) 
                    if mnt37[0] is None:
                        val37="0.0"
                    else:
                        val37=mnt37[0] 
                    r7c5.delete(0,END)
                    r7c5.insert(0,"$"+str(val37))
                    r7c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")                     
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r7c5, tag=("r7c5"))

                    r7c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1) 
                    if mnt27[0] is None:
                        val27="0.0"
                    else:
                        val27=mnt27[0] 
                    r7c6.delete(0,END)
                    r7c6.insert(0,"$"+str(val27))
                    r7c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")                 
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r7c6, tag=("r7c6"))


                    r7c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1) 
                    if mnt17[0] is None:
                        val17="0.0"
                    else:
                        val17=mnt17[0] 
                    r7c7.delete(0,END)
                    r7c7.insert(0,"$"+str(val17)) 
                    r7c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r7c7, tag=("r7c7"))

                    r7c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)  
                    if mnttt7[0] is None:
                        valtt7="0.0"
                    else:
                        valtt7=mnttt7[0] 
                    r7c8.delete(0,END)
                    r7c8.insert(0,"$"+str(valtt7))
                    r7c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r7c8, tag=("r7c8"))

                    #----------------------------------------------------------8 th row
                    lv_name=Label(frm_analiz, text="Sales-Hardware",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r8c1"))

                    


                    r8c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r8c2, tag=("r8c2"))

                    r8c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r8c3, tag=("r8c3"))

                    r8c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                        
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r8c4, tag=("r8c4"))


                    r8c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                       
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r8c5, tag=("r8c5"))

                    r8c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                          
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r8c6, tag=("r8c6"))

                    r8c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                              
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r8c7, tag=("r8c7"))

                    r8c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                            
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r8c8, tag=("r8c8"))

                    today_gt8 = date.today()
                    firsty_gt8= today_gt8.replace(day=1)
                    last_monthy_gt8 = firsty_gt8 -relativedelta(months=5)
                    
                    end_todayy_gt8 = last_monthy_gt8
                    end_firsty_gt8 = end_todayy_gt8.replace(day=1)
                    end_monthy_gt8 = end_firsty_gt8 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt8='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Hardware" and acctype="Income"'
                    sqly_gt8_val=(last_monthy_gt8,end_monthy_gt8,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt8,sqly_gt8_val)
                    mnty_gt8=fbcursor.fetchone()
                    


                    today58 = date.today()
                    first58 = today58.replace(day=1)
                    last_month58 = first58 -relativedelta(months=4)
                    
                    end_today58 = last_month58
                    end_first58 = end_today58.replace(day=1)
                    end_month58 = end_first58 -relativedelta(days=1)+relativedelta(months=1)

                    sql58='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Hardware" and acctype="Income"'
                    sql58_val=(last_month58,end_month58,dtl_cmp_pro[0],)
                    fbcursor.execute(sql58,sql58_val)
                    mnt58=fbcursor.fetchone()

                    today48 = date.today()
                    first48 = today48.replace(day=1)
                    last_month48 = first48 -relativedelta(months=3)
                    
                    end_today48 = last_month48
                    end_first48 = end_today48.replace(day=1)
                    end_month48 = end_first48 -relativedelta(days=1)+relativedelta(months=1)

                    sql48='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Hardware" and acctype="Income"'
                    sql48_val=(last_month48,end_month48,dtl_cmp_pro[0],)
                    fbcursor.execute(sql48,sql48_val)
                    mnt48=fbcursor.fetchone()

                    today38 = date.today()
                    first38 = today38.replace(day=1)
                    last_month38 = first38 -relativedelta(months=2)
                    
                    end_today38 = last_month38
                    end_first38 = end_today38.replace(day=1)
                    end_month38 = end_first38 -relativedelta(days=1)+relativedelta(months=1)

                    sql38='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Hardware" and acctype="Income"'
                    sql38_val=(last_month38,end_month38,dtl_cmp_pro[0],)
                    fbcursor.execute(sql38,sql38_val)
                    mnt38=fbcursor.fetchone()

                    today28 = date.today()
                    first28 = today28.replace(day=1)
                    last_month28 = first28 -relativedelta(months=1)
                    
                    end_today28 = last_month28
                    end_first28 = end_today28.replace(day=1)
                    end_month28 = end_first28 -relativedelta(days=1)+relativedelta(months=1)

                    sql28='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Hardware" and acctype="Income"'
                    sql28_val=(last_month28,end_month28,dtl_cmp_pro[0],)
                    fbcursor.execute(sql28,sql28_val)
                    mnt28=fbcursor.fetchone()

                    today18 = date.today()
                    first18 = today18.replace(day=1)
              

                    end_today18 = date.today()
                    end_first18 = end_today18.replace(day=1)
                    end_month18 = end_first18 -relativedelta(days=1)+relativedelta(months=1)

                    sql18='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Hardware" and acctype="Income"'
                    sql18_val=(first18,end_month18,dtl_cmp_pro[0],)
                    fbcursor.execute(sql18,sql18_val)
                    mnt18=fbcursor.fetchone()

                    sqltt8='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Hardware" and acctype="Income"'
                    sqltt_val8=(last_monthy_gt8,end_month18,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt8,sqltt_val8)
                    mnttt8=fbcursor.fetchone()

                    if mnty_gt8[0] is None:
                        val68="0.0"
                    else:
                        val68=mnty_gt8[0] 
                    r8c2.delete(0,END)
                    r8c2.insert(0,"$"+str(val68))
                    r8c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt58[0] is None:
                        val58="0.0"
                    else:
                        val58=mnt58[0] 
                    r8c3.delete(0,END)
                    r8c3.insert(0,"$"+str(val58))
                    r8c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt48[0] is None:
                        val48="0.0"
                    else:
                        val48=mnt48[0] 
                    r8c4.delete(0,END)
                    r8c4.insert(0,"$"+str(val48))
                    r8c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt38[0] is None:
                        val38="0.0"
                    else:
                        val38=mnt38[0] 
                    r8c5.delete(0,END)
                    r8c5.insert(0,"$"+str(val38))
                    r8c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt28[0] is None:
                        val28="0.0"
                    else:
                        val28=mnt28[0] 
                    r8c6.delete(0,END)
                    r8c6.insert(0,"$"+str(val28))
                    r8c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt18[0] is None:
                        val18="0.0"
                    else:
                        val18=mnt18[0] 
                    r8c7.delete(0,END)
                    r8c7.insert(0,"$"+str(val18))
                    r8c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt8[0] is None:
                        valtt8="0.0"
                    else:
                        valtt8=mnttt8[0] 
                    r8c8.delete(0,END)
                    r8c8.insert(0,"$"+str(valtt8))
                    r8c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")   

                    



                    #----------------------------------------------------------9 th row
                    lv_name=Label(frm_analiz, text="Sales-Software",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r9c1"))

                    r9c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1) 
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r9c2, tag=("r9c2"))

                    r9c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r9c3, tag=("r9c3"))

                    r9c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                     
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r9c4, tag=("r9c4"))


                    r9c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r9c5, tag=("r9c5"))

                    r9c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r9c6, tag=("r9c6"))


                    r9c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r9c7, tag=("r9c7"))

                    r9c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r9c8, tag=("r9c8"))

                    today_gt9 = date.today()
                    firsty_gt9= today_gt9.replace(day=1)
                    last_monthy_gt9 = firsty_gt9 -relativedelta(months=5)
                    
                    end_todayy_gt9 = last_monthy_gt9
                    end_firsty_gt9 = end_todayy_gt9.replace(day=1)
                    end_monthy_gt9 = end_firsty_gt9 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt9='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Software" and acctype="Income"'
                    sqly_gt9_val=(last_monthy_gt9,end_monthy_gt9,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt9,sqly_gt9_val)
                    mnty_gt9=fbcursor.fetchone()
                    


                    today59 = date.today()
                    first59 = today59.replace(day=1)
                    last_month59 = first59 -relativedelta(months=4)
                    
                    end_today59 = last_month59
                    end_first59 = end_today59.replace(day=1)
                    end_month59 = end_first59 -relativedelta(days=1)+relativedelta(months=1)

                    sql59='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Software" and acctype="Income"'
                    sql59_val=(last_month59,end_month59,dtl_cmp_pro[0],)
                    fbcursor.execute(sql59,sql59_val)
                    mnt59=fbcursor.fetchone()

                    today49 = date.today()
                    first49 = today49.replace(day=1)
                    last_month49 = first49 -relativedelta(months=3)
                    
                    end_today49 = last_month49
                    end_first49 = end_today49.replace(day=1)
                    end_month49 = end_first49 -relativedelta(days=1)+relativedelta(months=1)

                    sql49='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Software" and acctype="Income"'
                    sql49_val=(last_month49,end_month49,dtl_cmp_pro[0],)
                    fbcursor.execute(sql49,sql49_val)
                    mnt49=fbcursor.fetchone()

                    today39 = date.today()
                    first39 = today39.replace(day=1)
                    last_month39 = first39 -relativedelta(months=2)
                    
                    end_today39 = last_month39
                    end_first39 = end_today39.replace(day=1)
                    end_month39 = end_first39 -relativedelta(days=1)+relativedelta(months=1)

                    sql39='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Software" and acctype="Income"'
                    sql39_val=(last_month39,end_month39,dtl_cmp_pro[0],)
                    fbcursor.execute(sql39,sql39_val)
                    mnt39=fbcursor.fetchone()

                    today29 = date.today()
                    first29 = today29.replace(day=1)
                    last_month29 = first29 -relativedelta(months=1)
                    
                    end_today29 = last_month29
                    end_first29 = end_today29.replace(day=1)
                    end_month29 = end_first29 -relativedelta(days=1)+relativedelta(months=1)

                    sql29='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Software" and acctype="Income"'
                    sql29_val=(last_month29,end_month29,dtl_cmp_pro[0],)
                    fbcursor.execute(sql29,sql29_val)
                    mnt29=fbcursor.fetchone()

                    today19 = date.today()
                    first19 = today19.replace(day=1)
              

                    end_today19 = date.today()
                    end_first19 = end_today19.replace(day=1)
                    end_month19 = end_first19 -relativedelta(days=1)+relativedelta(months=1)

                    sql19='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Software" and acctype="Income"'
                    sql19_val=(first19,end_month19,dtl_cmp_pro[0],)
                    fbcursor.execute(sql19,sql19_val)
                    mnt19=fbcursor.fetchone()

                    sqltt9='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Software" and acctype="Income"'
                    sqltt_val9=(last_monthy_gt9,end_month19,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt9,sqltt_val9)
                    mnttt9=fbcursor.fetchone()
                    
                    if mnty_gt9[0] is None:
                        val69="0.0"
                    else:
                        val69=mnty_gt9[0] 
                    
                    r9c2.delete(0,END)
                    r9c2.insert(0,"$"+str(val69))
                    r9c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt59[0] is None:
                        val59="0.0"
                    else:
                        val59=mnt59[0] 
                    r9c3.delete(0,END)
                    r9c3.insert(0,"$"+str(val59))
                    r9c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt49[0] is None:
                        val49="0.0"
                    else:
                        val49=mnt49[0] 
                    r9c4.delete(0,END)
                    r9c4.insert(0,"$"+str(val49))
                    r9c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt39[0] is None:
                        val39="0.0"
                    else:
                        val39=mnt39[0] 
                    r9c5.delete(0,END)
                    r9c5.insert(0,"$"+str(val39))
                    r9c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt29[0] is None:
                        val29="0.0"
                    else:
                        val29=mnt29[0] 
                    r9c6.delete(0,END)
                    r9c6.insert(0,"$"+str(val29))
                    r9c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt19[0] is None:
                        val19="0.0"
                    else:
                        val19=mnt19[0] 
                    r9c7.delete(0,END)
                    r9c7.insert(0,"$"+str(val19))
                    r9c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt9[0] is None:
                        valtt9="0.0"
                    else:
                        valtt9=mnttt9[0] 
                    r9c8.delete(0,END)
                    r9c8.insert(0,"$"+str(valtt9))
                    r9c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")   

                    #----------------------------------------------------------10 th row
                    lv_name=Label(frm_analiz, text="Sales-Support and Maintanance",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r10c1"))

                    r10c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r10c2, tag=("r10c2"))

                    r10c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r10c3, tag=("r10c3"))

                    r10c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r10c4, tag=("r10c4"))


                    r10c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r10c5, tag=("r10c5"))

                    r10c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r10c6, tag=("r10c6"))


                    r10c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)               
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r10c7, tag=("r10c7"))

                    r10c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r10c8, tag=("r10c8"))

                    today_gt10 = date.today()
                    firsty_gt10= today_gt10.replace(day=1)
                    last_monthy_gt10 = firsty_gt10 -relativedelta(months=5)
                    
                    end_todayy_gt10 = last_monthy_gt10
                    end_firsty_gt10 = end_todayy_gt10.replace(day=1)
                    end_monthy_gt10 = end_firsty_gt10 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt10='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Support and Maintanance" and acctype="Income"'
                    sqly_gt10_val=(last_monthy_gt10,end_monthy_gt10,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt10,sqly_gt10_val)
                    mnty_gt10=fbcursor.fetchone()
                    


                    today510 = date.today()
                    first510 = today510.replace(day=1)
                    last_month510 = first510 -relativedelta(months=4)
                    
                    end_today510 = last_month510
                    end_first510 = end_today510.replace(day=1)
                    end_month510 = end_first510 -relativedelta(days=1)+relativedelta(months=1)

                    sql510='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Support and Maintanance" and acctype="Income"'
                    sql510_val=(last_month510,end_month510,dtl_cmp_pro[0],)
                    fbcursor.execute(sql510,sql510_val)
                    mnt510=fbcursor.fetchone()

                    today410 = date.today()
                    first410 = today410.replace(day=1)
                    last_month410 = first410 -relativedelta(months=3)
                    
                    end_today410 = last_month410
                    end_first410 = end_today410.replace(day=1)
                    end_month410 = end_first410 -relativedelta(days=1)+relativedelta(months=1)

                    sql410='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Support and Maintanance" and acctype="Income"'
                    sql410_val=(last_month410,end_month410,dtl_cmp_pro[0],)
                    fbcursor.execute(sql410,sql410_val)
                    mnt410=fbcursor.fetchone()

                    today310 = date.today()
                    first310 = today310.replace(day=1)
                    last_month310 = first310 -relativedelta(months=2)
                    
                    end_today310 = last_month310
                    end_first310 = end_today310.replace(day=1)
                    end_month310 = end_first310 -relativedelta(days=1)+relativedelta(months=1)

                    sql310='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Support and Maintanance" and acctype="Income"'
                    sql310_val=(last_month310,end_month310,dtl_cmp_pro[0],)
                    fbcursor.execute(sql310,sql310_val)
                    mnt310=fbcursor.fetchone()

                    today210 = date.today()
                    first210 = today210.replace(day=1)
                    last_month210 = first210 -relativedelta(months=1)
                    
                    end_today210 = last_month210
                    end_first210 = end_today210.replace(day=1)
                    end_month210 = end_first210 -relativedelta(days=1)+relativedelta(months=1)

                    sql210='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Support and Maintanance" and acctype="Income"'
                    sql210_val=(last_month210,end_month210,dtl_cmp_pro[0],)
                    fbcursor.execute(sql210,sql210_val)
                    mnt210=fbcursor.fetchone()

                    today110 = date.today()
                    first110 = today110.replace(day=1)
              

                    end_today110 = date.today()
                    end_first110 = end_today110.replace(day=1)
                    end_month110 = end_first110 -relativedelta(days=1)+relativedelta(months=1)

                    sql110='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Support and Maintanance" and acctype="Income"'
                    sql110_val=(first110,end_month110,dtl_cmp_pro[0],)
                    fbcursor.execute(sql110,sql110_val)
                    mnt110=fbcursor.fetchone()

                    sqltt10='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales-Support and Maintanance" and acctype="Income"'
                    sqltt_val10=(last_monthy_gt10,end_month110,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt10,sqltt_val10)
                    mnttt10=fbcursor.fetchone()
                    
                    if mnty_gt10[0] is None:
                        val610="0.0"
                    else:
                        val610=mnty_gt10[0] 
                    r10c2.delete(0,END)
                    r10c2.insert(0,"$"+str(val610))
                    r10c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt510[0] is None:
                        val510="0.0"
                    else:
                        val510=mnt510[0] 
                    r10c3.delete(0,END)
                    r10c3.insert(0,"$"+str(val510))
                    r10c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt410[0] is None:
                        val410="0.0"
                    else:
                        val410=mnt410[0] 
                    r10c4.delete(0,END)
                    r10c4.insert(0,"$"+str(val410))
                    r10c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt310[0] is None:
                        val310="0.0"
                    else:
                        val310=mnt310[0] 
                    r10c5.delete(0,END)
                    r10c5.insert(0,"$"+str(val310))
                    r10c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt210[0] is None:
                        val210="0.0"
                    else:
                        val210=mnt210[0] 
                    r10c6.delete(0,END)
                    r10c6.insert(0,"$"+str(val210))
                    r10c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt110[0] is None:
                        val110="0.0"
                    else:
                        val110=mnt110[0] 
                    r10c7.delete(0,END)
                    r10c7.insert(0,"$"+str(val110))
                    r10c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt10[0] is None:
                        valtt10="0.0"
                    else:
                        valtt10=mnttt10[0] 
                    r10c8.delete(0,END)
                    r10c8.insert(0,"$"+str(valtt10))
                    r10c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")   

                    #----------------------------------------------------------11 th row
                    lv_name=Label(frm_analiz, text="Sales Discounts",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r11c1"))

                    r11c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1) 
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r11c2, tag=("r11c2"))

                    r11c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1) 
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r11c3, tag=("r11c3"))

                    r11c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                     
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r11c4, tag=("r11c4"))


                    r11c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                     
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r11c5, tag=("r11c5"))

                    r11c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r11c6, tag=("r11c6"))


                    r11c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r11c7, tag=("r11c7"))

                    r11c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r11c8, tag=("r11c8"))
                    #----------------------------------------------------------------------calcu
                    today_gt11 = date.today()
                    firsty_gt11= today_gt11.replace(day=1)
                    last_monthy_gt11 = firsty_gt11 -relativedelta(months=5)
                    
                    end_todayy_gt11 = last_monthy_gt11
                    end_firsty_gt11 = end_todayy_gt11.replace(day=1)
                    end_monthy_gt11 = end_firsty_gt11 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt11='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales Discounts" and acctype="Income"'
                    sqly_gt11_val=(last_monthy_gt11,end_monthy_gt11,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt11,sqly_gt11_val)
                    mnty_gt11=fbcursor.fetchone()
                    


                    today511 = date.today()
                    first511 = today511.replace(day=1)
                    last_month511 = first511 -relativedelta(months=4)
                    
                    end_today511 = last_month511
                    end_first511 = end_today511.replace(day=1)
                    end_month511 = end_first511 -relativedelta(days=1)+relativedelta(months=1)

                    sql511='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales Discounts" and acctype="Income"'
                    sql511_val=(last_month511,end_month511,dtl_cmp_pro[0],)
                    fbcursor.execute(sql511,sql511_val)
                    mnt511=fbcursor.fetchone()

                    today411 = date.today()
                    first411 = today411.replace(day=1)
                    last_month411 = first411 -relativedelta(months=3)
                    
                    end_today411 = last_month411
                    end_first411 = end_today411.replace(day=1)
                    end_month411 = end_first411 -relativedelta(days=1)+relativedelta(months=1)

                    sql411='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales Discounts" and acctype="Income"'
                    sql411_val=(last_month411,end_month411,dtl_cmp_pro[0],)
                    fbcursor.execute(sql411,sql411_val)
                    mnt411=fbcursor.fetchone()

                    today311 = date.today()
                    first311 = today311.replace(day=1)
                    last_month311 = first311 -relativedelta(months=2)
                    
                    end_today311 = last_month311
                    end_first311 = end_today311.replace(day=1)
                    end_month311 = end_first311 -relativedelta(days=1)+relativedelta(months=1)

                    sql311='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales Discounts" and acctype="Income"'
                    sql311_val=(last_month311,end_month311,dtl_cmp_pro[0],)
                    fbcursor.execute(sql311,sql311_val)
                    mnt311=fbcursor.fetchone()

                    today211 = date.today()
                    first211 = today211.replace(day=1)
                    last_month211 = first211 -relativedelta(months=1)
                    
                    end_today211 = last_month211
                    end_first211 = end_today211.replace(day=1)
                    end_month211 = end_first211 -relativedelta(days=1)+relativedelta(months=1)

                    sql211='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales Discounts" and acctype="Income"'
                    sql211_val=(last_month211,end_month211,dtl_cmp_pro[0],)
                    fbcursor.execute(sql211,sql211_val)
                    mnt211=fbcursor.fetchone()

                    today111 = date.today()
                    first111 = today111.replace(day=1)
              

                    end_today111 = date.today()
                    end_first111 = end_today111.replace(day=1)
                    end_month111 = end_first111 -relativedelta(days=1)+relativedelta(months=1)

                    sql111='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales Discounts" and acctype="Income"'
                    sql111_val=(first111,end_month111,dtl_cmp_pro[0],)
                    fbcursor.execute(sql111,sql111_val)
                    mnt111=fbcursor.fetchone()

                    sqltt11='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales Discounts" and acctype="Income"'
                    sqltt_val11=(last_monthy_gt11,end_month111,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt11,sqltt_val11)
                    mnttt11=fbcursor.fetchone()
                    
                    if mnty_gt11[0] is None:
                        val611="0.0"
                    else:
                        val611=mnty_gt11[0] 
                    r11c2.delete(0,END)
                    r11c2.insert(0,"$"+str(val611))
                    r11c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt511[0] is None:
                        val511="0.0"
                    else:
                        val511=mnt511[0] 
                    r11c3.delete(0,END)
                    r11c3.insert(0,"$"+str(val511))
                    r11c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt411[0] is None:
                        val411="0.0"
                    else:
                        val411=mnt411[0] 
                    r11c4.delete(0,END)
                    r11c4.insert(0,"$"+str(val411))
                    r11c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt311[0] is None:
                        val311="0.0"
                    else:
                        val311=mnt311[0] 
                    r11c5.delete(0,END)
                    r11c5.insert(0,"$"+str(val311))
                    r11c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt211[0] is None:
                        val211="0.0"
                    else:
                        val211=mnt211[0] 
                    r11c6.delete(0,END)
                    r11c6.insert(0,"$"+str(val211))
                    r11c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt111[0] is None:
                        val111="0.0"
                    else:
                        val111=mnt111[0] 
                    r11c7.delete(0,END)
                    r11c7.insert(0,"$"+str(val111))
                    r11c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt11[0] is None:
                        valtt11="0.0"
                    else:
                        valtt11=mnttt11[0] 
                    r11c8.delete(0,END)
                    r11c8.insert(0,"$"+str(valtt11))
                    r11c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  


                    #----------------------------------------------------------12 th row
                    lv_name=Label(frm_analiz, text="Sales of Product Income",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r12c1"))

                    r12c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r12c2, tag=("r12c2"))

                    r12c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r12c3, tag=("r12c3"))

                    r12c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                     
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r12c4, tag=("r12c4"))


                    r12c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r12c5, tag=("r12c5"))

                    r12c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r12c6, tag=("r12c6"))


                    r12c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                     
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r12c7, tag=("r12c7"))

                    r12c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r12c8, tag=("r12c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt12 = date.today()
                    firsty_gt12= today_gt12.replace(day=1)
                    last_monthy_gt12 = firsty_gt12 -relativedelta(months=5)
                    
                    end_todayy_gt12 = last_monthy_gt12
                    end_firsty_gt12 = end_todayy_gt12.replace(day=1)
                    end_monthy_gt12 = end_firsty_gt12 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt12='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales of Product Income" and acctype="Income"'
                    sqly_gt12_val=(last_monthy_gt12,end_monthy_gt12,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt12,sqly_gt12_val)
                    mnty_gt12=fbcursor.fetchone()
                    


                    today512 = date.today()
                    first512 = today512.replace(day=1)
                    last_month512 = first512 -relativedelta(months=4)
                    
                    end_today512 = last_month512
                    end_first512 = end_today512.replace(day=1)
                    end_month512 = end_first512 -relativedelta(days=1)+relativedelta(months=1)

                    sql512='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales of Product Income" and acctype="Income"'
                    sql512_val=(last_month512,end_month512,dtl_cmp_pro[0],)
                    fbcursor.execute(sql512,sql512_val)
                    mnt512=fbcursor.fetchone()

                    today412 = date.today()
                    first412 = today412.replace(day=1)
                    last_month412 = first412 -relativedelta(months=3)
                    
                    end_today412 = last_month412
                    end_first412 = end_today412.replace(day=1)
                    end_month412 = end_first412 -relativedelta(days=1)+relativedelta(months=1)

                    sql412='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales of Product Income" and acctype="Income"'
                    sql412_val=(last_month412,end_month412,dtl_cmp_pro[0],)
                    fbcursor.execute(sql412,sql412_val)
                    mnt412=fbcursor.fetchone()

                    today312 = date.today()
                    first312 = today312.replace(day=1)
                    last_month312 = first312 -relativedelta(months=2)
                    
                    end_today312 = last_month312
                    end_first312 = end_today312.replace(day=1)
                    end_month312 = end_first312 -relativedelta(days=1)+relativedelta(months=1)

                    sql312='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales of Product Income" and acctype="Income"'
                    sql312_val=(last_month312,end_month312,dtl_cmp_pro[0],)
                    fbcursor.execute(sql312,sql312_val)
                    mnt312=fbcursor.fetchone()

                    today212 = date.today()
                    first212 = today212.replace(day=1)
                    last_month212 = first212 -relativedelta(months=1)
                    
                    end_today212 = last_month212
                    end_first212 = end_today212.replace(day=1)
                    end_month212 = end_first212 -relativedelta(days=1)+relativedelta(months=1)

                    sql212='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales of Product Income" and acctype="Income"'
                    sql212_val=(last_month212,end_month212,dtl_cmp_pro[0],)
                    fbcursor.execute(sql212,sql212_val)
                    mnt212=fbcursor.fetchone()

                    today121 = date.today()
                    first121 = today121.replace(day=1)
              

                    end_today121 = date.today()
                    end_first121 = end_today121.replace(day=1)
                    end_month121 = end_first121 -relativedelta(days=1)+relativedelta(months=1)

                    sql121='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales of Product Income" and acctype="Income"'
                    sql121_val=(first121,end_month121,dtl_cmp_pro[0],)
                    fbcursor.execute(sql121,sql121_val)
                    mnt121=fbcursor.fetchone()

                    sqltt12='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Sales of Product Income" and acctype="Income"'
                    sqltt_val12=(last_monthy_gt12,end_month121,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt12,sqltt_val12)
                    mnttt12=fbcursor.fetchone()
                    
                    if mnty_gt12[0] is None:
                        val612="0.0"
                    else:
                        val612=mnty_gt12[0] 
                    r12c2.delete(0,END)
                    r12c2.insert(0,"$"+str(val612))
                    r12c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt512[0] is None:
                        val512="0.0"
                    else:
                        val512=mnt512[0] 
                    r12c3.delete(0,END)
                    r12c3.insert(0,"$"+str(val512))
                    r12c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt412[0] is None:
                        val412="0.0"
                    else:
                        val412=mnt412[0] 
                    r12c4.delete(0,END)
                    r12c4.insert(0,"$"+str(val412))
                    r12c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt312[0] is None:
                        val312="0.0"
                    else:
                        val312=mnt312[0] 
                    r12c5.delete(0,END)
                    r12c5.insert(0,"$"+str(val312))
                    r12c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt212[0] is None:
                        val212="0.0"
                    else:
                        val212=mnt212[0] 
                    r12c6.delete(0,END)
                    r12c6.insert(0,"$"+str(val212))
                    r12c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt121[0] is None:
                        val121="0.0"
                    else:
                        val121=mnt121[0] 
                    r12c7.delete(0,END)
                    r12c7.insert(0,"$"+str(val121))
                    r12c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt12[0] is None:
                        valtt12="0.0"
                    else:
                        valtt12=mnttt12[0] 
                    r12c8.delete(0,END)
                    r12c8.insert(0,"$"+str(valtt12))
                    r12c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    #----------------------------------------------------------13 th row
                    lv_name=Label(frm_analiz, text="Services",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r13c1"))

                    r13c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r13c2, tag=("r13c2"))

                    r13c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1) 
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r13c3, tag=("r13c3"))

                    r13c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r13c4, tag=("r13c4"))


                    r13c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r13c5, tag=("r13c5"))

                    r13c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r13c6, tag=("r13c6"))


                    r13c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r13c7, tag=("r13c7"))

                    r13c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r13c8, tag=("r13c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt13 = date.today()
                    firsty_gt13= today_gt13.replace(day=1)
                    last_monthy_gt13 = firsty_gt13 -relativedelta(months=5)
                    
                    end_todayy_gt13 = last_monthy_gt13
                    end_firsty_gt13 = end_todayy_gt13.replace(day=1)
                    end_monthy_gt13 = end_firsty_gt13 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt13='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Services" and acctype="Income"'
                    sqly_gt13_val=(last_monthy_gt13,end_monthy_gt13,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt13,sqly_gt13_val)
                    mnty_gt13=fbcursor.fetchone()
                    


                    today513 = date.today()
                    first513 = today513.replace(day=1)
                    last_month513 = first513 -relativedelta(months=4)
                    
                    end_today513 = last_month513
                    end_first513 = end_today513.replace(day=1)
                    end_month513 = end_first513 -relativedelta(days=1)+relativedelta(months=1)

                    sql513='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Services" and acctype="Income"'
                    sql513_val=(last_month513,end_month513,dtl_cmp_pro[0],)
                    fbcursor.execute(sql513,sql513_val)
                    mnt513=fbcursor.fetchone()

                    today413 = date.today()
                    first413 = today413.replace(day=1)
                    last_month413 = first413 -relativedelta(months=3)
                    
                    end_today413 = last_month413
                    end_first413 = end_today413.replace(day=1)
                    end_month413 = end_first413 -relativedelta(days=1)+relativedelta(months=1)

                    sql413='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Services" and acctype="Income"'
                    sql413_val=(last_month413,end_month413,dtl_cmp_pro[0],)
                    fbcursor.execute(sql413,sql413_val)
                    mnt413=fbcursor.fetchone()

                    today313 = date.today()
                    first313 = today313.replace(day=1)
                    last_month313 = first313 -relativedelta(months=2)
                    
                    end_today313 = last_month313
                    end_first313 = end_today313.replace(day=1)
                    end_month313 = end_first313 -relativedelta(days=1)+relativedelta(months=1)

                    sql313='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Services" and acctype="Income"'
                    sql313_val=(last_month313,end_month313,dtl_cmp_pro[0],)
                    fbcursor.execute(sql313,sql313_val)
                    mnt313=fbcursor.fetchone()

                    today213 = date.today()
                    first213 = today213.replace(day=1)
                    last_month213 = first213 -relativedelta(months=1)
                    
                    end_today213 = last_month213
                    end_first213 = end_today213.replace(day=1)
                    end_month213 = end_first213 -relativedelta(days=1)+relativedelta(months=1)

                    sql213='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Services" and acctype="Income"'
                    sql213_val=(last_month213,end_month213,dtl_cmp_pro[0],)
                    fbcursor.execute(sql213,sql213_val)
                    mnt213=fbcursor.fetchone()

                    today131 = date.today()
                    first131 = today131.replace(day=1)
              

                    end_today131 = date.today()
                    end_first131 = end_today131.replace(day=1)
                    end_month131 = end_first131 -relativedelta(days=1)+relativedelta(months=1)

                    sql131='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Services" and acctype="Income"'
                    sql131_val=(first131,end_month131,dtl_cmp_pro[0],)
                    fbcursor.execute(sql131,sql131_val)
                    mnt131=fbcursor.fetchone()

                    sqltt13='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Services" and acctype="Income"'
                    sqltt_val13=(last_monthy_gt13,end_month131,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt13,sqltt_val13)
                    mnttt13=fbcursor.fetchone()
                    
                    if mnty_gt13[0] is None:
                        val613="0.0"
                    else:
                        val613=mnty_gt13[0] 
                    r13c2.delete(0,END)
                    r13c2.insert(0,"$"+str(val613))
                    r13c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt513[0] is None:
                        val513="0.0"
                    else:
                        val513=mnt513[0] 
                    r13c3.delete(0,END)
                    r13c3.insert(0,"$"+str(val513))
                    r13c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt413[0] is None:
                        val413="0.0"
                    else:
                        val413=mnt413[0] 
                    r13c4.delete(0,END)
                    r13c4.insert(0,"$"+str(val413))
                    r13c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt313[0] is None:
                        val313="0.0"
                    else:
                        val313=mnt313[0] 
                    r13c5.delete(0,END)
                    r13c5.insert(0,"$"+str(val313))
                    r13c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt213[0] is None:
                        val213="0.0"
                    else:
                        val213=mnt213[0] 
                    r13c6.delete(0,END)
                    r13c6.insert(0,"$"+str(val213))
                    r13c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt131[0] is None:
                        val131="0.0"
                    else:
                        val131=mnt131[0] 
                    r13c7.delete(0,END)
                    r13c7.insert(0,"$"+str(val131))
                    r13c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt13[0] is None:
                        valtt13="0.0"
                    else:
                        valtt13=mnttt13[0] 
                    r13c8.delete(0,END)
                    r13c8.insert(0,"$"+str(valtt13))
                    r13c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    #----------------------------------------------------------14 th row
                    lv_name=Label(frm_analiz, text="Unapplied Cash Payment Income",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r14c1"))

                    r14c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r14c2, tag=("r14c2"))

                    r14c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r14c3, tag=("r14c3"))

                    r14c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)         
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r14c4, tag=("r14c4"))


                    r14c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r14c5, tag=("r14c5"))

                    r14c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r14c6, tag=("r14c6"))


                    r14c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r14c7, tag=("r14c7"))

                    r14c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r14c8, tag=("r14c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt14 = date.today()
                    firsty_gt14= today_gt14.replace(day=1)
                    last_monthy_gt14 = firsty_gt14 -relativedelta(months=5)
                    
                    end_todayy_gt14 = last_monthy_gt14
                    end_firsty_gt14 = end_todayy_gt14.replace(day=1)
                    end_monthy_gt14 = end_firsty_gt14 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt14='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Unapplied Cash Payment Income" and acctype="Income"'
                    sqly_gt14_val=(last_monthy_gt14,end_monthy_gt14,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt14,sqly_gt14_val)
                    mnty_gt14=fbcursor.fetchone()
                    


                    today514 = date.today()
                    first514 = today514.replace(day=1)
                    last_month514 = first514 -relativedelta(months=4)
                    
                    end_today514 = last_month514
                    end_first514 = end_today514.replace(day=1)
                    end_month514 = end_first514 -relativedelta(days=1)+relativedelta(months=1)

                    sql514='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Unapplied Cash Payment Income" and acctype="Income"'
                    sql514_val=(last_month514,end_month514,dtl_cmp_pro[0],)
                    fbcursor.execute(sql514,sql514_val)
                    mnt514=fbcursor.fetchone()

                    today414 = date.today()
                    first414 = today414.replace(day=1)
                    last_month414 = first414 -relativedelta(months=3)
                    
                    end_today414 = last_month414
                    end_first414 = end_today414.replace(day=1)
                    end_month414 = end_first414 -relativedelta(days=1)+relativedelta(months=1)

                    sql414='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Unapplied Cash Payment Income" and acctype="Income"'
                    sql414_val=(last_month414,end_month414,dtl_cmp_pro[0],)
                    fbcursor.execute(sql414,sql414_val)
                    mnt414=fbcursor.fetchone()

                    today314 = date.today()
                    first314 = today314.replace(day=1)
                    last_month314 = first314 -relativedelta(months=2)
                    
                    end_today314 = last_month314
                    end_first314 = end_today314.replace(day=1)
                    end_month314 = end_first314 -relativedelta(days=1)+relativedelta(months=1)

                    sql314='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Unapplied Cash Payment Income" and acctype="Income"'
                    sql314_val=(last_month314,end_month314,dtl_cmp_pro[0],)
                    fbcursor.execute(sql314,sql314_val)
                    mnt314=fbcursor.fetchone()

                    today214 = date.today()
                    first214 = today214.replace(day=1)
                    last_month214 = first214 -relativedelta(months=1)
                    
                    end_today214 = last_month214
                    end_first214 = end_today214.replace(day=1)
                    end_month214 = end_first214 -relativedelta(days=1)+relativedelta(months=1)

                    sql214='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Unapplied Cash Payment Income" and acctype="Income"'
                    sql214_val=(last_month214,end_month214,dtl_cmp_pro[0],)
                    fbcursor.execute(sql214,sql214_val)
                    mnt214=fbcursor.fetchone()

                    today141 = date.today()
                    first141 = today141.replace(day=1)
              

                    end_today141 = date.today()
                    end_first141 = end_today141.replace(day=1)
                    end_month141 = end_first141 -relativedelta(days=1)+relativedelta(months=1)

                    sql141='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Unapplied Cash Payment Income" and acctype="Income"'
                    sql141_val=(first141,end_month141,dtl_cmp_pro[0],)
                    fbcursor.execute(sql141,sql141_val)
                    mnt141=fbcursor.fetchone()

                    sqltt14='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Unapplied Cash Payment Income" and acctype="Income"'
                    sqltt_val14=(last_monthy_gt14,end_month141,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt14,sqltt_val14)
                    mnttt14=fbcursor.fetchone()
                    
                    if mnty_gt14[0] is None:
                        val614="0.0"
                    else:
                        val614=mnty_gt14[0] 
                    r14c2.delete(0,END)
                    r14c2.insert(0,"$"+str(val614))
                    r14c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt514[0] is None:
                        val514="0.0"
                    else:
                        val514=mnt514[0] 
                    r14c3.delete(0,END)
                    r14c3.insert(0,"$"+str(val514))
                    r14c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt414[0] is None:
                        val414="0.0"
                    else:
                        val414=mnt414[0] 
                    r14c4.delete(0,END)
                    r14c4.insert(0,"$"+str(val414))
                    r14c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt314[0] is None:
                        val314="0.0"
                    else:
                        val314=mnt314[0] 
                    r14c5.delete(0,END)
                    r14c5.insert(0,"$"+str(val314))
                    r14c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt214[0] is None:
                        val214="0.0"
                    else:
                        val214=mnt214[0] 
                    r14c6.delete(0,END)
                    r14c6.insert(0,"$"+str(val214))
                    r14c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt141[0] is None:
                        val141="0.0"
                    else:
                        val141=mnt141[0] 
                    r14c7.delete(0,END)
                    r14c7.insert(0,"$"+str(val141))
                    r14c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt14[0] is None:
                        valtt14="0.0"
                    else:
                        valtt14=mnttt14[0] 
                    r14c8.delete(0,END)
                    r14c8.insert(0,"$"+str(valtt14))
                    r14c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    #----------------------------------------------------------15 th row
                    lv_name=Label(frm_analiz, text="Uncategorised Income",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r15c1"))

                    r15c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r15c2, tag=("r15c2"))

                    r15c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r15c3, tag=("r15c3"))

                    r15c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                      
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r15c4, tag=("r15c4"))


                    r15c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                      
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r15c5, tag=("r15c5"))

                    r15c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                     
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r15c6, tag=("r15c6"))


                    r15c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                      
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r15c7, tag=("r15c7"))

                    r15c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r15c8, tag=("r15c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt15 = date.today()
                    firsty_gt15= today_gt15.replace(day=1)
                    last_monthy_gt15 = firsty_gt15 -relativedelta(months=5)
                    
                    end_todayy_gt15 = last_monthy_gt15
                    end_firsty_gt15 = end_todayy_gt15.replace(day=1)
                    end_monthy_gt15 = end_firsty_gt15 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt15='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Uncategorised Income" and acctype="Income"'
                    sqly_gt15_val=(last_monthy_gt15,end_monthy_gt15,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt15,sqly_gt15_val)
                    mnty_gt15=fbcursor.fetchone()
                    


                    today515 = date.today()
                    first515 = today515.replace(day=1)
                    last_month515 = first515 -relativedelta(months=4)
                    
                    end_today515 = last_month515
                    end_first515 = end_today515.replace(day=1)
                    end_month515 = end_first515 -relativedelta(days=1)+relativedelta(months=1)

                    sql515='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Uncategorised Income" and acctype="Income"'
                    sql515_val=(last_month515,end_month515,dtl_cmp_pro[0],)
                    fbcursor.execute(sql515,sql515_val)
                    mnt515=fbcursor.fetchone()

                    today415 = date.today()
                    first415 = today415.replace(day=1)
                    last_month415 = first415 -relativedelta(months=3)
                    
                    end_today415 = last_month415
                    end_first415 = end_today415.replace(day=1)
                    end_month415 = end_first415 -relativedelta(days=1)+relativedelta(months=1)

                    sql415='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Uncategorised Income" and acctype="Income"'
                    sql415_val=(last_month415,end_month415,dtl_cmp_pro[0],)
                    fbcursor.execute(sql415,sql415_val)
                    mnt415=fbcursor.fetchone()

                    today315 = date.today()
                    first315 = today315.replace(day=1)
                    last_month315 = first315 -relativedelta(months=2)
                    
                    end_today315 = last_month315
                    end_first315 = end_today315.replace(day=1)
                    end_month315 = end_first315 -relativedelta(days=1)+relativedelta(months=1)

                    sql315='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Uncategorised Income" and acctype="Income"'
                    sql315_val=(last_month315,end_month315,dtl_cmp_pro[0],)
                    fbcursor.execute(sql315,sql315_val)
                    mnt315=fbcursor.fetchone()

                    today215 = date.today()
                    first215 = today215.replace(day=1)
                    last_month215 = first215 -relativedelta(months=1)
                    
                    end_today215 = last_month215
                    end_first215 = end_today215.replace(day=1)
                    end_month215 = end_first215 -relativedelta(days=1)+relativedelta(months=1)

                    sql215='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Uncategorised Income" and acctype="Income"'
                    sql215_val=(last_month215,end_month215,dtl_cmp_pro[0],)
                    fbcursor.execute(sql215,sql215_val)
                    mnt215=fbcursor.fetchone()

                    today151 = date.today()
                    first151 = today151.replace(day=1)
              

                    end_today151 = date.today()
                    end_first151 = end_today151.replace(day=1)
                    end_month151 = end_first151 -relativedelta(days=1)+relativedelta(months=1)

                    sql151='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Uncategorised Income" and acctype="Income"'
                    sql151_val=(first151,end_month151,dtl_cmp_pro[0],)
                    fbcursor.execute(sql151,sql151_val)
                    mnt151=fbcursor.fetchone()

                    sqltt15='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Uncategorised Income" and acctype="Income"'
                    sqltt_val15=(last_monthy_gt15,end_month151,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt15,sqltt_val15)
                    mnttt15=fbcursor.fetchone()
                    
                    if mnty_gt15[0] is None:
                        val615="0.0"
                    else:
                        val615=mnty_gt15[0] 
                    r15c2.delete(0,END)
                    r15c2.insert(0,"$"+str(val615))
                    r15c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt515[0] is None:
                        val515="0.0"
                    else:
                        val515=mnt515[0] 
                    r15c3.delete(0,END)
                    r15c3.insert(0,"$"+str(val515))
                    r15c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt415[0] is None:
                        val415="0.0"
                    else:
                        val415=mnt415[0] 
                    r15c4.delete(0,END)
                    r15c4.insert(0,"$"+str(val415))
                    r15c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt315[0] is None:
                        val315="0.0"
                    else:
                        val315=mnt315[0] 
                    r15c5.delete(0,END)
                    r15c5.insert(0,"$"+str(val315))
                    r15c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt215[0] is None:
                        val215="0.0"
                    else:
                        val215=mnt215[0] 
                    r15c6.delete(0,END)
                    r15c6.insert(0,"$"+str(val215))
                    r15c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt151[0] is None:
                        val151="0.0"
                    else:
                        val151=mnt151[0] 
                    r15c7.delete(0,END)
                    r15c7.insert(0,"$"+str(val151))
                    r15c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt15[0] is None:
                        valtt15="0.0"
                    else:
                        valtt15=mnttt15[0] 
                    r15c8.delete(0,END)
                    r15c8.insert(0,"$"+str(valtt15))
                    r15c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    #----------------------------------------------------------16 th row
                    lv_name=Label(frm_analiz, text="Other:",bg="#506579", width=159, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r16c1"))

                    

                    #----------------------------------------------------------17 th row
                    lv_name=Label(frm_analiz, text="Finance Charge Income",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r17c1"))

                    r17c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r17c2, tag=("r17c2"))

                    r17c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r17c3, tag=("r17c3"))

                    r17c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                     
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r17c4, tag=("r17c4"))


                    r17c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                       
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r17c5, tag=("r17c5"))

                    r17c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                     
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r17c6, tag=("r17c6"))


                    r17c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                       
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r17c7, tag=("r17c7"))

                    r17c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r17c8, tag=("r17c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt17 = date.today()
                    firsty_gt17= today_gt17.replace(day=1)
                    last_monthy_gt17 = firsty_gt17 -relativedelta(months=5)
                    
                    end_todayy_gt17 = last_monthy_gt17
                    end_firsty_gt17 = end_todayy_gt17.replace(day=1)
                    end_monthy_gt17 = end_firsty_gt17 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt17='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Finance Charge Income" and acctype="Other Income"'
                    sqly_gt17_val=(last_monthy_gt17,end_monthy_gt17,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt17,sqly_gt17_val)
                    mnty_gt17=fbcursor.fetchone()
                    


                    today517 = date.today()
                    first517 = today517.replace(day=1)
                    last_month517 = first517 -relativedelta(months=4)
                    
                    end_today517 = last_month517
                    end_first517 = end_today517.replace(day=1)
                    end_month517 = end_first517 -relativedelta(days=1)+relativedelta(months=1)

                    sql517='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Finance Charge Income" and acctype="Other Income"'
                    sql517_val=(last_month517,end_month517,dtl_cmp_pro[0],)
                    fbcursor.execute(sql517,sql517_val)
                    mnt517=fbcursor.fetchone()

                    today417 = date.today()
                    first417 = today417.replace(day=1)
                    last_month417 = first417 -relativedelta(months=3)
                    
                    end_today417 = last_month417
                    end_first417 = end_today417.replace(day=1)
                    end_month417 = end_first417 -relativedelta(days=1)+relativedelta(months=1)

                    sql417='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Finance Charge Income" and acctype="Other Income"'
                    sql417_val=(last_month417,end_month417,dtl_cmp_pro[0],)
                    fbcursor.execute(sql417,sql417_val)
                    mnt417=fbcursor.fetchone()

                    today317 = date.today()
                    first317 = today317.replace(day=1)
                    last_month317 = first317 -relativedelta(months=2)
                    
                    end_today317 = last_month317
                    end_first317 = end_today317.replace(day=1)
                    end_month317 = end_first317 -relativedelta(days=1)+relativedelta(months=1)

                    sql317='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Finance Charge Income" and acctype="Other Income"'
                    sql317_val=(last_month317,end_month317,dtl_cmp_pro[0],)
                    fbcursor.execute(sql317,sql317_val)
                    mnt317=fbcursor.fetchone()

                    today217 = date.today()
                    first217 = today217.replace(day=1)
                    last_month217 = first217 -relativedelta(months=1)
                    
                    end_today217 = last_month217
                    end_first217 = end_today217.replace(day=1)
                    end_month217 = end_first217 -relativedelta(days=1)+relativedelta(months=1)

                    sql217='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Finance Charge Income" and acctype="Other Income"'
                    sql217_val=(last_month217,end_month217,dtl_cmp_pro[0],)
                    fbcursor.execute(sql217,sql217_val)
                    mnt217=fbcursor.fetchone()

                    today171 = date.today()
                    first171 = today171.replace(day=1)
              

                    end_today171 = date.today()
                    end_first171 = end_today171.replace(day=1)
                    end_month171 = end_first171 -relativedelta(days=1)+relativedelta(months=1)

                    sql171='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Finance Charge Income" and acctype="Other Income"'
                    sql171_val=(first171,end_month171,dtl_cmp_pro[0],)
                    fbcursor.execute(sql171,sql171_val)
                    mnt171=fbcursor.fetchone()

                    sqltt17='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Finance Charge Income" and acctype="Other Income"'
                    sqltt_val17=(last_monthy_gt17,end_month171,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt17,sqltt_val17)
                    mnttt17=fbcursor.fetchone()
                    
                    if mnty_gt17[0] is None:
                        val617="0.0"
                    else:
                        val617=mnty_gt17[0] 
                    r17c2.delete(0,END)
                    r17c2.insert(0,"$"+str(val617))
                    r17c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt517[0] is None:
                        val517="0.0"
                    else:
                        val517=mnt517[0] 
                    r17c3.delete(0,END)
                    r17c3.insert(0,"$"+str(val517))
                    r17c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt417[0] is None:
                        val417="0.0"
                    else:
                        val417=mnt417[0] 
                    r17c4.delete(0,END)
                    r17c4.insert(0,"$"+str(val417))
                    r17c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt317[0] is None:
                        val317="0.0"
                    else:
                        val317=mnt317[0] 
                    r17c5.delete(0,END)
                    r17c5.insert(0,"$"+str(val317))
                    r17c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt217[0] is None:
                        val217="0.0"
                    else:
                        val217=mnt217[0] 
                    r17c6.delete(0,END)
                    r17c6.insert(0,"$"+str(val217))
                    r17c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt171[0] is None:
                        val171="0.0"
                    else:
                        val171=mnt171[0] 
                    r17c7.delete(0,END)
                    r17c7.insert(0,"$"+str(val171))
                    r17c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt17[0] is None:
                        valtt17="0.0"
                    else:
                        valtt17=mnttt17[0] 
                    r17c8.delete(0,END)
                    r17c8.insert(0,"$"+str(valtt17))
                    r17c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  


                    #----------------------------------------------------------18 th row
                    lv_name=Label(frm_analiz, text="Insurance Proceeds Received",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r18c1"))

                    r18c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r18c2, tag=("r18c2"))

                    r18c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r18c3, tag=("r18c3"))

                    r18c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                     
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r18c4, tag=("r18c4"))


                    r18c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                      
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r18c5, tag=("r18c5"))

                    r18c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                     
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r18c6, tag=("r18c6"))


                    r18c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                      
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r18c7, tag=("r18c7"))

                    r18c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r18c8, tag=("r18c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt18 = date.today()
                    firsty_gt18= today_gt18.replace(day=1)
                    last_monthy_gt18 = firsty_gt18 -relativedelta(months=5)
                    
                    end_todayy_gt18 = last_monthy_gt18
                    end_firsty_gt18 = end_todayy_gt18.replace(day=1)
                    end_monthy_gt18 = end_firsty_gt18 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt18='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Proceeds Received" and acctype="Other Income"'
                    sqly_gt18_val=(last_monthy_gt18,end_monthy_gt18,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt18,sqly_gt18_val)
                    mnty_gt18=fbcursor.fetchone()
                    


                    today518 = date.today()
                    first518 = today518.replace(day=1)
                    last_month518 = first518 -relativedelta(months=4)
                    
                    end_today518 = last_month518
                    end_first518 = end_today518.replace(day=1)
                    end_month518 = end_first518 -relativedelta(days=1)+relativedelta(months=1)

                    sql518='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Proceeds Received" and acctype="Other Income"'
                    sql518_val=(last_month518,end_month518,dtl_cmp_pro[0],)
                    fbcursor.execute(sql518,sql518_val)
                    mnt518=fbcursor.fetchone()

                    today418 = date.today()
                    first418 = today418.replace(day=1)
                    last_month418 = first418 -relativedelta(months=3)
                    
                    end_today418 = last_month418
                    end_first418 = end_today418.replace(day=1)
                    end_month418 = end_first418 -relativedelta(days=1)+relativedelta(months=1)

                    sql418='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Proceeds Received" and acctype="Other Income"'
                    sql418_val=(last_month418,end_month418,dtl_cmp_pro[0],)
                    fbcursor.execute(sql418,sql418_val)
                    mnt418=fbcursor.fetchone()

                    today318 = date.today()
                    first318 = today318.replace(day=1)
                    last_month318 = first318 -relativedelta(months=2)
                    
                    end_today318 = last_month318
                    end_first318 = end_today318.replace(day=1)
                    end_month318 = end_first318 -relativedelta(days=1)+relativedelta(months=1)

                    sql318='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Proceeds Received" and acctype="Other Income"'
                    sql318_val=(last_month318,end_month318,dtl_cmp_pro[0],)
                    fbcursor.execute(sql318,sql318_val)
                    mnt318=fbcursor.fetchone()

                    today218 = date.today()
                    first218 = today218.replace(day=1)
                    last_month218 = first218 -relativedelta(months=1)
                    
                    end_today218 = last_month218
                    end_first218 = end_today218.replace(day=1)
                    end_month218 = end_first218 -relativedelta(days=1)+relativedelta(months=1)

                    sql218='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Proceeds Received" and acctype="Other Income"'
                    sql218_val=(last_month218,end_month218,dtl_cmp_pro[0],)
                    fbcursor.execute(sql218,sql218_val)
                    mnt218=fbcursor.fetchone()

                    today181 = date.today()
                    first181 = today181.replace(day=1)
              

                    end_today181 = date.today()
                    end_first181 = end_today181.replace(day=1)
                    end_month181 = end_first181 -relativedelta(days=1)+relativedelta(months=1)

                    sql181='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Proceeds Received" and acctype="Other Income"'
                    sql181_val=(first181,end_month181,dtl_cmp_pro[0],)
                    fbcursor.execute(sql181,sql181_val)
                    mnt181=fbcursor.fetchone()

                    sqltt18='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Proceeds Received" and acctype="Other Income"'
                    sqltt_val18=(last_monthy_gt18,end_month181,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt18,sqltt_val18)
                    mnttt18=fbcursor.fetchone()
                    
                    if mnty_gt18[0] is None:
                        val618="0.0"
                    else:
                        val618=mnty_gt18[0] 
                    r18c2.delete(0,END)
                    r18c2.insert(0,"$"+str(val618))
                    r18c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt518[0] is None:
                        val518="0.0"
                    else:
                        val518=mnt518[0] 
                    r18c3.delete(0,END)
                    r18c3.insert(0,"$"+str(val518))
                    r18c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt418[0] is None:
                        val418="0.0"
                    else:
                        val418=mnt418[0] 
                    r18c4.delete(0,END)
                    r18c4.insert(0,"$"+str(val418))
                    r18c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt318[0] is None:
                        val318="0.0"
                    else:
                        val318=mnt318[0] 
                    r18c5.delete(0,END)
                    r18c5.insert(0,"$"+str(val318))
                    r18c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt218[0] is None:
                        val218="0.0"
                    else:
                        val218=mnt218[0] 
                    r18c6.delete(0,END)
                    r18c6.insert(0,"$"+str(val218))
                    r18c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt181[0] is None:
                        val181="0.0"
                    else:
                        val181=mnt181[0] 
                    r18c7.delete(0,END)
                    r18c7.insert(0,"$"+str(val181))
                    r18c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt18[0] is None:
                        valtt18="0.0"
                    else:
                        valtt18=mnttt18[0] 
                    r18c8.delete(0,END)
                    r18c8.insert(0,"$"+str(valtt18))
                    r18c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    #----------------------------------------------------------19 th row
                    lv_name=Label(frm_analiz, text="Interest Income",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r19c1"))

                    r19c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r19c2, tag=("r19c2"))

                    r19c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1) 
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r19c3, tag=("r19c3"))

                    r19c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r19c4, tag=("r19c4"))


                    r19c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r19c5, tag=("r19c5"))

                    r19c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r19c6, tag=("r19c6"))


                    r19c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r19c7, tag=("r19c7"))

                    r19c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                 
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r19c8, tag=("r19c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt19 = date.today()
                    firsty_gt19= today_gt19.replace(day=1)
                    last_monthy_gt19 = firsty_gt19 -relativedelta(months=5)
                    
                    end_todayy_gt19 = last_monthy_gt19
                    end_firsty_gt19 = end_todayy_gt19.replace(day=1)
                    end_monthy_gt19 = end_firsty_gt19 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt19='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Interest Income" and acctype="Other Income"'
                    sqly_gt19_val=(last_monthy_gt19,end_monthy_gt19,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt19,sqly_gt19_val)
                    mnty_gt19=fbcursor.fetchone()
                    


                    today519 = date.today()
                    first519 = today519.replace(day=1)
                    last_month519 = first519 -relativedelta(months=4)
                    
                    end_today519 = last_month519
                    end_first519 = end_today519.replace(day=1)
                    end_month519 = end_first519 -relativedelta(days=1)+relativedelta(months=1)

                    sql519='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Interest Income" and acctype="Other Income"'
                    sql519_val=(last_month519,end_month519,dtl_cmp_pro[0],)
                    fbcursor.execute(sql519,sql519_val)
                    mnt519=fbcursor.fetchone()

                    today419 = date.today()
                    first419 = today419.replace(day=1)
                    last_month419 = first419 -relativedelta(months=3)
                    
                    end_today419 = last_month419
                    end_first419 = end_today419.replace(day=1)
                    end_month419 = end_first419 -relativedelta(days=1)+relativedelta(months=1)

                    sql419='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Interest Income" and acctype="Other Income"'
                    sql419_val=(last_month419,end_month419,dtl_cmp_pro[0],)
                    fbcursor.execute(sql419,sql419_val)
                    mnt419=fbcursor.fetchone()

                    today319 = date.today()
                    first319 = today319.replace(day=1)
                    last_month319 = first319 -relativedelta(months=2)
                    
                    end_today319 = last_month319
                    end_first319 = end_today319.replace(day=1)
                    end_month319 = end_first319 -relativedelta(days=1)+relativedelta(months=1)

                    sql319='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Interest Income" and acctype="Other Income"'
                    sql319_val=(last_month319,end_month319,dtl_cmp_pro[0],)
                    fbcursor.execute(sql319,sql319_val)
                    mnt319=fbcursor.fetchone()

                    today219 = date.today()
                    first219 = today219.replace(day=1)
                    last_month219 = first219 -relativedelta(months=1)
                    
                    end_today219 = last_month219
                    end_first219 = end_today219.replace(day=1)
                    end_month219 = end_first219 -relativedelta(days=1)+relativedelta(months=1)

                    sql219='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Interest Income" and acctype="Other Income"'
                    sql219_val=(last_month219,end_month219,dtl_cmp_pro[0],)
                    fbcursor.execute(sql219,sql219_val)
                    mnt219=fbcursor.fetchone()

                    today191 = date.today()
                    first191 = today191.replace(day=1)
              

                    end_today191 = date.today()
                    end_first191 = end_today191.replace(day=1)
                    end_month191 = end_first191 -relativedelta(days=1)+relativedelta(months=1)

                    sql191='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Interest Income" and acctype="Other Income"'
                    sql191_val=(first191,end_month191,dtl_cmp_pro[0],)
                    fbcursor.execute(sql191,sql191_val)
                    mnt191=fbcursor.fetchone()

                    sqltt19='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Interest Income" and acctype="Other Income"'
                    sqltt_val19=(last_monthy_gt19,end_month191,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt19,sqltt_val19)
                    mnttt19=fbcursor.fetchone()
                    
                    if mnty_gt19[0] is None:
                        val619="0.0"
                    else:
                        val619=mnty_gt19[0] 
                    r19c2.delete(0,END)
                    r19c2.insert(0,"$"+str(val619))
                    r19c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt519[0] is None:
                        val519="0.0"
                    else:
                        val519=mnt519[0] 
                    r19c3.delete(0,END)
                    r19c3.insert(0,"$"+str(val519))
                    r19c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt419[0] is None:
                        val419="0.0"
                    else:
                        val419=mnt419[0] 
                    r19c4.delete(0,END)
                    r19c4.insert(0,"$"+str(val419))
                    r19c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt319[0] is None:
                        val319="0.0"
                    else:
                        val319=mnt319[0] 
                    r19c5.delete(0,END)
                    r19c5.insert(0,"$"+str(val319))
                    r19c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt219[0] is None:
                        val219="0.0"
                    else:
                        val219=mnt219[0] 
                    r19c6.delete(0,END)
                    r19c6.insert(0,"$"+str(val219))
                    r19c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt191[0] is None:
                        val191="0.0"
                    else:
                        val191=mnt191[0] 
                    r19c7.delete(0,END)
                    r19c7.insert(0,"$"+str(val191))
                    r19c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt19[0] is None:
                        valtt19="0.0"
                    else:
                        valtt19=mnttt19[0] 
                    r19c8.delete(0,END)
                    r19c8.insert(0,"$"+str(valtt19))
                    r19c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 


                    #----------------------------------------------------------20 th row
                    lv_name=Label(frm_analiz, text="Proceeds From Sale of Assets",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r20c1"))

                    r20c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1) 
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r20c2, tag=("r20c2"))

                    r20c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r20c3, tag=("r20c3"))

                    r20c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r20c4, tag=("r20c4"))


                    r20c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r20c5, tag=("r20c5"))

                    r20c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r20c6, tag=("r20c6"))


                    r20c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r20c7, tag=("r20c7"))

                    r20c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                 
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r20c8, tag=("r20c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt20 = date.today()
                    firsty_gt20= today_gt20.replace(day=1)
                    last_monthy_gt20 = firsty_gt20 -relativedelta(months=5)
                    
                    end_todayy_gt20 = last_monthy_gt20
                    end_firsty_gt20 = end_todayy_gt20.replace(day=1)
                    end_monthy_gt20 = end_firsty_gt20 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt20='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Proceeds From Sale of Assets" and acctype="Other Income"'
                    sqly_gt20_val=(last_monthy_gt20,end_monthy_gt20,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt20,sqly_gt20_val)
                    mnty_gt20=fbcursor.fetchone()
                    


                    today520 = date.today()
                    first520 = today520.replace(day=1)
                    last_month520 = first520 -relativedelta(months=4)
                    
                    end_today520 = last_month520
                    end_first520 = end_today520.replace(day=1)
                    end_month520 = end_first520 -relativedelta(days=1)+relativedelta(months=1)

                    sql520='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Proceeds From Sale of Assets" and acctype="Other Income"'
                    sql520_val=(last_month520,end_month520,dtl_cmp_pro[0],)
                    fbcursor.execute(sql520,sql520_val)
                    mnt520=fbcursor.fetchone()

                    today420 = date.today()
                    first420 = today420.replace(day=1)
                    last_month420 = first420 -relativedelta(months=3)
                    
                    end_today420 = last_month420
                    end_first420 = end_today420.replace(day=1)
                    end_month420 = end_first420 -relativedelta(days=1)+relativedelta(months=1)

                    sql420='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Proceeds From Sale of Assets" and acctype="Other Income"'
                    sql420_val=(last_month420,end_month420,dtl_cmp_pro[0],)
                    fbcursor.execute(sql420,sql420_val)
                    mnt420=fbcursor.fetchone()

                    today320 = date.today()
                    first320 = today320.replace(day=1)
                    last_month320 = first320 -relativedelta(months=2)
                    
                    end_today320 = last_month320
                    end_first320 = end_today320.replace(day=1)
                    end_month320 = end_first320 -relativedelta(days=1)+relativedelta(months=1)

                    sql320='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Proceeds From Sale of Assets" and acctype="Other Income"'
                    sql320_val=(last_month320,end_month320,dtl_cmp_pro[0],)
                    fbcursor.execute(sql320,sql320_val)
                    mnt320=fbcursor.fetchone()

                    today220 = date.today()
                    first220 = today220.replace(day=1)
                    last_month220 = first220 -relativedelta(months=1)
                    
                    end_today220 = last_month220
                    end_first220 = end_today220.replace(day=1)
                    end_month220 = end_first220 -relativedelta(days=1)+relativedelta(months=1)

                    sql220='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Proceeds From Sale of Assets" and acctype="Other Income"'
                    sql220_val=(last_month220,end_month220,dtl_cmp_pro[0],)
                    fbcursor.execute(sql220,sql220_val)
                    mnt220=fbcursor.fetchone()

                    today201 = date.today()
                    first201 = today201.replace(day=1)
              

                    end_today201 = date.today()
                    end_first201 = end_today201.replace(day=1)
                    end_month201 = end_first201 -relativedelta(days=1)+relativedelta(months=1)

                    sql201='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Proceeds From Sale of Assets" and acctype="Other Income"'
                    sql201_val=(first201,end_month201,dtl_cmp_pro[0],)
                    fbcursor.execute(sql201,sql201_val)
                    mnt201=fbcursor.fetchone()

                    sqltt20='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Proceeds From Sale of Assets" and acctype="Other Income"'
                    sqltt_val20=(last_monthy_gt20,end_month201,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt20,sqltt_val20)
                    mnttt20=fbcursor.fetchone()
                    
                    if mnty_gt20[0] is None:
                        val620="0.0"
                    else:
                        val620=mnty_gt20[0] 
                    r20c2.delete(0,END)
                    r20c2.insert(0,"$"+str(val620))
                    r20c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt520[0] is None:
                        val520="0.0"
                    else:
                        val520=mnt520[0] 
                    r20c3.delete(0,END)
                    r20c3.insert(0,"$"+str(val520))
                    r20c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt420[0] is None:
                        val420="0.0"
                    else:
                        val420=mnt420[0] 
                    r20c4.delete(0,END)
                    r20c4.insert(0,"$"+str(val420))
                    r20c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt320[0] is None:
                        val320="0.0"
                    else:
                        val320=mnt320[0] 
                    r20c5.delete(0,END)
                    r20c5.insert(0,"$"+str(val320))
                    r20c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt220[0] is None:
                        val220="0.0"
                    else:
                        val220=mnt220[0] 
                    r20c6.delete(0,END)
                    r20c6.insert(0,"$"+str(val220))
                    r20c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt201[0] is None:
                        val201="0.0"
                    else:
                        val201=mnt201[0] 
                    r20c7.delete(0,END)
                    r20c7.insert(0,"$"+str(val201))
                    r20c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt20[0] is None:
                        valtt20="0.0"
                    else:
                        valtt20=mnttt20[0] 
                    r20c8.delete(0,END)
                    r20c8.insert(0,"$"+str(valtt20))
                    r20c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")    

                    #----------------------------------------------------------21 th row
                    lv_name=Label(frm_analiz, text="Shipping and Delivery Income",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r21c1"))

                    r21c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r21c2, tag=("r21c2"))

                    r21c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r21c3, tag=("r21c3"))

                    r21c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r21c4, tag=("r21c4"))


                    r21c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r21c5, tag=("r21c5"))

                    r21c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r21c6, tag=("r21c6"))


                    r21c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r21c7, tag=("r21c7"))

                    r21c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r21c8, tag=("r21c8"))

                    #----------------------------------------------------------------------calcu
                    today_g21 = date.today()
                    firsty_g21= today_g21.replace(day=1)
                    last_monthy_g21 = firsty_g21 -relativedelta(months=5)
                    
                    end_todayy_g21 = last_monthy_g21
                    end_firsty_g21 = end_todayy_g21.replace(day=1)
                    end_monthy_g21 = end_firsty_g21 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_g21='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Shipping and Delivery Income" and acctype="Other Income"'
                    sqly_g21_val=(last_monthy_g21,end_monthy_g21,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_g21,sqly_g21_val)
                    mnty_g21=fbcursor.fetchone()
                    


                    today21 = date.today()
                    first21 = today21.replace(day=1)
                    last_month21 = first21 -relativedelta(months=4)
                    
                    end_today21 = last_month21
                    end_first21 = end_today21.replace(day=1)
                    end_month21 = end_first21 -relativedelta(days=1)+relativedelta(months=1)

                    sql21='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Shipping and Delivery Income" and acctype="Other Income"'
                    sql21_val=(last_month21,end_month21,dtl_cmp_pro[0],)
                    fbcursor.execute(sql21,sql21_val)
                    mnt21=fbcursor.fetchone()

                    today21 = date.today()
                    first21 = today21.replace(day=1)
                    last_month21 = first21 -relativedelta(months=3)
                    
                    end_today21 = last_month21
                    end_first21 = end_today21.replace(day=1)
                    end_month21 = end_first21 -relativedelta(days=1)+relativedelta(months=1)

                    sql21='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Shipping and Delivery Income" and acctype="Other Income"'
                    sql21_val=(last_month21,end_month21,dtl_cmp_pro[0],)
                    fbcursor.execute(sql21,sql21_val)
                    mnt21=fbcursor.fetchone()

                    today21 = date.today()
                    first21 = today21.replace(day=1)
                    last_month21 = first21 -relativedelta(months=2)
                    
                    end_today21 = last_month21
                    end_first21 = end_today21.replace(day=1)
                    end_month21 = end_first21 -relativedelta(days=1)+relativedelta(months=1)

                    sql21='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Shipping and Delivery Income" and acctype="Other Income"'
                    sql21_val=(last_month21,end_month21,dtl_cmp_pro[0],)
                    fbcursor.execute(sql21,sql21_val)
                    mnt21=fbcursor.fetchone()

                    today21 = date.today()
                    first21 = today21.replace(day=1)
                    last_month21 = first21 -relativedelta(months=1)
                    
                    end_today21 = last_month21
                    end_first21 = end_today21.replace(day=1)
                    end_month21 = end_first21 -relativedelta(days=1)+relativedelta(months=1)

                    sql21='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Shipping and Delivery Income" and acctype="Other Income"'
                    sql21_val=(last_month21,end_month21,dtl_cmp_pro[0],)
                    fbcursor.execute(sql21,sql21_val)
                    mnt21=fbcursor.fetchone()

                    toda211 = date.today()
                    firs211 = toda211.replace(day=1)
              

                    end_toda211 = date.today()
                    end_firs211 = end_toda211.replace(day=1)
                    end_mont211 = end_firs211 -relativedelta(days=1)+relativedelta(months=1)

                    sq211='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Shipping and Delivery Income" and acctype="Other Income"'
                    sq211_val=(firs211,end_mont211,dtl_cmp_pro[0],)
                    fbcursor.execute(sq211,sq211_val)
                    mn211=fbcursor.fetchone()

                    sqlt21='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Shipping and Delivery Income" and acctype="Other Income"'
                    sqltt_va21=(last_monthy_g21,end_mont211,dtl_cmp_pro[0],)
                    fbcursor.execute(sqlt21,sqltt_va21)
                    mntt21=fbcursor.fetchone()
                    
                    if mnty_g21[0] is None:
                        val21="0.0"
                    else:
                        val21=mnty_g21[0] 
                    r21c2.delete(0,END)
                    r21c2.insert(0,"$"+str(val21))
                    r21c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt21[0] is None:
                        val21="0.0"
                    else:
                        val21=mnt21[0] 
                    r21c3.delete(0,END)
                    r21c3.insert(0,"$"+str(val21))
                    r21c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt21[0] is None:
                        val21="0.0"
                    else:
                        val21=mnt21[0] 
                    r21c4.delete(0,END)
                    r21c4.insert(0,"$"+str(val21))
                    r21c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt21[0] is None:
                        val21="0.0"
                    else:
                        val21=mnt21[0] 
                    r21c5.delete(0,END)
                    r21c5.insert(0,"$"+str(val21))
                    r21c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt21[0] is None:
                        val21="0.0"
                    else:
                        val21=mnt21[0] 
                    r21c6.delete(0,END)
                    r21c6.insert(0,"$"+str(val21))
                    r21c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mn211[0] is None:
                        va211="0.0"
                    else:
                        va211=mn211[0] 
                    r21c7.delete(0,END)
                    r21c7.insert(0,"$"+str(va211))
                    r21c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mntt21[0] is None:
                        valt21="0.0"
                    else:
                        valt21=mntt21[0] 
                    r21c8.delete(0,END)
                    r21c8.insert(0,"$"+str(valt21))
                    r21c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")    
                    

                    #----------------------------------------------------------22 th row
                    lv_name=Label(frm_analiz, text="Total Cash Inflows",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r22c1"))

                    r22c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r22c2, tag=("r22c2"))

                    r22c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r22c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r22c3, tag=("r22c3"))

                    r22c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r22c4, tag=("r22c4"))


                    r22c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r22c5, tag=("r22c5"))

                    r22c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r22c6, tag=("r22c6"))


                    r22c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r22c7, tag=("r22c7"))

                    r22c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r22c8, tag=("r22c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt22 = date.today()
                    firsty_gt22= today_gt22.replace(day=1)
                    last_monthy_gt22 = firsty_gt22 -relativedelta(months=5)
                    
                    end_todayy_gt22 = last_monthy_gt22
                    end_firsty_gt22 = end_todayy_gt22.replace(day=1)
                    end_monthy_gt22 = end_firsty_gt22 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt22='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype="Income"'
                    sqly_gt22_val=(last_monthy_gt22,end_monthy_gt22,dtl_cmp_pro[0], )
                    fbcursor.execute(sqly_gt22,sqly_gt22_val)
                    mnty_gt22=fbcursor.fetchone()

                    sqly_gt22_2='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype="Other Income"'
                    sqly_gt22_2val=(last_monthy_gt22,end_monthy_gt22,dtl_cmp_pro[0], )
                    fbcursor.execute(sqly_gt22_2,sqly_gt22_2val)
                    mnty_gt22_2=fbcursor.fetchone()

                    
                    today522 = date.today()
                    first522 = today522.replace(day=1)
                    last_month522 = first522 -relativedelta(months=4)
                    
                    end_today522 = last_month522
                    end_first522 = end_today522.replace(day=1)
                    end_month522 = end_first522 -relativedelta(days=1)+relativedelta(months=1)

                    sql522='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype="Income"'
                    sql522_val=(last_month522,end_month522,dtl_cmp_pro[0],)
                    fbcursor.execute(sql522,sql522_val)
                    mnt522=fbcursor.fetchone()

                    sql5_22_2='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype="Other Income"'
                    sql5_22_2_val=(last_month522,end_month522,dtl_cmp_pro[0],)
                    fbcursor.execute(sql5_22_2,sql5_22_2_val)
                    mnt5_22_2=fbcursor.fetchone()

                    


                    today422 = date.today()
                    first422 = today422.replace(day=1)
                    last_month422 = first422 -relativedelta(months=3)
                    
                    end_today422 = last_month422
                    end_first422 = end_today422.replace(day=1)
                    end_month422 = end_first422 -relativedelta(days=1)+relativedelta(months=1)

                    sql422='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype="Income"'
                    sql422_val=(last_month422,end_month422,dtl_cmp_pro[0],)
                    fbcursor.execute(sql422,sql422_val)
                    mnt422=fbcursor.fetchone()

                    sql422_2='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype="Other Income"'
                    sql422_val_2=(last_month422,end_month422,dtl_cmp_pro[0],)
                    fbcursor.execute(sql422_2,sql422_val_2)
                    mnt422__2=fbcursor.fetchone()

                    today322 = date.today()
                    first322 = today322.replace(day=1)
                    last_month322 = first322 -relativedelta(months=2)
                    
                    end_today322 = last_month322
                    end_first322 = end_today322.replace(day=1)
                    end_month322 = end_first322 -relativedelta(days=1)+relativedelta(months=1)

                    sql322='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype="Income"'
                    sql322_val=(last_month322,end_month322,dtl_cmp_pro[0],)
                    fbcursor.execute(sql322,sql322_val)
                    mnt322=fbcursor.fetchone()

                    sql322_2='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype="Other Income"'
                    sql322_val_2=(last_month322,end_month322,dtl_cmp_pro[0],)
                    fbcursor.execute(sql322_2,sql322_val_2)
                    mnt322_2=fbcursor.fetchone()

                    today222 = date.today()
                    first222 = today222.replace(day=1)
                    last_month222 = first222 -relativedelta(months=1)
                    
                    end_today222 = last_month222
                    end_first222 = end_today222.replace(day=1)
                    end_month222 = end_first222 -relativedelta(days=1)+relativedelta(months=1)

                    sql222='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype="Income"'
                    sql222_val=(last_month222,end_month222,dtl_cmp_pro[0],)
                    fbcursor.execute(sql222,sql222_val)
                    mnt222=fbcursor.fetchone()

                    sql222_2='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype="Other Income"'
                    sql222_val_2=(last_month222,end_month222,dtl_cmp_pro[0],)
                    fbcursor.execute(sql222_2,sql222_val_2)
                    mnt222_2=fbcursor.fetchone()

                    today221 = date.today()
                    first221 = today221.replace(day=1)
              

                    end_today221 = date.today()
                    end_first221 = end_today221.replace(day=1)
                    end_month221 = end_first221 -relativedelta(days=1)+relativedelta(months=1)

                    sql221='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype="Income"'
                    sql221_val=(first221,end_month221,dtl_cmp_pro[0],)
                    fbcursor.execute(sql221,sql221_val)
                    mnt221=fbcursor.fetchone()

                    sql221_2='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype="Other Income"'
                    sql221_val_2=(first221,end_month221,dtl_cmp_pro[0],)
                    fbcursor.execute(sql221_2,sql221_val_2)
                    mnt221_2=fbcursor.fetchone()

                    sqltt22='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype="Income" and acctype="Other Income"'
                    sqltt_val22=(last_monthy_gt22,end_month221,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt22,sqltt_val22)
                    mnttt22=fbcursor.fetchone()
                    
                    if mnty_gt22[0]==None and mnty_gt22_2[0]==None:
                        val622="0.0"
                        sum6_22=0.0
                    else:
                        if mnty_gt22[0] is None:
                            in_vals22_6=0.0
                        else:
                            in_vals22_6=mnty_gt22[0]

                        if mnty_gt22_2[0]is None:
                            ot_vals22_6=0.0
                        else:
                            ot_vals22_6=mnty_gt22_2[0]

                        sum6_22=round(float(in_vals22_6)+float(ot_vals22_6),2)
                        val6_22=sum6_22
                    r22c2.delete(0,END)
                    r22c2.insert(0,"$"+str(val6_22))
                    r22c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt522[0]==None and mnt5_22_2[0]==None:
                        val622="0.0"
                        sum5_22=0.0
                    else:
                        if mnt522[0] is None:
                            in_vals22_5=0.0
                        else:
                            in_vals22_5=mnt522[0]

                        if mnt5_22_2[0]is None:
                            ot_vals22_5=0.0
                        else:
                            ot_vals22_5=mnt5_22_2[0]

                        sum5_22=round(float(in_vals22_5)+float(ot_vals22_5),2)
                        val5_22=sum5_22

                    r22c3.delete(0,END)
                    r22c3.insert(0,"$"+str(val5_22))
                    r22c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt422[0]==None and mnt422__2[0]==None:
                        val4_22="0.0"
                        sum4_22=0.0
                    else:
                        if mnt422[0] is None:
                            in_vals22_4=0.0
                        else:
                            in_vals22_4=mnt422[0]

                        if mnt422__2[0]is None:
                            ot_vals22_4=0.0
                        else:
                            ot_vals22_4=mnt422__2[0]

                        sum4_22=round(float(in_vals22_4)+float(ot_vals22_4),2)
                        val4_22=sum4_22
                    r22c4.delete(0,END)
                    r22c4.insert(0,"$"+str(val4_22))
                    r22c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt322[0]==None and mnt322_2[0]==None:
                        val3_22="0.0"
                        sum3_22=0.0
                    else:
                        if mnt322[0] is None:
                            in_vals22_3=0.0
                        else:
                            in_vals22_3=mnt322[0]

                        if mnt322_2[0]is None:
                            ot_vals22_3=0.0
                        else:
                            ot_vals22_3=mnt322_2[0]

                        sum3_22=round(float(in_vals22_3)+float(ot_vals22_3),2)
                        val3_22=sum3_22
                    r22c5.delete(0,END)
                    r22c5.insert(0,"$"+str(val3_22))
                    r22c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt222[0]==None and mnt222_2[0]==None:
                        val2_22="0.0"
                        sum2_22=0.0
                    else:
                        if mnt222[0] is None:
                            in_vals22_2=0.0
                        else:
                            in_vals22_2=mnt222[0]

                        if mnt222_2[0]is None:
                            ot_vals22_2=0.0
                        else:
                            ot_vals22_2=mnt222_2[0]

                        sum2_22=round(float(in_vals22_2)+float(ot_vals22_2),2)
                        val2_22=sum2_22 
                    r22c6.delete(0,END)
                    r22c6.insert(0,"$"+str(val2_22))
                    r22c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt221[0]==None and mnt221_2[0]==None:
                        val1_22="0.0"
                        sum1_22=0.0
                    else:
                        if mnt221[0] is None:
                            in_vals22_2=0.0
                        else:
                            in_vals22_2=mnt221[0]

                        if mnt221_2[0]is None:
                            ot_vals22_2=0.0
                        else:
                            ot_vals22_2=mnt221_2[0]

                        sum1_22=round(float(in_vals22_2)+float(ot_vals22_2),2)
                        val1_22=sum1_22 
                    r22c7.delete(0,END)
                    r22c7.insert(0,"$"+str(val1_22))
                    r22c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    tt_sm_22=round(float(sum1_22)+float(sum2_22)+float(sum3_22)+float(sum4_22)+float(sum5_22)+float(sum6_22),2)
                    r22c8.delete(0,END)
                    r22c8.insert(0,"$"+str(tt_sm_22))
                    r22c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")   

                    #----------------------------------------------------------23 th row
                    lv_name=Label(frm_analiz, text="Available Cash Balance",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r23c1"))

                    r23c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r23c2, tag=("r23c2"))

                    r23c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r23c3, tag=("r23c3"))

                    r23c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r23c4, tag=("r23c4"))


                    r23c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r23c5, tag=("r23c5"))

                    r23c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r23c6, tag=("r23c6"))


                    r23c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r23c7, tag=("r23c7"))

                    r23c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r23c8, tag=("r23c8"))

                    #----------------------------------------------------------------------calcu
                    
                    
                    # if mnty_gt23[0] is None:
                    #     val623="0.0"
                    # else:
                    #     val623=mnty_gt23[0] 
                    val623=round(float(sum6_22)+float(mnty_gt2[0]),2)
                    r23c2.delete(0,END)
                    r23c2.insert(0,"$"+str(val623))
                    r23c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    # if mnt523[0] is None:
                    #     val523="0.0"
                    # else:
                    #     val523=mnt523[0] 
                    val523=round(float(sum5_22)+float(mnt25[0]),2)
                    r23c3.delete(0,END)
                    r23c3.insert(0,"$"+str(val523))
                    r23c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    # if mnt423[0] is None:
                    #     val423="0.0"
                    # else:
                    #     val423=mnt423[0] 
                    val423=round(float(sum4_22)+float(mnt24[0]),2)
                    r23c4.delete(0,END)
                    r23c4.insert(0,"$"+str(val423))
                    r23c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    # if mnt323[0] is None:
                    #     val323="0.0"
                    # else:
                    #     val323=mnt323[0] 
                    val323=round(float(sum3_22)+float(mnt32[0]),2)
                    r23c5.delete(0,END)
                    r23c5.insert(0,"$"+str(val323))
                    r23c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    # if mnt232[0] is None:
                    #     val232="0.0"
                    # else:
                    #     val232=mnt232[0] 
                    val232=round(float(sum2_22)+float(mnt22[0]),2)
                    r23c6.delete(0,END)
                    r23c6.insert(0,"$"+str(val232))
                    r23c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    # if mnt231[0] is None:
                    #     val231="0.0"
                    # else:
                    #     val231=mnt231[0] 
                    val231=round(float(sum1_22)+float(mnt21[0]),2)
                    r23c7.delete(0,END)
                    r23c7.insert(0,"$"+str(val231))
                    r23c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    # if mnttt23[0] is None:
                    #     valtt23="0.0"
                    # else:
                    #     valtt23=mnttt23[0] 
                    tt_sm_23=round(float(val623)+float(val523)+float(val423)+float(val323)+float(val232)+float(val231),2)

                    r23c8.delete(0,END)
                    r23c8.insert(0,"$"+str(tt_sm_23))
                    r23c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    # #----------------------------------------------------------24 th row
                    # lv_name=Label(frm_analiz, text="",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r24c1"))

                    # r24c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r24c2, tag=("r24c2"))

                    # r24c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    # r24c3.insert(0,"$11111111111")
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r24c3, tag=("r24c3"))

                    # r24c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r24c4, tag=("r24c4"))


                    # r24c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r24c5, tag=("r24c5"))

                    # r24c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r24c6, tag=("r24c6"))


                    # r24c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r24c7, tag=("r24c7"))

                    # r24c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r24c8, tag=("r24c8"))

                    #----------------------------------------------------------25 th row
                    lv_name=Label(frm_analiz, text="Cash Outflows (Expenses):",bg="#506579", width=159, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r25c1"))

                    

                    #----------------------------------------------------------26 th row
                    lv_name=Label(frm_analiz, text="Advertising/Promotional",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r26c1"))

                    r26c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r26c2, tag=("r26c2"))

                    r26c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
        
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r26c3, tag=("r26c3"))

                    r26c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r26c4, tag=("r26c4"))


                    r26c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r26c5, tag=("r26c5"))

                    r26c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r26c6, tag=("r26c6"))


                    r26c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r26c7, tag=("r26c7"))

                    r26c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r26c8, tag=("r26c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt26 = date.today()
                    firsty_gt26= today_gt26.replace(day=1)
                    last_monthy_gt26 = firsty_gt26 -relativedelta(months=5)
                    
                    end_todayy_gt26 = last_monthy_gt26
                    end_firsty_gt26 = end_todayy_gt26.replace(day=1)
                    end_monthy_gt26 = end_firsty_gt26 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt26='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Advertising/Promotional" and acctype="Expenses"'
                    sqly_gt26_val=(last_monthy_gt26,end_monthy_gt26,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt26,sqly_gt26_val)
                    mnty_gt26=fbcursor.fetchone()
                    


                    today526 = date.today()
                    first526 = today526.replace(day=1)
                    last_month526 = first526 -relativedelta(months=4)
                    
                    end_today526 = last_month526
                    end_first526 = end_today526.replace(day=1)
                    end_month526 = end_first526 -relativedelta(days=1)+relativedelta(months=1)

                    sql526='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Advertising/Promotional" and acctype="Expenses"'
                    sql526_val=(last_month526,end_month526,dtl_cmp_pro[0],)
                    fbcursor.execute(sql526,sql526_val)
                    mnt526=fbcursor.fetchone()

                    today426 = date.today()
                    first426 = today426.replace(day=1)
                    last_month426 = first426 -relativedelta(months=3)
                    
                    end_today426 = last_month426
                    end_first426 = end_today426.replace(day=1)
                    end_month426 = end_first426 -relativedelta(days=1)+relativedelta(months=1)

                    sql426='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Advertising/Promotional" and acctype="Expenses"'
                    sql426_val=(last_month426,end_month426,dtl_cmp_pro[0],)
                    fbcursor.execute(sql426,sql426_val)
                    mnt426=fbcursor.fetchone()

                    today326 = date.today()
                    first326 = today326.replace(day=1)
                    last_month326 = first326 -relativedelta(months=2)
                    
                    end_today326 = last_month326
                    end_first326 = end_today326.replace(day=1)
                    end_month326 = end_first326 -relativedelta(days=1)+relativedelta(months=1)

                    sql326='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Advertising/Promotional" and acctype="Expenses"'
                    sql326_val=(last_month326,end_month326,dtl_cmp_pro[0],)
                    fbcursor.execute(sql326,sql326_val)
                    mnt326=fbcursor.fetchone()

                    today262 = date.today()
                    first262 = today262.replace(day=1)
                    last_month262 = first262 -relativedelta(months=1)
                    
                    end_today262 = last_month262
                    end_first262 = end_today262.replace(day=1)
                    end_month262 = end_first262 -relativedelta(days=1)+relativedelta(months=1)

                    sql262='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Advertising/Promotional" and acctype="Expenses"'
                    sql262_val=(last_month262,end_month262,dtl_cmp_pro[0],)
                    fbcursor.execute(sql262,sql262_val)
                    mnt262=fbcursor.fetchone()

                    today261 = date.today()
                    first261 = today261.replace(day=1)
              

                    end_today261 = date.today()
                    end_first261 = end_today261.replace(day=1)
                    end_month261 = end_first261 -relativedelta(days=1)+relativedelta(months=1)

                    sql261='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Advertising/Promotional" and acctype="Expenses"'
                    sql261_val=(first261,end_month261,dtl_cmp_pro[0],)
                    fbcursor.execute(sql261,sql261_val)
                    mnt261=fbcursor.fetchone()

                    sqltt26='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Advertising/Promotional" and acctype="Expenses"'
                    sqltt_val26=(last_monthy_gt26,end_month261,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt26,sqltt_val26)
                    mnttt26=fbcursor.fetchone()
                    
                    if mnty_gt26[0] is None:
                        val626="0.0"
                    else:
                        val626=mnty_gt26[0] 
                    r26c2.delete(0,END)
                    r26c2.insert(0,"$"+str(val626))
                    r26c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt526[0] is None:
                        val526="0.0"
                    else:
                        val526=mnt526[0] 
                    r26c3.delete(0,END)
                    r26c3.insert(0,"$"+str(val526))
                    r26c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt426[0] is None:
                        val426="0.0"
                    else:
                        val426=mnt426[0] 
                    r26c4.delete(0,END)
                    r26c4.insert(0,"$"+str(val426))
                    r26c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt326[0] is None:
                        val326="0.0"
                    else:
                        val326=mnt326[0] 
                    r26c5.delete(0,END)
                    r26c5.insert(0,"$"+str(val326))
                    r26c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt262[0] is None:
                        val262="0.0"
                    else:
                        val262=mnt262[0] 
                    r26c6.delete(0,END)
                    r26c6.insert(0,"$"+str(val262))
                    r26c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt261[0] is None:
                        val261="0.0"
                    else:
                        val261=mnt261[0] 
                    r26c7.delete(0,END)
                    r26c7.insert(0,"$"+str(val261))
                    r26c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt26[0] is None:
                        valtt26="0.0"
                    else:
                        valtt26=mnttt26[0] 
                    r26c8.delete(0,END)
                    r26c8.insert(0,"$"+str(valtt26))
                    r26c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 


                    #----------------------------------------------------------27 th row
                    lv_name=Label(frm_analiz, text="Bank Charges",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r27c1"))

                    r27c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r27c2, tag=("r27c2"))

                    r27c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r27c3, tag=("r27c3"))

                    r27c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r27c4, tag=("r27c4"))


                    r27c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r27c5, tag=("r27c5"))

                    r27c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r27c6, tag=("r27c6"))


                    r27c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r27c7, tag=("r27c7"))

                    r27c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r27c8, tag=("r27c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt27 = date.today()
                    firsty_gt27= today_gt27.replace(day=1)
                    last_monthy_gt27 = firsty_gt27 -relativedelta(months=5)
                    
                    end_todayy_gt27 = last_monthy_gt27
                    end_firsty_gt27 = end_todayy_gt27.replace(day=1)
                    end_monthy_gt27 = end_firsty_gt27 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt27='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Bank Charges" and acctype="Expenses"'
                    sqly_gt27_val=(last_monthy_gt27,end_monthy_gt27,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt27,sqly_gt27_val)
                    mnty_gt27=fbcursor.fetchone()
                    


                    today527 = date.today()
                    first527 = today527.replace(day=1)
                    last_month527 = first527 -relativedelta(months=4)
                    
                    end_today527 = last_month527
                    end_first527 = end_today527.replace(day=1)
                    end_month527 = end_first527 -relativedelta(days=1)+relativedelta(months=1)

                    sql527='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Bank Charges" and acctype="Expenses"'
                    sql527_val=(last_month527,end_month527,dtl_cmp_pro[0],)
                    fbcursor.execute(sql527,sql527_val)
                    mnt527=fbcursor.fetchone()

                    today427 = date.today()
                    first427 = today427.replace(day=1)
                    last_month427 = first427 -relativedelta(months=3)
                    
                    end_today427 = last_month427
                    end_first427 = end_today427.replace(day=1)
                    end_month427 = end_first427 -relativedelta(days=1)+relativedelta(months=1)

                    sql427='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Bank Charges" and acctype="Expenses"'
                    sql427_val=(last_month427,end_month427,dtl_cmp_pro[0],)
                    fbcursor.execute(sql427,sql427_val)
                    mnt427=fbcursor.fetchone()

                    today327 = date.today()
                    first327 = today327.replace(day=1)
                    last_month327 = first327 -relativedelta(months=2)
                    
                    end_today327 = last_month327
                    end_first327 = end_today327.replace(day=1)
                    end_month327 = end_first327 -relativedelta(days=1)+relativedelta(months=1)

                    sql327='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Bank Charges" and acctype="Expenses"'
                    sql327_val=(last_month327,end_month327,dtl_cmp_pro[0],)
                    fbcursor.execute(sql327,sql327_val)
                    mnt327=fbcursor.fetchone()

                    today272 = date.today()
                    first272 = today272.replace(day=1)
                    last_month272 = first272 -relativedelta(months=1)
                    
                    end_today272 = last_month272
                    end_first272 = end_today272.replace(day=1)
                    end_month272 = end_first272 -relativedelta(days=1)+relativedelta(months=1)

                    sql272='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Bank Charges" and acctype="Expenses"'
                    sql272_val=(last_month272,end_month272,dtl_cmp_pro[0],)
                    fbcursor.execute(sql272,sql272_val)
                    mnt272=fbcursor.fetchone()

                    today271 = date.today()
                    first271 = today271.replace(day=1)
              

                    end_today271 = date.today()
                    end_first271 = end_today271.replace(day=1)
                    end_month271 = end_first271 -relativedelta(days=1)+relativedelta(months=1)

                    sql271='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Bank Charges" and acctype="Expenses"'
                    sql271_val=(first271,end_month271,dtl_cmp_pro[0],)
                    fbcursor.execute(sql271,sql271_val)
                    mnt271=fbcursor.fetchone()

                    sqltt27='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Bank Charges" and acctype="Expenses"'
                    sqltt_val27=(last_monthy_gt27,end_month271,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt27,sqltt_val27)
                    mnttt27=fbcursor.fetchone()
                    
                    if mnty_gt27[0] is None:
                        val627="0.0"
                    else:
                        val627=mnty_gt27[0] 
                    r27c2.delete(0,END)
                    r27c2.insert(0,"$"+str(val627))
                    r27c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt527[0] is None:
                        val527="0.0"
                    else:
                        val527=mnt527[0] 
                    r27c3.delete(0,END)
                    r27c3.insert(0,"$"+str(val527))
                    r27c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt427[0] is None:
                        val427="0.0"
                    else:
                        val427=mnt427[0] 
                    r27c4.delete(0,END)
                    r27c4.insert(0,"$"+str(val427))
                    r27c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt327[0] is None:
                        val327="0.0"
                    else:
                        val327=mnt327[0] 
                    r27c5.delete(0,END)
                    r27c5.insert(0,"$"+str(val327))
                    r27c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt272[0] is None:
                        val272="0.0"
                    else:
                        val272=mnt272[0] 
                    r27c6.delete(0,END)
                    r27c6.insert(0,"$"+str(val272))
                    r27c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt271[0] is None:
                        val271="0.0"
                    else:
                        val271=mnt271[0] 
                    r27c7.delete(0,END)
                    r27c7.insert(0,"$"+str(val271))
                    r27c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt27[0] is None:
                        valtt27="0.0"
                    else:
                        valtt27=mnttt27[0] 
                    r27c8.delete(0,END)
                    r27c8.insert(0,"$"+str(valtt27))
                    r27c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 


                    #----------------------------------------------------------28 th row
                    lv_name=Label(frm_analiz, text="Business Licenses and Permitts",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r28c1"))

                    r28c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r28c2, tag=("r28c2"))

                    r28c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r28c3, tag=("r28c3"))

                    r28c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r28c4, tag=("r28c4"))


                    r28c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r28c5, tag=("r28c5"))

                    r28c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r28c6, tag=("r28c6"))


                    r28c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r28c7, tag=("r28c7"))

                    r28c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r28c8, tag=("r28c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt28 = date.today()
                    firsty_gt28= today_gt28.replace(day=1)
                    last_monthy_gt28 = firsty_gt28 -relativedelta(months=5)
                    
                    end_todayy_gt28 = last_monthy_gt28
                    end_firsty_gt28 = end_todayy_gt28.replace(day=1)
                    end_monthy_gt28 = end_firsty_gt28 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt28='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Business Licenses and Permitts" and acctype="Expenses"'
                    sqly_gt28_val=(last_monthy_gt28,end_monthy_gt28,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt28,sqly_gt28_val)
                    mnty_gt28=fbcursor.fetchone()
                    


                    today528 = date.today()
                    first528 = today528.replace(day=1)
                    last_month528 = first528 -relativedelta(months=4)
                    
                    end_today528 = last_month528
                    end_first528 = end_today528.replace(day=1)
                    end_month528 = end_first528 -relativedelta(days=1)+relativedelta(months=1)

                    sql528='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Business Licenses and Permitts" and acctype="Expenses"'
                    sql528_val=(last_month528,end_month528,dtl_cmp_pro[0],)
                    fbcursor.execute(sql528,sql528_val)
                    mnt528=fbcursor.fetchone()

                    today428 = date.today()
                    first428 = today428.replace(day=1)
                    last_month428 = first428 -relativedelta(months=3)
                    
                    end_today428 = last_month428
                    end_first428 = end_today428.replace(day=1)
                    end_month428 = end_first428 -relativedelta(days=1)+relativedelta(months=1)

                    sql428='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Business Licenses and Permitts" and acctype="Expenses"'
                    sql428_val=(last_month428,end_month428,dtl_cmp_pro[0],)
                    fbcursor.execute(sql428,sql428_val)
                    mnt428=fbcursor.fetchone()

                    today328 = date.today()
                    first328 = today328.replace(day=1)
                    last_month328 = first328 -relativedelta(months=2)
                    
                    end_today328 = last_month328
                    end_first328 = end_today328.replace(day=1)
                    end_month328 = end_first328 -relativedelta(days=1)+relativedelta(months=1)

                    sql328='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Business Licenses and Permitts" and acctype="Expenses"'
                    sql328_val=(last_month328,end_month328,dtl_cmp_pro[0],)
                    fbcursor.execute(sql328,sql328_val)
                    mnt328=fbcursor.fetchone()

                    today282 = date.today()
                    first282 = today282.replace(day=1)
                    last_month282 = first282 -relativedelta(months=1)
                    
                    end_today282 = last_month282
                    end_first282 = end_today282.replace(day=1)
                    end_month282 = end_first282 -relativedelta(days=1)+relativedelta(months=1)

                    sql282='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Business Licenses and Permitts" and acctype="Expenses"'
                    sql282_val=(last_month282,end_month282,dtl_cmp_pro[0],)
                    fbcursor.execute(sql282,sql282_val)
                    mnt282=fbcursor.fetchone()

                    today281 = date.today()
                    first281 = today281.replace(day=1)
              

                    end_today281 = date.today()
                    end_first281 = end_today281.replace(day=1)
                    end_month281 = end_first281 -relativedelta(days=1)+relativedelta(months=1)

                    sql281='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Business Licenses and Permitts" and acctype="Expenses"'
                    sql281_val=(first281,end_month281,dtl_cmp_pro[0],)
                    fbcursor.execute(sql281,sql281_val)
                    mnt281=fbcursor.fetchone()

                    sqltt28='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Business Licenses and Permitts" and acctype="Expenses"'
                    sqltt_val28=(last_monthy_gt28,end_month281,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt28,sqltt_val28)
                    mnttt28=fbcursor.fetchone()
                    
                    if mnty_gt28[0] is None:
                        val628="0.0"
                    else:
                        val628=mnty_gt28[0] 
                    r28c2.delete(0,END)
                    r28c2.insert(0,"$"+str(val628))
                    r28c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt528[0] is None:
                        val528="0.0"
                    else:
                        val528=mnt528[0] 
                    r28c3.delete(0,END)
                    r28c3.insert(0,"$"+str(val528))
                    r28c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt428[0] is None:
                        val428="0.0"
                    else:
                        val428=mnt428[0] 
                    r28c4.delete(0,END)
                    r28c4.insert(0,"$"+str(val428))
                    r28c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt328[0] is None:
                        val328="0.0"
                    else:
                        val328=mnt328[0] 
                    r28c5.delete(0,END)
                    r28c5.insert(0,"$"+str(val328))
                    r28c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt282[0] is None:
                        val282="0.0"
                    else:
                        val282=mnt282[0] 
                    r28c6.delete(0,END)
                    r28c6.insert(0,"$"+str(val282))
                    r28c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt281[0] is None:
                        val281="0.0"
                    else:
                        val281=mnt281[0] 
                    r28c7.delete(0,END)
                    r28c7.insert(0,"$"+str(val281))
                    r28c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt28[0] is None:
                        valtt28="0.0"
                    else:
                        valtt28=mnttt28[0] 
                    r28c8.delete(0,END)
                    r28c8.insert(0,"$"+str(valtt28))
                    r28c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 
                    #----------------------------------------------------------29 th row
                    lv_name=Label(frm_analiz, text="Computer and Internet Expense",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r29c1"))

                    r29c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r29c2, tag=("r29c2"))

                    r29c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)

                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r29c3, tag=("r29c3"))

                    r29c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r29c4, tag=("r29c4"))


                    r29c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r29c5, tag=("r29c5"))

                    r29c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r29c6, tag=("r29c6"))


                    r29c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r29c7, tag=("r29c7"))

                    r29c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r29c8, tag=("r29c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt29 = date.today()
                    firsty_gt29= today_gt29.replace(day=1)
                    last_monthy_gt29 = firsty_gt29 -relativedelta(months=5)
                    
                    end_todayy_gt29 = last_monthy_gt29
                    end_firsty_gt29 = end_todayy_gt29.replace(day=1)
                    end_monthy_gt29 = end_firsty_gt29 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt29='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Computer and Internet Expense" and acctype="Expenses"'
                    sqly_gt29_val=(last_monthy_gt29,end_monthy_gt29,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt29,sqly_gt29_val)
                    mnty_gt29=fbcursor.fetchone()
                    


                    today529 = date.today()
                    first529 = today529.replace(day=1)
                    last_month529 = first529 -relativedelta(months=4)
                    
                    end_today529 = last_month529
                    end_first529 = end_today529.replace(day=1)
                    end_month529 = end_first529 -relativedelta(days=1)+relativedelta(months=1)

                    sql529='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Computer and Internet Expense" and acctype="Expenses"'
                    sql529_val=(last_month529,end_month529,dtl_cmp_pro[0],)
                    fbcursor.execute(sql529,sql529_val)
                    mnt529=fbcursor.fetchone()

                    today429 = date.today()
                    first429 = today429.replace(day=1)
                    last_month429 = first429 -relativedelta(months=3)
                    
                    end_today429 = last_month429
                    end_first429 = end_today429.replace(day=1)
                    end_month429 = end_first429 -relativedelta(days=1)+relativedelta(months=1)

                    sql429='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Computer and Internet Expense" and acctype="Expenses"'
                    sql429_val=(last_month429,end_month429,dtl_cmp_pro[0],)
                    fbcursor.execute(sql429,sql429_val)
                    mnt429=fbcursor.fetchone()

                    today329 = date.today()
                    first329 = today329.replace(day=1)
                    last_month329 = first329 -relativedelta(months=2)
                    
                    end_today329 = last_month329
                    end_first329 = end_today329.replace(day=1)
                    end_month329 = end_first329 -relativedelta(days=1)+relativedelta(months=1)

                    sql329='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Computer and Internet Expense" and acctype="Expenses"'
                    sql329_val=(last_month329,end_month329,dtl_cmp_pro[0],)
                    fbcursor.execute(sql329,sql329_val)
                    mnt329=fbcursor.fetchone()

                    today292 = date.today()
                    first292 = today292.replace(day=1)
                    last_month292 = first292 -relativedelta(months=1)
                    
                    end_today292 = last_month292
                    end_first292 = end_today292.replace(day=1)
                    end_month292 = end_first292 -relativedelta(days=1)+relativedelta(months=1)

                    sql292='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Computer and Internet Expense" and acctype="Expenses"'
                    sql292_val=(last_month292,end_month292,dtl_cmp_pro[0],)
                    fbcursor.execute(sql292,sql292_val)
                    mnt292=fbcursor.fetchone()

                    today291 = date.today()
                    first291 = today291.replace(day=1)
              

                    end_today291 = date.today()
                    end_first291 = end_today291.replace(day=1)
                    end_month291 = end_first291 -relativedelta(days=1)+relativedelta(months=1)

                    sql291='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Computer and Internet Expense" and acctype="Expenses"'
                    sql291_val=(first291,end_month291,dtl_cmp_pro[0],)
                    fbcursor.execute(sql291,sql291_val)
                    mnt291=fbcursor.fetchone()

                    sqltt29='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Computer and Internet Expense" and acctype="Expenses"'
                    sqltt_val29=(last_monthy_gt29,end_month291,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt29,sqltt_val29)
                    mnttt29=fbcursor.fetchone()
                    
                    if mnty_gt29[0] is None:
                        val629="0.0"
                    else:
                        val629=mnty_gt29[0] 
                    r29c2.delete(0,END)
                    r29c2.insert(0,"$"+str(val629))
                    r29c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt529[0] is None:
                        val529="0.0"
                    else:
                        val529=mnt529[0] 
                    r29c3.delete(0,END)
                    r29c3.insert(0,"$"+str(val529))
                    r29c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt429[0] is None:
                        val429="0.0"
                    else:
                        val429=mnt429[0] 
                    r29c4.delete(0,END)
                    r29c4.insert(0,"$"+str(val429))
                    r29c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt329[0] is None:
                        val329="0.0"
                    else:
                        val329=mnt329[0] 
                    r29c5.delete(0,END)
                    r29c5.insert(0,"$"+str(val329))
                    r29c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt292[0] is None:
                        val292="0.0"
                    else:
                        val292=mnt292[0] 
                    r29c6.delete(0,END)
                    r29c6.insert(0,"$"+str(val292))
                    r29c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt291[0] is None:
                        val291="0.0"
                    else:
                        val291=mnt291[0] 
                    r29c7.delete(0,END)
                    r29c7.insert(0,"$"+str(val291))
                    r29c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt29[0] is None:
                        valtt29="0.0"
                    else:
                        valtt29=mnttt29[0] 
                    r29c8.delete(0,END)
                    r29c8.insert(0,"$"+str(valtt29))
                    r29c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 


                    #----------------------------------------------------------30 th row
                    lv_name=Label(frm_analiz, text="Computer and Internet Expense",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r30c1"))

                    r30c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r30c2, tag=("r30c2"))

                    r30c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r30c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r30c3, tag=("r30c3"))

                    r30c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r30c4, tag=("r30c4"))


                    r30c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r30c5, tag=("r30c5"))

                    r30c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r30c6, tag=("r30c6"))


                    r30c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r30c7, tag=("r30c7"))

                    r30c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r30c8, tag=("r30c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt30 = date.today()
                    firsty_gt30= today_gt30.replace(day=1)
                    last_monthy_gt30 = firsty_gt30 -relativedelta(months=5)
                    
                    end_todayy_gt30 = last_monthy_gt30
                    end_firsty_gt30 = end_todayy_gt30.replace(day=1)
                    end_monthy_gt30 = end_firsty_gt30 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt30='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Computer and Internet Expense" and acctype="Expenses"'
                    sqly_gt30_val=(last_monthy_gt30,end_monthy_gt30,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt30,sqly_gt30_val)
                    mnty_gt30=fbcursor.fetchone()
                    


                    today530 = date.today()
                    first530 = today530.replace(day=1)
                    last_month530 = first530 -relativedelta(months=4)
                    
                    end_today530 = last_month530
                    end_first530 = end_today530.replace(day=1)
                    end_month530 = end_first530 -relativedelta(days=1)+relativedelta(months=1)

                    sql530='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Computer and Internet Expense" and acctype="Expenses"'
                    sql530_val=(last_month530,end_month530,dtl_cmp_pro[0],)
                    fbcursor.execute(sql530,sql530_val)
                    mnt530=fbcursor.fetchone()

                    today430 = date.today()
                    first430 = today430.replace(day=1)
                    last_month430 = first430 -relativedelta(months=3)
                    
                    end_today430 = last_month430
                    end_first430 = end_today430.replace(day=1)
                    end_month430 = end_first430 -relativedelta(days=1)+relativedelta(months=1)

                    sql430='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Computer and Internet Expense" and acctype="Expenses"'
                    sql430_val=(last_month430,end_month430,dtl_cmp_pro[0],)
                    fbcursor.execute(sql430,sql430_val)
                    mnt430=fbcursor.fetchone()

                    today330 = date.today()
                    first330 = today330.replace(day=1)
                    last_month330 = first330 -relativedelta(months=2)
                    
                    end_today330 = last_month330
                    end_first330 = end_today330.replace(day=1)
                    end_month330 = end_first330 -relativedelta(days=1)+relativedelta(months=1)

                    sql330='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Computer and Internet Expense" and acctype="Expenses"'
                    sql330_val=(last_month330,end_month330,dtl_cmp_pro[0],)
                    fbcursor.execute(sql330,sql330_val)
                    mnt330=fbcursor.fetchone()

                    today302 = date.today()
                    first302 = today302.replace(day=1)
                    last_month302 = first302 -relativedelta(months=1)
                    
                    end_today302 = last_month302
                    end_first302 = end_today302.replace(day=1)
                    end_month302 = end_first302 -relativedelta(days=1)+relativedelta(months=1)

                    sql302='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Computer and Internet Expense" and acctype="Expenses"'
                    sql302_val=(last_month302,end_month302,dtl_cmp_pro[0],)
                    fbcursor.execute(sql302,sql302_val)
                    mnt302=fbcursor.fetchone()

                    today301 = date.today()
                    first301 = today301.replace(day=1)
              

                    end_today301 = date.today()
                    end_first301 = end_today301.replace(day=1)
                    end_month301 = end_first301 -relativedelta(days=1)+relativedelta(months=1)

                    sql301='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Computer and Internet Expense" and acctype="Expenses"'
                    sql301_val=(first301,end_month301,dtl_cmp_pro[0],)
                    fbcursor.execute(sql301,sql301_val)
                    mnt301=fbcursor.fetchone()

                    sqltt30='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Computer and Internet Expense" and acctype="Expenses"'
                    sqltt_val30=(last_monthy_gt30,end_month301,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt30,sqltt_val30)
                    mnttt30=fbcursor.fetchone()
                    
                    if mnty_gt30[0] is None:
                        val630="0.0"
                    else:
                        val630=mnty_gt30[0] 
                    r30c2.delete(0,END)
                    r30c2.insert(0,"$"+str(val630))
                    r30c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt530[0] is None:
                        val530="0.0"
                    else:
                        val530=mnt530[0] 
                    r30c3.delete(0,END)
                    r30c3.insert(0,"$"+str(val530))
                    r30c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt430[0] is None:
                        val430="0.0"
                    else:
                        val430=mnt430[0] 
                    r30c4.delete(0,END)
                    r30c4.insert(0,"$"+str(val430))
                    r30c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt330[0] is None:
                        val330="0.0"
                    else:
                        val330=mnt330[0] 
                    r30c5.delete(0,END)
                    r30c5.insert(0,"$"+str(val330))
                    r30c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt302[0] is None:
                        val302="0.0"
                    else:
                        val302=mnt302[0] 
                    r30c6.delete(0,END)
                    r30c6.insert(0,"$"+str(val302))
                    r30c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt301[0] is None:
                        val301="0.0"
                    else:
                        val301=mnt301[0] 
                    r30c7.delete(0,END)
                    r30c7.insert(0,"$"+str(val301))
                    r30c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt30[0] is None:
                        valtt30="0.0"
                    else:
                        valtt30=mnttt30[0] 
                    r30c8.delete(0,END)
                    r30c8.insert(0,"$"+str(valtt30))
                    r30c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 


                    #----------------------------------------------------------231 th row
                    lv_name=Label(frm_analiz, text="Continuing Education",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r31c1"))

                    r31c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r31c2, tag=("r31c2"))

                    r31c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r31c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r31c3, tag=("r31c3"))

                    r31c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r31c4, tag=("r31c4"))


                    r31c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r31c5, tag=("r31c5"))

                    r31c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r31c6, tag=("r31c6"))


                    r31c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r31c7, tag=("r31c7"))

                    r31c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r31c8, tag=("r31c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt31 = date.today()
                    firsty_gt31= today_gt31.replace(day=1)
                    last_monthy_gt31 = firsty_gt31 -relativedelta(months=5)
                    
                    end_todayy_gt31 = last_monthy_gt31
                    end_firsty_gt31 = end_todayy_gt31.replace(day=1)
                    end_monthy_gt31 = end_firsty_gt31 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt31='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Continuing Education" and acctype="Expenses"'
                    sqly_gt31_val=(last_monthy_gt31,end_monthy_gt31,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt31,sqly_gt31_val)
                    mnty_gt31=fbcursor.fetchone()
                    


                    today531 = date.today()
                    first531 = today531.replace(day=1)
                    last_month531 = first531 -relativedelta(months=4)
                    
                    end_today531 = last_month531
                    end_first531 = end_today531.replace(day=1)
                    end_month531 = end_first531 -relativedelta(days=1)+relativedelta(months=1)

                    sql531='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Continuing Education" and acctype="Expenses"'
                    sql531_val=(last_month531,end_month531,dtl_cmp_pro[0],)
                    fbcursor.execute(sql531,sql531_val)
                    mnt531=fbcursor.fetchone()

                    today431 = date.today()
                    first431 = today431.replace(day=1)
                    last_month431 = first431 -relativedelta(months=3)
                    
                    end_today431 = last_month431
                    end_first431 = end_today431.replace(day=1)
                    end_month431 = end_first431 -relativedelta(days=1)+relativedelta(months=1)

                    sql431='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Continuing Education" and acctype="Expenses"'
                    sql431_val=(last_month431,end_month431,dtl_cmp_pro[0],)
                    fbcursor.execute(sql431,sql431_val)
                    mnt431=fbcursor.fetchone()

                    today331 = date.today()
                    first331 = today331.replace(day=1)
                    last_month331 = first331 -relativedelta(months=2)
                    
                    end_today331 = last_month331
                    end_first331 = end_today331.replace(day=1)
                    end_month331 = end_first331 -relativedelta(days=1)+relativedelta(months=1)

                    sql331='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Continuing Education" and acctype="Expenses"'
                    sql331_val=(last_month331,end_month331,dtl_cmp_pro[0],)
                    fbcursor.execute(sql331,sql331_val)
                    mnt331=fbcursor.fetchone()

                    today312 = date.today()
                    first312 = today312.replace(day=1)
                    last_month312 = first312 -relativedelta(months=1)
                    
                    end_today312 = last_month312
                    end_first312 = end_today312.replace(day=1)
                    end_month312 = end_first312 -relativedelta(days=1)+relativedelta(months=1)

                    sql312='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Continuing Education" and acctype="Expenses"'
                    sql312_val=(last_month312,end_month312,dtl_cmp_pro[0],)
                    fbcursor.execute(sql312,sql312_val)
                    mnt312=fbcursor.fetchone()

                    today311 = date.today()
                    first311 = today311.replace(day=1)
              

                    end_today311 = date.today()
                    end_first311 = end_today311.replace(day=1)
                    end_month311 = end_first311 -relativedelta(days=1)+relativedelta(months=1)

                    sql311='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Continuing Education" and acctype="Expenses"'
                    sql311_val=(first311,end_month311,dtl_cmp_pro[0],)
                    fbcursor.execute(sql311,sql311_val)
                    mnt311=fbcursor.fetchone()

                    sqltt31='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Continuing Education" and acctype="Expenses"'
                    sqltt_val31=(last_monthy_gt31,end_month311,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt31,sqltt_val31)
                    mnttt31=fbcursor.fetchone()
                    
                    if mnty_gt31[0] is None:
                        val631="0.0"
                    else:
                        val631=mnty_gt31[0] 
                    r31c2.delete(0,END)
                    r31c2.insert(0,"$"+str(val631))
                    r31c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt531[0] is None:
                        val531="0.0"
                    else:
                        val531=mnt531[0] 
                    r31c3.delete(0,END)
                    r31c3.insert(0,"$"+str(val531))
                    r31c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt431[0] is None:
                        val431="0.0"
                    else:
                        val431=mnt431[0] 
                    r31c4.delete(0,END)
                    r31c4.insert(0,"$"+str(val431))
                    r31c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt331[0] is None:
                        val331="0.0"
                    else:
                        val331=mnt331[0] 
                    r31c5.delete(0,END)
                    r31c5.insert(0,"$"+str(val331))
                    r31c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt312[0] is None:
                        val312="0.0"
                    else:
                        val312=mnt312[0] 
                    r31c6.delete(0,END)
                    r31c6.insert(0,"$"+str(val312))
                    r31c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt311[0] is None:
                        val311="0.0"
                    else:
                        val311=mnt311[0] 
                    r31c7.delete(0,END)
                    r31c7.insert(0,"$"+str(val311))
                    r31c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt31[0] is None:
                        valtt31="0.0"
                    else:
                        valtt31=mnttt31[0] 
                    r31c8.delete(0,END)
                    r31c8.insert(0,"$"+str(valtt31))
                    r31c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 


                    
                    

                    #----------------------------------------------------------32 th row
                    lv_name=Label(frm_analiz, text="Depreciation Expense",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r32c1"))

                    r32c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r32c2, tag=("r32c2"))

                    r32c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                 
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r32c3, tag=("r32c3"))

                    r32c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r32c4, tag=("r32c4"))


                    r32c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r32c5, tag=("r32c5"))

                    r32c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r32c6, tag=("r32c6"))


                    r32c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r32c7, tag=("r32c7"))

                    r32c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r32c8, tag=("r32c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt32 = date.today()
                    firsty_gt32= today_gt32.replace(day=1)
                    last_monthy_gt32 = firsty_gt32 -relativedelta(months=5)
                    
                    end_todayy_gt32 = last_monthy_gt32
                    end_firsty_gt32 = end_todayy_gt32.replace(day=1)
                    end_monthy_gt32 = end_firsty_gt32 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt32='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Depreciation Expense" and acctype="Expenses"'
                    sqly_gt32_val=(last_monthy_gt32,end_monthy_gt32,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt32,sqly_gt32_val)
                    mnty_gt32=fbcursor.fetchone()
                    


                    today532 = date.today()
                    first532 = today532.replace(day=1)
                    last_month532 = first532 -relativedelta(months=4)
                    
                    end_today532 = last_month532
                    end_first532 = end_today532.replace(day=1)
                    end_month532 = end_first532 -relativedelta(days=1)+relativedelta(months=1)

                    sql532='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Depreciation Expense" and acctype="Expenses"'
                    sql532_val=(last_month532,end_month532,dtl_cmp_pro[0],)
                    fbcursor.execute(sql532,sql532_val)
                    mnt532=fbcursor.fetchone()

                    today432 = date.today()
                    first432 = today432.replace(day=1)
                    last_month432 = first432 -relativedelta(months=3)
                    
                    end_today432 = last_month432
                    end_first432 = end_today432.replace(day=1)
                    end_month432 = end_first432 -relativedelta(days=1)+relativedelta(months=1)

                    sql432='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Depreciation Expense" and acctype="Expenses"'
                    sql432_val=(last_month432,end_month432,dtl_cmp_pro[0],)
                    fbcursor.execute(sql432,sql432_val)
                    mnt432=fbcursor.fetchone()

                    today332 = date.today()
                    first332 = today332.replace(day=1)
                    last_month332 = first332 -relativedelta(months=2)
                    
                    end_today332 = last_month332
                    end_first332 = end_today332.replace(day=1)
                    end_month332 = end_first332 -relativedelta(days=1)+relativedelta(months=1)

                    sql332='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Depreciation Expense" and acctype="Expenses"'
                    sql332_val=(last_month332,end_month332,dtl_cmp_pro[0],)
                    fbcursor.execute(sql332,sql332_val)
                    mnt332=fbcursor.fetchone()

                    today322 = date.today()
                    first322 = today322.replace(day=1)
                    last_month322 = first322 -relativedelta(months=1)
                    
                    end_today322 = last_month322
                    end_first322 = end_today322.replace(day=1)
                    end_month322 = end_first322 -relativedelta(days=1)+relativedelta(months=1)

                    sql322='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Depreciation Expense" and acctype="Expenses"'
                    sql322_val=(last_month322,end_month322,dtl_cmp_pro[0],)
                    fbcursor.execute(sql322,sql322_val)
                    mnt322=fbcursor.fetchone()

                    today321 = date.today()
                    first321 = today321.replace(day=1)
              

                    end_today321 = date.today()
                    end_first321 = end_today321.replace(day=1)
                    end_month321 = end_first321 -relativedelta(days=1)+relativedelta(months=1)

                    sql321='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Depreciation Expense" and acctype="Expenses"'
                    sql321_val=(first321,end_month321,dtl_cmp_pro[0],)
                    fbcursor.execute(sql321,sql321_val)
                    mnt321=fbcursor.fetchone()

                    sqltt32='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Depreciation Expense" and acctype="Expenses"'
                    sqltt_val32=(last_monthy_gt32,end_month321,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt32,sqltt_val32)
                    mnttt32=fbcursor.fetchone()
                    
                    if mnty_gt32[0] is None:
                        val632="0.0"
                    else:
                        val632=mnty_gt32[0] 
                    r32c2.delete(0,END)
                    r32c2.insert(0,"$"+str(val632))
                    r32c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt532[0] is None:
                        val532="0.0"
                    else:
                        val532=mnt532[0] 
                    r32c3.delete(0,END)
                    r32c3.insert(0,"$"+str(val532))
                    r32c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt432[0] is None:
                        val432="0.0"
                    else:
                        val432=mnt432[0] 
                    r32c4.delete(0,END)
                    r32c4.insert(0,"$"+str(val432))
                    r32c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt332[0] is None:
                        val332="0.0"
                    else:
                        val332=mnt332[0] 
                    r32c5.delete(0,END)
                    r32c5.insert(0,"$"+str(val332))
                    r32c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt322[0] is None:
                        val322="0.0"
                    else:
                        val322=mnt322[0] 
                    r32c6.delete(0,END)
                    r32c6.insert(0,"$"+str(val322))
                    r32c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt321[0] is None:
                        val321="0.0"
                    else:
                        val321=mnt321[0] 
                    r32c7.delete(0,END)
                    r32c7.insert(0,"$"+str(val321))
                    r32c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt32[0] is None:
                        valtt32="0.0"
                    else:
                        valtt32=mnttt32[0] 
                    r32c8.delete(0,END)
                    r32c8.insert(0,"$"+str(valtt32))
                    r32c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 


                    #----------------------------------------------------------33 th row
                    lv_name=Label(frm_analiz, text="Dues and Subscriptions",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r33c1"))

                    r33c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r33c2, tag=("r33c2"))

                    r33c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r33c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r33c3, tag=("r33c3"))

                    r33c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r33c4, tag=("r33c4"))


                    r33c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r33c5, tag=("r33c5"))

                    r33c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r33c6, tag=("r33c6"))


                    r33c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r33c7, tag=("r33c7"))

                    r33c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r33c8, tag=("r33c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt33 = date.today()
                    firsty_gt33= today_gt33.replace(day=1)
                    last_monthy_gt33 = firsty_gt33 -relativedelta(months=5)
                    
                    end_todayy_gt33 = last_monthy_gt33
                    end_firsty_gt33 = end_todayy_gt33.replace(day=1)
                    end_monthy_gt33 = end_firsty_gt33 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt33='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Dues and Subscriptions" and acctype="Expenses"'
                    sqly_gt33_val=(last_monthy_gt33,end_monthy_gt33,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt33,sqly_gt33_val)
                    mnty_gt33=fbcursor.fetchone()
                    


                    today533 = date.today()
                    first533 = today533.replace(day=1)
                    last_month533 = first533 -relativedelta(months=4)
                    
                    end_today533 = last_month533
                    end_first533 = end_today533.replace(day=1)
                    end_month533 = end_first533 -relativedelta(days=1)+relativedelta(months=1)

                    sql533='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Dues and Subscriptions" and acctype="Expenses"'
                    sql533_val=(last_month533,end_month533,dtl_cmp_pro[0],)
                    fbcursor.execute(sql533,sql533_val)
                    mnt533=fbcursor.fetchone()

                    today433 = date.today()
                    first433 = today433.replace(day=1)
                    last_month433 = first433 -relativedelta(months=3)
                    
                    end_today433 = last_month433
                    end_first433 = end_today433.replace(day=1)
                    end_month433 = end_first433 -relativedelta(days=1)+relativedelta(months=1)

                    sql433='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Dues and Subscriptions" and acctype="Expenses"'
                    sql433_val=(last_month433,end_month433,dtl_cmp_pro[0],)
                    fbcursor.execute(sql433,sql433_val)
                    mnt433=fbcursor.fetchone()

                    today333 = date.today()
                    first333 = today333.replace(day=1)
                    last_month333 = first333 -relativedelta(months=2)
                    
                    end_today333 = last_month333
                    end_first333 = end_today333.replace(day=1)
                    end_month333 = end_first333 -relativedelta(days=1)+relativedelta(months=1)

                    sql333='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Dues and Subscriptions" and acctype="Expenses"'
                    sql333_val=(last_month333,end_month333,dtl_cmp_pro[0],)
                    fbcursor.execute(sql333,sql333_val)
                    mnt333=fbcursor.fetchone()

                    today332 = date.today()
                    first332 = today332.replace(day=1)
                    last_month332 = first332 -relativedelta(months=1)
                    
                    end_today332 = last_month332
                    end_first332 = end_today332.replace(day=1)
                    end_month332 = end_first332 -relativedelta(days=1)+relativedelta(months=1)

                    sql332='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Dues and Subscriptions" and acctype="Expenses"'
                    sql332_val=(last_month332,end_month332,dtl_cmp_pro[0],)
                    fbcursor.execute(sql332,sql332_val)
                    mnt332=fbcursor.fetchone()

                    today331 = date.today()
                    first331 = today331.replace(day=1)
              

                    end_today331 = date.today()
                    end_first331 = end_today331.replace(day=1)
                    end_month331 = end_first331 -relativedelta(days=1)+relativedelta(months=1)

                    sql331='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Dues and Subscriptions" and acctype="Expenses"'
                    sql331_val=(first331,end_month331,dtl_cmp_pro[0],)
                    fbcursor.execute(sql331,sql331_val)
                    mnt331=fbcursor.fetchone()

                    sqltt33='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Dues and Subscriptions" and acctype="Expenses"'
                    sqltt_val33=(last_monthy_gt33,end_month331,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt33,sqltt_val33)
                    mnttt33=fbcursor.fetchone()
                    
                    if mnty_gt33[0] is None:
                        val633="0.0"
                    else:
                        val633=mnty_gt33[0] 
                    r33c2.delete(0,END)
                    r33c2.insert(0,"$"+str(val633))
                    r33c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt533[0] is None:
                        val533="0.0"
                    else:
                        val533=mnt533[0] 
                    r33c3.delete(0,END)
                    r33c3.insert(0,"$"+str(val533))
                    r33c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt433[0] is None:
                        val433="0.0"
                    else:
                        val433=mnt433[0] 
                    r33c4.delete(0,END)
                    r33c4.insert(0,"$"+str(val433))
                    r33c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt333[0] is None:
                        val333="0.0"
                    else:
                        val333=mnt333[0] 
                    r33c5.delete(0,END)
                    r33c5.insert(0,"$"+str(val333))
                    r33c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt332[0] is None:
                        val332="0.0"
                    else:
                        val332=mnt332[0] 
                    r33c6.delete(0,END)
                    r33c6.insert(0,"$"+str(val332))
                    r33c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt331[0] is None:
                        val331="0.0"
                    else:
                        val331=mnt331[0] 
                    r33c7.delete(0,END)
                    r33c7.insert(0,"$"+str(val331))
                    r33c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt33[0] is None:
                        valtt33="0.0"
                    else:
                        valtt33=mnttt33[0] 
                    r33c8.delete(0,END)
                    r33c8.insert(0,"$"+str(valtt33))
                    r33c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    #----------------------------------------------------------34 th row
                    lv_name=Label(frm_analiz, text="Housekeeping Charges",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r34c1"))

                    r34c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r34c2, tag=("r34c2"))

                    r34c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r34c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r34c3, tag=("r34c3"))

                    r34c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r34c4, tag=("r34c4"))


                    r34c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r34c5, tag=("r34c5"))

                    r34c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r34c6, tag=("r34c6"))


                    r34c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r34c7, tag=("r34c7"))

                    r34c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r34c8, tag=("r34c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt34 = date.today()
                    firsty_gt34= today_gt34.replace(day=1)
                    last_monthy_gt34 = firsty_gt34 -relativedelta(months=5)
                    
                    end_todayy_gt34 = last_monthy_gt34
                    end_firsty_gt34 = end_todayy_gt34.replace(day=1)
                    end_monthy_gt34 = end_firsty_gt34 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt34='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Housekeeping Charges" and acctype="Expenses"'
                    sqly_gt34_val=(last_monthy_gt34,end_monthy_gt34,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt34,sqly_gt34_val)
                    mnty_gt34=fbcursor.fetchone()
                    


                    today534 = date.today()
                    first534 = today534.replace(day=1)
                    last_month534 = first534 -relativedelta(months=4)
                    
                    end_today534 = last_month534
                    end_first534 = end_today534.replace(day=1)
                    end_month534 = end_first534 -relativedelta(days=1)+relativedelta(months=1)

                    sql534='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Housekeeping Charges" and acctype="Expenses"'
                    sql534_val=(last_month534,end_month534,dtl_cmp_pro[0],)
                    fbcursor.execute(sql534,sql534_val)
                    mnt534=fbcursor.fetchone()

                    today434 = date.today()
                    first434 = today434.replace(day=1)
                    last_month434 = first434 -relativedelta(months=3)
                    
                    end_today434 = last_month434
                    end_first434 = end_today434.replace(day=1)
                    end_month434 = end_first434 -relativedelta(days=1)+relativedelta(months=1)

                    sql434='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Housekeeping Charges" and acctype="Expenses"'
                    sql434_val=(last_month434,end_month434,dtl_cmp_pro[0],)
                    fbcursor.execute(sql434,sql434_val)
                    mnt434=fbcursor.fetchone()

                    today334 = date.today()
                    first334 = today334.replace(day=1)
                    last_month334 = first334 -relativedelta(months=2)
                    
                    end_today334 = last_month334
                    end_first334 = end_today334.replace(day=1)
                    end_month334 = end_first334 -relativedelta(days=1)+relativedelta(months=1)

                    sql334='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Housekeeping Charges" and acctype="Expenses"'
                    sql334_val=(last_month334,end_month334,dtl_cmp_pro[0],)
                    fbcursor.execute(sql334,sql334_val)
                    mnt334=fbcursor.fetchone()

                    today342 = date.today()
                    first342 = today342.replace(day=1)
                    last_month342 = first342 -relativedelta(months=1)
                    
                    end_today342 = last_month342
                    end_first342 = end_today342.replace(day=1)
                    end_month342 = end_first342 -relativedelta(days=1)+relativedelta(months=1)

                    sql342='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Housekeeping Charges" and acctype="Expenses"'
                    sql342_val=(last_month342,end_month342,dtl_cmp_pro[0],)
                    fbcursor.execute(sql342,sql342_val)
                    mnt342=fbcursor.fetchone()

                    today341 = date.today()
                    first341 = today341.replace(day=1)
              

                    end_today341 = date.today()
                    end_first341 = end_today341.replace(day=1)
                    end_month341 = end_first341 -relativedelta(days=1)+relativedelta(months=1)

                    sql341='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Housekeeping Charges" and acctype="Expenses"'
                    sql341_val=(first341,end_month341,dtl_cmp_pro[0],)
                    fbcursor.execute(sql341,sql341_val)
                    mnt341=fbcursor.fetchone()

                    sqltt34='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Housekeeping Charges" and acctype="Expenses"'
                    sqltt_val34=(last_monthy_gt34,end_month341,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt34,sqltt_val34)
                    mnttt34=fbcursor.fetchone()
                    
                    if mnty_gt34[0] is None:
                        val634="0.0"
                    else:
                        val634=mnty_gt34[0] 
                    r34c2.delete(0,END)
                    r34c2.insert(0,"$"+str(val634))
                    r34c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt534[0] is None:
                        val534="0.0"
                    else:
                        val534=mnt534[0] 
                    r34c3.delete(0,END)
                    r34c3.insert(0,"$"+str(val534))
                    r34c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt434[0] is None:
                        val434="0.0"
                    else:
                        val434=mnt434[0] 
                    r34c4.delete(0,END)
                    r34c4.insert(0,"$"+str(val434))
                    r34c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt334[0] is None:
                        val334="0.0"
                    else:
                        val334=mnt334[0] 
                    r34c5.delete(0,END)
                    r34c5.insert(0,"$"+str(val334))
                    r34c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt342[0] is None:
                        val342="0.0"
                    else:
                        val342=mnt342[0] 
                    r34c6.delete(0,END)
                    r34c6.insert(0,"$"+str(val342))
                    r34c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt341[0] is None:
                        val341="0.0"
                    else:
                        val341=mnt341[0] 
                    r34c7.delete(0,END)
                    r34c7.insert(0,"$"+str(val341))
                    r34c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt34[0] is None:
                        valtt34="0.0"
                    else:
                        valtt34=mnttt34[0] 
                    r34c8.delete(0,END)
                    r34c8.insert(0,"$"+str(valtt34))
                    r34c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    #----------------------------------------------------------35 th row
                    lv_name=Label(frm_analiz, text="Insurance Expenses",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r35c1"))

                    r35c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r35c2, tag=("r35c2"))

                    r35c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r35c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r35c3, tag=("r35c3"))

                    r35c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r35c4, tag=("r35c4"))


                    r35c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r35c5, tag=("r35c5"))

                    r35c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r35c6, tag=("r35c6"))


                    r35c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r35c7, tag=("r35c7"))

                    r35c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r35c8, tag=("r35c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt35 = date.today()
                    firsty_gt35= today_gt35.replace(day=1)
                    last_monthy_gt35 = firsty_gt35 -relativedelta(months=5)
                    
                    end_todayy_gt35 = last_monthy_gt35
                    end_firsty_gt35 = end_todayy_gt35.replace(day=1)
                    end_monthy_gt35 = end_firsty_gt35 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt35='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses" and acctype="Expenses"'
                    sqly_gt35_val=(last_monthy_gt35,end_monthy_gt35,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt35,sqly_gt35_val)
                    mnty_gt35=fbcursor.fetchone()
                    


                    today535 = date.today()
                    first535 = today535.replace(day=1)
                    last_month535 = first535 -relativedelta(months=4)
                    
                    end_today535 = last_month535
                    end_first535 = end_today535.replace(day=1)
                    end_month535 = end_first535 -relativedelta(days=1)+relativedelta(months=1)

                    sql535='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses" and acctype="Expenses"'
                    sql535_val=(last_month535,end_month535,dtl_cmp_pro[0],)
                    fbcursor.execute(sql535,sql535_val)
                    mnt535=fbcursor.fetchone()

                    today435 = date.today()
                    first435 = today435.replace(day=1)
                    last_month435 = first435 -relativedelta(months=3)
                    
                    end_today435 = last_month435
                    end_first435 = end_today435.replace(day=1)
                    end_month435 = end_first435 -relativedelta(days=1)+relativedelta(months=1)

                    sql435='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses" and acctype="Expenses"'
                    sql435_val=(last_month435,end_month435,dtl_cmp_pro[0],)
                    fbcursor.execute(sql435,sql435_val)
                    mnt435=fbcursor.fetchone()

                    today335 = date.today()
                    first335 = today335.replace(day=1)
                    last_month335 = first335 -relativedelta(months=2)
                    
                    end_today335 = last_month335
                    end_first335 = end_today335.replace(day=1)
                    end_month335 = end_first335 -relativedelta(days=1)+relativedelta(months=1)

                    sql335='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses" and acctype="Expenses"'
                    sql335_val=(last_month335,end_month335,dtl_cmp_pro[0],)
                    fbcursor.execute(sql335,sql335_val)
                    mnt335=fbcursor.fetchone()

                    today352 = date.today()
                    first352 = today352.replace(day=1)
                    last_month352 = first352 -relativedelta(months=1)
                    
                    end_today352 = last_month352
                    end_first352 = end_today352.replace(day=1)
                    end_month352 = end_first352 -relativedelta(days=1)+relativedelta(months=1)

                    sql352='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses" and acctype="Expenses"'
                    sql352_val=(last_month352,end_month352,dtl_cmp_pro[0],)
                    fbcursor.execute(sql352,sql352_val)
                    mnt352=fbcursor.fetchone()

                    today351 = date.today()
                    first351 = today351.replace(day=1)
              

                    end_today351 = date.today()
                    end_first351 = end_today351.replace(day=1)
                    end_month351 = end_first351 -relativedelta(days=1)+relativedelta(months=1)

                    sql351='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses" and acctype="Expenses"'
                    sql351_val=(first351,end_month351,dtl_cmp_pro[0],)
                    fbcursor.execute(sql351,sql351_val)
                    mnt351=fbcursor.fetchone()

                    sqltt35='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses" and acctype="Expenses"'
                    sqltt_val35=(last_monthy_gt35,end_month351,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt35,sqltt_val35)
                    mnttt35=fbcursor.fetchone()
                    
                    if mnty_gt35[0] is None:
                        val635="0.0"
                    else:
                        val635=mnty_gt35[0] 
                    r35c2.delete(0,END)
                    r35c2.insert(0,"$"+str(val635))
                    r35c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt535[0] is None:
                        val535="0.0"
                    else:
                        val535=mnt535[0] 
                    r35c3.delete(0,END)
                    r35c3.insert(0,"$"+str(val535))
                    r35c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt435[0] is None:
                        val435="0.0"
                    else:
                        val435=mnt435[0] 
                    r35c4.delete(0,END)
                    r35c4.insert(0,"$"+str(val435))
                    r35c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt335[0] is None:
                        val335="0.0"
                    else:
                        val335=mnt335[0] 
                    r35c5.delete(0,END)
                    r35c5.insert(0,"$"+str(val335))
                    r35c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt352[0] is None:
                        val352="0.0"
                    else:
                        val352=mnt352[0] 
                    r35c6.delete(0,END)
                    r35c6.insert(0,"$"+str(val352))
                    r35c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt351[0] is None:
                        val351="0.0"
                    else:
                        val351=mnt351[0] 
                    r35c7.delete(0,END)
                    r35c7.insert(0,"$"+str(val351))
                    r35c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt35[0] is None:
                        valtt35="0.0"
                    else:
                        valtt35=mnttt35[0] 
                    r35c8.delete(0,END)
                    r35c8.insert(0,"$"+str(valtt35))
                    r35c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 


                    #----------------------------------------------------------36 th row
                    lv_name=Label(frm_analiz, text="Insurance Expenses-General Liability Insurance",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r36c1"))

                    r36c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r36c2, tag=("r36c2"))

                    r36c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r36c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r36c3, tag=("r36c3"))

                    r36c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r36c4, tag=("r36c4"))


                    r36c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r36c5, tag=("r36c5"))

                    r36c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r36c6, tag=("r36c6"))


                    r36c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r36c7, tag=("r36c7"))

                    r36c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r36c8, tag=("r36c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt36 = date.today()
                    firsty_gt36= today_gt36.replace(day=1)
                    last_monthy_gt36 = firsty_gt36 -relativedelta(months=5)
                    
                    end_todayy_gt36 = last_monthy_gt36
                    end_firsty_gt36 = end_todayy_gt36.replace(day=1)
                    end_monthy_gt36 = end_firsty_gt36 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt36='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-General Liability Insurance" and acctype="Expenses"'
                    sqly_gt36_val=(last_monthy_gt36,end_monthy_gt36,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt36,sqly_gt36_val)
                    mnty_gt36=fbcursor.fetchone()
                    


                    today536 = date.today()
                    first536 = today536.replace(day=1)
                    last_month536 = first536 -relativedelta(months=4)
                    
                    end_today536 = last_month536
                    end_first536 = end_today536.replace(day=1)
                    end_month536 = end_first536 -relativedelta(days=1)+relativedelta(months=1)

                    sql536='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-General Liability Insurance" and acctype="Expenses"'
                    sql536_val=(last_month536,end_month536,dtl_cmp_pro[0],)
                    fbcursor.execute(sql536,sql536_val)
                    mnt536=fbcursor.fetchone()

                    today436 = date.today()
                    first436 = today436.replace(day=1)
                    last_month436 = first436 -relativedelta(months=3)
                    
                    end_today436 = last_month436
                    end_first436 = end_today436.replace(day=1)
                    end_month436 = end_first436 -relativedelta(days=1)+relativedelta(months=1)

                    sql436='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-General Liability Insurance" and acctype="Expenses"'
                    sql436_val=(last_month436,end_month436,dtl_cmp_pro[0],)
                    fbcursor.execute(sql436,sql436_val)
                    mnt436=fbcursor.fetchone()

                    today336 = date.today()
                    first336 = today336.replace(day=1)
                    last_month336 = first336 -relativedelta(months=2)
                    
                    end_today336 = last_month336
                    end_first336 = end_today336.replace(day=1)
                    end_month336 = end_first336 -relativedelta(days=1)+relativedelta(months=1)

                    sql336='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-General Liability Insurance" and acctype="Expenses"'
                    sql336_val=(last_month336,end_month336,dtl_cmp_pro[0],)
                    fbcursor.execute(sql336,sql336_val)
                    mnt336=fbcursor.fetchone()

                    today362 = date.today()
                    first362 = today362.replace(day=1)
                    last_month362 = first362 -relativedelta(months=1)
                    
                    end_today362 = last_month362
                    end_first362 = end_today362.replace(day=1)
                    end_month362 = end_first362 -relativedelta(days=1)+relativedelta(months=1)

                    sql362='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-General Liability Insurance" and acctype="Expenses"'
                    sql362_val=(last_month362,end_month362,dtl_cmp_pro[0],)
                    fbcursor.execute(sql362,sql362_val)
                    mnt362=fbcursor.fetchone()

                    today361 = date.today()
                    first361 = today361.replace(day=1)
              

                    end_today361 = date.today()
                    end_first361 = end_today361.replace(day=1)
                    end_month361 = end_first361 -relativedelta(days=1)+relativedelta(months=1)

                    sql361='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-General Liability Insurance" and acctype="Expenses"'
                    sql361_val=(first361,end_month361,dtl_cmp_pro[0],)
                    fbcursor.execute(sql361,sql361_val)
                    mnt361=fbcursor.fetchone()

                    sqltt36='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-General Liability Insurance" and acctype="Expenses"'
                    sqltt_val36=(last_monthy_gt36,end_month361,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt36,sqltt_val36)
                    mnttt36=fbcursor.fetchone()
                    
                    if mnty_gt36[0] is None:
                        val636="0.0"
                    else:
                        val636=mnty_gt36[0] 
                    r36c2.delete(0,END)
                    r36c2.insert(0,"$"+str(val636))
                    r36c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt536[0] is None:
                        val536="0.0"
                    else:
                        val536=mnt536[0] 
                    r36c3.delete(0,END)
                    r36c3.insert(0,"$"+str(val536))
                    r36c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt436[0] is None:
                        val436="0.0"
                    else:
                        val436=mnt436[0] 
                    r36c4.delete(0,END)
                    r36c4.insert(0,"$"+str(val436))
                    r36c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt336[0] is None:
                        val336="0.0"
                    else:
                        val336=mnt336[0] 
                    r36c5.delete(0,END)
                    r36c5.insert(0,"$"+str(val336))
                    r36c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt362[0] is None:
                        val362="0.0"
                    else:
                        val362=mnt362[0] 
                    r36c6.delete(0,END)
                    r36c6.insert(0,"$"+str(val362))
                    r36c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt361[0] is None:
                        val361="0.0"
                    else:
                        val361=mnt361[0] 
                    r36c7.delete(0,END)
                    r36c7.insert(0,"$"+str(val361))
                    r36c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt36[0] is None:
                        valtt36="0.0"
                    else:
                        valtt36=mnttt36[0] 
                    r36c8.delete(0,END)
                    r36c8.insert(0,"$"+str(valtt36))
                    r36c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    #----------------------------------------------------------37 th row
                    lv_name=Label(frm_analiz, text="Insurance Expenses-Health Insurance",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r37c1"))

                    r37c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r37c2, tag=("r37c2"))

                    r37c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
             
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r37c3, tag=("r37c3"))

                    r37c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r37c4, tag=("r37c4"))


                    r37c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r37c5, tag=("r37c5"))

                    r37c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r37c6, tag=("r37c6"))


                    r37c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r37c7, tag=("r37c7"))

                    r37c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r37c8, tag=("r37c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt37 = date.today()
                    firsty_gt37= today_gt37.replace(day=1)
                    last_monthy_gt37 = firsty_gt37 -relativedelta(months=5)
                    
                    end_todayy_gt37 = last_monthy_gt37
                    end_firsty_gt37 = end_todayy_gt37.replace(day=1)
                    end_monthy_gt37 = end_firsty_gt37 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt37='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Health Insurance" and acctype="Expenses"'
                    sqly_gt37_val=(last_monthy_gt37,end_monthy_gt37,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt37,sqly_gt37_val)
                    mnty_gt37=fbcursor.fetchone()
                    


                    today537 = date.today()
                    first537 = today537.replace(day=1)
                    last_month537 = first537 -relativedelta(months=4)
                    
                    end_today537 = last_month537
                    end_first537 = end_today537.replace(day=1)
                    end_month537 = end_first537 -relativedelta(days=1)+relativedelta(months=1)

                    sql537='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Health Insurance" and acctype="Expenses"'
                    sql537_val=(last_month537,end_month537,dtl_cmp_pro[0],)
                    fbcursor.execute(sql537,sql537_val)
                    mnt537=fbcursor.fetchone()

                    today437 = date.today()
                    first437 = today437.replace(day=1)
                    last_month437 = first437 -relativedelta(months=3)
                    
                    end_today437 = last_month437
                    end_first437 = end_today437.replace(day=1)
                    end_month437 = end_first437 -relativedelta(days=1)+relativedelta(months=1)

                    sql437='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Health Insurance" and acctype="Expenses"'
                    sql437_val=(last_month437,end_month437,dtl_cmp_pro[0],)
                    fbcursor.execute(sql437,sql437_val)
                    mnt437=fbcursor.fetchone()

                    today337 = date.today()
                    first337 = today337.replace(day=1)
                    last_month337 = first337 -relativedelta(months=2)
                    
                    end_today337 = last_month337
                    end_first337 = end_today337.replace(day=1)
                    end_month337 = end_first337 -relativedelta(days=1)+relativedelta(months=1)

                    sql337='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Health Insurance" and acctype="Expenses"'
                    sql337_val=(last_month337,end_month337,dtl_cmp_pro[0],)
                    fbcursor.execute(sql337,sql337_val)
                    mnt337=fbcursor.fetchone()

                    today237 = date.today()
                    first237 = today237.replace(day=1)
                    last_month237 = first237 -relativedelta(months=1)
                    
                    end_today237 = last_month237
                    end_first237 = end_today237.replace(day=1)
                    end_month237 = end_first237 -relativedelta(days=1)+relativedelta(months=1)

                    sql237='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Health Insurance" and acctype="Expenses"'
                    sql237_val=(last_month237,end_month237,dtl_cmp_pro[0],)
                    fbcursor.execute(sql237,sql237_val)
                    mnt237=fbcursor.fetchone()

                    today371 = date.today()
                    first371 = today371.replace(day=1)
              

                    end_today371 = date.today()
                    end_first371 = end_today371.replace(day=1)
                    end_month371 = end_first371 -relativedelta(days=1)+relativedelta(months=1)

                    sql371='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Health Insurance" and acctype="Expenses"'
                    sql371_val=(first371,end_month371,dtl_cmp_pro[0],)
                    fbcursor.execute(sql371,sql371_val)
                    mnt371=fbcursor.fetchone()

                    sqltt37='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Health Insurance" and acctype="Expenses"'
                    sqltt_val37=(last_monthy_gt37,end_month371,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt37,sqltt_val37)
                    mnttt37=fbcursor.fetchone()
                    
                    if mnty_gt37[0] is None:
                        val637="0.0"
                    else:
                        val637=mnty_gt37[0] 
                    r37c2.delete(0,END)
                    r37c2.insert(0,"$"+str(val637))
                    r37c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt537[0] is None:
                        val537="0.0"
                    else:
                        val537=mnt537[0] 
                    r37c3.delete(0,END)
                    r37c3.insert(0,"$"+str(val537))
                    r37c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt437[0] is None:
                        val437="0.0"
                    else:
                        val437=mnt437[0] 
                    r37c4.delete(0,END)
                    r37c4.insert(0,"$"+str(val437))
                    r37c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt337[0] is None:
                        val337="0.0"
                    else:
                        val337=mnt337[0] 
                    r37c5.delete(0,END)
                    r37c5.insert(0,"$"+str(val337))
                    r37c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt237[0] is None:
                        val237="0.0"
                    else:
                        val237=mnt237[0] 
                    r37c6.delete(0,END)
                    r37c6.insert(0,"$"+str(val237))
                    r37c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt371[0] is None:
                        val371="0.0"
                    else:
                        val371=mnt371[0] 
                    r37c7.delete(0,END)
                    r37c7.insert(0,"$"+str(val371))
                    r37c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt37[0] is None:
                        valtt37="0.0"
                    else:
                        valtt37=mnttt37[0] 
                    r37c8.delete(0,END)
                    r37c8.insert(0,"$"+str(valtt37))
                    r37c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  


                    #----------------------------------------------------------28 th row
                    lv_name=Label(frm_analiz, text="Insurance Expenses-Life and Disability Insurance",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r38c1"))

                    r38c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r38c2, tag=("r38c2"))

                    r38c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r38c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r38c3, tag=("r38c3"))

                    r38c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r38c4, tag=("r38c4"))


                    r38c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r38c5, tag=("r38c5"))

                    r38c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r38c6, tag=("r38c6"))


                    r38c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r38c7, tag=("r38c7"))

                    r38c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r38c8, tag=("r38c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt38 = date.today()
                    firsty_gt38= today_gt38.replace(day=1)
                    last_monthy_gt38 = firsty_gt38 -relativedelta(months=5)
                    
                    end_todayy_gt38 = last_monthy_gt38
                    end_firsty_gt38 = end_todayy_gt38.replace(day=1)
                    end_monthy_gt38 = end_firsty_gt38 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt38='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Life and Disability Insurance" and acctype="Expenses"'
                    sqly_gt38_val=(last_monthy_gt38,end_monthy_gt38,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt38,sqly_gt38_val)
                    mnty_gt38=fbcursor.fetchone()
                    


                    today538 = date.today()
                    first538 = today538.replace(day=1)
                    last_month538 = first538 -relativedelta(months=4)
                    
                    end_today538 = last_month538
                    end_first538 = end_today538.replace(day=1)
                    end_month538 = end_first538 -relativedelta(days=1)+relativedelta(months=1)

                    sql538='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Life and Disability Insurance" and acctype="Expenses"'
                    sql538_val=(last_month538,end_month538,dtl_cmp_pro[0],)
                    fbcursor.execute(sql538,sql538_val)
                    mnt538=fbcursor.fetchone()

                    today438 = date.today()
                    first438 = today438.replace(day=1)
                    last_month438 = first438 -relativedelta(months=3)
                    
                    end_today438 = last_month438
                    end_first438 = end_today438.replace(day=1)
                    end_month438 = end_first438 -relativedelta(days=1)+relativedelta(months=1)

                    sql438='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Life and Disability Insurance" and acctype="Expenses"'
                    sql438_val=(last_month438,end_month438,dtl_cmp_pro[0],)
                    fbcursor.execute(sql438,sql438_val)
                    mnt438=fbcursor.fetchone()

                    today338 = date.today()
                    first338 = today338.replace(day=1)
                    last_month338 = first338 -relativedelta(months=2)
                    
                    end_today338 = last_month338
                    end_first338 = end_today338.replace(day=1)
                    end_month338 = end_first338 -relativedelta(days=1)+relativedelta(months=1)

                    sql338='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Life and Disability Insurance" and acctype="Expenses"'
                    sql338_val=(last_month338,end_month338,dtl_cmp_pro[0],)
                    fbcursor.execute(sql338,sql338_val)
                    mnt338=fbcursor.fetchone()

                    today238 = date.today()
                    first238 = today238.replace(day=1)
                    last_month238 = first238 -relativedelta(months=1)
                    
                    end_today238 = last_month238
                    end_first238 = end_today238.replace(day=1)
                    end_month238 = end_first238 -relativedelta(days=1)+relativedelta(months=1)

                    sql238='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Life and Disability Insurance" and acctype="Expenses"'
                    sql238_val=(last_month238,end_month238,dtl_cmp_pro[0],)
                    fbcursor.execute(sql238,sql238_val)
                    mnt238=fbcursor.fetchone()

                    today381 = date.today()
                    first381 = today381.replace(day=1)
              

                    end_today381 = date.today()
                    end_first381 = end_today381.replace(day=1)
                    end_month381 = end_first381 -relativedelta(days=1)+relativedelta(months=1)

                    sql381='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Life and Disability Insurance" and acctype="Expenses"'
                    sql381_val=(first381,end_month381,dtl_cmp_pro[0],)
                    fbcursor.execute(sql381,sql381_val)
                    mnt381=fbcursor.fetchone()

                    sqltt38='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Life and Disability Insurance" and acctype="Expenses"'
                    sqltt_val38=(last_monthy_gt38,end_month381,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt38,sqltt_val38)
                    mnttt38=fbcursor.fetchone()
                    
                    if mnty_gt38[0] is None:
                        val638="0.0"
                    else:
                        val638=mnty_gt38[0] 
                    r38c2.delete(0,END)
                    r38c2.insert(0,"$"+str(val638))
                    r38c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt538[0] is None:
                        val538="0.0"
                    else:
                        val538=mnt538[0] 
                    r38c3.delete(0,END)
                    r38c3.insert(0,"$"+str(val538))
                    r38c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt438[0] is None:
                        val438="0.0"
                    else:
                        val438=mnt438[0] 
                    r38c4.delete(0,END)
                    r38c4.insert(0,"$"+str(val438))
                    r38c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt338[0] is None:
                        val338="0.0"
                    else:
                        val338=mnt338[0] 
                    r38c5.delete(0,END)
                    r38c5.insert(0,"$"+str(val338))
                    r38c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt238[0] is None:
                        val238="0.0"
                    else:
                        val238=mnt238[0] 
                    r38c6.delete(0,END)
                    r38c6.insert(0,"$"+str(val238))
                    r38c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt381[0] is None:
                        val381="0.0"
                    else:
                        val381=mnt381[0] 
                    r38c7.delete(0,END)
                    r38c7.insert(0,"$"+str(val381))
                    r38c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt38[0] is None:
                        valtt38="0.0"
                    else:
                        valtt38=mnttt38[0] 
                    r38c8.delete(0,END)
                    r38c8.insert(0,"$"+str(valtt38))
                    r38c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    #----------------------------------------------------------39 th row
                    lv_name=Label(frm_analiz, text="Insurance Expenses-Professional Liability",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r39c1"))

                    r39c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r39c2, tag=("r39c2"))

                    r39c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r39c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r39c3, tag=("r39c3"))

                    r39c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r39c4, tag=("r39c4"))


                    r39c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r39c5, tag=("r39c5"))

                    r39c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r39c6, tag=("r39c6"))


                    r39c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r39c7, tag=("r39c7"))

                    r39c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r39c8, tag=("r39c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt39 = date.today()
                    firsty_gt39= today_gt39.replace(day=1)
                    last_monthy_gt39 = firsty_gt39 -relativedelta(months=5)
                    
                    end_todayy_gt39 = last_monthy_gt39
                    end_firsty_gt39 = end_todayy_gt39.replace(day=1)
                    end_monthy_gt39 = end_firsty_gt39 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt39='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Professional Liability" and acctype="Expenses"'
                    sqly_gt39_val=(last_monthy_gt39,end_monthy_gt39,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt39,sqly_gt39_val)
                    mnty_gt39=fbcursor.fetchone()
                    


                    today539 = date.today()
                    first539 = today539.replace(day=1)
                    last_month539 = first539 -relativedelta(months=4)
                    
                    end_today539 = last_month539
                    end_first539 = end_today539.replace(day=1)
                    end_month539 = end_first539 -relativedelta(days=1)+relativedelta(months=1)

                    sql539='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Professional Liability" and acctype="Expenses"'
                    sql539_val=(last_month539,end_month539,dtl_cmp_pro[0],)
                    fbcursor.execute(sql539,sql539_val)
                    mnt539=fbcursor.fetchone()

                    today439 = date.today()
                    first439 = today439.replace(day=1)
                    last_month439 = first439 -relativedelta(months=3)
                    
                    end_today439 = last_month439
                    end_first439 = end_today439.replace(day=1)
                    end_month439 = end_first439 -relativedelta(days=1)+relativedelta(months=1)

                    sql439='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Professional Liability" and acctype="Expenses"'
                    sql439_val=(last_month439,end_month439,dtl_cmp_pro[0],)
                    fbcursor.execute(sql439,sql439_val)
                    mnt439=fbcursor.fetchone()

                    today339 = date.today()
                    first339 = today339.replace(day=1)
                    last_month339 = first339 -relativedelta(months=2)
                    
                    end_today339 = last_month339
                    end_first339 = end_today339.replace(day=1)
                    end_month339 = end_first339 -relativedelta(days=1)+relativedelta(months=1)

                    sql339='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Professional Liability" and acctype="Expenses"'
                    sql339_val=(last_month339,end_month339,dtl_cmp_pro[0],)
                    fbcursor.execute(sql339,sql339_val)
                    mnt339=fbcursor.fetchone()

                    today239 = date.today()
                    first239 = today239.replace(day=1)
                    last_month239 = first239 -relativedelta(months=1)
                    
                    end_today239 = last_month239
                    end_first239 = end_today239.replace(day=1)
                    end_month239 = end_first239 -relativedelta(days=1)+relativedelta(months=1)

                    sql239='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Professional Liability" and acctype="Expenses"'
                    sql239_val=(last_month239,end_month239,dtl_cmp_pro[0],)
                    fbcursor.execute(sql239,sql239_val)
                    mnt239=fbcursor.fetchone()

                    today391 = date.today()
                    first391 = today391.replace(day=1)
              

                    end_today391 = date.today()
                    end_first391 = end_today391.replace(day=1)
                    end_month391 = end_first391 -relativedelta(days=1)+relativedelta(months=1)

                    sql391='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Professional Liability" and acctype="Expenses"'
                    sql391_val=(first391,end_month391,dtl_cmp_pro[0],)
                    fbcursor.execute(sql391,sql391_val)
                    mnt391=fbcursor.fetchone()

                    sqltt39='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Insurance Expenses-Professional Liability" and acctype="Expenses"'
                    sqltt_val39=(last_monthy_gt39,end_month391,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt39,sqltt_val39)
                    mnttt39=fbcursor.fetchone()
                    
                    if mnty_gt39[0] is None:
                        val639="0.0"
                    else:
                        val639=mnty_gt39[0] 
                    r39c2.delete(0,END)
                    r39c2.insert(0,"$"+str(val639))
                    r39c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt539[0] is None:
                        val539="0.0"
                    else:
                        val539=mnt539[0] 
                    r39c3.delete(0,END)
                    r39c3.insert(0,"$"+str(val539))
                    r39c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt439[0] is None:
                        val439="0.0"
                    else:
                        val439=mnt439[0] 
                    r39c4.delete(0,END)
                    r39c4.insert(0,"$"+str(val439))
                    r39c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt339[0] is None:
                        val339="0.0"
                    else:
                        val339=mnt339[0] 
                    r39c5.delete(0,END)
                    r39c5.insert(0,"$"+str(val339))
                    r39c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt239[0] is None:
                        val239="0.0"
                    else:
                        val239=mnt239[0] 
                    r39c6.delete(0,END)
                    r39c6.insert(0,"$"+str(val239))
                    r39c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt391[0] is None:
                        val391="0.0"
                    else:
                        val391=mnt391[0] 
                    r39c7.delete(0,END)
                    r39c7.insert(0,"$"+str(val391))
                    r39c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt39[0] is None:
                        valtt39="0.0"
                    else:
                        valtt39=mnttt39[0] 
                    r39c8.delete(0,END)
                    r39c8.insert(0,"$"+str(valtt39))
                    r39c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    #----------------------------------------------------------40 th row
                    lv_name=Label(frm_analiz, text="Interest Expenses",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r40c1"))

                    r40c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r40c2, tag=("r40c2"))

                    r40c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r40c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r40c3, tag=("r40c3"))

                    r40c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r40c4, tag=("r40c4"))


                    r40c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r40c5, tag=("r40c5"))

                    r40c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r40c6, tag=("r40c6"))


                    r40c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r40c7, tag=("r40c7"))

                    r40c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r40c8, tag=("r40c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt40 = date.today()
                    firsty_gt40= today_gt40.replace(day=1)
                    last_monthy_gt40 = firsty_gt40 -relativedelta(months=5)
                    
                    end_todayy_gt40 = last_monthy_gt40
                    end_firsty_gt40 = end_todayy_gt40.replace(day=1)
                    end_monthy_gt40 = end_firsty_gt40 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt40='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Interest Expenses" and acctype="Expenses"'
                    sqly_gt40_val=(last_monthy_gt40,end_monthy_gt40,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt40,sqly_gt40_val)
                    mnty_gt40=fbcursor.fetchone()
                    


                    today540 = date.today()
                    first540 = today540.replace(day=1)
                    last_month540 = first540 -relativedelta(months=4)
                    
                    end_today540 = last_month540
                    end_first540 = end_today540.replace(day=1)
                    end_month540 = end_first540 -relativedelta(days=1)+relativedelta(months=1)

                    sql540='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Interest Expenses" and acctype="Expenses"'
                    sql540_val=(last_month540,end_month540,dtl_cmp_pro[0],)
                    fbcursor.execute(sql540,sql540_val)
                    mnt540=fbcursor.fetchone()

                    today440 = date.today()
                    first440 = today440.replace(day=1)
                    last_month440 = first440 -relativedelta(months=3)
                    
                    end_today440 = last_month440
                    end_first440 = end_today440.replace(day=1)
                    end_month440 = end_first440 -relativedelta(days=1)+relativedelta(months=1)

                    sql440='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Interest Expenses" and acctype="Expenses"'
                    sql440_val=(last_month440,end_month440,dtl_cmp_pro[0],)
                    fbcursor.execute(sql440,sql440_val)
                    mnt440=fbcursor.fetchone()

                    today340 = date.today()
                    first340 = today340.replace(day=1)
                    last_month340 = first340 -relativedelta(months=2)
                    
                    end_today340 = last_month340
                    end_first340 = end_today340.replace(day=1)
                    end_month340 = end_first340 -relativedelta(days=1)+relativedelta(months=1)

                    sql340='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Interest Expenses" and acctype="Expenses"'
                    sql340_val=(last_month340,end_month340,dtl_cmp_pro[0],)
                    fbcursor.execute(sql340,sql340_val)
                    mnt340=fbcursor.fetchone()

                    today240 = date.today()
                    first240 = today240.replace(day=1)
                    last_month240 = first240 -relativedelta(months=1)
                    
                    end_today240 = last_month240
                    end_first240 = end_today240.replace(day=1)
                    end_month240 = end_first240 -relativedelta(days=1)+relativedelta(months=1)

                    sql240='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Interest Expenses" and acctype="Expenses"'
                    sql240_val=(last_month240,end_month240,dtl_cmp_pro[0],)
                    fbcursor.execute(sql240,sql240_val)
                    mnt240=fbcursor.fetchone()

                    today401 = date.today()
                    first401 = today401.replace(day=1)
              

                    end_today401 = date.today()
                    end_first401 = end_today401.replace(day=1)
                    end_month401 = end_first401 -relativedelta(days=1)+relativedelta(months=1)

                    sql401='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Interest Expenses" and acctype="Expenses"'
                    sql401_val=(first401,end_month401,dtl_cmp_pro[0],)
                    fbcursor.execute(sql401,sql401_val)
                    mnt401=fbcursor.fetchone()

                    sqltt40='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Interest Expenses" and acctype="Expenses"'
                    sqltt_val40=(last_monthy_gt40,end_month401,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt40,sqltt_val40)
                    mnttt40=fbcursor.fetchone()
                    
                    if mnty_gt40[0] is None:
                        val640="0.0"
                    else:
                        val640=mnty_gt40[0] 
                    r40c2.delete(0,END)
                    r40c2.insert(0,"$"+str(val640))
                    r40c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt540[0] is None:
                        val540="0.0"
                    else:
                        val540=mnt540[0] 
                    r40c3.delete(0,END)
                    r40c3.insert(0,"$"+str(val540))
                    r40c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt440[0] is None:
                        val440="0.0"
                    else:
                        val440=mnt440[0] 
                    r40c4.delete(0,END)
                    r40c4.insert(0,"$"+str(val440))
                    r40c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt340[0] is None:
                        val340="0.0"
                    else:
                        val340=mnt340[0] 
                    r40c5.delete(0,END)
                    r40c5.insert(0,"$"+str(val340))
                    r40c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt240[0] is None:
                        val240="0.0"
                    else:
                        val240=mnt240[0] 
                    r40c6.delete(0,END)
                    r40c6.insert(0,"$"+str(val240))
                    r40c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt401[0] is None:
                        val401="0.0"
                    else:
                        val401=mnt401[0] 
                    r40c7.delete(0,END)
                    r40c7.insert(0,"$"+str(val401))
                    r40c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt40[0] is None:
                        valtt40="0.0"
                    else:
                        valtt40=mnttt40[0] 
                    r40c8.delete(0,END)
                    r40c8.insert(0,"$"+str(valtt40))
                    r40c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    #----------------------------------------------------------41 th row
                    lv_name=Label(frm_analiz, text="Meals and Entertainment",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r41c1"))

                    r41c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r41c2, tag=("r41c2"))

                    r41c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r41c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r41c3, tag=("r41c3"))

                    r41c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r41c4, tag=("r41c4"))


                    r41c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r41c5, tag=("r41c5"))

                    r41c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r41c6, tag=("r41c6"))


                    r41c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r41c7, tag=("r41c7"))

                    r41c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r41c8, tag=("r41c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt41 = date.today()
                    firsty_gt41= today_gt41.replace(day=1)
                    last_monthy_gt41 = firsty_gt41 -relativedelta(months=5)
                    
                    end_todayy_gt41 = last_monthy_gt41
                    end_firsty_gt41 = end_todayy_gt41.replace(day=1)
                    end_monthy_gt41 = end_firsty_gt41 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt41='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Meals and Entertainment" and acctype="Expenses"'
                    sqly_gt41_val=(last_monthy_gt41,end_monthy_gt41,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt41,sqly_gt41_val)
                    mnty_gt41=fbcursor.fetchone()
                    


                    today541 = date.today()
                    first541 = today541.replace(day=1)
                    last_month541 = first541 -relativedelta(months=4)
                    
                    end_today541 = last_month541
                    end_first541 = end_today541.replace(day=1)
                    end_month541 = end_first541 -relativedelta(days=1)+relativedelta(months=1)

                    sql541='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Meals and Entertainment" and acctype="Expenses"'
                    sql541_val=(last_month541,end_month541,dtl_cmp_pro[0],)
                    fbcursor.execute(sql541,sql541_val)
                    mnt541=fbcursor.fetchone()

                    today441 = date.today()
                    first441 = today441.replace(day=1)
                    last_month441 = first441 -relativedelta(months=3)
                    
                    end_today441 = last_month441
                    end_first441 = end_today441.replace(day=1)
                    end_month441 = end_first441 -relativedelta(days=1)+relativedelta(months=1)

                    sql441='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Meals and Entertainment" and acctype="Expenses"'
                    sql441_val=(last_month441,end_month441,dtl_cmp_pro[0],)
                    fbcursor.execute(sql441,sql441_val)
                    mnt441=fbcursor.fetchone()

                    today341 = date.today()
                    first341 = today341.replace(day=1)
                    last_month341 = first341 -relativedelta(months=2)
                    
                    end_today341 = last_month341
                    end_first341 = end_today341.replace(day=1)
                    end_month341 = end_first341 -relativedelta(days=1)+relativedelta(months=1)

                    sql341='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Meals and Entertainment" and acctype="Expenses"'
                    sql341_val=(last_month341,end_month341,dtl_cmp_pro[0],)
                    fbcursor.execute(sql341,sql341_val)
                    mnt341=fbcursor.fetchone()

                    today241 = date.today()
                    first241 = today241.replace(day=1)
                    last_month241 = first241 -relativedelta(months=1)
                    
                    end_today241 = last_month241
                    end_first241 = end_today241.replace(day=1)
                    end_month241 = end_first241 -relativedelta(days=1)+relativedelta(months=1)

                    sql241='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Meals and Entertainment" and acctype="Expenses"'
                    sql241_val=(last_month241,end_month241,dtl_cmp_pro[0],)
                    fbcursor.execute(sql241,sql241_val)
                    mnt241=fbcursor.fetchone()

                    today411 = date.today()
                    first411 = today411.replace(day=1)
              

                    end_today411 = date.today()
                    end_first411 = end_today411.replace(day=1)
                    end_month411 = end_first411 -relativedelta(days=1)+relativedelta(months=1)

                    sql411='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Meals and Entertainment" and acctype="Expenses"'
                    sql411_val=(first411,end_month411,dtl_cmp_pro[0],)
                    fbcursor.execute(sql411,sql411_val)
                    mnt411=fbcursor.fetchone()

                    sqltt41='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Meals and Entertainment" and acctype="Expenses"'
                    sqltt_val41=(last_monthy_gt41,end_month411,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt41,sqltt_val41)
                    mnttt41=fbcursor.fetchone()
                    
                    if mnty_gt41[0] is None:
                        val641="0.0"
                    else:
                        val641=mnty_gt41[0] 
                    r41c2.delete(0,END)
                    r41c2.insert(0,"$"+str(val641))
                    r41c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt541[0] is None:
                        val541="0.0"
                    else:
                        val541=mnt541[0] 
                    r41c3.delete(0,END)
                    r41c3.insert(0,"$"+str(val541))
                    r41c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt441[0] is None:
                        val441="0.0"
                    else:
                        val441=mnt441[0] 
                    r41c4.delete(0,END)
                    r41c4.insert(0,"$"+str(val441))
                    r41c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt341[0] is None:
                        val341="0.0"
                    else:
                        val341=mnt341[0] 
                    r41c5.delete(0,END)
                    r41c5.insert(0,"$"+str(val341))
                    r41c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt241[0] is None:
                        val241="0.0"
                    else:
                        val241=mnt241[0] 
                    r41c6.delete(0,END)
                    r41c6.insert(0,"$"+str(val241))
                    r41c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt411[0] is None:
                        val411="0.0"
                    else:
                        val411=mnt411[0] 
                    r41c7.delete(0,END)
                    r41c7.insert(0,"$"+str(val411))
                    r41c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt41[0] is None:
                        valtt41="0.0"
                    else:
                        valtt41=mnttt41[0] 
                    r41c8.delete(0,END)
                    r41c8.insert(0,"$"+str(valtt41))
                    r41c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------42 th row
                    lv_name=Label(frm_analiz, text="Office Supplies",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r42c1"))

                    r42c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r42c2, tag=("r42c2"))

                    r42c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r42c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r42c3, tag=("r42c3"))

                    r42c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r42c4, tag=("r42c4"))


                    r42c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r42c5, tag=("r42c5"))

                    r42c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r42c6, tag=("r42c6"))


                    r42c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r42c7, tag=("r42c7"))

                    r42c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r42c8, tag=("r42c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt42 = date.today()
                    firsty_gt42= today_gt42.replace(day=1)
                    last_monthy_gt42 = firsty_gt42 -relativedelta(months=5)
                    
                    end_todayy_gt42 = last_monthy_gt42
                    end_firsty_gt42 = end_todayy_gt42.replace(day=1)
                    end_monthy_gt42 = end_firsty_gt42 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt42='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Office Supplies" and acctype="Expenses"'
                    sqly_gt42_val=(last_monthy_gt42,end_monthy_gt42,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt42,sqly_gt42_val)
                    mnty_gt42=fbcursor.fetchone()
                    


                    today542 = date.today()
                    first542 = today542.replace(day=1)
                    last_month542 = first542 -relativedelta(months=4)
                    
                    end_today542 = last_month542
                    end_first542 = end_today542.replace(day=1)
                    end_month542 = end_first542 -relativedelta(days=1)+relativedelta(months=1)

                    sql542='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Office Supplies" and acctype="Expenses"'
                    sql542_val=(last_month542,end_month542,dtl_cmp_pro[0],)
                    fbcursor.execute(sql542,sql542_val)
                    mnt542=fbcursor.fetchone()

                    today442 = date.today()
                    first442 = today442.replace(day=1)
                    last_month442 = first442 -relativedelta(months=3)
                    
                    end_today442 = last_month442
                    end_first442 = end_today442.replace(day=1)
                    end_month442 = end_first442 -relativedelta(days=1)+relativedelta(months=1)

                    sql442='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Office Supplies" and acctype="Expenses"'
                    sql442_val=(last_month442,end_month442,dtl_cmp_pro[0],)
                    fbcursor.execute(sql442,sql442_val)
                    mnt442=fbcursor.fetchone()

                    today342 = date.today()
                    first342 = today342.replace(day=1)
                    last_month342 = first342 -relativedelta(months=2)
                    
                    end_today342 = last_month342
                    end_first342 = end_today342.replace(day=1)
                    end_month342 = end_first342 -relativedelta(days=1)+relativedelta(months=1)

                    sql342='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Office Supplies" and acctype="Expenses"'
                    sql342_val=(last_month342,end_month342,dtl_cmp_pro[0],)
                    fbcursor.execute(sql342,sql342_val)
                    mnt342=fbcursor.fetchone()

                    today242 = date.today()
                    first242 = today242.replace(day=1)
                    last_month242 = first242 -relativedelta(months=1)
                    
                    end_today242 = last_month242
                    end_first242 = end_today242.replace(day=1)
                    end_month242 = end_first242 -relativedelta(days=1)+relativedelta(months=1)

                    sql242='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Office Supplies" and acctype="Expenses"'
                    sql242_val=(last_month242,end_month242,dtl_cmp_pro[0],)
                    fbcursor.execute(sql242,sql242_val)
                    mnt242=fbcursor.fetchone()

                    today421 = date.today()
                    first421 = today421.replace(day=1)
              

                    end_today421 = date.today()
                    end_first421 = end_today421.replace(day=1)
                    end_month421 = end_first421 -relativedelta(days=1)+relativedelta(months=1)

                    sql421='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Office Supplies" and acctype="Expenses"'
                    sql421_val=(first421,end_month421,dtl_cmp_pro[0],)
                    fbcursor.execute(sql421,sql421_val)
                    mnt421=fbcursor.fetchone()

                    sqltt42='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Office Supplies" and acctype="Expenses"'
                    sqltt_val42=(last_monthy_gt42,end_month421,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt42,sqltt_val42)
                    mnttt42=fbcursor.fetchone()
                    
                    if mnty_gt42[0] is None:
                        val642="0.0"
                    else:
                        val642=mnty_gt42[0] 
                    r42c2.delete(0,END)
                    r42c2.insert(0,"$"+str(val642))
                    r42c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt542[0] is None:
                        val542="0.0"
                    else:
                        val542=mnt542[0] 
                    r42c3.delete(0,END)
                    r42c3.insert(0,"$"+str(val542))
                    r42c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt442[0] is None:
                        val442="0.0"
                    else:
                        val442=mnt442[0] 
                    r42c4.delete(0,END)
                    r42c4.insert(0,"$"+str(val442))
                    r42c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt342[0] is None:
                        val342="0.0"
                    else:
                        val342=mnt342[0] 
                    r42c5.delete(0,END)
                    r42c5.insert(0,"$"+str(val342))
                    r42c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt242[0] is None:
                        val242="0.0"
                    else:
                        val242=mnt242[0] 
                    r42c6.delete(0,END)
                    r42c6.insert(0,"$"+str(val242))
                    r42c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt421[0] is None:
                        val421="0.0"
                    else:
                        val421=mnt421[0] 
                    r42c7.delete(0,END)
                    r42c7.insert(0,"$"+str(val421))
                    r42c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt42[0] is None:
                        valtt42="0.0"
                    else:
                        valtt42=mnttt42[0] 
                    r42c8.delete(0,END)
                    r42c8.insert(0,"$"+str(valtt42))
                    r42c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------43 th row
                    lv_name=Label(frm_analiz, text="Postage and Delivery",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r43c1"))

                    r43c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r43c2, tag=("r43c2"))

                    r43c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r43c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r43c3, tag=("r43c3"))

                    r43c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r43c4, tag=("r43c4"))


                    r43c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r43c5, tag=("r43c5"))

                    r43c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r43c6, tag=("r43c6"))


                    r43c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r43c7, tag=("r43c7"))

                    r43c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r43c8, tag=("r43c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt43 = date.today()
                    firsty_gt43= today_gt43.replace(day=1)
                    last_monthy_gt43 = firsty_gt43 -relativedelta(months=5)
                    
                    end_todayy_gt43 = last_monthy_gt43
                    end_firsty_gt43 = end_todayy_gt43.replace(day=1)
                    end_monthy_gt43 = end_firsty_gt43 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt43='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Postage and Delivery" and acctype="Expenses"'
                    sqly_gt43_val=(last_monthy_gt43,end_monthy_gt43,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt43,sqly_gt43_val)
                    mnty_gt43=fbcursor.fetchone()
                    


                    today543 = date.today()
                    first543 = today543.replace(day=1)
                    last_month543 = first543 -relativedelta(months=4)
                    
                    end_today543 = last_month543
                    end_first543 = end_today543.replace(day=1)
                    end_month543 = end_first543 -relativedelta(days=1)+relativedelta(months=1)

                    sql543='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Postage and Delivery" and acctype="Expenses"'
                    sql543_val=(last_month543,end_month543,dtl_cmp_pro[0],)
                    fbcursor.execute(sql543,sql543_val)
                    mnt543=fbcursor.fetchone()

                    today443 = date.today()
                    first443 = today443.replace(day=1)
                    last_month443 = first443 -relativedelta(months=3)
                    
                    end_today443 = last_month443
                    end_first443 = end_today443.replace(day=1)
                    end_month443 = end_first443 -relativedelta(days=1)+relativedelta(months=1)

                    sql443='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Postage and Delivery" and acctype="Expenses"'
                    sql443_val=(last_month443,end_month443,dtl_cmp_pro[0],)
                    fbcursor.execute(sql443,sql443_val)
                    mnt443=fbcursor.fetchone()

                    today343 = date.today()
                    first343 = today343.replace(day=1)
                    last_month343 = first343 -relativedelta(months=2)
                    
                    end_today343 = last_month343
                    end_first343 = end_today343.replace(day=1)
                    end_month343 = end_first343 -relativedelta(days=1)+relativedelta(months=1)

                    sql343='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Postage and Delivery" and acctype="Expenses"'
                    sql343_val=(last_month343,end_month343,dtl_cmp_pro[0],)
                    fbcursor.execute(sql343,sql343_val)
                    mnt343=fbcursor.fetchone()

                    today243 = date.today()
                    first243 = today243.replace(day=1)
                    last_month243 = first243 -relativedelta(months=1)
                    
                    end_today243 = last_month243
                    end_first243 = end_today243.replace(day=1)
                    end_month243 = end_first243 -relativedelta(days=1)+relativedelta(months=1)

                    sql243='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Postage and Delivery" and acctype="Expenses"'
                    sql243_val=(last_month243,end_month243,dtl_cmp_pro[0],)
                    fbcursor.execute(sql243,sql243_val)
                    mnt243=fbcursor.fetchone()

                    today431 = date.today()
                    first431 = today431.replace(day=1)
              

                    end_today431 = date.today()
                    end_first431 = end_today431.replace(day=1)
                    end_month431 = end_first431 -relativedelta(days=1)+relativedelta(months=1)

                    sql431='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Postage and Delivery" and acctype="Expenses"'
                    sql431_val=(first431,end_month431,dtl_cmp_pro[0],)
                    fbcursor.execute(sql431,sql431_val)
                    mnt431=fbcursor.fetchone()

                    sqltt43='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Postage and Delivery" and acctype="Expenses"'
                    sqltt_val43=(last_monthy_gt43,end_month431,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt43,sqltt_val43)
                    mnttt43=fbcursor.fetchone()
                    
                    if mnty_gt43[0] is None:
                        val643="0.0"
                    else:
                        val643=mnty_gt43[0] 
                    r43c2.delete(0,END)
                    r43c2.insert(0,"$"+str(val643))
                    r43c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt543[0] is None:
                        val543="0.0"
                    else:
                        val543=mnt543[0] 
                    r43c3.delete(0,END)
                    r43c3.insert(0,"$"+str(val543))
                    r43c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt443[0] is None:
                        val443="0.0"
                    else:
                        val443=mnt443[0] 
                    r43c4.delete(0,END)
                    r43c4.insert(0,"$"+str(val443))
                    r43c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt343[0] is None:
                        val343="0.0"
                    else:
                        val343=mnt343[0] 
                    r43c5.delete(0,END)
                    r43c5.insert(0,"$"+str(val343))
                    r43c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt243[0] is None:
                        val243="0.0"
                    else:
                        val243=mnt243[0] 
                    r43c6.delete(0,END)
                    r43c6.insert(0,"$"+str(val243))
                    r43c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt431[0] is None:
                        val431="0.0"
                    else:
                        val431=mnt431[0] 
                    r43c7.delete(0,END)
                    r43c7.insert(0,"$"+str(val431))
                    r43c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt43[0] is None:
                        valtt43="0.0"
                    else:
                        valtt43=mnttt43[0] 
                    r43c8.delete(0,END)
                    r43c8.insert(0,"$"+str(valtt43))
                    r43c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    

                    #----------------------------------------------------------44 th row
                    lv_name=Label(frm_analiz, text="Printing and Reproduction",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r44c1"))

                    r44c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r44c2, tag=("r44c2"))

                    r44c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r44c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r44c3, tag=("r44c3"))

                    r44c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r44c4, tag=("r44c4"))


                    r44c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r44c5, tag=("r44c5"))

                    r44c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r44c6, tag=("r44c6"))


                    r44c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r44c7, tag=("r44c7"))

                    r44c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r44c8, tag=("r44c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt44 = date.today()
                    firsty_gt44= today_gt44.replace(day=1)
                    last_monthy_gt44 = firsty_gt44 -relativedelta(months=5)
                    
                    end_todayy_gt44 = last_monthy_gt44
                    end_firsty_gt44 = end_todayy_gt44.replace(day=1)
                    end_monthy_gt44 = end_firsty_gt44 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt44='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Printing and Reproduction" and acctype="Expenses"'
                    sqly_gt44_val=(last_monthy_gt44,end_monthy_gt44,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt44,sqly_gt44_val)
                    mnty_gt44=fbcursor.fetchone()
                    


                    today544 = date.today()
                    first544 = today544.replace(day=1)
                    last_month544 = first544 -relativedelta(months=4)
                    
                    end_today544 = last_month544
                    end_first544 = end_today544.replace(day=1)
                    end_month544 = end_first544 -relativedelta(days=1)+relativedelta(months=1)

                    sql544='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Printing and Reproduction" and acctype="Expenses"'
                    sql544_val=(last_month544,end_month544,dtl_cmp_pro[0],)
                    fbcursor.execute(sql544,sql544_val)
                    mnt544=fbcursor.fetchone()

                    today444 = date.today()
                    first444 = today444.replace(day=1)
                    last_month444 = first444 -relativedelta(months=3)
                    
                    end_today444 = last_month444
                    end_first444 = end_today444.replace(day=1)
                    end_month444 = end_first444 -relativedelta(days=1)+relativedelta(months=1)

                    sql444='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Printing and Reproduction" and acctype="Expenses"'
                    sql444_val=(last_month444,end_month444,dtl_cmp_pro[0],)
                    fbcursor.execute(sql444,sql444_val)
                    mnt444=fbcursor.fetchone()

                    today344 = date.today()
                    first344 = today344.replace(day=1)
                    last_month344 = first344 -relativedelta(months=2)
                    
                    end_today344 = last_month344
                    end_first344 = end_today344.replace(day=1)
                    end_month344 = end_first344 -relativedelta(days=1)+relativedelta(months=1)

                    sql344='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Printing and Reproduction" and acctype="Expenses"'
                    sql344_val=(last_month344,end_month344,dtl_cmp_pro[0],)
                    fbcursor.execute(sql344,sql344_val)
                    mnt344=fbcursor.fetchone()

                    today244 = date.today()
                    first244 = today244.replace(day=1)
                    last_month244 = first244 -relativedelta(months=1)
                    
                    end_today244 = last_month244
                    end_first244 = end_today244.replace(day=1)
                    end_month244 = end_first244 -relativedelta(days=1)+relativedelta(months=1)

                    sql244='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Printing and Reproduction" and acctype="Expenses"'
                    sql244_val=(last_month244,end_month244,dtl_cmp_pro[0],)
                    fbcursor.execute(sql244,sql244_val)
                    mnt244=fbcursor.fetchone()

                    today441 = date.today()
                    first441 = today441.replace(day=1)
              

                    end_today441 = date.today()
                    end_first441 = end_today441.replace(day=1)
                    end_month441 = end_first441 -relativedelta(days=1)+relativedelta(months=1)

                    sql441='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Printing and Reproduction" and acctype="Expenses"'
                    sql441_val=(first441,end_month441,dtl_cmp_pro[0],)
                    fbcursor.execute(sql441,sql441_val)
                    mnt441=fbcursor.fetchone()

                    sqltt44='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Printing and Reproduction" and acctype="Expenses"'
                    sqltt_val44=(last_monthy_gt44,end_month441,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt44,sqltt_val44)
                    mnttt44=fbcursor.fetchone()
                    
                    if mnty_gt44[0] is None:
                        val644="0.0"
                    else:
                        val644=mnty_gt44[0] 
                    r44c2.delete(0,END)
                    r44c2.insert(0,"$"+str(val644))
                    r44c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt544[0] is None:
                        val544="0.0"
                    else:
                        val544=mnt544[0] 
                    r44c3.delete(0,END)
                    r44c3.insert(0,"$"+str(val544))
                    r44c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt444[0] is None:
                        val444="0.0"
                    else:
                        val444=mnt444[0] 
                    r44c4.delete(0,END)
                    r44c4.insert(0,"$"+str(val444))
                    r44c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt344[0] is None:
                        val344="0.0"
                    else:
                        val344=mnt344[0] 
                    r44c5.delete(0,END)
                    r44c5.insert(0,"$"+str(val344))
                    r44c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt244[0] is None:
                        val244="0.0"
                    else:
                        val244=mnt244[0] 
                    r44c6.delete(0,END)
                    r44c6.insert(0,"$"+str(val244))
                    r44c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt441[0] is None:
                        val441="0.0"
                    else:
                        val441=mnt441[0] 
                    r44c7.delete(0,END)
                    r44c7.insert(0,"$"+str(val441))
                    r44c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt44[0] is None:
                        valtt44="0.0"
                    else:
                        valtt44=mnttt44[0] 
                    r44c8.delete(0,END)
                    r44c8.insert(0,"$"+str(valtt44))
                    r44c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------45 th row
                    lv_name=Label(frm_analiz, text="Professional Fees",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r45c1"))

                    r45c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r45c2, tag=("r45c2"))

                    r45c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r45c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r45c3, tag=("r45c3"))

                    r45c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r45c4, tag=("r45c4"))


                    r45c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r45c5, tag=("r45c5"))

                    r45c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r45c6, tag=("r45c6"))


                    r45c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r45c7, tag=("r45c7"))

                    r45c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r45c8, tag=("r45c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt45 = date.today()
                    firsty_gt45= today_gt45.replace(day=1)
                    last_monthy_gt45 = firsty_gt45 -relativedelta(months=5)
                    
                    end_todayy_gt45 = last_monthy_gt45
                    end_firsty_gt45 = end_todayy_gt45.replace(day=1)
                    end_monthy_gt45 = end_firsty_gt45 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt45='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Professional Fees" and acctype="Expenses"'
                    sqly_gt45_val=(last_monthy_gt45,end_monthy_gt45,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt45,sqly_gt45_val)
                    mnty_gt45=fbcursor.fetchone()
                    


                    today545 = date.today()
                    first545 = today545.replace(day=1)
                    last_month545 = first545 -relativedelta(months=4)
                    
                    end_today545 = last_month545
                    end_first545 = end_today545.replace(day=1)
                    end_month545 = end_first545 -relativedelta(days=1)+relativedelta(months=1)

                    sql545='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Professional Fees" and acctype="Expenses"'
                    sql545_val=(last_month545,end_month545,dtl_cmp_pro[0],)
                    fbcursor.execute(sql545,sql545_val)
                    mnt545=fbcursor.fetchone()

                    today454 = date.today()
                    first454 = today454.replace(day=1)
                    last_month454 = first454 -relativedelta(months=3)
                    
                    end_today454 = last_month454
                    end_first454 = end_today454.replace(day=1)
                    end_month454 = end_first454 -relativedelta(days=1)+relativedelta(months=1)

                    sql454='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Professional Fees" and acctype="Expenses"'
                    sql454_val=(last_month454,end_month454,dtl_cmp_pro[0],)
                    fbcursor.execute(sql454,sql454_val)
                    mnt454=fbcursor.fetchone()

                    today345 = date.today()
                    first345 = today345.replace(day=1)
                    last_month345 = first345 -relativedelta(months=2)
                    
                    end_today345 = last_month345
                    end_first345 = end_today345.replace(day=1)
                    end_month345 = end_first345 -relativedelta(days=1)+relativedelta(months=1)

                    sql345='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Professional Fees" and acctype="Expenses"'
                    sql345_val=(last_month345,end_month345,dtl_cmp_pro[0],)
                    fbcursor.execute(sql345,sql345_val)
                    mnt345=fbcursor.fetchone()

                    today245 = date.today()
                    first245 = today245.replace(day=1)
                    last_month245 = first245 -relativedelta(months=1)
                    
                    end_today245 = last_month245
                    end_first245 = end_today245.replace(day=1)
                    end_month245 = end_first245 -relativedelta(days=1)+relativedelta(months=1)

                    sql245='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Professional Fees" and acctype="Expenses"'
                    sql245_val=(last_month245,end_month245,dtl_cmp_pro[0],)
                    fbcursor.execute(sql245,sql245_val)
                    mnt245=fbcursor.fetchone()

                    today451 = date.today()
                    first451 = today451.replace(day=1)
              

                    end_today451 = date.today()
                    end_first451 = end_today451.replace(day=1)
                    end_month451 = end_first451 -relativedelta(days=1)+relativedelta(months=1)

                    sql451='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Professional Fees" and acctype="Expenses"'
                    sql451_val=(first451,end_month451,dtl_cmp_pro[0],)
                    fbcursor.execute(sql451,sql451_val)
                    mnt451=fbcursor.fetchone()

                    sqltt45='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Professional Fees" and acctype="Expenses"'
                    sqltt_val45=(last_monthy_gt45,end_month451,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt45,sqltt_val45)
                    mnttt45=fbcursor.fetchone()
                    
                    if mnty_gt45[0] is None:
                        val645="0.0"
                    else:
                        val645=mnty_gt45[0] 
                    r45c2.delete(0,END)
                    r45c2.insert(0,"$"+str(val645))
                    r45c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt545[0] is None:
                        val545="0.0"
                    else:
                        val545=mnt545[0] 
                    r45c3.delete(0,END)
                    r45c3.insert(0,"$"+str(val545))
                    r45c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt454[0] is None:
                        val454="0.0"
                    else:
                        val454=mnt454[0] 
                    r45c4.delete(0,END)
                    r45c4.insert(0,"$"+str(val454))
                    r45c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt345[0] is None:
                        val345="0.0"
                    else:
                        val345=mnt345[0] 
                    r45c5.delete(0,END)
                    r45c5.insert(0,"$"+str(val345))
                    r45c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt245[0] is None:
                        val245="0.0"
                    else:
                        val245=mnt245[0] 
                    r45c6.delete(0,END)
                    r45c6.insert(0,"$"+str(val245))
                    r45c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt451[0] is None:
                        val451="0.0"
                    else:
                        val451=mnt451[0] 
                    r45c7.delete(0,END)
                    r45c7.insert(0,"$"+str(val451))
                    r45c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt45[0] is None:
                        valtt45="0.0"
                    else:
                        valtt45=mnttt45[0] 
                    r45c8.delete(0,END)
                    r45c8.insert(0,"$"+str(valtt45))
                    r45c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------46 th row
                    lv_name=Label(frm_analiz, text="Purchases",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r46c1"))

                    r46c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r46c2, tag=("r46c2"))

                    r46c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r46c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r46c3, tag=("r46c3"))

                    r46c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r46c4, tag=("r46c4"))


                    r46c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r46c5, tag=("r46c5"))

                    r46c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r46c6, tag=("r46c6"))


                    r46c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r46c7, tag=("r46c7"))

                    r46c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r46c8, tag=("r46c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt46 = date.today()
                    firsty_gt46= today_gt46.replace(day=1)
                    last_monthy_gt46 = firsty_gt46 -relativedelta(months=5)
                    
                    end_todayy_gt46 = last_monthy_gt46
                    end_firsty_gt46 = end_todayy_gt46.replace(day=1)
                    end_monthy_gt46 = end_firsty_gt46 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt46='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Purchases" and acctype="Expenses"'
                    sqly_gt46_val=(last_monthy_gt46,end_monthy_gt46,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt46,sqly_gt46_val)
                    mnty_gt46=fbcursor.fetchone()
                    


                    today546 = date.today()
                    first546 = today546.replace(day=1)
                    last_month546 = first546 -relativedelta(months=4)
                    
                    end_today546 = last_month546
                    end_first546 = end_today546.replace(day=1)
                    end_month546 = end_first546 -relativedelta(days=1)+relativedelta(months=1)

                    sql546='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Purchases" and acctype="Expenses"'
                    sql546_val=(last_month546,end_month546,dtl_cmp_pro[0],)
                    fbcursor.execute(sql546,sql546_val)
                    mnt546=fbcursor.fetchone()

                    today464 = date.today()
                    first464 = today464.replace(day=1)
                    last_month464 = first464 -relativedelta(months=3)
                    
                    end_today464 = last_month464
                    end_first464 = end_today464.replace(day=1)
                    end_month464 = end_first464 -relativedelta(days=1)+relativedelta(months=1)

                    sql464='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Purchases" and acctype="Expenses"'
                    sql464_val=(last_month464,end_month464,dtl_cmp_pro[0],)
                    fbcursor.execute(sql464,sql464_val)
                    mnt464=fbcursor.fetchone()

                    today346 = date.today()
                    first346 = today346.replace(day=1)
                    last_month346 = first346 -relativedelta(months=2)
                    
                    end_today346 = last_month346
                    end_first346 = end_today346.replace(day=1)
                    end_month346 = end_first346 -relativedelta(days=1)+relativedelta(months=1)

                    sql346='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Purchases" and acctype="Expenses"'
                    sql346_val=(last_month346,end_month346,dtl_cmp_pro[0],)
                    fbcursor.execute(sql346,sql346_val)
                    mnt346=fbcursor.fetchone()

                    today246 = date.today()
                    first246 = today246.replace(day=1)
                    last_month246 = first246 -relativedelta(months=1)
                    
                    end_today246 = last_month246
                    end_first246 = end_today246.replace(day=1)
                    end_month246 = end_first246 -relativedelta(days=1)+relativedelta(months=1)

                    sql246='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Purchases" and acctype="Expenses"'
                    sql246_val=(last_month246,end_month246,dtl_cmp_pro[0],)
                    fbcursor.execute(sql246,sql246_val)
                    mnt246=fbcursor.fetchone()

                    today461 = date.today()
                    first461 = today461.replace(day=1)
              

                    end_today461 = date.today()
                    end_first461 = end_today461.replace(day=1)
                    end_month461 = end_first461 -relativedelta(days=1)+relativedelta(months=1)

                    sql461='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Purchases" and acctype="Expenses"'
                    sql461_val=(first461,end_month461,dtl_cmp_pro[0],)
                    fbcursor.execute(sql461,sql461_val)
                    mnt461=fbcursor.fetchone()

                    sqltt46='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Purchases" and acctype="Expenses"'
                    sqltt_val46=(last_monthy_gt46,end_month461,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt46,sqltt_val46)
                    mnttt46=fbcursor.fetchone()
                    
                    if mnty_gt46[0] is None:
                        val646="0.0"
                    else:
                        val646=mnty_gt46[0] 
                    r46c2.delete(0,END)
                    r46c2.insert(0,"$"+str(val646))
                    r46c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt546[0] is None:
                        val546="0.0"
                    else:
                        val546=mnt546[0] 
                    r46c3.delete(0,END)
                    r46c3.insert(0,"$"+str(val546))
                    r46c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt464[0] is None:
                        val464="0.0"
                    else:
                        val464=mnt464[0] 
                    r46c4.delete(0,END)
                    r46c4.insert(0,"$"+str(val464))
                    r46c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt346[0] is None:
                        val346="0.0"
                    else:
                        val346=mnt346[0] 
                    r46c5.delete(0,END)
                    r46c5.insert(0,"$"+str(val346))
                    r46c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt246[0] is None:
                        val246="0.0"
                    else:
                        val246=mnt246[0] 
                    r46c6.delete(0,END)
                    r46c6.insert(0,"$"+str(val246))
                    r46c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt461[0] is None:
                        val461="0.0"
                    else:
                        val461=mnt461[0] 
                    r46c7.delete(0,END)
                    r46c7.insert(0,"$"+str(val461))
                    r46c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt46[0] is None:
                        valtt46="0.0"
                    else:
                        valtt46=mnttt46[0] 
                    r46c8.delete(0,END)
                    r46c8.insert(0,"$"+str(valtt46))
                    r46c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------47 th row
                    lv_name=Label(frm_analiz, text="Rent Expense",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r47c1"))

                    r47c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r47c2, tag=("r47c2"))

                    r47c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r47c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r47c3, tag=("r47c3"))

                    r47c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r47c4, tag=("r47c4"))


                    r47c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r47c5, tag=("r47c5"))

                    r47c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r47c6, tag=("r47c6"))


                    r47c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r47c7, tag=("r47c7"))

                    r47c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r47c8, tag=("r47c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt47 = date.today()
                    firsty_gt47= today_gt47.replace(day=1)
                    last_monthy_gt47 = firsty_gt47 -relativedelta(months=5)
                    
                    end_todayy_gt47 = last_monthy_gt47
                    end_firsty_gt47 = end_todayy_gt47.replace(day=1)
                    end_monthy_gt47 = end_firsty_gt47 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt47='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Rent Expense" and acctype="Expenses"'
                    sqly_gt47_val=(last_monthy_gt47,end_monthy_gt47,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt47,sqly_gt47_val)
                    mnty_gt47=fbcursor.fetchone()
                    


                    today547 = date.today()
                    first547 = today547.replace(day=1)
                    last_month547 = first547 -relativedelta(months=4)
                    
                    end_today547 = last_month547
                    end_first547 = end_today547.replace(day=1)
                    end_month547 = end_first547 -relativedelta(days=1)+relativedelta(months=1)

                    sql547='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Rent Expense" and acctype="Expenses"'
                    sql547_val=(last_month547,end_month547,dtl_cmp_pro[0],)
                    fbcursor.execute(sql547,sql547_val)
                    mnt547=fbcursor.fetchone()

                    today474 = date.today()
                    first474 = today474.replace(day=1)
                    last_month474 = first474 -relativedelta(months=3)
                    
                    end_today474 = last_month474
                    end_first474 = end_today474.replace(day=1)
                    end_month474 = end_first474 -relativedelta(days=1)+relativedelta(months=1)

                    sql474='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Rent Expense" and acctype="Expenses"'
                    sql474_val=(last_month474,end_month474,dtl_cmp_pro[0],)
                    fbcursor.execute(sql474,sql474_val)
                    mnt474=fbcursor.fetchone()

                    today347 = date.today()
                    first347 = today347.replace(day=1)
                    last_month347 = first347 -relativedelta(months=2)
                    
                    end_today347 = last_month347
                    end_first347 = end_today347.replace(day=1)
                    end_month347 = end_first347 -relativedelta(days=1)+relativedelta(months=1)

                    sql347='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Rent Expense" and acctype="Expenses"'
                    sql347_val=(last_month347,end_month347,dtl_cmp_pro[0],)
                    fbcursor.execute(sql347,sql347_val)
                    mnt347=fbcursor.fetchone()

                    today247 = date.today()
                    first247 = today247.replace(day=1)
                    last_month247 = first247 -relativedelta(months=1)
                    
                    end_today247 = last_month247
                    end_first247 = end_today247.replace(day=1)
                    end_month247 = end_first247 -relativedelta(days=1)+relativedelta(months=1)

                    sql247='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Rent Expense" and acctype="Expenses"'
                    sql247_val=(last_month247,end_month247,dtl_cmp_pro[0],)
                    fbcursor.execute(sql247,sql247_val)
                    mnt247=fbcursor.fetchone()

                    today471 = date.today()
                    first471 = today471.replace(day=1)
              

                    end_today471 = date.today()
                    end_first471 = end_today471.replace(day=1)
                    end_month471 = end_first471 -relativedelta(days=1)+relativedelta(months=1)

                    sql471='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Rent Expense" and acctype="Expenses"'
                    sql471_val=(first471,end_month471,dtl_cmp_pro[0],)
                    fbcursor.execute(sql471,sql471_val)
                    mnt471=fbcursor.fetchone()

                    sqltt47='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Rent Expense" and acctype="Expenses"'
                    sqltt_val47=(last_monthy_gt47,end_month471,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt47,sqltt_val47)
                    mnttt47=fbcursor.fetchone()
                    
                    if mnty_gt47[0] is None:
                        val647="0.0"
                    else:
                        val647=mnty_gt47[0] 
                    r47c2.delete(0,END)
                    r47c2.insert(0,"$"+str(val647))
                    r47c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt547[0] is None:
                        val547="0.0"
                    else:
                        val547=mnt547[0] 
                    r47c3.delete(0,END)
                    r47c3.insert(0,"$"+str(val547))
                    r47c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt474[0] is None:
                        val474="0.0"
                    else:
                        val474=mnt474[0] 
                    r47c4.delete(0,END)
                    r47c4.insert(0,"$"+str(val474))
                    r47c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt347[0] is None:
                        val347="0.0"
                    else:
                        val347=mnt347[0] 
                    r47c5.delete(0,END)
                    r47c5.insert(0,"$"+str(val347))
                    r47c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt247[0] is None:
                        val247="0.0"
                    else:
                        val247=mnt247[0] 
                    r47c6.delete(0,END)
                    r47c6.insert(0,"$"+str(val247))
                    r47c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt471[0] is None:
                        val471="0.0"
                    else:
                        val471=mnt471[0] 
                    r47c7.delete(0,END)
                    r47c7.insert(0,"$"+str(val471))
                    r47c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt47[0] is None:
                        valtt47="0.0"
                    else:
                        valtt47=mnttt47[0] 
                    r47c8.delete(0,END)
                    r47c8.insert(0,"$"+str(valtt47))
                    r47c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------48 th row
                    lv_name=Label(frm_analiz, text="Repair and Maintanance",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r48c1"))

                    r48c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r48c2, tag=("r48c2"))

                    r48c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r48c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r48c3, tag=("r48c3"))

                    r48c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r48c4, tag=("r48c4"))


                    r48c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r48c5, tag=("r48c5"))

                    r48c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r48c6, tag=("r48c6"))


                    r48c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r48c7, tag=("r48c7"))

                    r48c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r48c8, tag=("r48c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt48 = date.today()
                    firsty_gt48= today_gt48.replace(day=1)
                    last_monthy_gt48 = firsty_gt48 -relativedelta(months=5)
                    
                    end_todayy_gt48 = last_monthy_gt48
                    end_firsty_gt48 = end_todayy_gt48.replace(day=1)
                    end_monthy_gt48 = end_firsty_gt48 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt48='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Repair and Maintanance" and acctype="Expenses"'
                    sqly_gt48_val=(last_monthy_gt48,end_monthy_gt48,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt48,sqly_gt48_val)
                    mnty_gt48=fbcursor.fetchone()
                    


                    today548 = date.today()
                    first548 = today548.replace(day=1)
                    last_month548 = first548 -relativedelta(months=4)
                    
                    end_today548 = last_month548
                    end_first548 = end_today548.replace(day=1)
                    end_month548 = end_first548 -relativedelta(days=1)+relativedelta(months=1)

                    sql548='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Repair and Maintanance" and acctype="Expenses"'
                    sql548_val=(last_month548,end_month548,dtl_cmp_pro[0],)
                    fbcursor.execute(sql548,sql548_val)
                    mnt548=fbcursor.fetchone()

                    today484 = date.today()
                    first484 = today484.replace(day=1)
                    last_month484 = first484 -relativedelta(months=3)
                    
                    end_today484 = last_month484
                    end_first484 = end_today484.replace(day=1)
                    end_month484 = end_first484 -relativedelta(days=1)+relativedelta(months=1)

                    sql484='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Repair and Maintanance" and acctype="Expenses"'
                    sql484_val=(last_month484,end_month484,dtl_cmp_pro[0],)
                    fbcursor.execute(sql484,sql484_val)
                    mnt484=fbcursor.fetchone()

                    today348 = date.today()
                    first348 = today348.replace(day=1)
                    last_month348 = first348 -relativedelta(months=2)
                    
                    end_today348 = last_month348
                    end_first348 = end_today348.replace(day=1)
                    end_month348 = end_first348 -relativedelta(days=1)+relativedelta(months=1)

                    sql348='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Repair and Maintanance" and acctype="Expenses"'
                    sql348_val=(last_month348,end_month348,dtl_cmp_pro[0],)
                    fbcursor.execute(sql348,sql348_val)
                    mnt348=fbcursor.fetchone()

                    today248 = date.today()
                    first248 = today248.replace(day=1)
                    last_month248 = first248 -relativedelta(months=1)
                    
                    end_today248 = last_month248
                    end_first248 = end_today248.replace(day=1)
                    end_month248 = end_first248 -relativedelta(days=1)+relativedelta(months=1)

                    sql248='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Repair and Maintanance" and acctype="Expenses"'
                    sql248_val=(last_month248,end_month248,dtl_cmp_pro[0],)
                    fbcursor.execute(sql248,sql248_val)
                    mnt248=fbcursor.fetchone()

                    today481 = date.today()
                    first481 = today481.replace(day=1)
              

                    end_today481 = date.today()
                    end_first481 = end_today481.replace(day=1)
                    end_month481 = end_first481 -relativedelta(days=1)+relativedelta(months=1)

                    sql481='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Repair and Maintanance" and acctype="Expenses"'
                    sql481_val=(first481,end_month481,dtl_cmp_pro[0],)
                    fbcursor.execute(sql481,sql481_val)
                    mnt481=fbcursor.fetchone()

                    sqltt48='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Repair and Maintanance" and acctype="Expenses"'
                    sqltt_val48=(last_monthy_gt48,end_month481,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt48,sqltt_val48)
                    mnttt48=fbcursor.fetchone()
                    
                    if mnty_gt48[0] is None:
                        val648="0.0"
                    else:
                        val648=mnty_gt48[0] 
                    r48c2.delete(0,END)
                    r48c2.insert(0,"$"+str(val648))
                    r48c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt548[0] is None:
                        val548="0.0"
                    else:
                        val548=mnt548[0] 
                    r48c3.delete(0,END)
                    r48c3.insert(0,"$"+str(val548))
                    r48c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt484[0] is None:
                        val484="0.0"
                    else:
                        val484=mnt484[0] 
                    r48c4.delete(0,END)
                    r48c4.insert(0,"$"+str(val484))
                    r48c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt348[0] is None:
                        val348="0.0"
                    else:
                        val348=mnt348[0] 
                    r48c5.delete(0,END)
                    r48c5.insert(0,"$"+str(val348))
                    r48c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt248[0] is None:
                        val248="0.0"
                    else:
                        val248=mnt248[0] 
                    r48c6.delete(0,END)
                    r48c6.insert(0,"$"+str(val248))
                    r48c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt481[0] is None:
                        val481="0.0"
                    else:
                        val481=mnt481[0] 
                    r48c7.delete(0,END)
                    r48c7.insert(0,"$"+str(val481))
                    r48c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt48[0] is None:
                        valtt48="0.0"
                    else:
                        valtt48=mnttt48[0] 
                    r48c8.delete(0,END)
                    r48c8.insert(0,"$"+str(valtt48))
                    r48c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------49 th row
                    lv_name=Label(frm_analiz, text="Small Tools and Equipments",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r49c1"))

                    r49c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r49c2, tag=("r49c2"))

                    r49c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r49c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r49c3, tag=("r49c3"))

                    r49c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r49c4, tag=("r49c4"))


                    r49c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r49c5, tag=("r49c5"))

                    r49c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r49c6, tag=("r49c6"))


                    r49c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r49c7, tag=("r49c7"))

                    r49c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r49c8, tag=("r49c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt49 = date.today()
                    firsty_gt49= today_gt49.replace(day=1)
                    last_monthy_gt49 = firsty_gt49 -relativedelta(months=5)
                    
                    end_todayy_gt49 = last_monthy_gt49
                    end_firsty_gt49 = end_todayy_gt49.replace(day=1)
                    end_monthy_gt49 = end_firsty_gt49 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt49='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Small Tools and Equipments" and acctype="Expenses"'
                    sqly_gt49_val=(last_monthy_gt49,end_monthy_gt49,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt49,sqly_gt49_val)
                    mnty_gt49=fbcursor.fetchone()
                    


                    today549 = date.today()
                    first549 = today549.replace(day=1)
                    last_month549 = first549 -relativedelta(months=4)
                    
                    end_today549 = last_month549
                    end_first549 = end_today549.replace(day=1)
                    end_month549 = end_first549 -relativedelta(days=1)+relativedelta(months=1)

                    sql549='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Small Tools and Equipments" and acctype="Expenses"'
                    sql549_val=(last_month549,end_month549,dtl_cmp_pro[0],)
                    fbcursor.execute(sql549,sql549_val)
                    mnt549=fbcursor.fetchone()

                    today494 = date.today()
                    first494 = today494.replace(day=1)
                    last_month494 = first494 -relativedelta(months=3)
                    
                    end_today494 = last_month494
                    end_first494 = end_today494.replace(day=1)
                    end_month494 = end_first494 -relativedelta(days=1)+relativedelta(months=1)

                    sql494='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Small Tools and Equipments" and acctype="Expenses"'
                    sql494_val=(last_month494,end_month494,dtl_cmp_pro[0],)
                    fbcursor.execute(sql494,sql494_val)
                    mnt494=fbcursor.fetchone()

                    today349 = date.today()
                    first349 = today349.replace(day=1)
                    last_month349 = first349 -relativedelta(months=2)
                    
                    end_today349 = last_month349
                    end_first349 = end_today349.replace(day=1)
                    end_month349 = end_first349 -relativedelta(days=1)+relativedelta(months=1)

                    sql349='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Small Tools and Equipments" and acctype="Expenses"'
                    sql349_val=(last_month349,end_month349,dtl_cmp_pro[0],)
                    fbcursor.execute(sql349,sql349_val)
                    mnt349=fbcursor.fetchone()

                    today249 = date.today()
                    first249 = today249.replace(day=1)
                    last_month249 = first249 -relativedelta(months=1)
                    
                    end_today249 = last_month249
                    end_first249 = end_today249.replace(day=1)
                    end_month249 = end_first249 -relativedelta(days=1)+relativedelta(months=1)

                    sql249='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Small Tools and Equipments" and acctype="Expenses"'
                    sql249_val=(last_month249,end_month249,dtl_cmp_pro[0],)
                    fbcursor.execute(sql249,sql249_val)
                    mnt249=fbcursor.fetchone()

                    today491 = date.today()
                    first491 = today491.replace(day=1)
              

                    end_today491 = date.today()
                    end_first491 = end_today491.replace(day=1)
                    end_month491 = end_first491 -relativedelta(days=1)+relativedelta(months=1)

                    sql491='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Small Tools and Equipments" and acctype="Expenses"'
                    sql491_val=(first491,end_month491,dtl_cmp_pro[0],)
                    fbcursor.execute(sql491,sql491_val)
                    mnt491=fbcursor.fetchone()

                    sqltt49='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Small Tools and Equipments" and acctype="Expenses"'
                    sqltt_val49=(last_monthy_gt49,end_month491,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt49,sqltt_val49)
                    mnttt49=fbcursor.fetchone()
                    
                    if mnty_gt49[0] is None:
                        val649="0.0"
                    else:
                        val649=mnty_gt49[0] 
                    r49c2.delete(0,END)
                    r49c2.insert(0,"$"+str(val649))
                    r49c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt549[0] is None:
                        val549="0.0"
                    else:
                        val549=mnt549[0] 
                    r49c3.delete(0,END)
                    r49c3.insert(0,"$"+str(val549))
                    r49c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt494[0] is None:
                        val494="0.0"
                    else:
                        val494=mnt494[0] 
                    r49c4.delete(0,END)
                    r49c4.insert(0,"$"+str(val494))
                    r49c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt349[0] is None:
                        val349="0.0"
                    else:
                        val349=mnt349[0] 
                    r49c5.delete(0,END)
                    r49c5.insert(0,"$"+str(val349))
                    r49c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt249[0] is None:
                        val249="0.0"
                    else:
                        val249=mnt249[0] 
                    r49c6.delete(0,END)
                    r49c6.insert(0,"$"+str(val249))
                    r49c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt491[0] is None:
                        val491="0.0"
                    else:
                        val491=mnt491[0] 
                    r49c7.delete(0,END)
                    r49c7.insert(0,"$"+str(val491))
                    r49c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt49[0] is None:
                        valtt49="0.0"
                    else:
                        valtt49=mnttt49[0] 
                    r49c8.delete(0,END)
                    r49c8.insert(0,"$"+str(valtt49))
                    r49c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------50 th row
                    lv_name=Label(frm_analiz, text="Swachh Barath Cess Expense",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r50c1"))

                    r50c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r50c2, tag=("r50c2"))

                    r50c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r50c3, tag=("r50c3"))

                    r50c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r50c4, tag=("r50c4"))


                    r50c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r50c5, tag=("r50c5"))

                    r50c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r50c6, tag=("r50c6"))


                    r50c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r50c7, tag=("r50c7"))

                    r50c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r50c8, tag=("r50c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt50 = date.today()
                    firsty_gt50= today_gt50.replace(day=1)
                    last_monthy_gt50 = firsty_gt50 -relativedelta(months=5)
                    
                    end_todayy_gt50 = last_monthy_gt50
                    end_firsty_gt50 = end_todayy_gt50.replace(day=1)
                    end_monthy_gt50 = end_firsty_gt50 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt50='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Swachh Barath Cess Expense" and acctype="Expenses"'
                    sqly_gt50_val=(last_monthy_gt50,end_monthy_gt50,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt50,sqly_gt50_val)
                    mnty_gt50=fbcursor.fetchone()
                    


                    today550 = date.today()
                    first550 = today550.replace(day=1)
                    last_month550 = first550 -relativedelta(months=4)
                    
                    end_today550 = last_month550
                    end_first550 = end_today550.replace(day=1)
                    end_month550 = end_first550 -relativedelta(days=1)+relativedelta(months=1)

                    sql550='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Swachh Barath Cess Expense" and acctype="Expenses"'
                    sql550_val=(last_month550,end_month550,dtl_cmp_pro[0],)
                    fbcursor.execute(sql550,sql550_val)
                    mnt550=fbcursor.fetchone()

                    today504 = date.today()
                    first504 = today504.replace(day=1)
                    last_month504 = first504 -relativedelta(months=3)
                    
                    end_today504 = last_month504
                    end_first504 = end_today504.replace(day=1)
                    end_month504 = end_first504 -relativedelta(days=1)+relativedelta(months=1)

                    sql504='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Swachh Barath Cess Expense" and acctype="Expenses"'
                    sql504_val=(last_month504,end_month504,dtl_cmp_pro[0],)
                    fbcursor.execute(sql504,sql504_val)
                    mnt504=fbcursor.fetchone()

                    today350 = date.today()
                    first350 = today350.replace(day=1)
                    last_month350 = first350 -relativedelta(months=2)
                    
                    end_today350 = last_month350
                    end_first350 = end_today350.replace(day=1)
                    end_month350 = end_first350 -relativedelta(days=1)+relativedelta(months=1)

                    sql350='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Swachh Barath Cess Expense" and acctype="Expenses"'
                    sql350_val=(last_month350,end_month350,dtl_cmp_pro[0],)
                    fbcursor.execute(sql350,sql350_val)
                    mnt350=fbcursor.fetchone()

                    today250 = date.today()
                    first250 = today250.replace(day=1)
                    last_month250 = first250 -relativedelta(months=1)
                    
                    end_today250 = last_month250
                    end_first250 = end_today250.replace(day=1)
                    end_month250 = end_first250 -relativedelta(days=1)+relativedelta(months=1)

                    sql250='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Swachh Barath Cess Expense" and acctype="Expenses"'
                    sql250_val=(last_month250,end_month250,dtl_cmp_pro[0],)
                    fbcursor.execute(sql250,sql250_val)
                    mnt250=fbcursor.fetchone()

                    today501 = date.today()
                    first501 = today501.replace(day=1)
              

                    end_today501 = date.today()
                    end_first501 = end_today501.replace(day=1)
                    end_month501 = end_first501 -relativedelta(days=1)+relativedelta(months=1)

                    sql501='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Swachh Barath Cess Expense" and acctype="Expenses"'
                    sql501_val=(first501,end_month501,dtl_cmp_pro[0],)
                    fbcursor.execute(sql501,sql501_val)
                    mnt501=fbcursor.fetchone()

                    sqltt50='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Swachh Barath Cess Expense" and acctype="Expenses"'
                    sqltt_val50=(last_monthy_gt50,end_month501,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt50,sqltt_val50)
                    mnttt50=fbcursor.fetchone()
                    
                    if mnty_gt50[0] is None:
                        val650="0.0"
                    else:
                        val650=mnty_gt50[0] 
                    r50c2.delete(0,END)
                    r50c2.insert(0,"$"+str(val650))
                    r50c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt550[0] is None:
                        val550="0.0"
                    else:
                        val550=mnt550[0] 
                    r50c3.delete(0,END)
                    r50c3.insert(0,"$"+str(val550))
                    r50c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt504[0] is None:
                        val504="0.0"
                    else:
                        val504=mnt504[0] 
                    r50c4.delete(0,END)
                    r50c4.insert(0,"$"+str(val504))
                    r50c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt350[0] is None:
                        val350="0.0"
                    else:
                        val350=mnt350[0] 
                    r50c5.delete(0,END)
                    r50c5.insert(0,"$"+str(val350))
                    r50c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt250[0] is None:
                        val250="0.0"
                    else:
                        val250=mnt250[0] 
                    r50c6.delete(0,END)
                    r50c6.insert(0,"$"+str(val250))
                    r50c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt501[0] is None:
                        val501="0.0"
                    else:
                        val501=mnt501[0] 
                    r50c7.delete(0,END)
                    r50c7.insert(0,"$"+str(val501))
                    r50c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt50[0] is None:
                        valtt50="0.0"
                    else:
                        valtt50=mnttt50[0] 
                    r50c8.delete(0,END)
                    r50c8.insert(0,"$"+str(valtt50))
                    r50c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    #----------------------------------------------------------51 th row
                    lv_name=Label(frm_analiz, text="Taxes-Property",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r51c1"))

                    r51c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r51c2, tag=("r51c2"))

                    r51c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r51c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r51c3, tag=("r51c3"))

                    r51c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r51c4, tag=("r51c4"))


                    r51c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r51c5, tag=("r51c5"))

                    r51c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r51c6, tag=("r51c6"))


                    r51c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r51c7, tag=("r51c7"))

                    r51c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r51c8, tag=("r51c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt51 = date.today()
                    firsty_gt51= today_gt51.replace(day=1)
                    last_monthy_gt51 = firsty_gt51 -relativedelta(months=5)
                    
                    end_todayy_gt51 = last_monthy_gt51
                    end_firsty_gt51 = end_todayy_gt51.replace(day=1)
                    end_monthy_gt51 = end_firsty_gt51 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt51='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Taxes-Property" and acctype="Expenses"'
                    sqly_gt51_val=(last_monthy_gt51,end_monthy_gt51,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt51,sqly_gt51_val)
                    mnty_gt51=fbcursor.fetchone()
                    


                    today551 = date.today()
                    first551 = today551.replace(day=1)
                    last_month551 = first551 -relativedelta(months=4)
                    
                    end_today551 = last_month551
                    end_first551 = end_today551.replace(day=1)
                    end_month551 = end_first551 -relativedelta(days=1)+relativedelta(months=1)

                    sql551='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Taxes-Property" and acctype="Expenses"'
                    sql551_val=(last_month551,end_month551,dtl_cmp_pro[0],)
                    fbcursor.execute(sql551,sql551_val)
                    mnt551=fbcursor.fetchone()

                    today514 = date.today()
                    first514 = today514.replace(day=1)
                    last_month514 = first514 -relativedelta(months=3)
                    
                    end_today514 = last_month514
                    end_first514 = end_today514.replace(day=1)
                    end_month514 = end_first514 -relativedelta(days=1)+relativedelta(months=1)

                    sql514='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Taxes-Property" and acctype="Expenses"'
                    sql514_val=(last_month514,end_month514,dtl_cmp_pro[0],)
                    fbcursor.execute(sql514,sql514_val)
                    mnt514=fbcursor.fetchone()

                    today351 = date.today()
                    first351 = today351.replace(day=1)
                    last_month351 = first351 -relativedelta(months=2)
                    
                    end_today351 = last_month351
                    end_first351 = end_today351.replace(day=1)
                    end_month351 = end_first351 -relativedelta(days=1)+relativedelta(months=1)

                    sql351='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Taxes-Property" and acctype="Expenses"'
                    sql351_val=(last_month351,end_month351,dtl_cmp_pro[0],)
                    fbcursor.execute(sql351,sql351_val)
                    mnt351=fbcursor.fetchone()

                    today251 = date.today()
                    first251 = today251.replace(day=1)
                    last_month251 = first251 -relativedelta(months=1)
                    
                    end_today251 = last_month251
                    end_first251 = end_today251.replace(day=1)
                    end_month251 = end_first251 -relativedelta(days=1)+relativedelta(months=1)

                    sql251='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Taxes-Property" and acctype="Expenses"'
                    sql251_val=(last_month251,end_month251,dtl_cmp_pro[0],)
                    fbcursor.execute(sql251,sql251_val)
                    mnt251=fbcursor.fetchone()

                    today511 = date.today()
                    first511 = today511.replace(day=1)
              

                    end_today511 = date.today()
                    end_first511 = end_today511.replace(day=1)
                    end_month511 = end_first511 -relativedelta(days=1)+relativedelta(months=1)

                    sql511='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Taxes-Property" and acctype="Expenses"'
                    sql511_val=(first511,end_month511,dtl_cmp_pro[0],)
                    fbcursor.execute(sql511,sql511_val)
                    mnt511=fbcursor.fetchone()

                    sqltt51='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Taxes-Property" and acctype="Expenses"'
                    sqltt_val51=(last_monthy_gt51,end_month511,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt51,sqltt_val51)
                    mnttt51=fbcursor.fetchone()
                    
                    if mnty_gt51[0] is None:
                        val651="0.0"
                    else:
                        val651=mnty_gt51[0] 
                    r51c2.delete(0,END)
                    r51c2.insert(0,"$"+str(val651))
                    r51c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt551[0] is None:
                        val551="0.0"
                    else:
                        val551=mnt551[0] 
                    r51c3.delete(0,END)
                    r51c3.insert(0,"$"+str(val551))
                    r51c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt514[0] is None:
                        val514="0.0"
                    else:
                        val514=mnt514[0] 
                    r51c4.delete(0,END)
                    r51c4.insert(0,"$"+str(val514))
                    r51c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt351[0] is None:
                        val351="0.0"
                    else:
                        val351=mnt351[0] 
                    r51c5.delete(0,END)
                    r51c5.insert(0,"$"+str(val351))
                    r51c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt251[0] is None:
                        val251="0.0"
                    else:
                        val251=mnt251[0] 
                    r51c6.delete(0,END)
                    r51c6.insert(0,"$"+str(val251))
                    r51c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt511[0] is None:
                        val511="0.0"
                    else:
                        val511=mnt511[0] 
                    r51c7.delete(0,END)
                    r51c7.insert(0,"$"+str(val511))
                    r51c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt51[0] is None:
                        valtt51="0.0"
                    else:
                        valtt51=mnttt51[0] 
                    r51c8.delete(0,END)
                    r51c8.insert(0,"$"+str(valtt51))
                    r51c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")


                    #----------------------------------------------------------52 th row
                    lv_name=Label(frm_analiz, text="Telephone Expense",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r52c1"))

                    r52c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r52c2, tag=("r52c2"))

                    r52c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r52c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r52c3, tag=("r52c3"))

                    r52c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r52c4, tag=("r52c4"))


                    r52c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r52c5, tag=("r52c5"))

                    r52c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r52c6, tag=("r52c6"))


                    r52c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r52c7, tag=("r52c7"))

                    r52c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r52c8, tag=("r52c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt52 = date.today()
                    firsty_gt52= today_gt52.replace(day=1)
                    last_monthy_gt52 = firsty_gt52 -relativedelta(months=5)
                    
                    end_todayy_gt52 = last_monthy_gt52
                    end_firsty_gt52 = end_todayy_gt52.replace(day=1)
                    end_monthy_gt52 = end_firsty_gt52 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt52='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Telephone Expense" and acctype="Expenses"'
                    sqly_gt52_val=(last_monthy_gt52,end_monthy_gt52,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt52,sqly_gt52_val)
                    mnty_gt52=fbcursor.fetchone()
                    


                    today552 = date.today()
                    first552 = today552.replace(day=1)
                    last_month552 = first552 -relativedelta(months=4)
                    
                    end_today552 = last_month552
                    end_first552 = end_today552.replace(day=1)
                    end_month552 = end_first552 -relativedelta(days=1)+relativedelta(months=1)

                    sql552='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Telephone Expense" and acctype="Expenses"'
                    sql552_val=(last_month552,end_month552,dtl_cmp_pro[0],)
                    fbcursor.execute(sql552,sql552_val)
                    mnt552=fbcursor.fetchone()

                    today524 = date.today()
                    first524 = today524.replace(day=1)
                    last_month524 = first524 -relativedelta(months=3)
                    
                    end_today524 = last_month524
                    end_first524 = end_today524.replace(day=1)
                    end_month524 = end_first524 -relativedelta(days=1)+relativedelta(months=1)

                    sql524='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Telephone Expense" and acctype="Expenses"'
                    sql524_val=(last_month524,end_month524,dtl_cmp_pro[0],)
                    fbcursor.execute(sql524,sql524_val)
                    mnt524=fbcursor.fetchone()

                    today352 = date.today()
                    first352 = today352.replace(day=1)
                    last_month352 = first352 -relativedelta(months=2)
                    
                    end_today352 = last_month352
                    end_first352 = end_today352.replace(day=1)
                    end_month352 = end_first352 -relativedelta(days=1)+relativedelta(months=1)

                    sql352='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Telephone Expense" and acctype="Expenses"'
                    sql352_val=(last_month352,end_month352,dtl_cmp_pro[0],)
                    fbcursor.execute(sql352,sql352_val)
                    mnt352=fbcursor.fetchone()

                    today252 = date.today()
                    first252 = today252.replace(day=1)
                    last_month252 = first252 -relativedelta(months=1)
                    
                    end_today252 = last_month252
                    end_first252 = end_today252.replace(day=1)
                    end_month252 = end_first252 -relativedelta(days=1)+relativedelta(months=1)

                    sql252='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Telephone Expense" and acctype="Expenses"'
                    sql252_val=(last_month252,end_month252,dtl_cmp_pro[0],)
                    fbcursor.execute(sql252,sql252_val)
                    mnt252=fbcursor.fetchone()

                    today521 = date.today()
                    first521 = today521.replace(day=1)
              

                    end_today521 = date.today()
                    end_first521 = end_today521.replace(day=1)
                    end_month521 = end_first521 -relativedelta(days=1)+relativedelta(months=1)

                    sql521='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Telephone Expense" and acctype="Expenses"'
                    sql521_val=(first521,end_month521,dtl_cmp_pro[0],)
                    fbcursor.execute(sql521,sql521_val)
                    mnt521=fbcursor.fetchone()

                    sqltt52='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Telephone Expense" and acctype="Expenses"'
                    sqltt_val52=(last_monthy_gt52,end_month521,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt52,sqltt_val52)
                    mnttt52=fbcursor.fetchone()
                    
                    if mnty_gt52[0] is None:
                        val652="0.0"
                    else:
                        val652=mnty_gt52[0] 
                    r52c2.delete(0,END)
                    r52c2.insert(0,"$"+str(val652))
                    r52c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt552[0] is None:
                        val552="0.0"
                    else:
                        val552=mnt552[0] 
                    r52c3.delete(0,END)
                    r52c3.insert(0,"$"+str(val552))
                    r52c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt524[0] is None:
                        val524="0.0"
                    else:
                        val524=mnt524[0] 
                    r52c4.delete(0,END)
                    r52c4.insert(0,"$"+str(val524))
                    r52c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt352[0] is None:
                        val352="0.0"
                    else:
                        val352=mnt352[0] 
                    r52c5.delete(0,END)
                    r52c5.insert(0,"$"+str(val352))
                    r52c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt252[0] is None:
                        val252="0.0"
                    else:
                        val252=mnt252[0] 
                    r52c6.delete(0,END)
                    r52c6.insert(0,"$"+str(val252))
                    r52c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt521[0] is None:
                        val521="0.0"
                    else:
                        val521=mnt521[0] 
                    r52c7.delete(0,END)
                    r52c7.insert(0,"$"+str(val521))
                    r52c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt52[0] is None:
                        valtt52="0.0"
                    else:
                        valtt52=mnttt52[0] 
                    r52c8.delete(0,END)
                    r52c8.insert(0,"$"+str(valtt52))
                    r52c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")


                    #----------------------------------------------------------53 th row
                    lv_name=Label(frm_analiz, text="Travel Expense",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r53c1"))

                    r53c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r53c2, tag=("r53c2"))

                    r53c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r53c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r53c3, tag=("r53c3"))

                    r53c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r53c4, tag=("r53c4"))


                    r53c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r53c5, tag=("r53c5"))

                    r53c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r53c6, tag=("r53c6"))


                    r53c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r53c7, tag=("r53c7"))

                    r53c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r53c8, tag=("r53c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt53 = date.today()
                    firsty_gt53= today_gt53.replace(day=1)
                    last_monthy_gt53 = firsty_gt53 -relativedelta(months=5)
                    
                    end_todayy_gt53 = last_monthy_gt53
                    end_firsty_gt53 = end_todayy_gt53.replace(day=1)
                    end_monthy_gt53 = end_firsty_gt53 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt53='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Travel Expense" and acctype="Expenses"'
                    sqly_gt53_val=(last_monthy_gt53,end_monthy_gt53,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt53,sqly_gt53_val)
                    mnty_gt53=fbcursor.fetchone()
                    


                    today553 = date.today()
                    first553 = today553.replace(day=1)
                    last_month553 = first553 -relativedelta(months=4)
                    
                    end_today553 = last_month553
                    end_first553 = end_today553.replace(day=1)
                    end_month553 = end_first553 -relativedelta(days=1)+relativedelta(months=1)

                    sql553='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Travel Expense" and acctype="Expenses"'
                    sql553_val=(last_month553,end_month553,dtl_cmp_pro[0],)
                    fbcursor.execute(sql553,sql553_val)
                    mnt553=fbcursor.fetchone()

                    today534 = date.today()
                    first534 = today534.replace(day=1)
                    last_month534 = first534 -relativedelta(months=3)
                    
                    end_today534 = last_month534
                    end_first534 = end_today534.replace(day=1)
                    end_month534 = end_first534 -relativedelta(days=1)+relativedelta(months=1)

                    sql534='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Travel Expense" and acctype="Expenses"'
                    sql534_val=(last_month534,end_month534,dtl_cmp_pro[0],)
                    fbcursor.execute(sql534,sql534_val)
                    mnt534=fbcursor.fetchone()

                    today353 = date.today()
                    first353 = today353.replace(day=1)
                    last_month353 = first353 -relativedelta(months=2)
                    
                    end_today353 = last_month353
                    end_first353 = end_today353.replace(day=1)
                    end_month353 = end_first353 -relativedelta(days=1)+relativedelta(months=1)

                    sql353='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Travel Expense" and acctype="Expenses"'
                    sql353_val=(last_month353,end_month353,dtl_cmp_pro[0],)
                    fbcursor.execute(sql353,sql353_val)
                    mnt353=fbcursor.fetchone()

                    today253 = date.today()
                    first253 = today253.replace(day=1)
                    last_month253 = first253 -relativedelta(months=1)
                    
                    end_today253 = last_month253
                    end_first253 = end_today253.replace(day=1)
                    end_month253 = end_first253 -relativedelta(days=1)+relativedelta(months=1)

                    sql253='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Travel Expense" and acctype="Expenses"'
                    sql253_val=(last_month253,end_month253,dtl_cmp_pro[0],)
                    fbcursor.execute(sql253,sql253_val)
                    mnt253=fbcursor.fetchone()

                    today531 = date.today()
                    first531 = today531.replace(day=1)
              

                    end_today531 = date.today()
                    end_first531 = end_today531.replace(day=1)
                    end_month531 = end_first531 -relativedelta(days=1)+relativedelta(months=1)

                    sql531='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Travel Expense" and acctype="Expenses"'
                    sql531_val=(first531,end_month531,dtl_cmp_pro[0],)
                    fbcursor.execute(sql531,sql531_val)
                    mnt531=fbcursor.fetchone()

                    sqltt53='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Travel Expense" and acctype="Expenses"'
                    sqltt_val53=(last_monthy_gt53,end_month531,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt53,sqltt_val53)
                    mnttt53=fbcursor.fetchone()
                    
                    if mnty_gt53[0] is None:
                        val653="0.0"
                    else:
                        val653=mnty_gt53[0] 
                    r53c2.delete(0,END)
                    r53c2.insert(0,"$"+str(val653))
                    r53c2.config(state=DISABLED,disabledbackground="#213b53",disabledforeground="white")  

                    if mnt553[0] is None:
                        val553="0.0"
                    else:
                        val553=mnt553[0] 
                    r53c3.delete(0,END)
                    r53c3.insert(0,"$"+str(val553))
                    r53c3.config(state=DISABLED,disabledbackground="#213b53",disabledforeground="white")  

                    if mnt534[0] is None:
                        val534="0.0"
                    else:
                        val534=mnt534[0] 
                    r53c4.delete(0,END)
                    r53c4.insert(0,"$"+str(val534))
                    r53c4.config(state=DISABLED,disabledbackground="#213b53",disabledforeground="white")  

                    if mnt353[0] is None:
                        val353="0.0"
                    else:
                        val353=mnt353[0] 
                    r53c5.delete(0,END)
                    r53c5.insert(0,"$"+str(val353))
                    r53c5.config(state=DISABLED,disabledbackground="#213b53",disabledforeground="white") 

                    if mnt253[0] is None:
                        val253="0.0"
                    else:
                        val253=mnt253[0] 
                    r53c6.delete(0,END)
                    r53c6.insert(0,"$"+str(val253))
                    r53c6.config(state=DISABLED,disabledbackground="#213b53",disabledforeground="white")

                    if mnt531[0] is None:
                        val531="0.0"
                    else:
                        val531=mnt531[0] 
                    r53c7.delete(0,END)
                    r53c7.insert(0,"$"+str(val531))
                    r53c7.config(state=DISABLED,disabledbackground="#213b53",disabledforeground="white") 

                    if mnttt53[0] is None:
                        valtt53="0.0"
                    else:
                        valtt53=mnttt53[0] 
                    r53c8.delete(0,END)
                    r53c8.insert(0,"$"+str(valtt53))
                    r53c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")


                    #----------------------------------------------------------54 th row
                    lv_name=Label(frm_analiz, text="Uncategorised Expense",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r54c1"))

                    r54c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r54c2, tag=("r54c2"))

                    r54c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r54c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r54c3, tag=("r54c3"))

                    r54c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r54c4, tag=("r54c4"))


                    r54c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r54c5, tag=("r54c5"))

                    r54c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r54c6, tag=("r54c6"))


                    r54c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r54c7, tag=("r54c7"))

                    r54c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r54c8, tag=("r54c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt54 = date.today()
                    firsty_gt54= today_gt54.replace(day=1)
                    last_monthy_gt54 = firsty_gt54 -relativedelta(months=5)
                    
                    end_todayy_gt54 = last_monthy_gt54
                    end_firsty_gt54 = end_todayy_gt54.replace(day=1)
                    end_monthy_gt54 = end_firsty_gt54 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt54='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Uncategorised Expense" and acctype="Expenses"'
                    sqly_gt54_val=(last_monthy_gt54,end_monthy_gt54,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt54,sqly_gt54_val)
                    mnty_gt54=fbcursor.fetchone()
                    


                    today554 = date.today()
                    first554 = today554.replace(day=1)
                    last_month554 = first554 -relativedelta(months=4)
                    
                    end_today554 = last_month554
                    end_first554 = end_today554.replace(day=1)
                    end_month554 = end_first554 -relativedelta(days=1)+relativedelta(months=1)

                    sql554='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Uncategorised Expense" and acctype="Expenses"'
                    sql554_val=(last_month554,end_month554,dtl_cmp_pro[0],)
                    fbcursor.execute(sql554,sql554_val)
                    mnt554=fbcursor.fetchone()

                    today544 = date.today()
                    first544 = today544.replace(day=1)
                    last_month544 = first544 -relativedelta(months=3)
                    
                    end_today544 = last_month544
                    end_first544 = end_today544.replace(day=1)
                    end_month544 = end_first544 -relativedelta(days=1)+relativedelta(months=1)

                    sql544='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Uncategorised Expense" and acctype="Expenses"'
                    sql544_val=(last_month544,end_month544,dtl_cmp_pro[0],)
                    fbcursor.execute(sql544,sql544_val)
                    mnt544=fbcursor.fetchone()

                    today354 = date.today()
                    first354 = today354.replace(day=1)
                    last_month354 = first354 -relativedelta(months=2)
                    
                    end_today354 = last_month354
                    end_first354 = end_today354.replace(day=1)
                    end_month354 = end_first354 -relativedelta(days=1)+relativedelta(months=1)

                    sql354='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Uncategorised Expense" and acctype="Expenses"'
                    sql354_val=(last_month354,end_month354,dtl_cmp_pro[0],)
                    fbcursor.execute(sql354,sql354_val)
                    mnt354=fbcursor.fetchone()

                    today254 = date.today()
                    first254 = today254.replace(day=1)
                    last_month254 = first254 -relativedelta(months=1)
                    
                    end_today254 = last_month254
                    end_first254 = end_today254.replace(day=1)
                    end_month254 = end_first254 -relativedelta(days=1)+relativedelta(months=1)

                    sql254='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Uncategorised Expense" and acctype="Expenses"'
                    sql254_val=(last_month254,end_month254,dtl_cmp_pro[0],)
                    fbcursor.execute(sql254,sql254_val)
                    mnt254=fbcursor.fetchone()

                    today541 = date.today()
                    first541 = today541.replace(day=1)
              

                    end_today541 = date.today()
                    end_first541 = end_today541.replace(day=1)
                    end_month541 = end_first541 -relativedelta(days=1)+relativedelta(months=1)

                    sql541='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Uncategorised Expense" and acctype="Expenses"'
                    sql541_val=(first541,end_month541,dtl_cmp_pro[0],)
                    fbcursor.execute(sql541,sql541_val)
                    mnt541=fbcursor.fetchone()

                    sqltt54='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Uncategorised Expense" and acctype="Expenses"'
                    sqltt_val54=(last_monthy_gt54,end_month541,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt54,sqltt_val54)
                    mnttt54=fbcursor.fetchone()
                    
                    if mnty_gt54[0] is None:
                        val654="0.0"
                    else:
                        val654=mnty_gt54[0] 
                    r54c2.delete(0,END)
                    r54c2.insert(0,"$"+str(val654))
                    r54c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt554[0] is None:
                        val554="0.0"
                    else:
                        val554=mnt554[0] 
                    r54c3.delete(0,END)
                    r54c3.insert(0,"$"+str(val554))
                    r54c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt544[0] is None:
                        val544="0.0"
                    else:
                        val544=mnt544[0] 
                    r54c4.delete(0,END)
                    r54c4.insert(0,"$"+str(val544))
                    r54c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt354[0] is None:
                        val354="0.0"
                    else:
                        val354=mnt354[0] 
                    r54c5.delete(0,END)
                    r54c5.insert(0,"$"+str(val354))
                    r54c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt254[0] is None:
                        val254="0.0"
                    else:
                        val254=mnt254[0] 
                    r54c6.delete(0,END)
                    r54c6.insert(0,"$"+str(val254))
                    r54c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt541[0] is None:
                        val541="0.0"
                    else:
                        val541=mnt541[0] 
                    r54c7.delete(0,END)
                    r54c7.insert(0,"$"+str(val541))
                    r54c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt54[0] is None:
                        valtt54="0.0"
                    else:
                        valtt54=mnttt54[0] 
                    r54c8.delete(0,END)
                    r54c8.insert(0,"$"+str(valtt54))
                    r54c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")


                    #----------------------------------------------------------55 th row
                    lv_name=Label(frm_analiz, text="Utilities",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r55c1"))

                    r55c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r55c2, tag=("r55c2"))

                    r55c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r55c3, tag=("r55c3"))

                    r55c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r55c4, tag=("r55c4"))


                    r55c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r55c5, tag=("r55c5"))

                    r55c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r55c6, tag=("r55c6"))


                    r55c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r55c7, tag=("r55c7"))

                    r55c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r55c8, tag=("r55c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt55 = date.today()
                    firsty_gt55= today_gt55.replace(day=1)
                    last_monthy_gt55 = firsty_gt55 -relativedelta(months=5)
                    
                    end_todayy_gt55 = last_monthy_gt55
                    end_firsty_gt55 = end_todayy_gt55.replace(day=1)
                    end_monthy_gt55 = end_firsty_gt55 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt55='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Utilities" and acctype="Expenses"'
                    sqly_gt55_val=(last_monthy_gt55,end_monthy_gt55,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt55,sqly_gt55_val)
                    mnty_gt55=fbcursor.fetchone()
                    


                    today555 = date.today()
                    first555 = today555.replace(day=1)
                    last_month555 = first555 -relativedelta(months=4)
                    
                    end_today555 = last_month555
                    end_first555 = end_today555.replace(day=1)
                    end_month555 = end_first555 -relativedelta(days=1)+relativedelta(months=1)

                    sql555='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Utilities" and acctype="Expenses"'
                    sql555_val=(last_month555,end_month555,dtl_cmp_pro[0],)
                    fbcursor.execute(sql555,sql555_val)
                    mnt555=fbcursor.fetchone()

                    today554 = date.today()
                    first554 = today554.replace(day=1)
                    last_month554 = first554 -relativedelta(months=3)
                    
                    end_today554 = last_month554
                    end_first554 = end_today554.replace(day=1)
                    end_month554 = end_first554 -relativedelta(days=1)+relativedelta(months=1)

                    sql554='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Utilities" and acctype="Expenses"'
                    sql554_val=(last_month554,end_month554,dtl_cmp_pro[0],)
                    fbcursor.execute(sql554,sql554_val)
                    mnt554=fbcursor.fetchone()

                    today355 = date.today()
                    first355 = today355.replace(day=1)
                    last_month355 = first355 -relativedelta(months=2)
                    
                    end_today355 = last_month355
                    end_first355 = end_today355.replace(day=1)
                    end_month355 = end_first355 -relativedelta(days=1)+relativedelta(months=1)

                    sql355='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Utilities" and acctype="Expenses"'
                    sql355_val=(last_month355,end_month355,dtl_cmp_pro[0],)
                    fbcursor.execute(sql355,sql355_val)
                    mnt355=fbcursor.fetchone()

                    today255 = date.today()
                    first255 = today255.replace(day=1)
                    last_month255 = first255 -relativedelta(months=1)
                    
                    end_today255 = last_month255
                    end_first255 = end_today255.replace(day=1)
                    end_month255 = end_first255 -relativedelta(days=1)+relativedelta(months=1)

                    sql255='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Utilities" and acctype="Expenses"'
                    sql255_val=(last_month255,end_month255,dtl_cmp_pro[0],)
                    fbcursor.execute(sql255,sql255_val)
                    mnt255=fbcursor.fetchone()

                    today551 = date.today()
                    first551 = today551.replace(day=1)
              

                    end_today551 = date.today()
                    end_first551 = end_today551.replace(day=1)
                    end_month551 = end_first551 -relativedelta(days=1)+relativedelta(months=1)

                    sql551='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Utilities" and acctype="Expenses"'
                    sql551_val=(first551,end_month551,dtl_cmp_pro[0],)
                    fbcursor.execute(sql551,sql551_val)
                    mnt551=fbcursor.fetchone()

                    sqltt55='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Utilities" and acctype="Expenses"'
                    sqltt_val55=(last_monthy_gt55,end_month551,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt55,sqltt_val55)
                    mnttt55=fbcursor.fetchone()
                    
                    if mnty_gt55[0] is None:
                        val655="0.0"
                    else:
                        val655=mnty_gt55[0] 
                    r55c2.delete(0,END)
                    r55c2.insert(0,"$"+str(val655))
                    r55c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt555[0] is None:
                        val555="0.0"
                    else:
                        val555=mnt555[0] 
                    r55c3.delete(0,END)
                    r55c3.insert(0,"$"+str(val555))
                    r55c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt554[0] is None:
                        val554="0.0"
                    else:
                        val554=mnt554[0] 
                    r55c4.delete(0,END)
                    r55c4.insert(0,"$"+str(val554))
                    r55c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt355[0] is None:
                        val355="0.0"
                    else:
                        val355=mnt355[0] 
                    r55c5.delete(0,END)
                    r55c5.insert(0,"$"+str(val355))
                    r55c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt255[0] is None:
                        val255="0.0"
                    else:
                        val255=mnt255[0] 
                    r55c6.delete(0,END)
                    r55c6.insert(0,"$"+str(val255))
                    r55c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt551[0] is None:
                        val551="0.0"
                    else:
                        val551=mnt551[0] 
                    r55c7.delete(0,END)
                    r55c7.insert(0,"$"+str(val551))
                    r55c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt55[0] is None:
                        valtt55="0.0"
                    else:
                        valtt55=mnttt55[0] 
                    r55c8.delete(0,END)
                    r55c8.insert(0,"$"+str(valtt55))
                    r55c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------56 th row
                    lv_name=Label(frm_analiz, text="Other:",bg="#506579", width=159, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r56c1"))

                    
                    

                    #----------------------------------------------------------57 th row
                    lv_name=Label(frm_analiz, text="Ask My Accountant",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r57c1"))

                    r57c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r57c2, tag=("r57c2"))

                    r57c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r57c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r57c3, tag=("r57c3"))

                    r57c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r57c4, tag=("r57c4"))


                    r57c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r57c5, tag=("r57c5"))

                    r57c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r57c6, tag=("r57c6"))


                    r57c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r57c7, tag=("r57c7"))

                    r57c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r57c8, tag=("r57c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt57 = date.today()
                    firsty_gt57= today_gt57.replace(day=1)
                    last_monthy_gt57 = firsty_gt57 -relativedelta(months=5)
                    
                    end_todayy_gt57 = last_monthy_gt57
                    end_firsty_gt57 = end_todayy_gt57.replace(day=1)
                    end_monthy_gt57 = end_firsty_gt57 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt57='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Ask My Accountant" and acctype="Other Expenses"'
                    sqly_gt57_val=(last_monthy_gt57,end_monthy_gt57,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt57,sqly_gt57_val)
                    mnty_gt57=fbcursor.fetchone()
                    


                    today575 = date.today()
                    first575 = today575.replace(day=1)
                    last_month575 = first575 -relativedelta(months=4)
                    
                    end_today575 = last_month575
                    end_first575 = end_today575.replace(day=1)
                    end_month575 = end_first575 -relativedelta(days=1)+relativedelta(months=1)

                    sql575='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Ask My Accountant" and acctype="Other Expenses"'
                    sql575_val=(last_month575,end_month575,dtl_cmp_pro[0],)
                    fbcursor.execute(sql575,sql575_val)
                    mnt575=fbcursor.fetchone()

                    today574 = date.today()
                    first574 = today574.replace(day=1)
                    last_month574 = first574 -relativedelta(months=3)
                    
                    end_today574 = last_month574
                    end_first574 = end_today574.replace(day=1)
                    end_month574 = end_first574 -relativedelta(days=1)+relativedelta(months=1)

                    sql574='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Ask My Accountant" and acctype="Other Expenses"'
                    sql574_val=(last_month574,end_month574,dtl_cmp_pro[0],)
                    fbcursor.execute(sql574,sql574_val)
                    mnt574=fbcursor.fetchone()

                    today357 = date.today()
                    first357 = today357.replace(day=1)
                    last_month357 = first357 -relativedelta(months=2)
                    
                    end_today357 = last_month357
                    end_first357 = end_today357.replace(day=1)
                    end_month357 = end_first357 -relativedelta(days=1)+relativedelta(months=1)

                    sql357='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Ask My Accountant" and acctype="Other Expenses"'
                    sql357_val=(last_month357,end_month357,dtl_cmp_pro[0],)
                    fbcursor.execute(sql357,sql357_val)
                    mnt357=fbcursor.fetchone()

                    today257 = date.today()
                    first257 = today257.replace(day=1)
                    last_month257 = first257 -relativedelta(months=1)
                    
                    end_today257 = last_month257
                    end_first257 = end_today257.replace(day=1)
                    end_month257 = end_first257 -relativedelta(days=1)+relativedelta(months=1)

                    sql257='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Ask My Accountant" and acctype="Other Expenses"'
                    sql257_val=(last_month257,end_month257,dtl_cmp_pro[0],)
                    fbcursor.execute(sql257,sql257_val)
                    mnt257=fbcursor.fetchone()

                    today571 = date.today()
                    first571 = today571.replace(day=1)
              

                    end_today571 = date.today()
                    end_first571 = end_today571.replace(day=1)
                    end_month571 = end_first571 -relativedelta(days=1)+relativedelta(months=1)

                    sql571='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Ask My Accountant" and acctype="Other Expenses"'
                    sql571_val=(first571,end_month571,dtl_cmp_pro[0],)
                    fbcursor.execute(sql571,sql571_val)
                    mnt571=fbcursor.fetchone()

                    sqltt57='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Ask My Accountant" and acctype="Other Expenses"'
                    sqltt_val57=(last_monthy_gt57,end_month571,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt57,sqltt_val57)
                    mnttt57=fbcursor.fetchone()
                    
                    if mnty_gt57[0] is None:
                        val657="0.0"
                    else:
                        val657=mnty_gt57[0] 
                    r57c2.delete(0,END)
                    r57c2.insert(0,"$"+str(val657))
                    r57c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt575[0] is None:
                        val575="0.0"
                    else:
                        val575=mnt575[0] 
                    r57c3.delete(0,END)
                    r57c3.insert(0,"$"+str(val575))
                    r57c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt574[0] is None:
                        val574="0.0"
                    else:
                        val574=mnt574[0] 
                    r57c4.delete(0,END)
                    r57c4.insert(0,"$"+str(val574))
                    r57c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt357[0] is None:
                        val357="0.0"
                    else:
                        val357=mnt357[0] 
                    r57c5.delete(0,END)
                    r57c5.insert(0,"$"+str(val357))
                    r57c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt257[0] is None:
                        val257="0.0"
                    else:
                        val257=mnt257[0] 
                    r57c6.delete(0,END)
                    r57c6.insert(0,"$"+str(val257))
                    r57c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt571[0] is None:
                        val571="0.0"
                    else:
                        val571=mnt571[0] 
                    r57c7.delete(0,END)
                    r57c7.insert(0,"$"+str(val571))
                    r57c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt57[0] is None:
                        valtt57="0.0"
                    else:
                        valtt57=mnttt57[0] 
                    r57c8.delete(0,END)
                    r57c8.insert(0,"$"+str(valtt57))
                    r57c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")


                    #----------------------------------------------------------58 th row
                    lv_name=Label(frm_analiz, text="CGST Write-Off",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r58c1"))

                    r58c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r58c2, tag=("r58c2"))

                    r58c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r58c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r58c3, tag=("r58c3"))

                    r58c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r58c4, tag=("r58c4"))


                    r58c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r58c5, tag=("r58c5"))

                    r58c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r58c6, tag=("r58c6"))


                    r58c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r58c7, tag=("r58c7"))

                    r58c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r58c8, tag=("r58c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt58 = date.today()
                    firsty_gt58= today_gt58.replace(day=1)
                    last_monthy_gt58 = firsty_gt58 -relativedelta(months=5)
                    
                    end_todayy_gt58 = last_monthy_gt58
                    end_firsty_gt58 = end_todayy_gt58.replace(day=1)
                    end_monthy_gt58 = end_firsty_gt58 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt58='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="CGST Write-Off" and acctype="Other Expenses"'
                    sqly_gt58_val=(last_monthy_gt58,end_monthy_gt58,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt58,sqly_gt58_val)
                    mnty_gt58=fbcursor.fetchone()
                    


                    today585 = date.today()
                    first585 = today585.replace(day=1)
                    last_month585 = first585 -relativedelta(months=4)
                    
                    end_today585 = last_month585
                    end_first585 = end_today585.replace(day=1)
                    end_month585 = end_first585 -relativedelta(days=1)+relativedelta(months=1)

                    sql585='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="CGST Write-Off" and acctype="Other Expenses"'
                    sql585_val=(last_month585,end_month585,dtl_cmp_pro[0],)
                    fbcursor.execute(sql585,sql585_val)
                    mnt585=fbcursor.fetchone()

                    today584 = date.today()
                    first584 = today584.replace(day=1)
                    last_month584 = first584 -relativedelta(months=3)
                    
                    end_today584 = last_month584
                    end_first584 = end_today584.replace(day=1)
                    end_month584 = end_first584 -relativedelta(days=1)+relativedelta(months=1)

                    sql584='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="CGST Write-Off" and acctype="Other Expenses"'
                    sql584_val=(last_month584,end_month584,dtl_cmp_pro[0],)
                    fbcursor.execute(sql584,sql584_val)
                    mnt584=fbcursor.fetchone()

                    today358 = date.today()
                    first358 = today358.replace(day=1)
                    last_month358 = first358 -relativedelta(months=2)
                    
                    end_today358 = last_month358
                    end_first358 = end_today358.replace(day=1)
                    end_month358 = end_first358 -relativedelta(days=1)+relativedelta(months=1)

                    sql358='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="CGST Write-Off" and acctype="Other Expenses"'
                    sql358_val=(last_month358,end_month358,dtl_cmp_pro[0],)
                    fbcursor.execute(sql358,sql358_val)
                    mnt358=fbcursor.fetchone()

                    today258 = date.today()
                    first258 = today258.replace(day=1)
                    last_month258 = first258 -relativedelta(months=1)
                    
                    end_today258 = last_month258
                    end_first258 = end_today258.replace(day=1)
                    end_month258 = end_first258 -relativedelta(days=1)+relativedelta(months=1)

                    sql258='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="CGST Write-Off" and acctype="Other Expenses"'
                    sql258_val=(last_month258,end_month258,dtl_cmp_pro[0],)
                    fbcursor.execute(sql258,sql258_val)
                    mnt258=fbcursor.fetchone()

                    today581 = date.today()
                    first581 = today581.replace(day=1)
              

                    end_today581 = date.today()
                    end_first581 = end_today581.replace(day=1)
                    end_month581 = end_first581 -relativedelta(days=1)+relativedelta(months=1)

                    sql581='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="CGST Write-Off" and acctype="Other Expenses"'
                    sql581_val=(first581,end_month581,dtl_cmp_pro[0],)
                    fbcursor.execute(sql581,sql581_val)
                    mnt581=fbcursor.fetchone()

                    sqltt58='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="CGST Write-Off" and acctype="Other Expenses"'
                    sqltt_val58=(last_monthy_gt58,end_month581,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt58,sqltt_val58)
                    mnttt58=fbcursor.fetchone()
                    
                    if mnty_gt58[0] is None:
                        val658="0.0"
                    else:
                        val658=mnty_gt58[0] 
                    r58c2.delete(0,END)
                    r58c2.insert(0,"$"+str(val658))
                    r58c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt585[0] is None:
                        val585="0.0"
                    else:
                        val585=mnt585[0] 
                    r58c3.delete(0,END)
                    r58c3.insert(0,"$"+str(val585))
                    r58c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt584[0] is None:
                        val584="0.0"
                    else:
                        val584=mnt584[0] 
                    r58c4.delete(0,END)
                    r58c4.insert(0,"$"+str(val584))
                    r58c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt358[0] is None:
                        val358="0.0"
                    else:
                        val358=mnt358[0] 
                    r58c5.delete(0,END)
                    r58c5.insert(0,"$"+str(val358))
                    r58c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt258[0] is None:
                        val258="0.0"
                    else:
                        val258=mnt258[0] 
                    r58c6.delete(0,END)
                    r58c6.insert(0,"$"+str(val258))
                    r58c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt581[0] is None:
                        val581="0.0"
                    else:
                        val581=mnt581[0] 
                    r58c7.delete(0,END)
                    r58c7.insert(0,"$"+str(val581))
                    r58c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt58[0] is None:
                        valtt58="0.0"
                    else:
                        valtt58=mnttt58[0] 
                    r58c8.delete(0,END)
                    r58c8.insert(0,"$"+str(valtt58))
                    r58c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")


                    #----------------------------------------------------------59 th row
                    lv_name=Label(frm_analiz, text="GST Write-Off",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r59c1"))

                    r59c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r59c2, tag=("r59c2"))

                    r59c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r59c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r59c3, tag=("r59c3"))

                    r59c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r59c4, tag=("r59c4"))


                    r59c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r59c5, tag=("r59c5"))

                    r59c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r59c6, tag=("r59c6"))


                    r59c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r59c7, tag=("r59c7"))

                    r59c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r59c8, tag=("r59c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt59 = date.today()
                    firsty_gt59= today_gt59.replace(day=1)
                    last_monthy_gt59 = firsty_gt59 -relativedelta(months=5)
                    
                    end_todayy_gt59 = last_monthy_gt59
                    end_firsty_gt59 = end_todayy_gt59.replace(day=1)
                    end_monthy_gt59 = end_firsty_gt59 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt59='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="GST Write-Off" and acctype="Other Expenses"'
                    sqly_gt59_val=(last_monthy_gt59,end_monthy_gt59,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt59,sqly_gt59_val)
                    mnty_gt59=fbcursor.fetchone()
                    


                    today595 = date.today()
                    first595 = today595.replace(day=1)
                    last_month595 = first595 -relativedelta(months=4)
                    
                    end_today595 = last_month595
                    end_first595 = end_today595.replace(day=1)
                    end_month595 = end_first595 -relativedelta(days=1)+relativedelta(months=1)

                    sql595='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="GST Write-Off" and acctype="Other Expenses"'
                    sql595_val=(last_month595,end_month595,dtl_cmp_pro[0],)
                    fbcursor.execute(sql595,sql595_val)
                    mnt595=fbcursor.fetchone()

                    today594 = date.today()
                    first594 = today594.replace(day=1)
                    last_month594 = first594 -relativedelta(months=3)
                    
                    end_today594 = last_month594
                    end_first594 = end_today594.replace(day=1)
                    end_month594 = end_first594 -relativedelta(days=1)+relativedelta(months=1)

                    sql594='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="GST Write-Off" and acctype="Other Expenses"'
                    sql594_val=(last_month594,end_month594,dtl_cmp_pro[0],)
                    fbcursor.execute(sql594,sql594_val)
                    mnt594=fbcursor.fetchone()

                    today359 = date.today()
                    first359 = today359.replace(day=1)
                    last_month359 = first359 -relativedelta(months=2)
                    
                    end_today359 = last_month359
                    end_first359 = end_today359.replace(day=1)
                    end_month359 = end_first359 -relativedelta(days=1)+relativedelta(months=1)

                    sql359='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="GST Write-Off" and acctype="Other Expenses"'
                    sql359_val=(last_month359,end_month359,dtl_cmp_pro[0],)
                    fbcursor.execute(sql359,sql359_val)
                    mnt359=fbcursor.fetchone()

                    today259 = date.today()
                    first259 = today259.replace(day=1)
                    last_month259 = first259 -relativedelta(months=1)
                    
                    end_today259 = last_month259
                    end_first259 = end_today259.replace(day=1)
                    end_month259 = end_first259 -relativedelta(days=1)+relativedelta(months=1)

                    sql259='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="GST Write-Off" and acctype="Other Expenses"'
                    sql259_val=(last_month259,end_month259,dtl_cmp_pro[0],)
                    fbcursor.execute(sql259,sql259_val)
                    mnt259=fbcursor.fetchone()

                    today591 = date.today()
                    first591 = today591.replace(day=1)
              

                    end_today591 = date.today()
                    end_first591 = end_today591.replace(day=1)
                    end_month591 = end_first591 -relativedelta(days=1)+relativedelta(months=1)

                    sql591='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="GST Write-Off" and acctype="Other Expenses"'
                    sql591_val=(first591,end_month591,dtl_cmp_pro[0],)
                    fbcursor.execute(sql591,sql591_val)
                    mnt591=fbcursor.fetchone()

                    sqltt59='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="GST Write-Off" and acctype="Other Expenses"'
                    sqltt_val59=(last_monthy_gt59,end_month591,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt59,sqltt_val59)
                    mnttt59=fbcursor.fetchone()
                    
                    if mnty_gt59[0] is None:
                        val659="0.0"
                    else:
                        val659=mnty_gt59[0] 
                    r59c2.delete(0,END)
                    r59c2.insert(0,"$"+str(val659))
                    r59c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt595[0] is None:
                        val595="0.0"
                    else:
                        val595=mnt595[0] 
                    r59c3.delete(0,END)
                    r59c3.insert(0,"$"+str(val595))
                    r59c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt594[0] is None:
                        val594="0.0"
                    else:
                        val594=mnt594[0] 
                    r59c4.delete(0,END)
                    r59c4.insert(0,"$"+str(val594))
                    r59c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt359[0] is None:
                        val359="0.0"
                    else:
                        val359=mnt359[0] 
                    r59c5.delete(0,END)
                    r59c5.insert(0,"$"+str(val359))
                    r59c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt259[0] is None:
                        val259="0.0"
                    else:
                        val259=mnt259[0] 
                    r59c6.delete(0,END)
                    r59c6.insert(0,"$"+str(val259))
                    r59c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt591[0] is None:
                        val591="0.0"
                    else:
                        val591=mnt591[0] 
                    r59c7.delete(0,END)
                    r59c7.insert(0,"$"+str(val591))
                    r59c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt59[0] is None:
                        valtt59="0.0"
                    else:
                        valtt59=mnttt59[0] 
                    r59c8.delete(0,END)
                    r59c8.insert(0,"$"+str(valtt59))
                    r59c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------60 th row
                    lv_name=Label(frm_analiz, text="IGST Write-Off",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r60c1"))

                    r60c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r60c2, tag=("r60c2"))

                    r60c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r60c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r60c3, tag=("r60c3"))

                    r60c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r60c4, tag=("r60c4"))


                    r60c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r60c5, tag=("r60c5"))

                    r60c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r60c6, tag=("r60c6"))


                    r60c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r60c7, tag=("r60c7"))

                    r60c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r60c8, tag=("r60c8"))

                    #----------------------------------------------------------------------calcu
                    today_gt60 = date.today()
                    firsty_gt60= today_gt60.replace(day=1)
                    last_monthy_gt60 = firsty_gt60 -relativedelta(months=5)
                    
                    end_todayy_gt60 = last_monthy_gt60
                    end_firsty_gt60 = end_todayy_gt60.replace(day=1)
                    end_monthy_gt60 = end_firsty_gt60 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt60='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="IGST Write-Off" and acctype="Other Expenses"'
                    sqly_gt60_val=(last_monthy_gt60,end_monthy_gt60,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt60,sqly_gt60_val)
                    mnty_gt60=fbcursor.fetchone()
                    


                    today605 = date.today()
                    first605 = today605.replace(day=1)
                    last_month605 = first605 -relativedelta(months=4)
                    
                    end_today605 = last_month605
                    end_first605 = end_today605.replace(day=1)
                    end_month605 = end_first605 -relativedelta(days=1)+relativedelta(months=1)

                    sql605='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="IGST Write-Off" and acctype="Other Expenses"'
                    sql605_val=(last_month605,end_month605,dtl_cmp_pro[0],)
                    fbcursor.execute(sql605,sql605_val)
                    mnt605=fbcursor.fetchone()

                    today604 = date.today()
                    first604 = today604.replace(day=1)
                    last_month604 = first604 -relativedelta(months=3)
                    
                    end_today604 = last_month604
                    end_first604 = end_today604.replace(day=1)
                    end_month604 = end_first604 -relativedelta(days=1)+relativedelta(months=1)

                    sql604='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="IGST Write-Off" and acctype="Other Expenses"'
                    sql604_val=(last_month604,end_month604,dtl_cmp_pro[0],)
                    fbcursor.execute(sql604,sql604_val)
                    mnt604=fbcursor.fetchone()

                    today360 = date.today()
                    first360 = today360.replace(day=1)
                    last_month360 = first360 -relativedelta(months=2)
                    
                    end_today360 = last_month360
                    end_first360 = end_today360.replace(day=1)
                    end_month360 = end_first360 -relativedelta(days=1)+relativedelta(months=1)

                    sql360='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="IGST Write-Off" and acctype="Other Expenses"'
                    sql360_val=(last_month360,end_month360,dtl_cmp_pro[0],)
                    fbcursor.execute(sql360,sql360_val)
                    mnt360=fbcursor.fetchone()

                    today260 = date.today()
                    first260 = today260.replace(day=1)
                    last_month260 = first260 -relativedelta(months=1)
                    
                    end_today260 = last_month260
                    end_first260 = end_today260.replace(day=1)
                    end_month260 = end_first260 -relativedelta(days=1)+relativedelta(months=1)

                    sql260='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="IGST Write-Off" and acctype="Other Expenses"'
                    sql260_val=(last_month260,end_month260,dtl_cmp_pro[0],)
                    fbcursor.execute(sql260,sql260_val)
                    mnt260=fbcursor.fetchone()

                    today601 = date.today()
                    first601 = today601.replace(day=1)
              

                    end_today601 = date.today()
                    end_first601 = end_today601.replace(day=1)
                    end_month601 = end_first601 -relativedelta(days=1)+relativedelta(months=1)

                    sql601='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="IGST Write-Off" and acctype="Other Expenses"'
                    sql601_val=(first601,end_month601,dtl_cmp_pro[0],)
                    fbcursor.execute(sql601,sql601_val)
                    mnt601=fbcursor.fetchone()

                    sqltt60='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="IGST Write-Off" and acctype="Other Expenses"'
                    sqltt_val60=(last_monthy_gt60,end_month601,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt60,sqltt_val60)
                    mnttt60=fbcursor.fetchone()
                    
                    if mnty_gt60[0] is None:
                        val660="0.0"
                    else:
                        val660=mnty_gt60[0] 
                    r60c2.delete(0,END)
                    r60c2.insert(0,"$"+str(val660))
                    r60c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt605[0] is None:
                        val605="0.0"
                    else:
                        val605=mnt605[0] 
                    r60c3.delete(0,END)
                    r60c3.insert(0,"$"+str(val605))
                    r60c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt604[0] is None:
                        val604="0.0"
                    else:
                        val604=mnt604[0] 
                    r60c4.delete(0,END)
                    r60c4.insert(0,"$"+str(val604))
                    r60c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt360[0] is None:
                        val360="0.0"
                    else:
                        val360=mnt360[0] 
                    r60c5.delete(0,END)
                    r60c5.insert(0,"$"+str(val360))
                    r60c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt260[0] is None:
                        val260="0.0"
                    else:
                        val260=mnt260[0] 
                    r60c6.delete(0,END)
                    r60c6.insert(0,"$"+str(val260))
                    r60c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt601[0] is None:
                        val601="0.0"
                    else:
                        val601=mnt601[0] 
                    r60c7.delete(0,END)
                    r60c7.insert(0,"$"+str(val601))
                    r60c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt60[0] is None:
                        valtt60="0.0"
                    else:
                        valtt60=mnttt60[0] 
                    r60c8.delete(0,END)
                    r60c8.insert(0,"$"+str(valtt60))
                    r60c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------61 th row
                    lv_name=Label(frm_analiz, text="Miscellaneous Expense",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r61c1"))

                    r61c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r61c2, tag=("r61c2"))

                    r61c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r61c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r61c3, tag=("r61c3"))

                    r61c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r61c4, tag=("r61c4"))


                    r61c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r61c5, tag=("r61c5"))

                    r61c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r61c6, tag=("r61c6"))


                    r61c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r61c7, tag=("r61c7"))

                    r61c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r61c8, tag=("r61c8"))
                    #----------------------------------------------------------------------
                    today_gt61 = date.today()
                    firsty_gt61= today_gt61.replace(day=1)
                    last_monthy_gt61 = firsty_gt61 -relativedelta(months=5)
                    
                    end_todayy_gt61 = last_monthy_gt61
                    end_firsty_gt61 = end_todayy_gt61.replace(day=1)
                    end_monthy_gt61 = end_firsty_gt61 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt61='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Miscellaneous Expense" and acctype="Other Expenses"'
                    sqly_gt61_val=(last_monthy_gt61,end_monthy_gt61,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt61,sqly_gt61_val)
                    mnty_gt61=fbcursor.fetchone()
                    


                    today615 = date.today()
                    first615 = today615.replace(day=1)
                    last_month615 = first615 -relativedelta(months=4)
                    
                    end_today615 = last_month615
                    end_first615 = end_today615.replace(day=1)
                    end_month615 = end_first615 -relativedelta(days=1)+relativedelta(months=1)

                    sql615='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Miscellaneous Expense" and acctype="Other Expenses"'
                    sql615_val=(last_month615,end_month615,dtl_cmp_pro[0],)
                    fbcursor.execute(sql615,sql615_val)
                    mnt615=fbcursor.fetchone()

                    today614 = date.today()
                    first614 = today614.replace(day=1)
                    last_month614 = first614 -relativedelta(months=3)
                    
                    end_today614 = last_month614
                    end_first614 = end_today614.replace(day=1)
                    end_month614 = end_first614 -relativedelta(days=1)+relativedelta(months=1)

                    sql614='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Miscellaneous Expense" and acctype="Other Expenses"'
                    sql614_val=(last_month614,end_month614,dtl_cmp_pro[0],)
                    fbcursor.execute(sql614,sql614_val)
                    mnt614=fbcursor.fetchone()

                    today361 = date.today()
                    first361 = today361.replace(day=1)
                    last_month361 = first361 -relativedelta(months=2)
                    
                    end_today361 = last_month361
                    end_first361 = end_today361.replace(day=1)
                    end_month361 = end_first361 -relativedelta(days=1)+relativedelta(months=1)

                    sql361='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Miscellaneous Expense" and acctype="Other Expenses"'
                    sql361_val=(last_month361,end_month361,dtl_cmp_pro[0],)
                    fbcursor.execute(sql361,sql361_val)
                    mnt361=fbcursor.fetchone()

                    today261 = date.today()
                    first261 = today261.replace(day=1)
                    last_month261 = first261 -relativedelta(months=1)
                    
                    end_today261 = last_month261
                    end_first261 = end_today261.replace(day=1)
                    end_month261 = end_first261 -relativedelta(days=1)+relativedelta(months=1)

                    sql261='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Miscellaneous Expense" and acctype="Other Expenses"'
                    sql261_val=(last_month261,end_month261,dtl_cmp_pro[0],)
                    fbcursor.execute(sql261,sql261_val)
                    mnt261=fbcursor.fetchone()

                    today611 = date.today()
                    first611 = today611.replace(day=1)
              

                    end_today611 = date.today()
                    end_first611 = end_today611.replace(day=1)
                    end_month611 = end_first611 -relativedelta(days=1)+relativedelta(months=1)

                    sql611='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Miscellaneous Expense" and acctype="Other Expenses"'
                    sql611_val=(first611,end_month611,dtl_cmp_pro[0],)
                    fbcursor.execute(sql611,sql611_val)
                    mnt611=fbcursor.fetchone()

                    sqltt61='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Miscellaneous Expense" and acctype="Other Expenses"'
                    sqltt_val61=(last_monthy_gt61,end_month611,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt61,sqltt_val61)
                    mnttt61=fbcursor.fetchone()
                    
                    if mnty_gt61[0] is None:
                        val661="0.0"
                    else:
                        val661=mnty_gt61[0] 
                    r61c2.delete(0,END)
                    r61c2.insert(0,"$"+str(val661))
                    r61c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt615[0] is None:
                        val615="0.0"
                    else:
                        val615=mnt615[0] 
                    r61c3.delete(0,END)
                    r61c3.insert(0,"$"+str(val615))
                    r61c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt614[0] is None:
                        val614="0.0"
                    else:
                        val614=mnt614[0] 
                    r61c4.delete(0,END)
                    r61c4.insert(0,"$"+str(val614))
                    r61c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt361[0] is None:
                        val361="0.0"
                    else:
                        val361=mnt361[0] 
                    r61c5.delete(0,END)
                    r61c5.insert(0,"$"+str(val361))
                    r61c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt261[0] is None:
                        val261="0.0"
                    else:
                        val261=mnt261[0] 
                    r61c6.delete(0,END)
                    r61c6.insert(0,"$"+str(val261))
                    r61c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt611[0] is None:
                        val611="0.0"
                    else:
                        val611=mnt611[0] 
                    r61c7.delete(0,END)
                    r61c7.insert(0,"$"+str(val611))
                    r61c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt61[0] is None:
                        valtt61="0.0"
                    else:
                        valtt61=mnttt61[0] 
                    r61c8.delete(0,END)
                    r61c8.insert(0,"$"+str(valtt61))
                    r61c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------62 th row
                    lv_name=Label(frm_analiz, text="Political Contributions",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r62c1"))

                    r62c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r62c2, tag=("r62c2"))

                    r62c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r62c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r62c3, tag=("r62c3"))

                    r62c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r62c4, tag=("r62c4"))


                    r62c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r62c5, tag=("r62c5"))

                    r62c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r62c6, tag=("r62c6"))


                    r62c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r62c7, tag=("r62c7"))

                    r62c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r62c8, tag=("r62c8"))

                    #----------------------------------------------------------------------
                    today_gt62 = date.today()
                    firsty_gt62= today_gt62.replace(day=1)
                    last_monthy_gt62 = firsty_gt62 -relativedelta(months=5)
                    
                    end_todayy_gt62 = last_monthy_gt62
                    end_firsty_gt62 = end_todayy_gt62.replace(day=1)
                    end_monthy_gt62 = end_firsty_gt62 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt62='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Political Contributions" and acctype="Other Expenses"'
                    sqly_gt62_val=(last_monthy_gt62,end_monthy_gt62,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt62,sqly_gt62_val)
                    mnty_gt62=fbcursor.fetchone()
                    


                    today625 = date.today()
                    first625 = today625.replace(day=1)
                    last_month625 = first625 -relativedelta(months=4)
                    
                    end_today625 = last_month625
                    end_first625 = end_today625.replace(day=1)
                    end_month625 = end_first625 -relativedelta(days=1)+relativedelta(months=1)

                    sql625='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Political Contributions" and acctype="Other Expenses"'
                    sql625_val=(last_month625,end_month625,dtl_cmp_pro[0],)
                    fbcursor.execute(sql625,sql625_val)
                    mnt625=fbcursor.fetchone()

                    today624 = date.today()
                    first624 = today624.replace(day=1)
                    last_month624 = first624 -relativedelta(months=3)
                    
                    end_today624 = last_month624
                    end_first624 = end_today624.replace(day=1)
                    end_month624 = end_first624 -relativedelta(days=1)+relativedelta(months=1)

                    sql624='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Political Contributions" and acctype="Other Expenses"'
                    sql624_val=(last_month624,end_month624,dtl_cmp_pro[0],)
                    fbcursor.execute(sql624,sql624_val)
                    mnt624=fbcursor.fetchone()

                    today362 = date.today()
                    first362 = today362.replace(day=1)
                    last_month362 = first362 -relativedelta(months=2)
                    
                    end_today362 = last_month362
                    end_first362 = end_today362.replace(day=1)
                    end_month362 = end_first362 -relativedelta(days=1)+relativedelta(months=1)

                    sql362='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Political Contributions" and acctype="Other Expenses"'
                    sql362_val=(last_month362,end_month362,dtl_cmp_pro[0],)
                    fbcursor.execute(sql362,sql362_val)
                    mnt362=fbcursor.fetchone()

                    today262 = date.today()
                    first262 = today262.replace(day=1)
                    last_month262 = first262 -relativedelta(months=1)
                    
                    end_today262 = last_month262
                    end_first262 = end_today262.replace(day=1)
                    end_month262 = end_first262 -relativedelta(days=1)+relativedelta(months=1)

                    sql262='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Political Contributions" and acctype="Other Expenses"'
                    sql262_val=(last_month262,end_month262,dtl_cmp_pro[0],)
                    fbcursor.execute(sql262,sql262_val)
                    mnt262=fbcursor.fetchone()

                    today621 = date.today()
                    first621 = today621.replace(day=1)
              

                    end_today621 = date.today()
                    end_first621 = end_today621.replace(day=1)
                    end_month621 = end_first621 -relativedelta(days=1)+relativedelta(months=1)

                    sql621='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Political Contributions" and acctype="Other Expenses"'
                    sql621_val=(first621,end_month621,dtl_cmp_pro[0],)
                    fbcursor.execute(sql621,sql621_val)
                    mnt621=fbcursor.fetchone()

                    sqltt62='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Political Contributions" and acctype="Other Expenses"'
                    sqltt_val62=(last_monthy_gt62,end_month621,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt62,sqltt_val62)
                    mnttt62=fbcursor.fetchone()
                    
                    if mnty_gt62[0] is None:
                        val662="0.0"
                    else:
                        val662=mnty_gt62[0] 
                    r62c2.delete(0,END)
                    r62c2.insert(0,"$"+str(val662))
                    r62c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt625[0] is None:
                        val625="0.0"
                    else:
                        val625=mnt625[0] 
                    r62c3.delete(0,END)
                    r62c3.insert(0,"$"+str(val625))
                    r62c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt624[0] is None:
                        val624="0.0"
                    else:
                        val624=mnt624[0] 
                    r62c4.delete(0,END)
                    r62c4.insert(0,"$"+str(val624))
                    r62c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt362[0] is None:
                        val362="0.0"
                    else:
                        val362=mnt362[0] 
                    r62c5.delete(0,END)
                    r62c5.insert(0,"$"+str(val362))
                    r62c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt262[0] is None:
                        val262="0.0"
                    else:
                        val262=mnt262[0] 
                    r62c6.delete(0,END)
                    r62c6.insert(0,"$"+str(val262))
                    r62c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt621[0] is None:
                        val621="0.0"
                    else:
                        val621=mnt621[0] 
                    r62c7.delete(0,END)
                    r62c7.insert(0,"$"+str(val621))
                    r62c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt62[0] is None:
                        valtt62="0.0"
                    else:
                        valtt62=mnttt62[0] 
                    r62c8.delete(0,END)
                    r62c8.insert(0,"$"+str(valtt62))
                    r62c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")


                    #----------------------------------------------------------63th row
                    lv_name=Label(frm_analiz, text="Reconciliation Discrepancies",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r63c1"))

                    r63c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r63c2, tag=("r63c2"))

                    r63c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r63c3, tag=("r63c3"))

                    r63c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r63c4, tag=("r63c4"))


                    r63c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r63c5, tag=("r63c5"))

                    r63c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r63c6, tag=("r63c6"))


                    r63c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r63c7, tag=("r63c7"))

                    r63c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r63c8, tag=("r63c8"))

                    #----------------------------------------------------------------------
                    today_gt63 = date.today()
                    firsty_gt63= today_gt63.replace(day=1)
                    last_monthy_gt63 = firsty_gt63 -relativedelta(months=5)
                    
                    end_todayy_gt63 = last_monthy_gt63
                    end_firsty_gt63 = end_todayy_gt63.replace(day=1)
                    end_monthy_gt63 = end_firsty_gt63 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt63='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Reconciliation Discrepancies" and acctype="Other Expenses"'
                    sqly_gt63_val=(last_monthy_gt63,end_monthy_gt63,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt63,sqly_gt63_val)
                    mnty_gt63=fbcursor.fetchone()
                    


                    today635 = date.today()
                    first635 = today635.replace(day=1)
                    last_month635 = first635 -relativedelta(months=4)
                    
                    end_today635 = last_month635
                    end_first635 = end_today635.replace(day=1)
                    end_month635 = end_first635 -relativedelta(days=1)+relativedelta(months=1)

                    sql635='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Reconciliation Discrepancies" and acctype="Other Expenses"'
                    sql635_val=(last_month635,end_month635,dtl_cmp_pro[0],)
                    fbcursor.execute(sql635,sql635_val)
                    mnt635=fbcursor.fetchone()

                    today634 = date.today()
                    first634 = today634.replace(day=1)
                    last_month634 = first634 -relativedelta(months=3)
                    
                    end_today634 = last_month634
                    end_first634 = end_today634.replace(day=1)
                    end_month634 = end_first634 -relativedelta(days=1)+relativedelta(months=1)

                    sql634='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Reconciliation Discrepancies" and acctype="Other Expenses"'
                    sql634_val=(last_month634,end_month634,dtl_cmp_pro[0],)
                    fbcursor.execute(sql634,sql634_val)
                    mnt634=fbcursor.fetchone()

                    today363 = date.today()
                    first363 = today363.replace(day=1)
                    last_month363 = first363 -relativedelta(months=2)
                    
                    end_today363 = last_month363
                    end_first363 = end_today363.replace(day=1)
                    end_month363 = end_first363 -relativedelta(days=1)+relativedelta(months=1)

                    sql363='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Reconciliation Discrepancies" and acctype="Other Expenses"'
                    sql363_val=(last_month363,end_month363,dtl_cmp_pro[0],)
                    fbcursor.execute(sql363,sql363_val)
                    mnt363=fbcursor.fetchone()

                    today263 = date.today()
                    first263 = today263.replace(day=1)
                    last_month263 = first263 -relativedelta(months=1)
                    
                    end_today263 = last_month263
                    end_first263 = end_today263.replace(day=1)
                    end_month263 = end_first263 -relativedelta(days=1)+relativedelta(months=1)

                    sql263='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Reconciliation Discrepancies" and acctype="Other Expenses"'
                    sql263_val=(last_month263,end_month263,dtl_cmp_pro[0],)
                    fbcursor.execute(sql263,sql263_val)
                    mnt263=fbcursor.fetchone()

                    today631 = date.today()
                    first631 = today631.replace(day=1)
              

                    end_today631 = date.today()
                    end_first631 = end_today631.replace(day=1)
                    end_month631 = end_first631 -relativedelta(days=1)+relativedelta(months=1)

                    sql631='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Reconciliation Discrepancies" and acctype="Other Expenses"'
                    sql631_val=(first631,end_month631,dtl_cmp_pro[0],)
                    fbcursor.execute(sql631,sql631_val)
                    mnt631=fbcursor.fetchone()

                    sqltt63='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Reconciliation Discrepancies" and acctype="Other Expenses"'
                    sqltt_val63=(last_monthy_gt63,end_month631,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt63,sqltt_val63)
                    mnttt63=fbcursor.fetchone()
                    
                    if mnty_gt63[0] is None:
                        val663="0.0"
                    else:
                        val663=mnty_gt63[0] 
                    r63c2.delete(0,END)
                    r63c2.insert(0,"$"+str(val663))
                    r63c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt635[0] is None:
                        val635="0.0"
                    else:
                        val635=mnt635[0] 
                    r63c3.delete(0,END)
                    r63c3.insert(0,"$"+str(val635))
                    r63c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt634[0] is None:
                        val634="0.0"
                    else:
                        val634=mnt634[0] 
                    r63c4.delete(0,END)
                    r63c4.insert(0,"$"+str(val634))
                    r63c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt363[0] is None:
                        val363="0.0"
                    else:
                        val363=mnt363[0] 
                    r63c5.delete(0,END)
                    r63c5.insert(0,"$"+str(val363))
                    r63c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt263[0] is None:
                        val263="0.0"
                    else:
                        val263=mnt263[0] 
                    r63c6.delete(0,END)
                    r63c6.insert(0,"$"+str(val263))
                    r63c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt631[0] is None:
                        val631="0.0"
                    else:
                        val631=mnt631[0] 
                    r63c7.delete(0,END)
                    r63c7.insert(0,"$"+str(val631))
                    r63c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt63[0] is None:
                        valtt63="0.0"
                    else:
                        valtt63=mnttt63[0] 
                    r63c8.delete(0,END)
                    r63c8.insert(0,"$"+str(valtt63))
                    r63c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------64 th row
                    lv_name=Label(frm_analiz, text="SGST Write-Off",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r64c1"))

                    r64c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r64c2, tag=("r64c2"))

                    r64c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r64c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r64c3, tag=("r64c3"))

                    r64c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r64c4, tag=("r64c4"))


                    r64c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r64c5, tag=("r64c5"))

                    r64c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r64c6, tag=("r64c6"))


                    r64c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r64c7, tag=("r64c7"))

                    r64c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r64c8, tag=("r64c8"))

                    #----------------------------------------------------------------------
                    today_gt64 = date.today()
                    firsty_gt64= today_gt64.replace(day=1)
                    last_monthy_gt64 = firsty_gt64 -relativedelta(months=5)
                    
                    end_todayy_gt64 = last_monthy_gt64
                    end_firsty_gt64 = end_todayy_gt64.replace(day=1)
                    end_monthy_gt64 = end_firsty_gt64 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt64='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="SGST Write-Off" and acctype="Other Expenses"'
                    sqly_gt64_val=(last_monthy_gt64,end_monthy_gt64,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt64,sqly_gt64_val)
                    mnty_gt64=fbcursor.fetchone()
                    


                    today645 = date.today()
                    first645 = today645.replace(day=1)
                    last_month645 = first645 -relativedelta(months=4)
                    
                    end_today645 = last_month645
                    end_first645 = end_today645.replace(day=1)
                    end_month645 = end_first645 -relativedelta(days=1)+relativedelta(months=1)

                    sql645='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="SGST Write-Off" and acctype="Other Expenses"'
                    sql645_val=(last_month645,end_month645,dtl_cmp_pro[0],)
                    fbcursor.execute(sql645,sql645_val)
                    mnt645=fbcursor.fetchone()

                    today644 = date.today()
                    first644 = today644.replace(day=1)
                    last_month644 = first644 -relativedelta(months=3)
                    
                    end_today644 = last_month644
                    end_first644 = end_today644.replace(day=1)
                    end_month644 = end_first644 -relativedelta(days=1)+relativedelta(months=1)

                    sql644='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="SGST Write-Off" and acctype="Other Expenses"'
                    sql644_val=(last_month644,end_month644,dtl_cmp_pro[0],)
                    fbcursor.execute(sql644,sql644_val)
                    mnt644=fbcursor.fetchone()

                    today364 = date.today()
                    first364 = today364.replace(day=1)
                    last_month364 = first364 -relativedelta(months=2)
                    
                    end_today364 = last_month364
                    end_first364 = end_today364.replace(day=1)
                    end_month364 = end_first364 -relativedelta(days=1)+relativedelta(months=1)

                    sql364='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="SGST Write-Off" and acctype="Other Expenses"'
                    sql364_val=(last_month364,end_month364,dtl_cmp_pro[0],)
                    fbcursor.execute(sql364,sql364_val)
                    mnt364=fbcursor.fetchone()

                    today264 = date.today()
                    first264 = today264.replace(day=1)
                    last_month264 = first264 -relativedelta(months=1)
                    
                    end_today264 = last_month264
                    end_first264 = end_today264.replace(day=1)
                    end_month264 = end_first264 -relativedelta(days=1)+relativedelta(months=1)

                    sql264='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="SGST Write-Off" and acctype="Other Expenses"'
                    sql264_val=(last_month264,end_month264,dtl_cmp_pro[0],)
                    fbcursor.execute(sql264,sql264_val)
                    mnt264=fbcursor.fetchone()

                    today641 = date.today()
                    first641 = today641.replace(day=1)
              

                    end_today641 = date.today()
                    end_first641 = end_today641.replace(day=1)
                    end_month641 = end_first641 -relativedelta(days=1)+relativedelta(months=1)

                    sql641='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="SGST Write-Off" and acctype="Other Expenses"'
                    sql641_val=(first641,end_month641,dtl_cmp_pro[0],)
                    fbcursor.execute(sql641,sql641_val)
                    mnt641=fbcursor.fetchone()

                    sqltt64='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="SGST Write-Off" and acctype="Other Expenses"'
                    sqltt_val64=(last_monthy_gt64,end_month641,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt64,sqltt_val64)
                    mnttt64=fbcursor.fetchone()
                    
                    if mnty_gt64[0] is None:
                        val664="0.0"
                    else:
                        val664=mnty_gt64[0] 
                    r64c2.delete(0,END)
                    r64c2.insert(0,"$"+str(val664))
                    r64c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt645[0] is None:
                        val645="0.0"
                    else:
                        val645=mnt645[0] 
                    r64c3.delete(0,END)
                    r64c3.insert(0,"$"+str(val645))
                    r64c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt644[0] is None:
                        val644="0.0"
                    else:
                        val644=mnt644[0] 
                    r64c4.delete(0,END)
                    r64c4.insert(0,"$"+str(val644))
                    r64c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt364[0] is None:
                        val364="0.0"
                    else:
                        val364=mnt364[0] 
                    r64c5.delete(0,END)
                    r64c5.insert(0,"$"+str(val364))
                    r64c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt264[0] is None:
                        val264="0.0"
                    else:
                        val264=mnt264[0] 
                    r64c6.delete(0,END)
                    r64c6.insert(0,"$"+str(val264))
                    r64c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt641[0] is None:
                        val641="0.0"
                    else:
                        val641=mnt641[0] 
                    r64c7.delete(0,END)
                    r64c7.insert(0,"$"+str(val641))
                    r64c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt64[0] is None:
                        valtt64="0.0"
                    else:
                        valtt64=mnttt64[0] 
                    r64c8.delete(0,END)
                    r64c8.insert(0,"$"+str(valtt64))
                    r64c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------65 th row
                    lv_name=Label(frm_analiz, text="Tax Write-Off",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r65c1"))

                    r65c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r65c2, tag=("r65c2"))

                    r65c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r65c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r65c3, tag=("r65c3"))

                    r65c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r65c4, tag=("r65c4"))


                    r65c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r65c5, tag=("r65c5"))

                    r65c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r65c6, tag=("r65c6"))


                    r65c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r65c7, tag=("r65c7"))

                    r65c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r65c8, tag=("r65c8"))

                    #----------------------------------------------------------------------
                    today_gt65 = date.today()
                    firsty_gt65= today_gt65.replace(day=1)
                    last_monthy_gt65 = firsty_gt65 -relativedelta(months=5)
                    
                    end_todayy_gt65 = last_monthy_gt65
                    end_firsty_gt65 = end_todayy_gt65.replace(day=1)
                    end_monthy_gt65 = end_firsty_gt65 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt65='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Tax Write-Off" and acctype="Other Expenses"'
                    sqly_gt65_val=(last_monthy_gt65,end_monthy_gt65,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt65,sqly_gt65_val)
                    mnty_gt65=fbcursor.fetchone()
                    


                    today655 = date.today()
                    first655 = today655.replace(day=1)
                    last_month655 = first655 -relativedelta(months=4)
                    
                    end_today655 = last_month655
                    end_first655 = end_today655.replace(day=1)
                    end_month655 = end_first655 -relativedelta(days=1)+relativedelta(months=1)

                    sql655='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Tax Write-Off" and acctype="Other Expenses"'
                    sql655_val=(last_month655,end_month655,dtl_cmp_pro[0],)
                    fbcursor.execute(sql655,sql655_val)
                    mnt655=fbcursor.fetchone()

                    today654 = date.today()
                    first654 = today654.replace(day=1)
                    last_month654 = first654 -relativedelta(months=3)
                    
                    end_today654 = last_month654
                    end_first654 = end_today654.replace(day=1)
                    end_month654 = end_first654 -relativedelta(days=1)+relativedelta(months=1)

                    sql654='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Tax Write-Off" and acctype="Other Expenses"'
                    sql654_val=(last_month654,end_month654,dtl_cmp_pro[0],)
                    fbcursor.execute(sql654,sql654_val)
                    mnt654=fbcursor.fetchone()

                    today365 = date.today()
                    first365 = today365.replace(day=1)
                    last_month365 = first365 -relativedelta(months=2)
                    
                    end_today365 = last_month365
                    end_first365 = end_today365.replace(day=1)
                    end_month365 = end_first365 -relativedelta(days=1)+relativedelta(months=1)

                    sql365='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Tax Write-Off" and acctype="Other Expenses"'
                    sql365_val=(last_month365,end_month365,dtl_cmp_pro[0],)
                    fbcursor.execute(sql365,sql365_val)
                    mnt365=fbcursor.fetchone()

                    today265 = date.today()
                    first265 = today265.replace(day=1)
                    last_month265 = first265 -relativedelta(months=1)
                    
                    end_today265 = last_month265
                    end_first265 = end_today265.replace(day=1)
                    end_month265 = end_first265 -relativedelta(days=1)+relativedelta(months=1)

                    sql265='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Tax Write-Off" and acctype="Other Expenses"'
                    sql265_val=(last_month265,end_month265,dtl_cmp_pro[0],)
                    fbcursor.execute(sql265,sql265_val)
                    mnt265=fbcursor.fetchone()

                    today651 = date.today()
                    first651 = today651.replace(day=1)
              

                    end_today651 = date.today()
                    end_first651 = end_today651.replace(day=1)
                    end_month651 = end_first651 -relativedelta(days=1)+relativedelta(months=1)

                    sql651='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Tax Write-Off" and acctype="Other Expenses"'
                    sql651_val=(first651,end_month651,dtl_cmp_pro[0],)
                    fbcursor.execute(sql651,sql651_val)
                    mnt651=fbcursor.fetchone()

                    sqltt65='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Tax Write-Off" and acctype="Other Expenses"'
                    sqltt_val65=(last_monthy_gt65,end_month651,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt65,sqltt_val65)
                    mnttt65=fbcursor.fetchone()
                    
                    if mnty_gt65[0] is None:
                        val665="0.0"
                    else:
                        val665=mnty_gt65[0] 
                    r65c2.delete(0,END)
                    r65c2.insert(0,"$"+str(val665))
                    r65c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt655[0] is None:
                        val655="0.0"
                    else:
                        val655=mnt655[0] 
                    r65c3.delete(0,END)
                    r65c3.insert(0,"$"+str(val655))
                    r65c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt654[0] is None:
                        val654="0.0"
                    else:
                        val654=mnt654[0] 
                    r65c4.delete(0,END)
                    r65c4.insert(0,"$"+str(val654))
                    r65c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt365[0] is None:
                        val365="0.0"
                    else:
                        val365=mnt365[0] 
                    r65c5.delete(0,END)
                    r65c5.insert(0,"$"+str(val365))
                    r65c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt265[0] is None:
                        val265="0.0"
                    else:
                        val265=mnt265[0] 
                    r65c6.delete(0,END)
                    r65c6.insert(0,"$"+str(val265))
                    r65c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt651[0] is None:
                        val651="0.0"
                    else:
                        val651=mnt651[0] 
                    r65c7.delete(0,END)
                    r65c7.insert(0,"$"+str(val651))
                    r65c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt65[0] is None:
                        valtt65="0.0"
                    else:
                        valtt65=mnttt65[0] 
                    r65c8.delete(0,END)
                    r65c8.insert(0,"$"+str(valtt65))
                    r65c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------66 th row
                    lv_name=Label(frm_analiz, text="Vehicle Expenses",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r66c1"))

                    r66c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r66c2, tag=("r66c2"))

                    r66c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r66c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r66c3, tag=("r66c3"))

                    r66c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r66c4, tag=("r66c4"))


                    r66c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r66c5, tag=("r66c5"))

                    r66c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r66c6, tag=("r66c6"))


                    r66c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r66c7, tag=("r66c7"))

                    r66c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r66c8, tag=("r66c8"))

                    #----------------------------------------------------------------------
                    today_gt66 = date.today()
                    firsty_gt66= today_gt66.replace(day=1)
                    last_monthy_gt66 = firsty_gt66 -relativedelta(months=5)
                    
                    end_todayy_gt66 = last_monthy_gt66
                    end_firsty_gt66 = end_todayy_gt66.replace(day=1)
                    end_monthy_gt66 = end_firsty_gt66 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt66='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Vehicle Expenses" and acctype="Other Expenses"'
                    sqly_gt66_val=(last_monthy_gt66,end_monthy_gt66,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt66,sqly_gt66_val)
                    mnty_gt66=fbcursor.fetchone()
                    


                    today665 = date.today()
                    first665 = today665.replace(day=1)
                    last_month665 = first665 -relativedelta(months=4)
                    
                    end_today665 = last_month665
                    end_first665 = end_today665.replace(day=1)
                    end_month665 = end_first665 -relativedelta(days=1)+relativedelta(months=1)

                    sql665='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Vehicle Expenses" and acctype="Other Expenses"'
                    sql665_val=(last_month665,end_month665,dtl_cmp_pro[0],)
                    fbcursor.execute(sql665,sql665_val)
                    mnt665=fbcursor.fetchone()

                    today664 = date.today()
                    first664 = today664.replace(day=1)
                    last_month664 = first664 -relativedelta(months=3)
                    
                    end_today664 = last_month664
                    end_first664 = end_today664.replace(day=1)
                    end_month664 = end_first664 -relativedelta(days=1)+relativedelta(months=1)

                    sql664='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Vehicle Expenses" and acctype="Other Expenses"'
                    sql664_val=(last_month664,end_month664,dtl_cmp_pro[0],)
                    fbcursor.execute(sql664,sql664_val)
                    mnt664=fbcursor.fetchone()

                    today366 = date.today()
                    first366 = today366.replace(day=1)
                    last_month366 = first366 -relativedelta(months=2)
                    
                    end_today366 = last_month366
                    end_first366 = end_today366.replace(day=1)
                    end_month366 = end_first366 -relativedelta(days=1)+relativedelta(months=1)

                    sql366='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Vehicle Expenses" and acctype="Other Expenses"'
                    sql366_val=(last_month366,end_month366,dtl_cmp_pro[0],)
                    fbcursor.execute(sql366,sql366_val)
                    mnt366=fbcursor.fetchone()

                    today266 = date.today()
                    first266 = today266.replace(day=1)
                    last_month266 = first266 -relativedelta(months=1)
                    
                    end_today266 = last_month266
                    end_first266 = end_today266.replace(day=1)
                    end_month266 = end_first266 -relativedelta(days=1)+relativedelta(months=1)

                    sql266='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Vehicle Expenses" and acctype="Other Expenses"'
                    sql266_val=(last_month266,end_month266,dtl_cmp_pro[0],)
                    fbcursor.execute(sql266,sql266_val)
                    mnt266=fbcursor.fetchone()

                    today661 = date.today()
                    first661 = today661.replace(day=1)
              

                    end_today661 = date.today()
                    end_first661 = end_today661.replace(day=1)
                    end_month661 = end_first661 -relativedelta(days=1)+relativedelta(months=1)

                    sql661='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Vehicle Expenses" and acctype="Other Expenses"'
                    sql661_val=(first661,end_month661,dtl_cmp_pro[0],)
                    fbcursor.execute(sql661,sql661_val)
                    mnt661=fbcursor.fetchone()

                    sqltt66='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and name="Vehicle Expenses" and acctype="Other Expenses"'
                    sqltt_val66=(last_monthy_gt66,end_month661,dtl_cmp_pro[0],)
                    fbcursor.execute(sqltt66,sqltt_val66)
                    mnttt66=fbcursor.fetchone()
                    
                    if mnty_gt66[0] is None:
                        val666="0.0"
                    else:
                        val666=mnty_gt66[0] 
                    r66c2.delete(0,END)
                    r66c2.insert(0,"$"+str(val666))
                    r66c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt665[0] is None:
                        val665="0.0"
                    else:
                        val665=mnt665[0] 
                    r66c3.delete(0,END)
                    r66c3.insert(0,"$"+str(val665))
                    r66c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt664[0] is None:
                        val664="0.0"
                    else:
                        val664=mnt664[0] 
                    r66c4.delete(0,END)
                    r66c4.insert(0,"$"+str(val664))
                    r66c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt366[0] is None:
                        val366="0.0"
                    else:
                        val366=mnt366[0] 
                    r66c5.delete(0,END)
                    r66c5.insert(0,"$"+str(val366))
                    r66c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt266[0] is None:
                        val266="0.0"
                    else:
                        val266=mnt266[0] 
                    r66c6.delete(0,END)
                    r66c6.insert(0,"$"+str(val266))
                    r66c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt661[0] is None:
                        val661="0.0"
                    else:
                        val661=mnt661[0] 
                    r66c7.delete(0,END)
                    r66c7.insert(0,"$"+str(val661))
                    r66c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnttt66[0] is None:
                        valtt66="0.0"
                    else:
                        valtt66=mnttt66[0] 
                    r66c8.delete(0,END)
                    r66c8.insert(0,"$"+str(valtt66))
                    r66c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    #----------------------------------------------------------67 th row
                    lv_name=Label(frm_analiz, text="Total Cash Outflows",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r67c1"))

                    r67c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r67c2, tag=("r67c2"))

                    r67c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r67c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r67c3, tag=("r67c3"))

                    r67c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r67c4, tag=("r67c4"))


                    r67c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r67c5, tag=("r67c5"))

                    r67c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r67c6, tag=("r67c6"))


                    r67c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r67c7, tag=("r67c7"))

                    r67c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r67c8, tag=("r67c8"))

                    #-----------------------------------------------------------------------------
                    today_gt67 = date.today()
                    firsty_gt67= today_gt67.replace(day=1)
                    last_monthy_gt67 = firsty_gt67 -relativedelta(months=5)
                    
                    end_todayy_gt67 = last_monthy_gt67
                    end_firsty_gt67 = end_todayy_gt67.replace(day=1)
                    end_monthy_gt67 = end_firsty_gt67 -relativedelta(days=1)+relativedelta(months=1)

                    sqly_gt67='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype in ("Other Expenses","Expenses")'
                    sqly_gt67_val=(last_monthy_gt67,end_monthy_gt67,dtl_cmp_pro[0],)
                    fbcursor.execute(sqly_gt67,sqly_gt67_val)
                    mnty_gt67=fbcursor.fetchone()
                    


                    today675 = date.today()
                    first675 = today675.replace(day=1)
                    last_month675 = first675 -relativedelta(months=4)
                    
                    end_today675 = last_month675
                    end_first675 = end_today675.replace(day=1)
                    end_month675 = end_first675 -relativedelta(days=1)+relativedelta(months=1)

                    sql675='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype in ("Other Expenses","Expenses")'
                    sql675_val=(last_month675,end_month675,dtl_cmp_pro[0],)
                    fbcursor.execute(sql675,sql675_val)
                    mnt675=fbcursor.fetchone()

                    today674 = date.today()
                    first674 = today674.replace(day=1)
                    last_month674 = first674 -relativedelta(months=3)
                    
                    end_today674 = last_month674
                    end_first674 = end_today674.replace(day=1)
                    end_month674 = end_first674 -relativedelta(days=1)+relativedelta(months=1)

                    sql674='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype in ("Other Expenses","Expenses")'
                    sql674_val=(last_month674,end_month674,dtl_cmp_pro[0],)
                    fbcursor.execute(sql674,sql674_val)
                    mnt674=fbcursor.fetchone()

                    today367 = date.today()
                    first367 = today367.replace(day=1)
                    last_month367 = first367 -relativedelta(months=2)
                    
                    end_today367 = last_month367
                    end_first367 = end_today367.replace(day=1)
                    end_month367 = end_first367 -relativedelta(days=1)+relativedelta(months=1)

                    sql367='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype in ("Other Expenses","Expenses")'
                    sql367_val=(last_month367,end_month367,dtl_cmp_pro[0],)
                    fbcursor.execute(sql367,sql367_val)
                    mnt367=fbcursor.fetchone()

                    today267 = date.today()
                    first267 = today267.replace(day=1)
                    last_month267 = first267 -relativedelta(months=1)
                    
                    end_today267 = last_month267
                    end_first267 = end_today267.replace(day=1)
                    end_month267 = end_first267 -relativedelta(days=1)+relativedelta(months=1)

                    sql267='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype in ("Other Expenses","Expenses")'
                    sql267_val=(last_month267,end_month267,dtl_cmp_pro[0],)
                    fbcursor.execute(sql267,sql267_val)
                    mnt267=fbcursor.fetchone()

                    today671 = date.today()
                    first671 = today671.replace(day=1)
              

                    end_today671 = date.today()
                    end_first671 = end_today671.replace(day=1)
                    end_month671 = end_first671 -relativedelta(days=1)+relativedelta(months=1)

                    sql671='select sum(balance) from app1_accounts1 where asof between %s and %s and cid_id=%s and acctype in ("Other Expenses","Expenses")'
                    sql671_val=(first671,end_month671,dtl_cmp_pro[0],)
                    fbcursor.execute(sql671,sql671_val)
                    mnt671=fbcursor.fetchone()

                    
                    
                    if mnty_gt67[0] is None:
                        val676=0.0
                    else:
                        val676=mnty_gt67[0] 
                    r67c2.delete(0,END)
                    r67c2.insert(0,"$"+str(val676))
                    r67c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt675[0] is None:
                        val675="0.0"
                    else:
                        val675=mnt675[0] 
                    r67c3.delete(0,END)
                    r67c3.insert(0,"$"+str(val675))
                    r67c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt674[0] is None:
                        val674="0.0"
                    else:
                        val674=mnt674[0] 
                    r67c4.delete(0,END)
                    r67c4.insert(0,"$"+str(val674))
                    r67c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    if mnt367[0] is None:
                        val367="0.0"
                    else:
                        val367=mnt367[0] 
                    r67c5.delete(0,END)
                    r67c5.insert(0,"$"+str(val367))
                    r67c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    if mnt267[0] is None:
                        val267="0.0"
                    else:
                        val267=mnt267[0] 
                    r67c6.delete(0,END)
                    r67c6.insert(0,"$"+str(val267))
                    r67c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    if mnt671[0] is None:
                        val671="0.0"
                    else:
                        val671=mnt671[0] 
                    r67c7.delete(0,END)
                    r67c7.insert(0,"$"+str(val671))
                    r67c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    # if mnttt67[0] is None:
                    #     valtt67="0.0"
                    # else:
                    #     valtt67=mnttt67[0] 
                    sum_tt_67=round(float(mnty_gt67[0])+float(mnt675[0])+float(mnt674[0])+float(mnt367[0])+float(mnt267[0])+float(mnt671[0]),2)
                    r67c8.delete(0,END)
                    r67c8.insert(0,"$"+str(sum_tt_67))
                    r67c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    #----------------------------------------------------------68 th row
                    lv_name=Label(frm_analiz, text="Ending Cash Balance",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r68c1"))

                    r68c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r68c2, tag=("r68c2"))

                    r68c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    r68c3.insert(0,"$11111111111")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r68c3, tag=("r68c3"))

                    r68c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r68c4, tag=("r68c4"))


                    r68c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r68c5, tag=("r68c5"))

                    r68c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r68c6, tag=("r68c6"))


                    r68c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r68c7, tag=("r68c7"))

                    r68c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r68c8, tag=("r68c8"))

                    #----------------------------------------------------------------------
                    
                    
                    # if mnty_gt68[0] is None:
                    #     val686="0.0"
                    # else:
                    #     val686=mnty_gt68[0] 
                    val686=round(float(val623)-float(mnty_gt67[0]))
                    r68c2.delete(0,END)
                    r68c2.insert(0,"$"+str(val686))
                    r68c2.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    # if mnt685[0] is None:
                    #     val685="0.0"
                    # else:
                    #     val685=mnt685[0] 
                    val685=round(float(val523)-float(mnt675[0]))
                    r68c3.delete(0,END)
                    r68c3.insert(0,"$"+str(val685))
                    r68c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    # if mnt684[0] is None:
                    #     val684="0.0"
                    # else:
                    #     val684=mnt684[0] 
                    val684=round(float(val423)-float(mnt674[0]))
                    r68c4.delete(0,END)
                    r68c4.insert(0,"$"+str(val684))
                    r68c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")  

                    # if mnt368[0] is None:
                    #     val368="0.0"
                    # else:
                    #     val368=mnt368[0] 
                    val368=round(float(val323)-float(mnt367[0]))
                    r68c5.delete(0,END)
                    r68c5.insert(0,"$"+str(val368))
                    r68c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    # if mnt268[0] is None:
                    #     val268="0.0"
                    # else:
                    #     val268=mnt268[0] 
                    val268=round(float(val232)-float(mnt267[0]))
                    r68c6.delete(0,END)
                    r68c6.insert(0,"$"+str(val268))
                    r68c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    # if mnt681[0] is None:
                    #     val681="0.0"
                    # else:
                    #     val681=mnt681[0] 
                    val681=round(float(val231)-float(mnt671[0]))
                    r68c7.delete(0,END)
                    r68c7.insert(0,"$"+str(val681))
                    r68c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    # if mnttt68[0] is None:
                    #     valtt68="0.0"
                    # else:
                    #     valtt68=mnttt68[0] 
                    tt_sm_68=round(float(val686)+float(val685)+float(val684)+float(val368)+float(val268)+float(val681),2)
                    r68c8.delete(0,END)
                    r68c8.insert(0,"$"+str(tt_sm_68))
                    r68c8.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")


                    #*********************************************************************************************beginning balance
                    
                    # r2c3.delete(0,END)
                    # r2c3.insert(0,"$"+str(val686))
                    # r2c3.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white") 

                    # r2c4.delete(0,END)
                    # r2c4.insert(0,"$"+str(val685))
                    # r2c4.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    # r2c5.delete(0,END)
                    # r2c5.insert(0,"$"+str(val684))
                    # r2c5.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    # r2c6.delete(0,END)
                    # r2c6.insert(0,"$"+str(val368))
                    # r2c6.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")

                    # r2c7.delete(0,END)
                    # r2c6.insert(0,"$"+str(val268))
                    # r2c7.config(state=DISABLED,disabledbackground="#213b52",disabledforeground="white")
                    
                    # tt_sm_23=round(float(val623)+float(val523)+float(val423)+float(val323)+float(val232)+float(val231),2)

                    # #----------------------------------------------------------69th row
                    # lv_name=Label(frm_analiz, text="Ending Cash Balance",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r69c1"))

                    # r69c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r69c2, tag=("r69c2"))

                    # r69c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    # r69c3.insert(0,"$11111111111")
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r69c3, tag=("r69c3"))

                    # r69c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r69c4, tag=("r69c4"))


                    # r69c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r69c5, tag=("r69c5"))

                    # r69c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r69c6, tag=("r69c6"))


                    # r69c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r69c7, tag=("r69c7"))

                    # r69c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r69c8, tag=("r69c8"))
                    # #----------------------------------------------------------70 th row
                    # lv_name=Label(frm_analiz, text="January",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r70c1"))

                    # r70c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r70c2, tag=("r70c2"))

                    # r70c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    # r70c3.insert(0,"$11111111111")
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r70c3, tag=("r70c3"))

                    # r70c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r70c4, tag=("r70c4"))


                    # r70c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r70c5, tag=("r70c5"))

                    # r70c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r70c6, tag=("r70c6"))


                    # r70c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r70c7, tag=("r70c7"))

                    # r70c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r70c8, tag=("r70c8"))

                    # #----------------------------------------------------------71 th row
                    # lv_name=Label(frm_analiz, text="January",bg="#213b52", width=42, fg="White", anchor="nw",font=('Calibri 12 bold'))
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="center", window=lv_name,tag=("r71c1"))

                    # r71c2 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r71c2, tag=("r71c2"))

                    # r71c3 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)
                    # r71c3.insert(0,"$11111111111")
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r71c3, tag=("r71c3"))

                    # r71c4 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                    
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r71c4, tag=("r71c4"))


                    # r71c5 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r71c5, tag=("r71c5"))

                    # r71c6 = Entry(frm_analiz, width=13 ,font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r71c6, tag=("r71c6"))


                    # r71c7 = Entry(frm_analiz, width=13, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                   
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r71c7, tag=("r71c7"))

                    # r71c8 = Entry(frm_analiz, width=18, font=('Calibri 13'), bg="#213b52",fg="white", bd=1)                  
                    # win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=r71c8, tag=("r71c8"))

                    

                    #******************************************************************Check Cash flow
                    tab10_3.grid_columnconfigure(0,weight=1)
                    tab10_3.grid_rowconfigure(0,weight=1)

                    fin_cash_flow=Frame(tab10_3,bg="#2f516f",)
                    fin_cash_flow.grid(row=0,column=0,sticky='nsew')
                    
                    def res_wid_flow(event):
                        dwidth = event.width
                        dheight = event.height
                        dcanvas = event.widget
                        
                        
                        
                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/13
                        y2 = dheight/4

                        dcanvas.coords("bg_polygen_flow",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )   

                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/3.5
                        y2 = dheight/.42

                        dcanvas.coords("bg_polygen_flow2",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )   
                        
                        dcanvas.coords("leb_hdd",dwidth/2,dheight/7)
                        dcanvas.coords("hd_fl_sub",dwidth/2,dheight/5.2)   
                        dcanvas.coords("flow_hr",dwidth/40,dheight/4.5,dwidth/1.03,dheight/4.5)

                        dcanvas.coords("hf_lb_2",dwidth/2,dheight/3) 
                        dcanvas.coords("flow_hr2",dwidth/40,dheight/2.5,dwidth/1.03,dheight/2.5)
                        dcanvas.coords("img_flow",dwidth/40 ,dheight/2.3) 
                        dcanvas.coords("cmb_bx_fl",dwidth/2 ,dheight/2) 
                        dcanvas.coords("hd_fl_hde",dwidth/1.9 ,dheight/2.1) 
                        dcanvas.coords("hd_fl_hds",dwidth/1.35 ,dheight/1.5) 
                        dcanvas.coords("hd_fl_hrs",dwidth/2 ,dheight/1.4,dwidth/1.03 ,dheight/1.4) 

                        dcanvas.coords("nm_nm21",dwidth/1.75 ,dheight/1.25) 
                        dcanvas.coords("hd_lb_hds",dwidth/1.64  ,dheight/1.3) 

                         
                        

                        dcanvas.coords("nm_nm241",dwidth/1.3 ,dheight/1.25)
                        dcanvas.coords("lb_nm241",dwidth/1.230 ,dheight/1.3)

                        

                        dcanvas.coords("cash_hd",dwidth/2 ,dheight/.85)
                        dcanvas.coords("tree_flow",dwidth/33 ,dheight/.80)
                        dcanvas.coords("btn_flow",dwidth/1.45 ,dheight/1)
                        dcanvas.coords("scrollbary",dwidth/1.04 ,dheight/.80)
                        

                    fin_cash_flow.grid_rowconfigure(0,weight=1)
                    fin_cash_flow.grid_columnconfigure(0,weight=1)

                    frm_flow = Canvas(fin_cash_flow,height=700,bg='#2f516f',scrollregion=(0,0,700,1500))
                    flow_scrl = Scrollbar(fin_cash_flow,orient=VERTICAL)
                    flow_scrl.grid(row=0,column=2,sticky='ns')
                    flow_scrl.config(command=frm_flow.yview)
                    frm_flow.bind("<Configure>", res_wid_flow)
                    frm_flow.config(yscrollcommand=flow_scrl.set)
                    frm_flow.grid(row=0,column=0,sticky='nsew')

                    scrollbary = Scrollbar(fin_cash_flow, orient=VERTICAL)

                    #----------------------------------------------------------------------------------heder 1
                    rth2 = frm_flow.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_flow"),smooth=True,)

                    lv_name=Label(frm_flow, text="Reconcile An Account",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
                    win_inv1 = frm_flow.create_window(0, 0, anchor="center", window=lv_name,tag=("leb_hdd"))
                    frm_flow.create_line(0, 0, 0, 0,fill="gray", tag=("flow_hr") )

                    lv_name=Label(frm_flow, text="Open your statement and let's get started.",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                    win_inv1 = frm_flow.create_window(0, 0, anchor="center", window=lv_name,tag=("hd_fl_sub"))


                    #----------------------------------------------------------------------------------heder 2
                    rth2 = frm_flow.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_flow2"),smooth=True,)

                    lv_name=Label(frm_flow, text="Which account do you want to reconcile..??",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                    win_inv1 = frm_flow.create_window(0, 0, anchor="center", window=lv_name,tag=("hf_lb_2"))
                    
                    frm_flow.create_line(0, 0, 0, 0,fill="gray", tag=("flow_hr2") )

                    img = Label(frm_flow, image = cash_flow,bg="#213b52",  justify=RIGHT)
                    win_inv1 = frm_flow.create_window(0, 0, anchor="nw", window=img, tag=("img_flow"))

                    def qry_run():

                        
                        
                        sql_qryrn='select * from app1_accounts1 where cid_id =%s and acctype=%s and asof between %s and %s'
                        sql_qryrn_val=(dtl_cmp_pro[0],date_frt.get(),dt_entry_bg.get_date(),dt_entry_ent.get_date(),)
                        fbcursor.execute(sql_qryrn,sql_qryrn_val)
                        flow_tb_val=fbcursor.fetchall()
                        
                        for record in flow_tree.get_children():
                            flow_tree.delete(record)
                        if flow_tb_val is not None:
                        
                            count_qry=0

                            for i in flow_tb_val:
                                flow_tree.insert(parent='', index='end', iid=count_qry, text='hello', values=(i[0],i[3],i[1],i[2],i[8],"$"+str(i[7])))
                                count_qry +=1
                        else:
                            flow_tree.insert(parent='', index='end', iid=count_qry, text='hello', values=("-","-","-","No Data","-","-"))
                        # for i in range(100):
                        #     flow_tree.insert(parent='', index='end', iid=i, text='hello', values=("-","-","No Data","-"))
                                

                    lv_name=Label(frm_flow, text="Account",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                    win_inv1 = frm_flow.create_window(0, 0, anchor="center", window=lv_name,tag=("hd_fl_hde"))

                    date_frt= StringVar()
                    glt_type = ttk.Combobox(frm_flow,textvariable=date_frt,width=55,font=('Calibri 16'))

                    sql_qrycmp='select DISTINCT acctype from app1_accounts1 where cid_id =%s'
                    sql_qrycmp_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_qrycmp,sql_qrycmp_val)
                    flow_cmb_val=fbcursor.fetchall()
                    cmp_ls=[]
                    for i in flow_cmb_val:
                                cmp_ls.append(i[0])
                    
                    glt_type['values'] = cmp_ls
                    glt_type.bind('<<ComboboxSelected>>', "chart_tp_slt")
                    glt_type.current(0)
                    win_inv1 = frm_flow.create_window(0, 0, anchor="nw", window=glt_type, tag=("cmb_bx_fl"))

                    lv_name=Label(frm_flow, text="Enter the following from your statement.",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                    win_inv1 = frm_flow.create_window(0, 0, anchor="center", window=lv_name,tag=("hd_fl_hds"))

                    frm_flow.create_line(0, 0, 0, 0,fill="gray", tag=("hd_fl_hrs") )

                    but_gl = customtkinter.CTkButton(master=frm_flow,command=qry_run,text="Run",bg="#213b52")
                    win_inv1 = frm_flow.create_window(0, 0, anchor="nw", window=but_gl, tag=("btn_flow"))


                    lv_name=Label(frm_flow, text="Cash Flow Details",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
                    win_inv1 = frm_flow.create_window(0, 0, anchor="center", window=lv_name,tag=("cash_hd"))
                    #table
            
                    
                    fgth = ttk.Style()
                    fgth.theme_use("default")
                    fgth.configure("Treeview", background="#2f516f", foreground="white",fieldbackground="#2f516f",rowheight=25,font=(None,11),)
                    fgth.configure("Treeview.Heading",background="#1b3857",activeforeground="black",foreground="white",font=(None,11), justify="center")  
                    global flow_tree
                    flow_tree = ttk.Treeview(frm_flow, columns = (1,2,3,4,5,6),show = "headings", heigh=25, yscrollcommand=scrollbary.set)
                    # flow_tree.pack(side = 'top')
                    flow_tree.heading(1, text="ID")
                    flow_tree.heading(2, text="NAME")
                    flow_tree.heading(3, text="TYPE")
                    flow_tree.heading(4, text="DETAIL TYPE")
                    flow_tree.heading(5, text="DATE")
                    flow_tree.heading(6, text="FINSYS BALANCE")
                    
                    flow_tree.column(1, width = 112)
                    flow_tree.column(2, width = 312)
                    flow_tree.column(3, width =200)
                    flow_tree.column(4, width = 312)
                    flow_tree.column(5, width = 112)
                    flow_tree.column(6, width =200)
                    
                    scrollbary.config(command=flow_tree.yview)
                    scrollbary.grid(row=0,column=1,sticky='ns')
                    
                    window_label_4 = frm_flow.create_window(0, 0, anchor="nw", window=flow_tree,tags=('tree_flow'))

                    lv_name=Label(frm_flow, text="Ending Balance",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                    win_inv1 = frm_flow.create_window(0, 0, anchor="center", window=lv_name,tag=("lb_nm241"))

                    
                    
                    lv_name=Label(frm_flow, text="Bigining Date",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                    win_inv1 = frm_flow.create_window(0, 0, anchor="center", window=lv_name,tag=("hd_lb_hds"))

                    dt_entry_bg = DateEntry(frm_flow,width=15 , font=('Calibri 16'),date_pattern='Y-mm-dd',borderwidth=2)
                    win_inv1 = frm_flow.create_window(0, 0, anchor="nw", window=dt_entry_bg, tag=("nm_nm21"))

                    dt_entry_ent = DateEntry(frm_flow,width=15 , font=('Calibri 16'),date_pattern='Y-mm-dd',borderwidth=2)
                    win_inv1 = frm_flow.create_window(0, 0, anchor="nw", window=dt_entry_ent, tag=("nm_nm241"))


                    
                    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                    # 
                    # {My Account}
                    
                    def search_dash():
                        if srh_top.get()=="Dashboard":
                            pass
                        else:
                            pass
                    srh_top = Entry(tp_lb_srh, width=50, font=('Calibri 16'))
                    srh_top.insert(0,"Search")
                    srh_top.bind("<Button-1>",srh_fn)
                    srh_top.grid(row=2,column=1,padx=(30,0), pady=20,sticky='nsew')

                    srh_btn6 = Button(tp_lb_srh, image=srh_img, command=search_dash, bg="#213b52", fg="black",border=0)
                    srh_btn6.grid(row=2,column=4,padx=(0,30))
                    Sys_mains_frame=Frame(tab9, height=750,bg="#2f516f")
                    Sys_mains_frame.pack(fill=X)
                    
                else:
                    messagebox.showerror("Login Failed","Invalid username or password")
                    pass
    
#---------------------------------------------------------------------------------------------------------------Company Second Portion
def cmpny_crt2():
    

    cmp_name=cmp_nm.get()
    cmp_address=cmp_cmpn.get()
    cmp_ctys=cmp_cty.get()
    state=cmp_stat.get()
    cmp_pins=cmp_pin.get()
    cmp_emails=cmp_email.get()
    cmp_phs=cmp_ph.get()
    cmp_filess=cmp_files.get()
    if cmp_name is not None:
        sql_log_sql='select id from auth_user where username=%s'
        sql_log_sql_val=(sys_usr.get(),)
        
        fbcursor.execute(sql_log_sql,sql_log_sql_val,)
        id=fbcursor.fetchone()
        
        signup_cmp_sql="insert into app1_company(cname,caddress,city,state,pincode,cemail,phone,cimg,id_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
        signup_cmp_sql_val=(cmp_name,cmp_address,cmp_ctys,state,cmp_pins,cmp_emails,cmp_phs,cmp_filess,id[0])
        fbcursor.execute(signup_cmp_sql,signup_cmp_sql_val,)
        finsysdb.commit()
    else:
        messagebox.showerror("Company Creation Failed","Enter your company details")

    main_frame_cmpny.pack_forget()
    global main_frame_cmpny2,nm_nm2,industry_tp,cmp_type,bs_act_man,paid_typ
    main_frame_cmpny2=Frame(root, height=750,bg="#213b52")
    main_frame_cmpny2.pack(fill=X,)

    cmpny_dt_frm2=Frame(main_frame_cmpny2, height=650, width=500,bg="white")
    cmpny_dt_frm2.pack(pady=105)

    def responsive_wid_cmp2(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("cmpny_hd1",dwidth/40,dheight/15)
        dcanvas.coords("nm_nm2",dwidth/6,dheight/5)
        dcanvas.coords("cmpny_cntry",dwidth/6,dheight/3.2)
        dcanvas.coords("cmpny_cntry2",dwidth/6,dheight/2.35)
        dcanvas.coords("r1",dwidth/2.2,dheight/1.8)
        dcanvas.coords("r2",dwidth/2.2,dheight/1.6)
        dcanvas.coords("cmpny_cntry3",dwidth/6,dheight/1.38)
        # dcanvas.coords("button_cmp2",dwidth/4.3,dheight/1.2)
        # dcanvas.coords("button_cmp3",dwidth/1.9,dheight/1.2)
        dcanvas.coords("button_cmp3",dwidth/2.8,dheight/1.1)
        

        dcanvas.coords("cmp_lbl1",dwidth/6,dheight/3.8)
        dcanvas.coords("cmp_lbl2",dwidth/6,dheight/2.7)
        dcanvas.coords("cmp_lbl3",dwidth/6,dheight/2)
        dcanvas.coords("cmp_lbl4",dwidth/6,dheight/1.46)
        

    lf_cmpy2= Canvas(cmpny_dt_frm2,height=650, width=500)
    lf_cmpy2.bind("<Configure>", responsive_wid_cmp2)
    lf_cmpy2.pack(fill=X)

    def name_ent2(event):
        if nm_nm2.get()=="Legal Business Name":
            nm_nm2.delete(0,END)
        else:
            pass


    cmpny_hd1=Label(lf_cmpy2, text="Let's Start Building Your FinsYs",font=('Calibri 28 bold'), fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_hd1, tag=("cmpny_hd1"))

    

    nm_nm2 = Entry(cmpny_dt_frm2, width=30, font=('Calibri 16'),borderwidth=2)
    nm_nm2.insert(0,"Legal Business Name")
    nm_nm2.bind("<Button-1>",name_ent2)
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=nm_nm2, tag=("nm_nm2"))

    cmp_lbl1=Label(cmpny_dt_frm2, text="Your Industry",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl1, tag=("cmp_lbl1"))

    industry_tp= StringVar()
    cmpny_cntry = ttk.Combobox(cmpny_dt_frm2,textvariable=industry_tp,width=29,font=('Calibri 16'))
    
    cmpny_cntry['values'] = ('Accounting Services','Consultants, doctors, Lawyers and similar','Information Tecnology','Manufacturing','Professional, Scientific and Technical Services','Restaurant/Bar and similar','Retail and Smilar','Other Finanacial Services')
   
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry, tag=("cmpny_cntry"))

    cmp_lbl2=Label(cmpny_dt_frm2, text="Company type",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl2, tag=("cmp_lbl2"))

    cmp_type = StringVar()
    cmpny_cntry2 = ttk.Combobox(cmpny_dt_frm2,textvariable=cmp_type,width=29,font=('Calibri 16'))
    
    cmpny_cntry2['values'] = ('Private Limited Company','Public Limited Company','Joint-Venture Company','Partnership Firm Company','One Person Company','Branch Office Company','Non Government Organization')
    
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry2, tag=("cmpny_cntry2"))
    
    cmp_lbl3=Label(cmpny_dt_frm2, text="Do you have an Accountant, Bookkeeper or Tax Pro ?",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl3, tag=("cmp_lbl3"))

    bs_act_man=StringVar()
    r1=Radiobutton(cmpny_dt_frm2, text = "Yes", variable = bs_act_man, value ="Yes",font=('Calibri 16'))
    r1.select()
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=r1, tag=("r1"))

    r2=Radiobutton(cmpny_dt_frm2, text = "No", variable = bs_act_man, value ="No",font=('Calibri 16'))
    r2.select()
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=r2, tag=("r2"))


    cmp_lbl4=Label(cmpny_dt_frm2, text="How do you like to get paid?",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl4, tag=("cmp_lbl4"))
    
    paid_typ = StringVar()
    cmpny_cntry3 = ttk.Combobox(cmpny_dt_frm2,textvariable=paid_typ,width=29,font=('Calibri 16'))
    cmpny_cntry3['values'] = ('Cash','Cheque','Credit card/Debit card','Bank Transfer','Paypal/Other service')
   
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry3, tag=("cmpny_cntry3"))
    def prev_funct():
        main_frame_cmpny.pack(fill=X,)

    # button_cmp2 = customtkinter.CTkButton(master=cmpny_dt_frm2,command=prev_funct,text="Previous",bg="#213b52")
    # win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=button_cmp2, tag=("button_cmp2"))
    button_cmp3 = customtkinter.CTkButton(master=cmpny_dt_frm2,command=fun_sign_in,text="Submit",bg="#213b52")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=button_cmp3, tag=("button_cmp3"))
#-------------------------------------------------------------------------------------------------------------------company creation

def cmpny_crt1():
    
    first_name=fst_nm.get()
    last_name=lst_nm.get()
    email=sys_em.get()
    username=sys_usr.get()
    password=sys_pass.get()
    con_password=sys_cf.get()
    join_dt=datetime.today()
    sql_signup='select * from auth_user'
    fbcursor.execute(sql_signup)
    check_none=fbcursor.fetchone()
    global main_frame_cmpny,cmp_nm,cmp_cmpn,cmp_cty,cmp_pin,cmp_email,cmp_ph,cmp_files,cmp_stat
    if check_none is not None:
        if check_none[4]!=username and check_none[1]!=password:
            
            if password==con_password and con_password==password :
                
                signup_sql="insert into auth_user(first_name,last_name,email,username,password,date_joined) VALUES(%s,%s,%s,%s,%s,%s)" #adding values into db
                signup_sql_val=(first_name,last_name,email,username,password,join_dt,)
                fbcursor.execute(signup_sql,signup_sql_val,)
                finsysdb.commit()
                try:
                    main_frame_cmpny2.pack_forget()
                except:
                    pass
                try:
                    main_frame_signup.pack_forget()
                except:
                    pass
                
                main_frame_cmpny=Frame(root, height=750,bg="#213b52")
                main_frame_cmpny.pack(fill=X,)

                cmpny_dt_frm=Frame(main_frame_cmpny, height=650, width=500,bg="white")
                cmpny_dt_frm.pack(pady=50)

                def name_ent(event):
                    if cmp_nm.get()=="Company Name":
                        cmp_nm.delete(0,END)
                    else:
                        pass

                def cmp_add(event):
                    if cmp_cmpn.get()=="Company Address":
                            cmp_cmpn.delete(0,END)
                    else:
                        pass
                def cty_ent(event):
                    if cmp_cty.get()=="City":
                        cmp_cty.delete(0,END)
                    else:
                        pass

                def em_ent(event):
                    if cmp_email.get()=="Email":
                            cmp_email.delete(0,END)
                    else:
                        pass
                def ph_ent(event):
                    if cmp_ph.get()=="Phone Number":
                        cmp_ph.delete(0,END)
                    else:
                        pass

                def fil_ent(event):
                    sql_log_sql='select * from auth_user where username=%s'
                    vals=(sys_usr.get(),)
                    fbcursor.execute(sql_log_sql,vals)
                    check_logins=fbcursor.fetchone()
                    
                    cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
                    logo_crp=cmp_logo.split('/',-1)
                    im1 = Image.open(r""+cmp_logo) 
                    im1 = im1.save("profilepic/propic"+str(check_logins[0])+".png")
                    
                    cmp_files.delete(0,END)
                    cmp_files.insert(0,logo_crp[-1])
                
                def responsive_wid_cmp1(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
            

                    dcanvas.coords("cmpny_hd",dwidth/2,dheight/13)
                    dcanvas.coords("nm_nm",dwidth/2,dheight/5)
                    dcanvas.coords("cmp_cmpn",dwidth/2,dheight/3.5)
                    dcanvas.coords("cmp_cty",dwidth/2,dheight/2.7)
                    dcanvas.coords("cmpny_cntry",dwidth/2,dheight/2.2)
                    dcanvas.coords("cmp_pin",dwidth/2,dheight/1.85)
                    dcanvas.coords("cmp_email",dwidth/2,dheight/1.6)
                    dcanvas.coords("cmp_ph",dwidth/2,dheight/1.4)
                    dcanvas.coords("cmp_files",dwidth/2,dheight/1.25)
                    dcanvas.coords("button_cmp",dwidth/2,dheight/1.1)


                lf_cmpy1= Canvas(cmpny_dt_frm,height=650, width=500)
                lf_cmpy1.bind("<Configure>", responsive_wid_cmp1)
                lf_cmpy1.pack(fill=X)

                cmpny_hd=Label(lf_cmpy1, text="We're Happy you're Here!",font=('Calibri 30 bold'), fg="black")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_hd, tag=("cmpny_hd"))


                cmp_nm = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_nm.insert(0,"Company Name")
                cmp_nm.bind("<Button-1>",name_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_nm, tag=("nm_nm"))

                cmp_cmpn = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cmpn.insert(0,"Company Address")
                cmp_cmpn.bind("<Button-1>",cmp_add)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cmpn, tag=("cmp_cmpn"))

                cmp_cty = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cty.insert(0,"City")
                cmp_cty.bind("<Button-1>",cty_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cty, tag=("cmp_cty"))

                cmp_stat = StringVar()
                cmpny_cntry = ttk.Combobox(lf_cmpy1,textvariable=cmp_stat,width=29,font=('Calibri 16'))
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_cntry, tag=("cmpny_cntry"))
                cmpny_cntry['values'] = ('Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua And Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia And Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', 'Croatia', 'Curacao', 'Cyprus', 'Czech Republic', 'Democratic Republic Of The Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Estonia', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle Of Man', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Libyan Arab Jamahiriya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Russian Federation', 'Rwanda', 'Saint Kitts And Nevis', 'Saint Lucia', 'Saint Martin', 'Saint Pierre And Miquelon', 'Saint Vincent And The Grenadines', 'Samoa', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Taiwan', 'Tajikistan', 'Tanzania', 'Tanzania, United Republic Of', 'Thailand', 'Togo', 'Tonga', 'Trinidad And Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks And Caicos Islands', 'U.S. Virgin Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Wallis And Futuna', 'Yemen', 'Zambia', 'Zimbabwe')
                cmpny_cntry.current(0)

                cmp_pin = Spinbox(lf_cmpy1,from_=1,to=1000000,width=29, font=('Calibri 16'),borderwidth=2)
                cmp_pin.delete(0,END)
                cmp_pin.insert(0,"Pincode")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_pin, tag=("cmp_pin"))

                def validateb211(value):
        
                        """
                        Validat the email entry
                        :param value:
                        :return:
                        """
                        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                        if re.fullmatch(pattern, value) is None:
                            
                            return False

                        cmp_email.config(fg="black")
                        return True

                def on_invalidb211():
                        cmp_email.config(fg="red")
                        

                cmp_email = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_email.insert(0,"Email")
                cmp_email.bind("<Button-1>",em_ent)
                vcmdb211 = (lf_cmpy1.register(validateb211), '%P')
                ivcmdb211 = (lf_cmpy1.register(on_invalidb211),)
                cmp_email.config(validate='focusout', validatecommand=vcmdb211, invalidcommand=ivcmdb211)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_email, tag=("cmp_email"))

                cmp_ph = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_ph.insert(0,"Phone Number")
                cmp_ph.bind("<Button-1>",ph_ent)
                def validate_telb51(value):
        
                        pattern = r'^[0-9]\d{9}$'
                        if re.fullmatch(pattern, value) is None:
                            
                            return False
                        cmp_ph.config(fg="black")
                        return True

                def on_invalid_telb51():
                        cmp_ph.config(fg="red")
                        
                v_tel_cmdb51 = (lf_cmpy1.register(validate_telb51), '%P')
                iv_tel_cmdb51 = (lf_cmpy1.register(on_invalid_telb51),)
                cmp_ph.config(validate='focusout', validatecommand=v_tel_cmdb51, invalidcommand=iv_tel_cmdb51)

                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_ph, tag=("cmp_ph"))

                cmp_files = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_files.insert(0,"No file Chosen")
                cmp_files.bind("<Button-1>",fil_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_files, tag=("cmp_files"))

                button_cmp = customtkinter.CTkButton(master=lf_cmpy1,command=cmpny_crt2,text="Next",bg="#213b52")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=button_cmp, tag=("button_cmp"))
            else:
                messagebox.showerror("Sign Up Failed","password and conform password does not match")
        else:
            messagebox.showerror("Sign Up Failed","Username and password already exist")
    else:
        if password==con_password and con_password==password :
                
                signup_sql="insert into auth_user(first_name,last_name,email,username,password) VALUES(%s,%s,%s,%s,%s)" #adding values into db
                signup_sql_val=(first_name,last_name,email,username,password,)
                fbcursor.execute(signup_sql,signup_sql_val,)
                finsysdb.commit()
                try:
                    main_frame_cmpny2.pack_forget()
                except:
                    pass
                try:
                    main_frame_signup.pack_forget()
                except:
                    pass
                
                main_frame_cmpny=Frame(root, height=750,bg="#213b52")
                main_frame_cmpny.pack(fill=X,)

                cmpny_dt_frm=Frame(main_frame_cmpny, height=650, width=500,bg="white")
                cmpny_dt_frm.pack(pady=50)

                def name_ent(event):
                    if nm_nm.get()=="Company Name":
                        nm_nm.delete(0,END)
                    else:
                        pass

                def cmp_add(event):
                    if cmp_cmpn.get()=="Company Address":
                            cmp_cmpn.delete(0,END)
                    else:
                        pass
                def cty_ent(event):
                    if cmp_cty.get()=="City":
                        cmp_cty.delete(0,END)
                    else:
                        pass

                def em_ent(event):
                    if cmp_email.get()=="Email":
                            cmp_email.delete(0,END)
                    else:
                        pass
                def ph_ent(event):
                    if cmp_ph.get()=="Phone Number":
                        cmp_ph.delete(0,END)
                    else:
                        pass

                def fil_ent(event):
                    sql_log_sql='select * from auth_user where username=%s'
                    vals=(sys_usr.get(),)
                    fbcursor.execute(sql_log_sql,vals)
                    check_logins=fbcursor.fetchone()
                    cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
                    logo_crp=cmp_logo.split('/',-1)
                    im1 = Image.open(r""+cmp_logo) 
                    im1 = im1.save("profilepic/propic"+str(check_logins[0])+".png")
                    
                    cmp_files.delete(0,END)
                    cmp_files.insert(0,logo_crp[-1])
                
                def responsive_wid_cmp1(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
            

                    dcanvas.coords("cmpny_hd",dwidth/2,dheight/13)
                    dcanvas.coords("nm_nm",dwidth/2,dheight/5)
                    dcanvas.coords("cmp_cmpn",dwidth/2,dheight/3.5)
                    dcanvas.coords("cmp_cty",dwidth/2,dheight/2.7)
                    dcanvas.coords("cmpny_cntry",dwidth/2,dheight/2.2)
                    dcanvas.coords("cmp_pin",dwidth/2,dheight/1.85)
                    dcanvas.coords("cmp_email",dwidth/2,dheight/1.6)
                    dcanvas.coords("cmp_ph",dwidth/2,dheight/1.4)
                    dcanvas.coords("cmp_files",dwidth/2,dheight/1.25)
                    dcanvas.coords("button_cmp",dwidth/2,dheight/1.1)


                lf_cmpy1= Canvas(cmpny_dt_frm,height=650, width=500)
                lf_cmpy1.bind("<Configure>", responsive_wid_cmp1)
                lf_cmpy1.pack(fill=X)

                cmpny_hd=Label(lf_cmpy1, text="We're Happy you're Here!",font=('Calibri 30 bold'), fg="black")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_hd, tag=("cmpny_hd"))


                nm_nm = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
                nm_nm.insert(0,"Company Name")
                nm_nm.bind("<Button-1>",name_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=nm_nm, tag=("nm_nm"))

                cmp_cmpn = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cmpn.insert(0,"Company Address")
                cmp_cmpn.bind("<Button-1>",cmp_add)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cmpn, tag=("cmp_cmpn"))

                cmp_cty = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cty.insert(0,"City")
                cmp_cty.bind("<Button-1>",cty_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cty, tag=("cmp_cty"))

                invset_bg_var = StringVar()
                cmpny_cntry = ttk.Combobox(lf_cmpy1,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_cntry, tag=("cmpny_cntry"))
                cmpny_cntry['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
                cmpny_cntry.current(0)

                cmp_pin = Spinbox(lf_cmpy1,from_=1,to=1000000,width=29, font=('Calibri 16'),borderwidth=2)
                cmp_pin.delete(0,END)
                cmp_pin.insert(0,"Pincode")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_pin, tag=("cmp_pin"))
            

                cmp_email = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_email.insert(0,"Email")
                cmp_email.bind("<Button-1>",em_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_email, tag=("cmp_email"))

                cmp_ph = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_ph.insert(0,"Phone Number")
                cmp_ph.bind("<Button-1>",ph_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_ph, tag=("cmp_ph"))

                cmp_files = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_files.insert(0,"No file Chosen")
                cmp_files.bind("<Button-1>",fil_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_files, tag=("cmp_files"))

                button_cmp = customtkinter.CTkButton(master=lf_cmpy1,command=cmpny_crt2,text="Next",bg="#213b52")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=button_cmp, tag=("button_cmp"))
        else:
                messagebox.showerror("Sign Up Failed","password and conform password does not match")
  
#--------------------------------------------------------------------------------------------------------Sign in frame in signup section
def fun_sign_in():
    try:
        bs_nm=nm_nm2.get()
        ind_type=industry_tp.get()
        com_typ=cmp_type.get()
        acount_manage=bs_act_man.get()
        paid_type=paid_typ.get()

        sql_log_sql='select id from auth_user where username=%s'
        sql_log_sql_val=(sys_usr.get(),)
            
        fbcursor.execute(sql_log_sql,sql_log_sql_val,)
        id=fbcursor.fetchone()
        signup_cmp_sql="update app1_company set bname=%s,industry=%s,ctype=%s,abt=%s,paid=%s  where id_id=%s" #adding values into db
        signup_cmp_sql_val=(bs_nm,ind_type,com_typ,acount_manage,paid_type,id[0],)
        fbcursor.execute(signup_cmp_sql,signup_cmp_sql_val,)
        finsysdb.commit()
    except:
        pass


    try:
        main_frame_signup.pack_forget()
    except:
        pass
    try:
        main_frame_cmpny2.pack_forget()
    except:
        pass

    main_frame_signin.pack(fill=X,)
    
#---------------------------------------------------------------------------------------------------------------------Sign Up Section
def func_sign_up():
    
    global main_frame_signup,fst_nm,lst_nm,sys_em,sys_usr,sys_pass,sys_cf
    main_frame_signin.pack_forget()

    main_frame_signup=Frame(root, height=750)
    main_frame_signup.pack(fill=X,)

    def responsive_wid_signup(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("round_signup",dwidth/2,-dheight/.5,dwidth/.7,dheight/.5)
        dcanvas.coords("sign_in_lb",dwidth/6,dheight/12)
        dcanvas.coords("fst_nm",dwidth/8.5,dheight/5)
        dcanvas.coords("lst_nm",dwidth/8.5,dheight/3.5)
        dcanvas.coords("sys_em",dwidth/8.5,dheight/2.7)
        dcanvas.coords("sys_usr",dwidth/8.5,dheight/2.2)
        dcanvas.coords("sys_pass",dwidth/8.5,dheight/1.85)
        dcanvas.coords("sys_cf",dwidth/8.5,dheight/1.6)
        dcanvas.coords("button_sign",dwidth/6,dheight/1.4)
        dcanvas.coords("lft_lab",dwidth/1.4,dheight/18)
        dcanvas.coords("lft_lab2",dwidth/1.52,dheight/10)
        dcanvas.coords("btn_signup2",dwidth/1.36,dheight/6.6)
        dcanvas.coords("label_img",dwidth/1.8,dheight/5)
        
        


    lf_signup= Canvas(main_frame_signup,width=1500, height=1500)
    lf_signup.bind("<Configure>", responsive_wid_signup)
    lf_signup.pack(fill=X)

    lf_signup.create_oval(0,0,0,0,fill="#213b52", tag=("round_signup"))

    # #--------------------------------------------------------------------------------sign up section
    sign_in_lb=Label(lf_signup, text="Sign Up",font=('Calibri 30 bold'), fg="black")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sign_in_lb, tag=("sign_in_lb"))

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
            messagebox.showerror("Password Format","The password length must be greater than or equal to 8 \n>The password must contain one or more uppercase characters\n>The password must contain one or more lowercase characters\n>The password must contain one or more numeric values\n>The password must contain one or more special characters")
        else:
            pass
    
    def nme5(event):
        if sys_cf.get()=="Confirm Password":
            sys_cf.delete(0,END)
        else:
            pass
    
    

    fst_nm = Entry(lf_signup, width=25, font=('Calibri 16'))
    fst_nm.insert(0,"Firstname")
    fst_nm.bind("<Button-1>",nme)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=fst_nm, tag=("fst_nm"))

    lst_nm = Entry(lf_signup,  width=25, font=('Calibri 16'))
    lst_nm.insert(0,"Lastname")
    lst_nm.bind("<Button-1>",nme1)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lst_nm, tag=("lst_nm"))

    
    sys_em = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_em.insert(0,"Email")
    sys_em.bind("<Button-1>",nme2)
    def validateb211(value):
        
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value) is None:
                            
            return False

        sys_em.config(fg="black")
        return True

    def on_invalidb211():
        
        sys_em.config(fg="red")

    vcmdb211 = (lf_signup.register(validateb211), '%P')
    ivcmdb211 = (lf_signup.register(on_invalidb211),)
    sys_em.config(validate='focusout', validatecommand=vcmdb211, invalidcommand=ivcmdb211)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_em, tag=("sys_em"))

    sys_usr = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_usr.insert(0,"Username")
    sys_usr.bind("<Button-1>",nme3)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_usr, tag=("sys_usr"))

    sys_pass = Entry(lf_signup, width=25, font=('Calibri 16'),)
    sys_pass.insert(0,"Password")
    sys_pass.bind("<Button-1>",nme4)
    def pas_val_fun(value):
        
        pattern = r'(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
        if re.fullmatch(pattern, value) is None:
                            
            return False

        sys_pass.config(fg="black")
        return True

    def pass_inval_fun():
        sys_pass.config(fg="red")

    pas_val = (lf_signup.register(pas_val_fun), '%P')
    pass_inval = (lf_signup.register(pass_inval_fun),)

    sys_pass.config(validate='focusout', validatecommand=pas_val, invalidcommand=pass_inval)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_pass, tag=("sys_pass"))

    sys_cf = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_cf.insert(0,"Confirm Password")
    sys_cf.bind("<Button-1>",nme5)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_cf, tag=("sys_cf"))

    button_sign = customtkinter.CTkButton(master=lf_signup, command=cmpny_crt1,text="Sign Up",bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=button_sign, tag=("button_sign"))

    label_img = Label(lf_signup, image = sign_up,bg="#213b52", width=800,anchor="w")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=label_img, tag=("label_img"))
    
    

    lft_lab=Label(lf_signup, text="One of us ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab, tag=("lft_lab"))
    lft_lab2=Label(lf_signup, text="click here for work with FinsYs.",font=('Calibri 16 bold'), fg="white", bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab2, tag=("lft_lab2"))

    btn_signup2 = Button(lf_signup, text='Sign In', command=fun_sign_in, bg="white", fg="black",borderwidth = 3,height=1,width=10)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=btn_signup2, tag=("btn_signup2"))


main_frame_signin=Frame(root, height=750)
main_frame_signin.pack(fill=X,)


def sig_nm(event):
        if nm_ent.get()=="Username":
            nm_ent.delete(0,END)
        else:
            pass

def sig_pass(event):
        if pass_ent.get()=="********":
            pass_ent.delete(0,END)
        else:
            pass


def responsive_wid_login(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("sign_inlb",dwidth/1.4,dheight/4)

        dcanvas.coords("nm_ent",dwidth/1.5,dheight/2.7)
        dcanvas.coords("pass_ent",dwidth/1.5,dheight/2.2)
        dcanvas.coords("button",dwidth/1.4,dheight/1.8)
        dcanvas.coords("round_login",-dwidth/2,-dheight/.5,dwidth/2,dheight/.5)
        dcanvas.coords("lft_lab",dwidth/4,dheight/18)
        dcanvas.coords("lft_lab2",dwidth/6,dheight/10)
        dcanvas.coords("btn2",dwidth/3.7,dheight/6.6)
        dcanvas.coords("img",dwidth/16,dheight/5.5)
    

lf_signup= Canvas(main_frame_signin,width=1366,height=750)
lf_signup.bind("<Configure>", responsive_wid_login)
lf_signup.pack(fill=X)

sign_inlb=Label(lf_signup, text="Sign In",font=('Calibri 30 bold'), fg="black")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sign_inlb, tag=("sign_inlb"))

nm_ent = Entry(lf_signup, width=25, font=('Calibri 16'))
nm_ent.insert(0,"Username")
nm_ent.bind("<Button-1>",sig_nm)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=nm_ent, tag=("nm_ent"))

pass_ent = Entry(lf_signup, width=25, font=('Calibri 16'),show="*")
pass_ent.insert(0,"********")
pass_ent.bind("<Button-1>",sig_pass)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=pass_ent, tag=("pass_ent"))

button = customtkinter.CTkButton(master=main_frame_signin,command=main_sign_in,text="Log In",bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=button, tag=("button"))

# #------------------------------------------------------------------------------------------------------------------------left canvas

lf_signup.create_oval(0,0,0,0,fill="#213b52", tag=("round_login"))

img = Label(lf_signup, image = exprefreshIcon,bg="#213b52", width=500, justify=RIGHT)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=img, tag=("img"))

lft_lab=Label(lf_signup, text="New here ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab, tag=("lft_lab"))
lft_lab2=Label(lf_signup, text="Join here to start a business with FinsYs!",font=('Calibri 16 bold'), fg="white", bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab2, tag=("lft_lab2"))

btn2 = Button(main_frame_signin, text = 'Sign Up', command = func_sign_up, bg="white", fg="black",borderwidth = 3,height=1,width=10)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=btn2, tag=("btn2"))

root.mainloop()