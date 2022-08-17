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
resized_flow= cash_fl.resize((620,680))
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
                                                print(pro_new_pass)
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
                    sql_incomes="select sum(balance) from app1_accounts1 where cid_id=%s and detype='Income'"
                    sql_incomes_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_incomes,sql_incomes_val,)
                    incom_dtls=fbcursor.fetchone()
                    
                    if incom_dtls[0]==None or incom_dtls[0]=='':
                        tot_inc=0.0
                    else:
                        tot_inc=incom_dtls[0]
                    
                
                    #-----------------------------------------------------expense
                    sql_pro="select sum(balance) from app1_accounts1 where cid_id=%s and detype='Expenses'"
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

                    sql_pro="select sum(balance) from app1_accounts1 where cid_id=%s and detype='Expenses'"
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

                    sql_typ="select balance from app1_accounts1 where cid_id=%s and detype='Expenses'"
                    sql_typ_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_typ,sql_typ_val,)
                    exp_typ=fbcursor.fetchall()

                    sql_typs="select name from app1_accounts1 where cid_id=%s and detype='Expenses'"
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

                    sql_income="select sum(balance) from app1_accounts1 where cid_id=%s and detype='Income'"
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

                    sql_income_chart="select balance,name from app1_accounts1 where cid_id=%s and detype='Income'"
                    sql_income_chart_val=(dtl_cmp_pro[0],)
                    fbcursor.execute(sql_income_chart,sql_income_chart_val,)
                    incom_chart=fbcursor.fetchall()
                    
                    try:
                        sizes = []
                        for i in incom_chart:
                            sizes.append(i[0])
                    except:
                        sizes=0
                    sql_lb_chart="select name from app1_accounts1 where cid_id=%s and detype='Income'"
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
                        y2 = dheight/.10


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
                        
     
                    fin_cash_analiz.grid_rowconfigure(0,weight=1)
                    fin_cash_analiz.grid_columnconfigure(0,weight=1)

                    frm_analiz = Canvas(fin_cash_analiz,height=700,bg='#2f516f',scrollregion=(0,0,700,1200))
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
                    
                    dat_type['values'] = ('All Dates','Custom', 'Today', 'This Month','This Financial Year')
                    dat_type.bind('<<ComboboxSelected>>', "chart_tp_slt")
                    dat_type.current(0)
                
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=dat_type, tag=("cmb_bx"))

                    button15 = customtkinter.CTkButton(master=frm_analiz,command=main_sign_in,text="Run Report",bg="#213b52")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=button15, tag=("button15"))

                    button25 = customtkinter.CTkButton(master=frm_analiz,command=main_sign_in,text="Back",bg="#213b52")
                    win_inv1 = frm_analiz.create_window(0, 0, anchor="nw", window=button25, tag=("button25"))

                    

                    rth2 = frm_analiz.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_anal3"),smooth=True,)

                    fgth = ttk.Style()
                    fgth.theme_use("default")
                    fgth.configure("Treeview", background="#2f516f", foreground="white",fieldbackground="#2f516f",rowheight=25,font=(None,11))
                    fgth.configure("Treeview.Heading",background="#1b3857",activeforeground="black",foreground="white",font=(None,11))  

                    pro_tree = ttk.Treeview(frm_analiz, columns = (1,2,3,4,5,6,7,8),show = "headings")
                    # pro_tree.pack(side = 'top')
                    pro_tree.heading(1)
                    pro_tree.heading(2, text="[Month]")
                    pro_tree.heading(3, text="[Month]")
                    pro_tree.heading(4, text="[Month]")
                    pro_tree.heading(5, text="[Month]")
                    pro_tree.heading(6, text="[Month]")
                    pro_tree.heading(7, text="[Month]")
                    pro_tree.heading(8, text="TOTAL")
                    
                    pro_tree.column(1, width = 300)
                    pro_tree.column(2, width = 125)
                    pro_tree.column(3, width = 125)
                    pro_tree.column(4, width = 125)
                    pro_tree.column(5, width = 125)
                    pro_tree.column(6, width = 125)
                    pro_tree.column(7, width = 125)
                    pro_tree.column(8, width = 200)
                    window_label_4 = frm_analiz.create_window(0, 0, anchor="nw", window=pro_tree,tags=('ptree1'))


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
                        y2 = dheight/.55

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
                        dcanvas.coords("nm_nm21",dwidth/2 ,dheight/1.25) 
                        dcanvas.coords("hd_lb_hds",dwidth/1.8 ,dheight/1.3) 
                        dcanvas.coords("nm_nm251",dwidth/1.5 ,dheight/1.25) 
                        dcanvas.coords("hd_fl_lb",dwidth/1.41 ,dheight/1.3) 
                        
                        dcanvas.coords("nm_nm241",dwidth/1.2 ,dheight/1.25)
                        dcanvas.coords("lb_nm241",dwidth/1.15 ,dheight/1.3)
                
                        

                    fin_cash_flow.grid_rowconfigure(0,weight=1)
                    fin_cash_flow.grid_columnconfigure(0,weight=1)

                    frm_flow = Canvas(fin_cash_flow,height=700,bg='#2f516f',scrollregion=(0,0,700,1200))
                    flow_scrl = Scrollbar(fin_cash_flow,orient=VERTICAL)
                    flow_scrl.grid(row=0,column=1,sticky='ns')
                    flow_scrl.config(command=frm_flow.yview)
                    frm_flow.bind("<Configure>", res_wid_flow)
                    frm_flow.config(yscrollcommand=flow_scrl.set)
                    frm_flow.grid(row=0,column=0,sticky='nsew')

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

                    lv_name=Label(frm_flow, text="Account",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                    win_inv1 = frm_flow.create_window(0, 0, anchor="center", window=lv_name,tag=("hd_fl_hde"))

                    chrt_flow= StringVar()
                    glt_type = ttk.Combobox(frm_flow,textvariable=chrt_flow,width=55,font=('Calibri 16'))
                    glt_type['values'] = ('All Dates','Custom', 'Today', 'This Month','This Financial Year')
                    glt_type.bind('<<ComboboxSelected>>', "chart_tp_slt")
                    glt_type.current(0)
                    win_inv1 = frm_flow.create_window(0, 0, anchor="nw", window=glt_type, tag=("cmb_bx_fl"))

                    lv_name=Label(frm_flow, text="Enter the following from your statement.",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                    win_inv1 = frm_flow.create_window(0, 0, anchor="center", window=lv_name,tag=("hd_fl_hds"))

                    frm_flow.create_line(0, 0, 0, 0,fill="gray", tag=("hd_fl_hrs") )

                    lv_name=Label(frm_flow, text="Beginning balance",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                    win_inv1 = frm_flow.create_window(0, 0, anchor="center", window=lv_name,tag=("hd_lb_hds"))

                    nm_nm21 = Spinbox(frm_flow, width=15 ,from_=1,to=1000000, font=('Calibri 16'),borderwidth=2)
                    win_inv1 = frm_flow.create_window(0, 0, anchor="nw", window=nm_nm21, tag=("nm_nm21"))

                    lv_name=Label(frm_flow, text="Ending balance",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                    win_inv1 = frm_flow.create_window(0, 0, anchor="center", window=lv_name,tag=("hd_fl_lb"))
                    nm_nm251 = Spinbox(frm_flow, width=15 ,from_=1,to=1000000, font=('Calibri 16'),borderwidth=2)
                    win_inv1 = frm_flow.create_window(0, 0, anchor="nw", window=nm_nm251, tag=("nm_nm251"))
                    
                    lv_name=Label(frm_flow, text="Ending date",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                    win_inv1 = frm_flow.create_window(0, 0, anchor="center", window=lv_name,tag=("lb_nm241"))
                    nm_nm241 = Entry(frm_flow,width=15 , font=('Calibri 16'),borderwidth=2)
                    win_inv1 = frm_flow.create_window(0, 0, anchor="nw", window=nm_nm241, tag=("nm_nm241"))


                    
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