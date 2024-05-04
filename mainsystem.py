from tkinter import *
import tkinter.messagebox as msg
import tkinter as tk
from tkinter import ttk
import mysql.connector as conn
import re
from tktooltip import ToolTip
from PIL import Image,ImageTk
import cv2
import numpy as np
import os
from datetime import datetime, time, timedelta, timezone
import csv
import random


class facerecognitionattendancesys:
#  todo :  login page 
     def loginpage(self):   
        #   childwindows = tk.Tk()
          childwindows.geometry("1430x820+0+0")
          childwindows.title("Login Page")
          
           # todo: set background image  
          bgimage = Image.open("C:\\Projectwork\\images\\technology.png") 
          bgimagere = bgimage.resize((int(bgimage.width * 0.2), int(bgimage.height * 0.3) ) )
          bgimg = ImageTk.PhotoImage(bgimagere)
          bg = tk.Label(childwindows, image=bgimg)
          bg.photo = bgimg
          bg.place(x=0, y=0, width=1500, height=830)
          
          login_frame = tk.Frame(childwindows,bg="#050051", relief='ridge', border=15)
          login_frame.place(x=435, y=150, width=600, height=400)
          
          loginlbl = tk.Label(childwindows, text="Login", font=("arial",15), bg="#050051", fg="white")
          loginlbl.place(x=670, y=170, width=90, height=30)

          # todo: -----------------> username textbox <-----------------------------------------------------  
          login_lbl_user = tk.Label(childwindows, text="Username", bg="#050051", fg="white", font="cambria 15")
          login_lbl_user.place(x=655, y=240, width="100", height=20)
          
          #todo: username in not allow digit

          def on_validate(Value, reason, widget):
              is_alpha = Value.isalpha() or Value ==""
              if is_alpha:
                  usernamemessagelbl.config(text="")
              else:
                  usernamemessagelbl.config(text="Digit are not allow in username", fg="red")
              return is_alpha
        
          valid = childwindows.register(on_validate)
          
          usernamemessagelbl = tk.Label(childwindows, text="", font=("arial",8), bg="#050051")
          usernamemessagelbl.place(x=660, y=290, width="200", height="20")
            
          login_txtbox_user = tk.Entry(childwindows, relief="solid", font="arial 17", validate='key', validatecommand=(valid, '%P','%d','%W') )
          login_txtbox_user.place(x=655, y=260, width=220, height=30)
          loginuser = ToolTip(login_txtbox_user, "Enter Username (e.g. staff) only allowed string(5 length)")
          login_txtbox_user.bind('<KeyPress>',lambda event: [ on_validate ,usermaxlen(login_txtbox_user, 5, usernamemessagelbl), ] )
          login_txtbox_user.bind("<Tab>", lambda event: on_entry_tabkey(event))
          
          #todo: username are blank, no move next field    ---------------------------------------------------------------------------------- 
          def validate_username(event):
                user = login_txtbox_user.get()
                if not user:
                    usernamemessagelbl.config(text="Username cannot be empty!", fg="red")
                    return False
                elif not re.match(r"^[a-zA-Z]{5,}$", user):
                    usernamemessagelbl.config(text="Invalid Username", fg="red")
                    return False
                else:
                    usernamemessagelbl.config(text="Valid Username", fg="green")
                    return True
          def on_entry_tabkey(event):
              if not validate_username(event):
                  return "break"
          #todo:  ----------------------------------------------------------------------------------------------------------------------------- 
        
          def usermaxlen(entry, max_length, usernamemessagelbl):
                  text = entry.get()
                  if len(text) > max_length:
                      entry.delete(max_length, "end")
                      usernamemessagelbl.configure(text=f"Username Maximum {max_length} character Allowed", fg="red")
                  else:
                      usernamemessagelbl.configure(text="", fg="green")
          # todo: |_______________________________________________________________________________________________________________________________________| 

          # todo: ---------------> password textbox <-----------------------------------------------------------------------------|
          login_lbl_pass = tk.Label(text="Password", bg="#050051", fg="white", font="cambria 15")
          login_lbl_pass.place(x=655, y=310, width=100, height=27)

          passwordmessagelbl = tk.Label(childwindows, text="", font=("arial",7), bg="#050051")
          passwordmessagelbl.place(x=660, y=365, width=300, height=20)  
         
          login_txtbox_pass = tk.Entry(relief="solid", font="arial 17",show="*")
          login_txtbox_pass.place(x=655, y=335, width=220, height=28)
          loginpassw = ToolTip(login_txtbox_pass,f"Enter Password (e.g.'staff1_123') only allowed[5 char, 1 Special Character, 4 digit]")
          # login_txtbox_user.bind('<KeyRelease>', loginpassw )
          login_txtbox_pass.bind("<KeyPress>", lambda event: passmaxlen(login_txtbox_pass, 10, passwordmessagelbl), loginpassw)
          login_txtbox_pass.bind("<Tab>", lambda event: on_entry_tab_username(event) )
          
          def validate_password(event):
                passw = login_txtbox_pass.get()
                if not passw:
                    passwordmessagelbl.config(text="Password Cannot be empty", fg="red")
                    return False
                
                elif passw == passw and len(passw) <= 10:
                    passwordmessagelbl.config("Valid Password", fg="green")
                    return True
                
                elif not re.match(r"^[a-z0-9_]{10,}$", passw):
                    passwordmessagelbl.config(text="Password invalid", fg="red")
                    return False
                else:
                    passwordmessagelbl.config(text="Valid Password", fg="green")
                    return True
          def on_entry_tab_username(event):
              if not validate_password(event):
                  return "break"

          def passmaxlen(entry, max_length, passwordmessagelbl):
              text = entry.get()
              if len(text) > max_length:
                  entry.delete(max_length, "end")
                  passwordmessagelbl.config(text=f"Password Maximum {max_length} Allowed(1 special character, 4 digit, 5 character)", fg="red")
              else:
                  passwordmessagelbl.config(text="", fg="green")
          #todo:--------------------------------------------------------------------------------------------------------| 

          def hide_password():
                if login_txtbox_pass['show'] == "*":
                    login_txtbox_pass['show'] = ""
                    show_password_button.config(image=eye_open_img)
                else:
                    login_txtbox_pass['show'] = "*"
                    show_password_button.config(image=eye_close_img)    

          eye_open_img = ImageTk.PhotoImage(Image.open("C:\\Projectwork\\images\\openeye.png").resize((22, 22)))
          eye_close_img = ImageTk.PhotoImage(Image.open("C:\\Projectwork\\images\\closeeye.png").resize((22, 22)))
          
          show_password_button = tk.Button(childwindows, image=eye_close_img, command=hide_password, bd=0, bg="white", activebackground='white')
          show_password_button.place(x=840, y=340, width=30, height=20)

          # todo: login button <------------------------------------------------------|
          login_btn = tk.Button(text="Login", relief="groove", border=10, borderwidth=5, fg="maroon", cursor="hand2" ,command= lambda : loginpage_validation() )
          login_btn.place(x=680, y=420, width=80, height=40)
          login_btn.bind("<Return>", lambda event: loginpage_validation())
          
          def loginpage_validation():
          #todo: validation of loginpage
                    user = login_txtbox_user.get()
                    passw = login_txtbox_pass.get()

                    if not user==user:
                        usernamemessagelbl.configure(text=f"Wrong username", fg="red")
    
                    if not passw == passw:
                        ps = passwordmessagelbl.configure(text=f"Wrong password", fg="red")   
                        passwordmessagelbl.bind("<Tab>", ps)
   
                    if user=="" or passw=="":
                        msg.showerror(title="Error", message="Username or Password are Required, Please Fill Username Or Password")    
                    else:
                      try:
                         con = conn.connect(host="localhost", username="root", password="", database="facerecognitionattendancesystem")
                         cur = con.cursor()
                      except:
                          msg.showerror("Error", "Database connectivity issue, Please try again")
                          return
                      query = "use facerecognitionattendancesystem"
                      cur.execute(query)
                      query = "select * from admin where username=%s and password=%s"
                      cur.execute(query, (user,passw))
                      row = cur.fetchone()
                      if row==None:
                           msg.showerror("Error","invalid Username or Password")
                      else:
                          usernamemessagelbl.configure(text="valid username", fg="green")
                          passwordmessagelbl.configure(text="valid password", fg="green")
                          msg.showinfo("Success","Login Successful...")
                          opensystem()
                                                
                          
                         
         
          # todo: reset button <--------------------------------------------------------|
          reset_btn = tk.Button(text="Reset", relief="groove", border=10, borderwidth=5, fg="maroon", cursor='hand2', command= lambda: resetfield())
          reset_btn.place(x=790, y=420, width=80, height=40)
          reset_btn.bind("<Return>", lambda event: resetfield() )
          def resetfield():
                    login_txtbox_user.delete(0, "end")
                    login_txtbox_pass.delete(0, "end")
                        
          def opensystem():
             childwindows.destroy()
             GUI(self)
              
          def GUI(self):
                 childwindow = tk.Tk()
                 childwindow.geometry("1430x820+0+0")
                 childwindow.title("Face Recognition Attendance System")
               
               #todo: Image for background    
                 path = "C:\\Projectwork\\images\\facerecognitionre.png"
                 mainbg = Image.open(path)
                 img1 = mainbg.resize((int(mainbg.width * 0.4), int(mainbg.height * 0.4)))
                 img = ImageTk.PhotoImage(img1)
                 imglbl = tk.Label(childwindow, image=img)
                 imglbl.photo = img
                 imglbl.place(x=0,y=0, width=1520, height=840) 
                         
                 
               
                 # todo: this function to work student registration    
                 def module1():
                     studentregister()
                     
                 # todo: this function to work face detector    
                 def module2():
                     facerecognition()
                  
                 # todo: this function to work train dataset images 
                 def module3():
                     traindataset()
                     
                 # todo: this function to work manyimages store    
                 def module4():
                     manyimages()
                 
                 # todo: this function to work attendance record     
                 def module5():
                     attendance()
                
                 def module6():
                     help()   
                        
                 def module7():
                     aboutus()       
                     
               
            #    todo: create database and table 
            #    con = conn.connect(host="localhost", user="root", password="",)
            #    cur = con.cursor()
            #    cur.execute("create database facerecognitionattendancesystem")
            #    cur.execute("use facerecognitionattendancesystem")
               
               # todo: implement individual module --------------------------------------------------------------------------------------------------------|          
               
                 colorfrm = tk.Frame(childwindow, bg="#020730")
                 colorfrm.place(x=0, y=0, width=140, height=840)
                 
                 forgotbtn = tk.Button(childwindow, text="Forgot Password?" , font=("new times roman", 12), fg="white", bg="#020730", activebackground="#020730", activeforeground="white", cursor='hand2' ,bd=0, command= lambda : forgotpassw())
                 forgotbtn.place(x=5, y=780, width=130, height=45)          
                 def forgotpassw():
                          forgotfrm = tk.Tk()
                          forgotfrm.title("Forgot Your Password")

                          forgotfrm.minsize(400,500)
                          forgotfrm.maxsize(400,500)
                          forgotfrm.configure(bg="salmon")
        
                          forget_lbl_user = tk.Label(forgotfrm, text="Username", bg="salmon", fg="white", relief="flat", font="cambria 15")
                          forget_lbl_user.place(x=110, y=55, width=87, height=30)

                          forgotusermessage = tk.Label(forgotfrm, text="", font=("arial",10), bg="salmon")
                          forgotusermessage.place(x=110, y=115, width=200, height=30)

                          def forget_hide_newpass():
                              if  forget_txtbox_newpass['show']=="*":
                                   forget_txtbox_newpass['show']=""
                              else:
                                   forget_txtbox_newpass['show']="*"

                          def usernamevalidation(value, reason):
                                   max_length = 5

                                   if not value.isdigit() and len(value) <= max_length:
                                       return True 
                                   else:
                                       return False
                                   
                                   
                          validuser = forgotfrm.register(usernamevalidation)                  
                          forget_txtbox_user = tk.Entry(forgotfrm, font=("arial", 16), validate='key', validatecommand=(validuser, '%P', '%S'))
                          forget_txtbox_user.place(x=110, y=80, width=200, height=30)
                          forget_txtbox_user.bind('<KeyPress>',lambda event: [ usernamevalidation ] )
                          forget_txtbox_user.bind("<Tab>", lambda event: [ usernamevalidation])

                          forgot_new_pass_hide = tk.Checkbutton(forgotfrm, text="show password", bg="salmon", activebackground="salmon", command = lambda:forget_hide_newpass())
                          forgot_new_pass_hide.place(x=110, y=205, width=103, height=30)

                          def password_maxlength(value):
                              max_len = 10
                              return len(value) <= max_len

                          forget_lbl_new_pass = tk.Label(forgotfrm, text="New Password", bg="salmon", fg="white", relief="flat", font="cambria 15")
                          forget_lbl_new_pass.place(x=110, y=150, width=125, height=30)

                          valid = forgotfrm.register(password_maxlength)
                          forget_txtbox_newpass = tk.Entry(forgotfrm, font="arial 16", show="*" , validate='key', validatecommand=(valid, '%P'))
                          forget_txtbox_newpass.place(x=110, y=175, width=200, height=30)

                          def forget_con_pass(): 
                              if  forget_txtbox_con_pass['show']=="*":
                                  forget_txtbox_con_pass['show']=""
                              else:
                                  forget_txtbox_con_pass['show']="*"    

                          forgot_con_pass = tk.Checkbutton(forgotfrm, text="show password", bg="salmon", activebackground="salmon", command= lambda : forget_con_pass())
                          forgot_con_pass.place(x=110, y=315, width=100, height=30)

                          forget_lbl_con_pass = tk.Label(forgotfrm, text="Confirm Password", bg="salmon", fg="white", relief="flat", font="cambria 15")
                          forget_lbl_con_pass.place(x=110, y=260, width=160, height=30)
                          def confpasswordvalidation(value):
                              max_len = 10
                              return len(value) <= max_len
                          

                          validcon = forgotfrm.register(confpasswordvalidation)
                          forget_txtbox_con_pass = tk.Entry(forgotfrm, font="arial 16", show="*", validate='key', validatecommand=(validcon, '%P')) 
                          forget_txtbox_con_pass.place(x=110, y=285, width=200, height=30)

                          forgot_btn = tk.Button(forgotfrm, text="Forgot Password", relief='raised', border=5, fg="maroon",activebackground="maroon" ,activeforeground="white",command=lambda event=None: [ forgotpassword(),] )
                          forgot_btn.place(x=110, y=450, width=100,  height=30)         

                          def forgotpassword():
                                    special_ch = ['_',]
                                    if forget_txtbox_user.get()=="" or forget_txtbox_newpass.get()=="" or forget_txtbox_con_pass.get()=="":
                                        msg.showerror("Error", "All Fields are Required!", parent=forgotfrm)
                                    elif not any(ch in special_ch for ch in forget_txtbox_newpass):
                                          msg.showwarning('WARNING','At least 1 Special Character ( _ ) Required!')
                                    elif sum(1 for ch in forget_txtbox_newpass if ch.isupper() or ch.islower()) < 5:
                                          msg.showwarning('WARNING','At least 5 upper or lower case characters required!')
                                    elif sum(1 for ch in forget_txtbox_newpass if ch.isdigit()) < 4:
                                          msg.showwarning('WARNING','At least 4 numbers required!')
                                    elif len(forget_txtbox_newpass) < 10:
                                          msg.showwarning('Length!','Password must be Maximum of 10 characters!')
                                    elif forget_txtbox_newpass != forget_txtbox_con_pass.get():
                                          msg.showerror("Error", "New Password and Confirm Password Do Not Match!")
                                    elif forget_txtbox_newpass.get() != forget_txtbox_con_pass.get():
                                        msg.showerror("Error", "Password and Confirm Password Does not Match", parent=forgotfrm)
                                    else:
                                         con = conn.connect(host="localhost", user="root", password="", db="facerecognitionattendancesystem")
                                         cur = con.cursor()
                                         forgt = "UPDATE admin SET password=%s WHERE username=%s"
                                         query = (forget_txtbox_newpass.get(), forget_txtbox_user.get())
                                         try:
                                             cur.execute(forgt,(query))
                                             con.commit()
                                             msg.showinfo("Success", "Your Password Change Successful..", parent=forgotfrm)
                                             con.close()
                                         except Exception as rs:
                                             msg.showerror("Error", f"Due To:{rs}", parent=forgotfrm)
      
      
                          forgot_btn_reset = tk.Button(forgotfrm, text="Reset", relief='raised', border=5, fg="maroon",activebackground="maroon" ,activeforeground="white", command= lambda :  forgotreset())
                          forgot_btn_reset.place(x=240, y=450, width=70, height=30)

                          def forgotreset():
                              forget_txtbox_user.delete(0, "end")
                              forget_txtbox_newpass.delete(0, "end")
                              forget_txtbox_con_pass.delete(0, "end")


                          forgotfrm.mainloop() 
               
               
               
                 firstmodule = tk.Button(childwindow, bd=4 ,text="Student Registration", font=("arial", 10), relief="flat", command= lambda  : module1(), cursor="hand2" )
                 firstmodule.place(x=5, y=60, width=125, height=40)
                 firstmodule.bind('<Return>', lambda  : module1())
                 
                 secondmodule = tk.Button(childwindow,  bd=4 , text="face recognition", font=("arial", 10), relief="flat", command= lambda : module2(),  cursor="hand2" )
                 secondmodule.place(x=5, y=120, width=125, height=40)
                 secondmodule.bind('<Return>', lambda : module2())
                 
                 thirdmodule = tk.Button(childwindow,  bd=4 , text="Train Data set", font=("arial", 10), relief="flat", command= lambda : module3(),  cursor="hand2")
                 thirdmodule.place(x=5, y=180, width=125, height=40)
                 thirdmodule.bind('<Return>', lambda  : module3())
                 
                 fourmodule = tk.Button(childwindow,  bd=4 ,text="Images", font=("arial", 10), relief="flat" , cursor="hand2", command= lambda : module4())
                 fourmodule.place(x=5, y=240, width=125, height=40)
                 fourmodule.bind('<Return>', lambda  : module4())
                 
                 fivemodule = tk.Button(childwindow,  bd=4 ,text="Attendance",  font=("arial", 10), relief="flat" , cursor="hand2", command= lambda : module5())
                 fivemodule.place(x=5, y=300, width=125, height=40)
                 fivemodule.bind('<Return>', lambda  : module5())
                          
                 sixmodule = tk.Button(childwindow ,  bd=4 ,text="Help", font=("arial", 10), relief="flat" , cursor="hand2", command= lambda : module6())
                 sixmodule.place(x=5, y=360, width=125, height=40)
                 sixmodule.bind('<Return>', lambda  : module6())
                 
                 sevenmodule = tk.Button(childwindow ,  bd=4 ,text="About Us", font=("arial", 10), relief="flat" , cursor="hand2", command= lambda : module7())
                 sevenmodule.place(x=5, y=450, width=125, height=40)
                 sevenmodule.bind('<Return>', lambda  : module7())
               
               #todo:--------------------------------------------Ending-------------------------------------------------------------------------------------------|    
               
               
                # todo: Student Registration
                 def studentregister():
                              # todo: logic of Student Registration <-------------------Start---------------------------------------------------------------------|
                              
                              
                              path = "C:\\Projectwork\\imagepro\\new\\4884273.jpg"
                              mainbg = Image.open(path)
                              img1 = mainbg.resize((int(mainbg.width * 0.6), int(mainbg.height * 0.6)))
                              img = ImageTk.PhotoImage(img1)
                              studentfrm1 = tk.Label(childwindow, image=img )
                              imglbl.photo = img
                              studentfrm1.place(x=0, y=0, width=1440+0, height=830+0)
                              
                              back1 = tk.Button(studentfrm1, text="Back", font=("arial", 12), command= lambda : exitmodule1(), cursor='hand2')
                              back1.place(x=15, y=30, width=100, height=50)
                              def exitmodule1():
                                   studentfrm1.destroy()
                                   
                              titlefrm = tk.Frame(studentfrm1, bg="green")
                              titlefrm.place(x=0, y=82, width=1440, height=8)     
                              
                              #todo: college details fields ---------start-----------------------------------------------------------------|    
                              frm = tk.LabelFrame(studentfrm1, text="College Detail", bg="white")
                              frm.place(x=1, y=95, width=870 , height=400)
                              
                              deptnamelbl = tk.Label(studentfrm1, text="College-Name", font=("cambria", 11), bg="white")
                              deptnamelbl.place(x=20, y=155, width=120, height=25)
                              
                              def nametocourse(event):
                                  selectname = dept_name.get()
                                  dept_courses.set('')
                               #    dept_courses['values'] = []
                                  
                                  if selectname == "Shree P.M. Patel College of Computer Science & Technology":
                                      dept_courses['values'] = ['BCA', 'MSC(CS)', "MSC(IT)", "PGDCA"]
                                   #    dept_courses['values'] = ['BCA','IT', 'CS', "MSC(IT)", "PGDCA"]
                                  elif selectname ==  "Smt J. B. Patel College Of Commerce Stuides And Research, Anand":
                                      dept_courses['values'] = ["BCom(Guj)","BCom(Eng)"]
                                  elif selectname == "Arts College":
                                      dept_courses['values'] = ['BA', 'MA']
                                  elif selectname == "Shree P.M. Patel Institute of Business Administration":
                                      dept_courses["values"] = ["BBA(Gen)", "BBA(ITM)", "BBA(ISM)"]
                                  elif selectname == "Smt. Jayaben B. Patel Post Graduate Institute Of Business Studies & Research":
                                       dept_courses['values'] = ['Mcom', 'MoEM&PR']
                                  elif selectname ==  "Shree P.M. Patel Institute of Biosciences":  
                                       dept_courses['values'] = ['Bsc(BioTech)','Bsc(Micbio)','BSc(Chem)'] 
                                  elif selectname == "Shree P.M. Patel College of Electronics & Communication":
                                      dept_courses['values'] = ['Bsc(Chem)', 'Bsc(Phys)', 'Bsc(Math)', 'Bsc(CS)', 'Bsc(E)']
                                       
                              name = tk.StringVar()        
                              dept_name = ttk.Combobox(studentfrm1, textvariable=name,values=[ 
                                                                                               
                                                                                               "Shree P.M. Patel College of Computer Science & Technology",
                                                                                               "Shree P.M. Patel Institute of Biosciences",
                                                                                               "Shree P.M. Patel College of Electronics & Communication",
                                                                                               "Shree P.M. Patel Institute of Integrated M.Sc In Biotechnology",
                                                                                               "Shree P.M. Patel Institute of Postgraduate Studies & Research In Science",
                                                                                               "Shri P.M. Patel Institute of Pg Studies And Research In Applied Science",
                                                                                               "Smt. Minakshiben D. Patel Institue of Physical Scienec And Research",
                                                                                               "Smt. Kamlaben P. Patel College Of Home Science"
                                                                                               "Smt. Kamlaben P. Patel Institute of Physiotherapy & Occupational Therapy"
                                                                                               "Shree P.M. Patel College of Paramedical Science & Technology",
                                                                                               "Dr. Indravadan P. Patel Institute Of Medical Technology & Research",
                                                                                               "Shree P.M. Patel Institute of Business Administration",
                                                                                               "Smt J. B. Patel College Of Commerce Stuides And Research, Anand",
                                                                                               "Smt. Jayaben B. Patel Post Graduate Institute Of Business Studies & Research",
                                                                                               "Commerce College","Arts College", "Business College" 
                                                                                              
                                                                                              ]
                                                       )
                              dept_name.place(x=20, y=180, width=400, height=25)
                              dept_name.current()
                              dept_name.bind("<<ComboboxSelected>>", lambda event : nametocourse(event))
                              dept_name.set('Select College Name')
                              
                              deptcoursenamelbl = tk.Label(studentfrm1, text="College-Course-Name", font=("cambria", 11), bg="white")
                              deptcoursenamelbl.place(x=20, y=225, width=167, height=25)
                              
                              course = tk.StringVar()
                              dept_courses = ttk.Combobox(studentfrm1,textvariable=course)
                              dept_courses.place(x=20, y=248, width=200, height=25)
                              dept_courses.set('Select College Course')
                              
                             
                               #    elif selectyear == "Business College":
                               #        dept_courses["values"] = ["BBA(General)", "BBA(ITM)", "BBA(ISM)"]
                              deptyearlbl = tk.Label(studentfrm1, text="College-Year", font=("cambria", 11), bg="white")
                              deptyearlbl.place(x=20, y=287, width=115, height=25)
                              
                              year = tk.StringVar() 
                              dept_year = ttk.Combobox(studentfrm1, values=["FY","SY","TY"], textvariable=year)
                              dept_year.place(x=20, y=310, width=130, height=25)
                              dept_year.bind("<<ComboboxSelected>>", lambda event: selectyeartosem(event))
                              dept_year.set('Select Year')
                              
                              deptsemlbl = tk.Label(studentfrm1, text="College-Semester", font=("cambria", 11), bg="white")
                              deptsemlbl.place(x=20, y=345, width=130, height=25)
                              
                              sem = tk.StringVar()
                              dept_sem = ttk.Combobox(studentfrm1, textvariable=sem)
                              dept_sem.place(x=20, y=368, width=140, height=25)
                              dept_sem.set('Select Semester')
                              
                              def selectyeartosem(event):
                                  selectyear = dept_year.get()
                                  dept_sem.set('')
                                  if selectyear == "FY":
                                      dept_sem['values'] = ['SEM-I','SEM-II']
                                  elif selectyear ==  "SY":
                                      dept_sem['values'] = ["SEM-III", "SEM-IV"]
                                  elif selectyear == "TY":
                                      dept_sem['values'] = ['SEM-V', 'SEM-VI']
                                      
                                      
                              # todo: ------------------------------------ END college details ---------------------------------------------------|    
                                      
                              studentfrm = tk.LabelFrame(studentfrm1, text="Student Registration", bg="white")
                              studentfrm.place(x=875, y=95, width=630 , height=400)
                              
                              # todo: student id textbox, label, message  <-----------------------------------------------------------|  
                              studentidlbl = tk.Label(studentfrm1, text="Student-ID:",bg="white", font=("arial",10), fg="black")
                              studentidlbl.place(x=900, y=150, width=100, height=25)
                              
                              studentidmessage = tk.Label(studentfrm1, text="", bg="white", font=('arial', 10))
                              studentidmessage.place(x=1110, y=150, width=250, height=25)
                              
                              studentid = tk.StringVar()
                              def notusechar(value, reason, widget):
                                  is_digit = value.isdigit() or value==""
                                  if is_digit:              
                                      studentidmessage.config(text="")
                                  else:
                                      studentidmessage.config(text="Character not allow in student_id", fg="red", width=250)
                                  return is_digit    
                              
                              def studidmaxlen(entry, max_length, Label):
                                  text = entry.get()
                                  if len(text) > max_length:
                                      entry.delete(max_length, "end")
                                      studentidmessage.config(text="maximum 3 Digit allow", fg="red")
                                  else:
                                      studentidmessage.config(text="")
                                      
                              valid = studentfrm1.register(notusechar)
                              studentidtxt = tk.Entry(studentfrm1, font=("arial", 12), relief='solid',  textvariable=studentid, validate='key', validatecommand= (valid, '%P', '%S', '%W') )
                              studentidtxt.place(x=985, y=150, width=125, height=25)
                              studentidtxt.bind('<KeyPress>', lambda event :  [ studidmaxlen(studentidtxt, 3, studentidmessage), notusechar] )
                  
                              # todo: student name label,textbox, message <----------------------------------------------  
                              studentnamemessage = tk.Label(studentfrm1, text="", bg="white")
                              studentnamemessage.place(x=1140, y=200, width=190, height=25)
                              
                              studentnamelbl = tk.Label(studentfrm1, text="Student-Name:", bg="white", font=("arial",10))
                              studentnamelbl.place(x=890, y=200, width=100, height=25)
           
                           #    valid = studentfrm1.register(on_validate)
                              def on_validate(Value, reason, widget):
                                       is_alpha = Value.isalpha() or Value ==""
                                       if is_alpha:
                                           studentnamemessage.config(text="")
                                       else:
                                           studentnamemessage.config(text="Digit are not allow in student_name", fg="red")
                                       return is_alpha
                                   
                              validname =  studentfrm1.register(on_validate)
                              studentname = tk.StringVar()
                              studentnametxt = tk.Entry(studentfrm1, font=("arial", 12), relief='solid' ,textvariable=studentname, validate='key', validatecommand=(validname, '%P','%d','%W') )
                              studentnametxt.place(x=985, y=200, width=125, height=25)
                              studentnametxt.bind('<KeyPress>', lambda event : [ studnamemaxlen(studentnametxt, 15, studentnamemessage), on_validate ])
                              
                              def studnamemaxlen(entry, max_length, label):
                                  text = entry.get()
                                  if len(text) > max_length:
                                      entry.delete(max_length, "end")
                                      studentnamemessage.config(text="maximum 15 character allow", fg="red")
                                  else:
                                      studentnamemessage.config(text="")
                                      
                              # todo: student roll no [label, textbox , message] 
                              
                              studentrollnolbl = tk.Label(studentfrm1, text="Student-Rollno:", bg="white", font=("arial",10))
                              studentrollnolbl.place(x=888, y=250, width=100, height=25)
                              
                              studentrollnomessage = tk.Label(studentfrm1, text="", bg="white")  
                              studentrollnomessage.place(x=1145,y=250, width=215, height=25)
                              
                              studentrollno = tk.StringVar()
                              
                              def rollnotusechar(value, reason, widget):
                                       is_digit = value.isdigit() or value == ""
                                       if is_digit:
                                           studentrollnomessage.config(text="")
                                       else:
                                           studentrollnomessage.config(text="Character are not allow in student_rollno", fg="red")
                                       return is_digit
                                   
                              def studrollmaxlen(entry, max_length, label):
                                  text = entry.get()
                                  if len(text) > max_length:
                                      entry.delete(max_length, "end")
                                      studentrollnomessage.config(text="maximum 3 length allow",fg="red")
                                  else:
                                      studentrollnomessage.config(text="")     
                                   
                              validrollno =  studentfrm1.register(rollnotusechar)
                              studentrollnotxt = tk.Entry(studentfrm1, font=("arial", 12), relief='solid',  textvariable=studentrollno, validate='key' , validatecommand=(validrollno, '%P','%S','%W')) 
                              studentrollnotxt.place(x=985, y=250, width=125, height=25 )
                              studentrollnotxt.bind('<KeyPress>', lambda event: [ studrollmaxlen(studentrollnotxt, 3, studentrollnomessage), rollnotusechar])
                            
                              # todo: gender   [label, textbox , message]
                              genderlbl = tk.Label(studentfrm1, text="Gender:", bg="white", font=("arial",10))
                              genderlbl.place(x=918, y=305, width=80, height=25)
                              
                              gendermessage = tk.Label(studentfrm1, text="", bg="white")
                              gendermessage.place(x=1150, y=305, width=160, height=25)
                              
                              gender = tk.StringVar()
                              genderlist = ttk.Combobox(studentfrm1, values=["Male","Female"], textvariable=gender)
                              genderlist.place(x=985, y=305, width=125, height=25)
                              genderlist.set('Select Gender')
                             
                             
                             
                            #todo: TAKE PHOTO SAMPLE   
                              takeimgsamplebtn = tk.Button(studentfrm1, text="Add Image Sample", font=("arial",10), fg="white", bg="green", activebackground="green" , activeforeground="white", command= lambda : takesample())
                              takeimgsamplebtn.place(x=915, y=430, width=190, height=30)
                              
                              

                              
                            #   def takesample():
                            #     try:
                            #         if not all([studentidtxt.get(), studentnametxt.get(), studentrollnotxt.get(), genderlist.get(), dept_name.get(), dept_courses.get(), dept_year.get(), dept_sem.get()]):
                            #             msg.showerror("Error", "Please fill out all fields.", parent=studentfrm)
                            #             return

                            #         face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
                            #         camera = cv2.VideoCapture(0)
                            #         img_id = 0

                            #         studname = studentnametxt.get()
                            #         studrollno = studentrollnotxt.get()
                            #         save_dir = "C:/Projectwork/facealgorithm/trainimagedataset/"

                            #         existing_files = os.listdir(save_dir)
                            #         existing_files = [file.split(".")[0] for file in existing_files]
                            #         if f"{studname}.{studrollno}" in existing_files:
                            #             msg.showerror("Error", f"Image for {studname}.{studrollno} already exists.", parent=studentfrm1)
                            #             return

                            #         while True:
                            #             ret, frmcam = camera.read()
                            #             if not ret:
                            #                 msg.showerror("Error", "Failed to access camera.", parent=studentfrm1)
                            #                 break
                                        
                            #             faces = face_cascade.detectMultiScale(frmcam, scaleFactor=1.5, minNeighbors=15)
                            #             for x, y, w, h in faces:
                            #                 cv2.rectangle(frmcam, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            #                 face_cropping = frmcam[y:y+h, x:x+w]

                            #                 img_id += 1
                            #                 face = cv2.resize(face_cropping, (450, 450))
                            #                 filepath = os.path.join(save_dir, f"{studname}.{studrollno}.{img_id}.jpg")
                            #                 cv2.imwrite(filepath, face)

                            #                 cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            #                 cv2.imshow("Take Image Sample", face)

                            #                 if cv2.waitKey(1) == 13 or img_id == 100:
                            #                     break
                                            
                            #             if cv2.waitKey(1) == 13 or img_id == 100:
                            #                 break

                            #         camera.release()
                            #         cv2.destroyAllWindows()
                            #         msg.showinfo("Success", "Image capture completed.", parent=studentfrm1)
                            #     except Exception as e:
                            #         msg.showerror("Error", str(e), parent=studentfrm1)
                              def takesample():
                                    if not all([studentidtxt.get(), studentnametxt.get(), studentrollnotxt.get(), genderlist.get(), dept_name.get(), dept_courses.get(), dept_year.get(), dept_sem.get()]):
                                       msg.showerror("Error", "Please Select Your Name Record", parent=studentfrm)   
                                    else:                        
                                          try:
                                                 #todo: load predefine data on face frontal from opencv
                                                 facee = cv2.CascadeClassifier("C:\\Projectwork\\facealgorithm\\haarcascade_frontalface_default.xml")
                                                 def face_crop(img):
                                                     faces = facee.detectMultiScale(img, scaleFactor=1.5, minNeighbors=15)
                                                     for x,y,w,h in faces:
                                                         cv2.rectangle(img, (x,y), (x + w, y + h), (0,255,0), 2)
                                                         face_cropping = img[y:y+h, x:x+w]
                                                         return face_cropping

                                                 camera = cv2.VideoCapture(0)
                                                 img_id = 0

                                                 studname = studentnametxt.get()
                                                 studrollno = studentrollnotxt.get()

                                                 existing_files = os.listdir("C:\\Projectwork\\facealgorithm\\trainimagedataset\\")
                                                 existing_files = [ file.split(".")[0] for file in existing_files ]
                                                 if f"{studname}.{studrollno}" in existing_files:
                                                      msg.showerror("Error", f"Image for {studname}.{studrollno} already exists.", parent=studentfrm1)

                                                 while True:
                                                     _ , frmcam = camera.read()
                                                     capture_face = face_crop(frmcam)

                                                     if capture_face is not None:
                                                          img_id +=1
                                                          face = cv2.resize(capture_face, (400,400) )
                                                          filepath = f"C:\\Projectwork\\facealgorithm\\trainimagedataset\\{studname}.{studrollno}"+"."+str(img_id)+".jpg"
                                                           
                                                          if os.path.exists(filepath):
                                                              cv2.imwrite(filepath, face)
                                                              cv2.putText(face, str(img_id), (50, 50) ,cv2.FONT_HERSHEY_COMPLEX, 2 , (0,255,0), 2)
                                                              cv2.imshow("Take Image Sample", face)

                                                              if cv2.waitKey(1) == 13 or int(img_id) == 100:
                                                                  break
                                                              
                                                 camera.release()
                                                 cv2.destroyAllWindows()
                                                 msg.showinfo("Result", "Generating Data Sets Completed...", parent=studentfrm1)
                                          except Exception as t:
                                              msg.showerror("Error", f"Please Open WEB-CAM", parent=studentfrm1)
                              
                              #todo: insert record logic  ---------------------------------------------------------------------------------------|
                              def selectquery():
                                       try:
                                           con = conn.connect(host="localhost", user="root", password="", database="facerecognitionattendancesystem")
                                           cur = con.cursor()
                                           cur.execute("SELECT * FROM student")
                                           row = cur.fetchall()
                               
                                           if row:
                                               treeview.delete(*treeview.get_children())
                                               for rows in row:
                                                   treeview.insert("", "end", values=rows)
                                               con.commit()
                                           con.close()   
                                       except Exception as s:
                                           msg.showerror("Error", f"{s}", parent=studentfrm1)
                                           
                              insertbtn = tk.Button(studentfrm1, text="INSERT", bg="blue", fg="white", bd=5, activebackground="blue", activeforeground="white", command= lambda : insertdata(), cursor='hand2')
                              insertbtn.place(x=10, y=504, width=110, height=40)
                              insertbtn.bind('<Return>', lambda : insertdata())
                             
                              def insertdata():
                                  con = conn.connect(host="localhost", user="root", password="", db="facerecognitionattendancesystem")
                                  cur = con.cursor()
                                  
                                  if not all([studentidtxt.get(), studentnametxt.get(), studentrollnotxt.get(), genderlist.get(), dept_name.get(), dept_courses.get(), dept_year.get(), dept_sem.get()]):
                                           msg.showerror("Error", "All fields are required!", parent=studentfrm)
                                  if studentidtxt.get() == "":
                                      msg.showerror("Error", "student id is Required!", parent=studentfrm1)
                                  elif studentnametxt.get() == "":
                                      msg.showerror("Error", "studentname is Required!",parent=studentfrm1)
                                  elif studentrollnotxt.get() == "":
                                      msg.showerror("Error", "Studentrollnumber is Required!",parent=studentfrm1)
                                  elif genderlist.get() == "Select Gender":
                                      msg.showerror("Error", "Gender is Required!",parent=studentfrm1)
                                  elif dept_name.get() == "Select College Name":
                                      msg.showerror("Error", "College Name Field is Required!", parent=studentfrm1)
                                  elif dept_courses.get() == "Select College Course":
                                      msg.showerror("Error", "College courses Field is Required!", parent=studentfrm1)
                                  elif dept_year.get()== "Select Year":
                                      msg.showerror("Error", "College year Field is Required!", parent=studentfrm1) 
                                  elif dept_sem.get() == "Select Semester":
                                      msg.showerror("Error", "College semester Field is Required!", parent=studentfrm1)  
                                  elif studentid.get() != studentrollno.get() :
                                      msg.showerror("Error", "Student ID and Student Roll No must be the same", parent=studentfrm1)
                                  else:   
                                     try:
                                       con = conn.connect(host="localhost", user="root", password="", db="facerecognitionattendancesystem")
                                       cur = con.cursor()
           
                                       insertrecord = '''INSERT INTO student (student_id, student_name, student_rollno, gender, college_name, college_course, college_year, college_semester) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'''
                                       insertdata = (studentid.get(), studentname.get(), studentrollno.get(), gender.get(),
                                                     name.get(), course.get(), year.get(), sem.get(),)
           
                                       insertrecordcollege = '''INSERT INTO college(college_name, college_courses, college_course_year, college_semester, student_id, student_name) VALUES (%s,%s,%s,%s,%s,%s)'''
                                       insertcollege = (name.get(), course.get(), year.get(), sem.get(), studentid.get(), studentname.get())
           
                                       cur.execute("SELECT * FROM student WHERE student_id=%s", (studentid.get(),))
                                       row = cur.fetchone()
                                       if row:
                                           msg.showwarning(title="Warning", message="Record already exists", parent=studentfrm1)
                                       else:
                                           cur.execute(insertrecord, insertdata) 
                                           cur.execute(insertrecordcollege, insertcollege)
                                           con.commit()
                                           selectquery()
                                           msg.showinfo("Success", "Record inserted successfully")
                                           resetquery()
                                     except Exception as e:
                                         msg.showerror("Error", f"Due to: {e}")
                                         print(e)
                                     finally:
                                         con.close()    
                                      
                              updatebtn = tk.Button(studentfrm1, text="UPDATE", bg="blue", fg="white", bd=5, activebackground="blue", activeforeground="white", command= lambda : updatequery(), cursor='hand2' )
                              updatebtn.place(x=150, y=504, width=110, height=40)
                              def updatequery():
                               # todo: start logic Update Query 
                                       if not all([studentidtxt.get(), studentnametxt.get(), studentrollnotxt.get(), genderlist.get(), dept_name.get(), dept_courses.get(), dept_year.get(), dept_sem.get()]):
                                           msg.showerror("Error", "Please Select Record!", parent=studentfrm)
                                       elif studentidtxt.get() == "":
                                           msg.showerror("Error", "student id is Required!", parent=studentfrm1)
                                       elif studentnametxt.get() == "":
                                           msg.showerror("Error", "studentname is Required!",parent=studentfrm1)
                                       elif studentrollnotxt.get() == "":
                                           msg.showerror("Error", "Studentrollnumber is Required!",parent=studentfrm1)
                                       elif genderlist.get() == "":
                                           msg.showerror("Error", "Gender is Required!",parent=studentfrm1)
                                       elif dept_name.get() == "":
                                           msg.showerror("Error", "College Name Field is Required!", parent=studentfrm1)
                                       elif dept_courses.get() == "":
                                           msg.showerror("Error", "College courses Field is Required!", parent=studentfrm1)
                                       elif dept_year.get()=="":
                                           msg.showerror("Error", "College year Field is Required!", parent=studentfrm1) 
                                       elif dept_sem.get() == "":
                                           msg.showerror("Error", "College semester Field is Required!", parent=studentfrm1)
                                       elif studentidtxt.get() != studentrollnotxt.get():
                                           msg.showerror("Error", "student id Must be Same as Student_rollno")
                                       else:
                                             # todo: Update Query <-------------------------------------------------------------------------------------------|
                                             update = '''UPDATE student SET student_id=%s, student_name=%s, student_rollno=%s, gender=%s, college_name=%s, college_course=%s, college_year=%s, college_semester=%s WHERE student_id=%s'''
                                             updaterecord = (studentid.get(), studentname.get(), studentrollno.get(), gender.get(), name.get(), course.get(), year.get(), sem.get(), studentid.get())
                                             
                                             try:
                                                 con = conn.connect(host="localhost", user="root", password="", db="facerecognitionattendancesystem") 
                                                 cur = con.cursor()
                                                 
                                                 updatemsg = msg.askyesno("Update", "Do you want to Update This Record", parent=studentfrm1)
                                                 if updatemsg:
                                                     cur.execute(update, updaterecord)
                                                     con.commit()
                                                     selectquery()
                                                     resetquery()
                                                     msg.showinfo("Success", "Record Successfully Updated...", parent=studentfrm1)
                                                 else:
                                                     return
                                                 con.close()
                                             except Exception as u:
                                                 msg.showerror("Error", f"{u}", parent=studentfrm1)
                                                   
                              #todo: DELETE Query -----------Starting-----------------------------------------------|
                              deletebtn = tk.Button(studentfrm1, text="DELETE", bg="blue", fg="white", bd=5, activebackground="blue", activeforeground="white", command= lambda : deletequery(), cursor='hand2')
                              deletebtn.place(x=300, y=504, width=110, height=40)  
                              def deletequery():
                                  try:
                                      con = conn.connect(host="localhost", user="root", password="", db="facerecognitionattendancesystem")
                                      cur = con.cursor()
                                      if studentid.get()=="" or studentname.get()=="" or studentrollno.get()=="" or gender.get()==""  or name.get()=="" or course.get()=="" or year.get()=="" or sem.get()=="":
                                           msg.showerror("Error", "Please Select All The Fields")
                                      else:    
                                           deletemsg = msg.askyesno("Delete!", "Do You Want to Delete this Record", parent=studentfrm1)
                                           if deletemsg > 0:
                                               deletesyn = ''' DELETE FROM student WHERE student_id=%s '''
                                               deleterecord = (
                                                                studentid.get(),
                                                              )
                                               cur.execute(deletesyn,(deleterecord))
                                           else:
                                               if not deletemsg :
                                                   return
                                           msg.showwarning("Warning", "Are You Sure to Delete this Record", parent=studentfrm1)
                                           con.commit()
                                           selectquery()
                                           con.close()
                                  except Exception as d :
                                      msg.showerror("Error", f"{d}", parent=studentfrm1)
                              #todo: backtofield function use for insert the record then treeview in mouse click after selected data back to fields            
                              def backtofield(event):
                                   datafocus = treeview.focus()
                                   dataitem = treeview.item(datafocus)
                                   datafields = dataitem["values"]
           
                                   studentid.set(datafields[0]),
                                   studentname.set(datafields[1]),
                                   studentrollno.set(datafields[2]),
                                   gender.set(datafields[3]),
                                   name.set(datafields[4]),
                                   course.set(datafields[5]),
                                   year.set(datafields[6]),
                                   sem.set(datafields[7]),
                                   # imagesample.set(datafields[8])
                                      
                        
                              # todo: RESET the logic ---------> Start  RESET <----------------------------------------------------------------------------------------------------------|   
                              resetbtn = tk.Button(studentfrm1, text="Reset", bg="blue", fg="white", bd=5, activebackground="blue", activeforeground="white", command= lambda : resetquery(), cursor='hand2')
                              resetbtn.place(x=450, y=504, width=110, height=40)
                              
                              def resetquery():
                                  studentidtxt.delete(0, "end")
                                  studentnametxt.delete(0, "end")
                                  studentrollnotxt.delete(0, "end")
                                  genderlist.delete(0, "end")
                                  dept_name.delete(0, "end")
                                  dept_courses.delete(0, "end")
                                  dept_year.delete(0, "end")
                                  dept_sem.delete(0,"end")
                              
                                  
                              #todo: ---------------------> Ending RESET logic <--------------------------------------------------------------------------------------------------------------------|   
                              
                              #todo: single  show  record and multiple show record  
                              
                              searchlbl = tk.Label(studentfrm1, text="Search:", font=("arial",18), fg="white", bg="#0D2A66", )
                              searchlbl.place(x=590, y=507, width=130, height=35)
                               
                              searchrecord = ttk.Combobox(studentfrm1, values=["student_id","student_name","student_rollno","gender","college_name","college_Course","college_year","college_semester"], font=("arial",10))
                              searchrecord.place(x=700, y=507, width=130, height=35)
                              searchrecord.set("Select")
                              
                              showtxt  = tk.Entry(studentfrm1, font=("arial", 17), bd=3, relief='solid')
                              showtxt.place(x=850, y=507, width=150, height=35)
                              
                              showbtn = tk.Button(studentfrm1, text="Search", bg="blue", fg="white", bd=5, activebackground="blue", activeforeground="white", command= lambda: search())
                              showbtn.place(x=1050, y=504, width=150, height=40)  
                              def search():
                                  selected_column = searchrecord.get()
                                  search_value = showtxt.get()
                                  
                                  if not selected_column or not search_value:
                                      return
                                  try: 
                                           con =  conn.connect(host="localhost", user="root", password="", db="facerecognitionattendancesystem")
                                           cur = con.cursor()
                                           select = f"SELECT student_id, student_name, student_rollno, gender, college_name, college_course, college_year, college_semester FROM student WHERE {selected_column}=%s"
                                           cur.execute(select, (search_value,))
                                           row = cur.fetchall()
                                           if row==None:
                                               msg.showerror("Error", "Data Not Found", parent=studentfrm1)
                                               con.commit()
                                           fetchdata(row)
                                          
                                  except Exception as se:
                                         msg.showerror("Error", f"Due To:{se}", parent=studentfrm1)
                                         print(se)
                                  else:
                                      if selected_column == "Select" and search_value == "" : 
                                          msg.showerror("Error","Please Select Particular Field", parent=studentfrm1)       
                                              
                              showallre = tk.Button(studentfrm1, text="Show All", bg="blue", fg="white", bd=5, activebackground="green", activeforeground="white", command= lambda : showallrecord())
                              showallre.place(x=1300, y=504, width=110, height=40)
                              def showallrecord():
                                  try:
                                       con =  conn.connect(host="localhost", user="root", password="", db="facerecognitionattendancesystem")
                                       cur = con.cursor()
                                       cur.execute("SELECT * FROM student")
                                       show = cur.fetchall()
                                       fetchdata(show)
                                  except Exception as sh:
                                      msg.showerror("Error",f"{sh}")
                                           
                              def fetchdata(records):
                               #    global mydata
                               # #    mydata = rows
                               #    treeview.delete(*treeview.get_children())
                                  for item in treeview.get_children():
                                      treeview.delete(item)
                                      
                                  for record in records:
                                      treeview.insert("", "end", values=record) 
                                  
                        
                              #todo: create DataFrame <----------------Starting-----------------------------------------------------------------------------------------------------------------------------|    
                              fieldcolumn = ["Student_ID","Student_Name","Student_RollNo","Gender","College_name","College_courses", "College_year", "College_semester",]
                              treeview =  ttk.Treeview(studentfrm1, columns=fieldcolumn, selectmode='extended')
                              
                              treeview.heading("Student_ID", text="Student_ID")
                              treeview.heading("Student_Name", text="Student_Name")
                              treeview.heading("Student_RollNo", text="Student_RollNo")
                              treeview.heading("Gender", text="Gender")
                           #    treeview.heading("Status", text="Status")
                              treeview.heading("College_name", text="College_name")
                              treeview.heading("College_courses", text="College_courses")
                              treeview.heading("College_year", text="College_year")
                              treeview.heading("College_semester", text="College_semester")
                           #    treeview.heading("ImageSample", text="ImageSample")
                              treeview['show']="headings"
                              
                              #todo:  [        ]     
                              treeview.column("Student_ID",  width=50)
                              treeview.column("Student_Name", width=100)
                              treeview.column("Student_RollNo",  width=50)
                              treeview.column("Gender",  width=70)
                              treeview.column("College_name",  width=500)
                              treeview.column("College_courses", width=80)
                              treeview.column("College_year", width=50)
                              treeview.column("College_semester", width=80)
                          
                              selectquery()
                              treeview.place(x=0, y=550, width=1440, height=280)
                              search()
               
                              treeview.bind("<ButtonRelease>", backtofield)
                              rightscroll = ttk.Scrollbar(treeview, orient="vertical", command= treeview.yview)  # todo         |
                              treeview.configure(yscrollcommand=rightscroll.set)
                              rightscroll.pack(side="right", fill="y")               
                              
                              bottomscroll = ttk.Scrollbar(treeview, orient='horizontal', command=treeview.xview) # todo     ___
                              treeview.configure(xscrollcommand=bottomscroll.set)
                              bottomscroll.pack(side="bottom", fill="x")
                                                 
                              #todo: DataFrame -----------------> Ending <-----------------------------------------------------------------------------------------------|    
                             
                              #todo: this function is use for person insert record and data frame in show record then data frame inside mouse button left click after stored data focus back to fields     
           
                             
                # todo:________________________END OF Student Register_____________________________________________________________________________| 
                              
                # TODO: FACE RECONGITION MODULE  <---------------STARTING-------------------------------------------------------------------------|  
                 def facerecognition():
                        facebgimg = Image.open("C:\\Projectwork\\images\\refullface.jpg")
                        img2 = facebgimg.resize((int(facebgimg.width * 0.3), int(facebgimg.height * 0.2)))
                        showimg = ImageTk.PhotoImage(img2)  
                        facefrm2 = tk.Label(childwindow, image=showimg)
                        facefrm2.photo = showimg
                        facefrm2.place(x=1, y=1, width=1430, height=840)

                        # facepath = "C:\\Projectwork\\images\\2420383.png"
                        # facebg = Image.open(facepath)
                        # faceimg = mainbg.resize((int(facebg.width * 0.1), int(facebg.height * 0.1)))
                        # faceimod = ImageTk.PhotoImage(faceimg)
                        facebtn = tk.Button(facefrm2, text="Face Recognition", font=("arial",15), relief="raised", bg="#AE5257", fg="white", bd=5, cursor='hand2', command= lambda : logicfaces(self))
                        facebtn.place(x=620, y=770, width=200, height=42)
                        # facebtn.photo = faceimod

                        # def mark_attendance(i,n,r,c):
                        #     fieldname = ['ID','Name','Rollno','Date','Time','Day','Status']
                        #     with open(f"C:\\Projectwork\\excel\\attendance.csv","r+", newline="\n") as f:
                        #      #    reader = csv.DictReader(f)
                        #         datalist = f.readlines()
                        #      #    datalist = list(reader)
                        #         namelist = []
                        #         for line in datalist:
                        #             entry = line.split((","))
                        #             namelist.append(entry[0])

                        #         if ((i not in namelist) and (n not in namelist) and (r not in namelist) and (c not in namelist))   :
                        #             now = datetime.now()
                        #             dt = now.strftime('%d/%m/%Y')
                        #             te =  now.strftime('%H:%M:%S')
                        #             dy = now.strftime('%A')

                        #             f.writelines(f"\n{i},{n},{r},{c},{dt},{te},{dy},Present")


                        # todo: logic of FACE RECOGNITION <------Starting-------------------------------------------------|   
                        def logicfaces(self):
                         #   try:
                              def recognizer(img, classifier, scaleFactor, minNeighbours, color, text, clf):

                                         classifier = cv2.CascadeClassifier("C:\\Projectwork\\facealgorithm\\haarcascade_frontalface_default.xml")
                                         gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                                         faces = classifier.detectMultiScale(gray, scaleFactor, minNeighbours)
                                         coord = []

                                         for (x,y,w,h) in faces:
                                             cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
                                             id,predict = clf.predict(gray[y:y+h, x:x+w])

                                             confidence = int((100*(1-predict/300)))

                                             con = conn.connect(host="localhost", user="root", password="", db="facerecognitionattendancesystem")
                                             cur = con.cursor()


                                             cur.execute("SELECT student_id, student_name, student_rollno, college_name FROM student WHERE student_id=%s",(id,))
                                             student_info = cur.fetchone()

                                             if student_info :
                                                 i, n, r, c = student_info
                                                 i = str(i)
                                                 n = str(n)
                                                 r = str(r) 
                                                 c = str(c)

                                             if confidence > 77:
                                                 cv2.putText(img, f"College_Name:{c}", (x,y - 113), cv2.FONT_HERSHEY_COMPLEX, 1.3, (255,0,0), 2)
                                                 cv2.putText(img, f"ID:{i}"   , (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 1.3 , (255,0,0), 2)
                                                 cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 1.3 , (255,0,0), 2)
                                                 cv2.putText(img, f"Roll-No:{r}", (x,y - 25), cv2.FONT_HERSHEY_COMPLEX, 1.3, (255,0,0), 2) 
                                             else:
                                                 cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)
                                                 cv2.putText(img, f"Unknown Person", (x,y - 10), cv2.FONT_HERSHEY_PLAIN, 1.3, (0,0,255), 2)
                                                #  mark_attendance(i,n,r,c)
                                             coord = [x, y, w, h]
                                         return coord
                              def facedetect(img, clf, faceCascade):
                                     coord = recognizer(img, faceCascade, 1.3, 20, (0,0,255), "Face", clf)
                                     return img

                              faceCascade = cv2.CascadeClassifier("C:\\Projectwork\\facealgorithm\\haarcascade_frontalface_default.xml")
                              clf = cv2.face.LBPHFaceRecognizer.create()
                              clf.read("classifier.xml")

                              webcam = cv2.VideoCapture(0)
                              while True:
                                  _, img = webcam.read()

                                  img = facedetect(img, clf, faceCascade)

                                  cv2.imshow("Face Recognition System", img)
                                  if cv2.waitKey(1) == ord("q"):
                                      break
                              webcam.release()
                              cv2.destroyAllWindows()

                        #todo: FACE RECOGNITION logic <--------Ending------------------------------------------------------------------------------|  
                         #   except Exception as cam:
                         #         msg.showerror("Error", "Please set the Cameras")        
                        back2 = tk.Button(facefrm2, text="Back", font=("arial", 12), command= lambda : exitmodule2())
                        back2.place(x=15, y=30, width=100, height=50)    
                        def exitmodule2():
                            facefrm2.destroy()
               #TODO: FACE RECOGNITION MODULE  <-------ENDING--------------------------------------------------------------------------------------------|     
                       
               #todo: TRAIN DATASET logic <---------------STARTING--------------------------------------------------------------------------------------------|    
               #todo:    
                 def traindataset():
                        trainfrm3 = tk.Frame(childwindow,)
                        trainfrm3.place(x=0, y=0, width=1500, height=840)
                        
                        facebgimg = Image.open("C:\\Projectwork\\images\\haarFace.jpg")
                        img2 = facebgimg.resize((int(facebgimg.width * 2.1), int(facebgimg.height * 1.5)))
                        showimg = ImageTk.PhotoImage(img2)  
                        facefrm2 = tk.Label(trainfrm3, image=showimg)
                        facefrm2.photo = showimg
                        facefrm2.place(x=0, y=0, width=1430, height=820)     
                        

                        trainbtn = tk.Button(trainfrm3, text="Train Data", font=("arial",12), relief="raised", bg="blue", fg="white", bd=5 , activebackground="blue", activeforeground="white" ,command= lambda : logictrain(self))
                        trainbtn.place(x=570, y=350, width=290, height=80)
                        #todo: algorithm local binary patterns histogram    
                        def logictrain(self):
                            data_dir = "C:\\Projectwork\\facealgorithm\\trainimagedataset"
                            path = [ os.path.join(data_dir, file) for file in os.listdir(data_dir) ]

                            faces = []
                            ids = []

                            for image in path:
                                img = Image.open(image).convert('L') 
                                imagenp = np.array(img,'uint8')
                                id = int(os.path.split(image)[1].split('.')[1])

                                faces.append(imagenp)
                                ids.append(id)

                                cv2.imshow("Training dataset Images", imagenp)

                                if cv2.waitKey(1)==13:
                                    break
                                
                            ids = np.array(ids)
                            #todo: train [ LBPH Face recognition ] classifier and save 
                            clf = cv2.face.LBPHFaceRecognizer.create()
                            clf.train(faces, ids)
                            clf.write("classifier.xml")
                            cv2.destroyAllWindows()
                            msg.showinfo("Result", "Train DataSets Completed... ") 
                        back3 = tk.Button(trainfrm3, text="Back", font=("arial", 12), command= lambda : exitmodule3())
                        back3.place(x=25, y=30, width=100, height=50)

                        def exitmodule3():
                            trainfrm3.destroy()
                
                 #TODO: -----------------> TRAIN DATA MODULE <------ENDING---------------------------------------------------------------------------------------| 
                
                 #TODO: logic of MULTIPLE IMAGES STORE IN trainimagedataset FOLDER
                 def manyimages():
                    os.startfile("C:\\Projectwork\\facealgorithm\\trainimagedataset")
               
                 #todo: Multiple images module Ending <---------------------------------------------------------------------------------------------------------------|    
              
              
                #todo: ATTENDANCE MODULE <-----------STARTING-----------------------------------------------------------------------------------------------------------------------------| 
                #todo:            _____ _____   |----   |\  |        |
                #todo:        /\    |     |     |----   | \ |     ___|
                #todo:       /  \   |     |     |----   |  \|     |__|
                 def attendance():
                            attendfrm = tk.Frame(childwindow, bg="maroon")
                            attendfrm.place(x=0, y=0, width=1500, height=840)
                            mydata = []


                            backbtn = tk.Button(attendfrm, text="BACK", font=("arial",12), command= lambda : backmain())
                            backbtn.place(x=10, y=20, width=100, height=40) 
                            def backmain():
                                attendfrm.destroy()

                            bglbl = tk.Label(attendfrm, text="ATTENDANCE Pannel", font=("times new romans",35), bg="maroon", fg="white")
                            bglbl.place(x=500, y=3, width=475, height=80)


                            #todo: attendance related label -----------------------------------------------------------|    
                            attendlblframe = tk.LabelFrame(attendfrm, text="Attendance Details" , bd=5, relief='flat')
                            attendlblframe.place(x=5, y=70, width=640, height=755)

                            lblattendid = tk.Label(attendfrm, text="Student_id:",font=("arial",13),)
                            lblattendid.place(x=10, y=120, width=130, height=25)

                            lblattendstdname = tk.Label(attendfrm, text="Student_Name:",font=("arial",13),)
                            lblattendstdname.place(x=10, y=160, width=130, height=25)

                            lblattendstdroll = tk.Label(attendfrm, text="Student_Rollno:",font=("arial",13),)
                            lblattendstdroll.place(x=10, y=200, width=130, height=25)

                            # lblattendcollegename = tk.Label(attendfrm, text="College_Name:",font=("arial",13),)
                            # lblattendcollegename.place(x=10, y=240, width=130, height=25)

                            #todo: ending -------------------------------------------------------------------------------|

                            #todo: attendance related textbox,dropdownlist  <--------------------------------------------------------| 

                            attendstudmessage = tk.Label(attendfrm, text="", fg="white")
                            attendstudmessage.place(x=300, y=120, width=150, height=30)

                            def notallowchar(char):
                                if char.isalpha() and attendtxtstudid.get()!='alphabet' :
                                    return True
                                else:
                                    return False

                            stdid = tk.StringVar()
                            attendtxtstudid = tk.Entry(attendfrm, font=("arial",12), textvariable=stdid)    
                            attendtxtstudid.place(x=140, y=120, width=150, height=25)
                            attendtxtstudid.bind('<KeyPress>', lambda event :  [ studidmaxlen(attendtxtstudid, 3, attendstudmessage), notallowchar])

                            def studidmaxlen(entry, max_length, namemessage):
                                text = entry.get()
                                if len(text) > max_length:
                                    entry.delete(max_length, "end")
                                    namemessage.config(text="maximum 3 Digit allow", fg="red")
                                else:
                                    namemessage.config(text="")

                            stdname = tk.StringVar()
                            studnamemessage = tk.Label(attendfrm, text="", fg="red")
                            attendstudmessage.place(x=300, y=190, width=150, height=30)
                            def studnamemaxlen(entry, max_length, studnamemessage):
                                text = entry.get()
                                if len(text) >= max_length:
                                    entry.delete(max_length, "end")
                                    studnamemessage.config(text="Maximum 15 Digit Allowed", fg="red")
                                else:
                                    studnamemessage.config(text="")


                            def on_validate(Value, reason, widget):
                                     is_alpha = Value.isalpha() or Value ==""
                                     if is_alpha:
                                         studnamemessage.config(text="")
                                     else:
                                         studnamemessage.config(text="digit are not allow in username", fg="red")
                                     return is_alpha
                            validstdname =  attendfrm.register(on_validate)

                #             studentname = tk.StringVar()
                #             studentnametxt = tk.Entry(studentfrm1, font=("arial", 12), textvariable=studentname, validate='key', validatecommand=(validname, '%P','%d','%W') )
                #             studentnametxt.place(x=620, y=190, width=125, height=25)
                            stdrollnomessage = tk.Label(attendfrm, text="", font=('arial',10))
                            
                            attendtxtstudname = tk.Entry(attendfrm, validate='key', font=("arial",12) ,textvariable=stdname, validatecommand=(validstdname, '%P','%d','%W')  )
                            attendtxtstudname.place(x=140, y=160, width=150, height=25)
                            attendtxtstudname.bind('<KeyPress>', lambda event : [ studnamemaxlen(attendtxtstudname, 15, studnamemessage), on_validate ])

                            stdrollno = tk.StringVar()
                            def studidvalidation(value, reason):
                                max_length = 3

                                if not value.isalpha() and len(value) <= max_length:
                                    return True 
                                else:
                                    return False

                            validrollno = attendfrm.register(studidvalidation)
                            attendtxtstudroll = tk.Entry(attendfrm, textvariable=stdrollno, font=("arial", 12), validate='key', validatecommand=(validrollno, '%P', '%S'))
                            attendtxtstudroll.place(x=140, y=200, width=150, height=25) 

                            collegenamelist= []        

                            #todo: ending <------------------------------------------------------------------------------------------------|

                            #todo: csv file export csv file logic  --------------------------------------------------------------------------|
                            def fetchdata(rows):
                                for item in attendtreeview.get_children():
                                    attendtreeview.delete(item)
                                for i in rows:
                                    attendtreeview.insert("", "end", values=i)

                            savecsvbtn = tk.Button(attendfrm, text="CSV Report", command= lambda: savecsvfile(), font=("times new romans",14), bg="blue", fg="white", activeforeground="white", activebackground="blue"  ,relief='groove', bd=8, cursor="hand2",)
                            savecsvbtn.place(x=10, y=740, width=630, height=75)        
                            def savecsvfile():
                                try:
                                    con = conn.connect(user="root", host="localhost", password="", db="facerecognitionattendancesystem")
                                    cur = con.cursor()

                                    now = datetime.now()

                                    cur.execute("SELECT * FROM attendance")
                                    data = cur.fetchall()

                                    with open(f"C:\\Projectwork\\excel\\Student_attendance{now.strftime('%Y-%m-%d')}.csv", mode='w', newline="") as file:
                                        writer = csv.writer(file)
                                        writer.writerow(["Student_ID","Student_Name","Student_Rollno", "Time", "Date", "Status", "Day"])
                                        writer.writerows(data)
                                    msg.askyesno("SaveFile", "Are You Sure to Save Your Record in CSV File", parent=attendfrm)
                                 #    msg.showinfo("Success", "Your Record Export to CSV File Successfully!", parent=attendfrm)  
                                except Exception as s:
                                    msg.showerror("Error", f"Due To:{s}",parent=attendfrm)          

                            def selectedquery():
                                     try:
                                         con = conn.connect(host="localhost", user="root", password="", database="facerecognitionattendancesystem")
                                         cur = con.cursor()
                                         cur.execute("SELECT * FROM attendance")
                                         row = cur.fetchall()

                                         if row:
                                             attendtreeview.delete(*attendtreeview.get_children())
                                             for rows in row:
                                                 attendtreeview.insert("", "end", values=rows)
                                             con.commit()
                                         con.close()   
                                     except Exception as s:
                                         msg.showerror("Error", f"{s}")

                            updatedata = tk.Button(attendfrm, text="Update", font=("times new romans",14), bg="blue", fg="white", activeforeground="white", activebackground="blue"  ,relief='groove', bd=8, cursor="hand2", command= lambda :  updatequery())
                            updatedata.place(x=225, y=665, width=210, height=70)
                            def updatequery():

                                if attendtxtstudid.get()=="" and attendtxtstudname.get()=="" or attendtxtstudroll.get()=="" :
                                    msg.showerror("Error","Please Fill All Fields are Required!", parent=attendfrm)
                                elif  attendtxtstudid.get()=="":
                                    msg.showerror("Error","Student_id Field are Required!", parent=attendfrm) 
                                elif attendtxtstudname.get() == "":
                                    msg.showerror("Error", "Student_Name Field are Required!", parent=attendfrm)
                                elif attendtxtstudroll.get() == "":
                                    msg.showerror("Error", "Student_Rollno Field are Required!", parent=attendfrm)    
                                else:
                                    try:
                                        update = msg.askyesno("Update!", "Do You Want to Update this Record!", parent=attendfrm)
                                        if update > 0 :
                                            con = conn.connect(user="root", host="localhost", password="", db="facerecognitionattendancesystem")
                                            cur = con.cursor()
                                            cur.execute("UPDATE set attendance student_id=%s, student_name=%s, student_rollno=%s WHERE student_id=%s", 
                                                            (
                                                              attendtxtstudid.get(),
                                                              attendtxtstudname.get(),
                                                              attendtxtstudroll.get(),
                                                            )
                                                        )
                                        else:
                                            if not update:
                                                return
                                        msg.showinfo("Success","Record Updated Successfull", parent=attendfrm)
                                        con.commit()
                                        fetchdata()
                                        con.close()

                                    except Exception as up:
                                        msg.showerror("Error", f"Due To:{str(up)}", parent=attendfrm)

                            resetdata = tk.Button(attendfrm, text="Reset", font=("times new romans",14), bg="blue", fg="white", activeforeground="white", activebackground="blue"  ,relief='groove', bd=8, cursor="hand2", command= lambda : resetquery())
                            resetdata.place(x=440, y=665, width=200, height=70)
                            def resetquery():
                                 attendtxtstudid.delete(0,"end"),
                                 attendtxtstudname.delete(0, "end"),
                                 attendtxtstudroll.delete(0, "end"),

                            deletedata = tk.Button(attendfrm, text="Delete", font=("times new romans",14), bg="blue", fg="white", activeforeground="white", activebackground="blue"  ,relief='groove', bd=8, cursor="hand2", command= lambda : deletedata())   
                            deletedata.place(x=10, y=665, width=210, height=70)
                            def deletedata():

                                if attendtxtstudid.get()=="" or attendtxtstudname.get()=="" or attendtxtstudroll.get()=="":
                                    msg.showerror("Error", "Select The Record", parent=attendfrm)
                                elif attendtxtstudid.get()=="":
                                    msg.showerror("Error", "Student_ID Must be Required!", parent=attendfrm)
                                else:
                                  try:  
                                      delete = msg.askyesno("Delete", "Do you want to Delete This Record!", parent=attendfrm)
                                      if delete > 0 :
                                          con = conn.connect(host="localhost", user="root", password="" , db="facerecognitionattendancesystem")
                                          cur = con.cursor()
                                          delequery = "DELETE FROM attendance WHERE student_id=%s"
                                          val =  (  
                                                    attendtxtstudid.get(),
                                                 )
                                          cur.execute(delequery, (val) )
                                      else:
                                          if not delete:
                                              return
                                      msg.showwarning("Warning", "Are You Sure to Delete this Record", parent=attendfrm)
                                      con.commit()
                                      selectedquery()
                                      resetquery()
                                      con.close()
                                  except Exception as de:
                                      msg.showerror("Error", f"Due To:{str(de)}", parent=attendfrm)

                  #         todo: importcsv, exporcsv file ----> Ending <---------------------------------------------------------------------------------->|    
                            def backfields(event):
                                focuscur = attendtreeview.focus()
                                content = attendtreeview.item(focuscur)
                                data = content['values']

                                stdid.set(data[0]),
                                stdname.set(data[1]),
                                stdrollno.set(data[2]),

                  #         todo :  Attendance Treeview data report  <----------------------------------------------------------------------------------------------------------------|  
                            fieldcolumn = ["Student_ID","Student_Name","Student_RollNo","Time", "Date", "Status", "Day"]
                            attendtreeview =  ttk.Treeview(attendfrm, columns=fieldcolumn, selectmode='extended', )

                            attendtreeview.heading("Student_ID", text="Student_ID")
                            attendtreeview.heading("Student_Name", text="Student_Name")
                            attendtreeview.heading("Student_RollNo", text="Student_RollNo")
                #             attendtreeview.heading("Gender", text="Gender")
                #             treeview.heading("College_name", text="College_name")
                            attendtreeview.heading("Time", text="Time")
                            attendtreeview.heading("Date", text="Date")
                #             attendtreeview.heading("College_semester", text="College_semester")
                            attendtreeview.heading("Status", text="Status")
                            attendtreeview.heading("Day", text="Day")
                            attendtreeview['show']="headings"

                            #todo:  [        ]     
                            attendtreeview.column("Student_ID",  width=200)
                            attendtreeview.column("Student_Name", width=200)
                            attendtreeview.column("Student_RollNo",  width=200)
                #             attendtreeview.column("Gender",  width=200)
                            attendtreeview.column("Time", width=200)
                            attendtreeview.column("Date", width=200)
                #           attendtreeview.column("College_semester", width=200)
                            attendtreeview.column("Status",  width=200)
                            attendtreeview.column("Day", width=200)

                            attendtreeview.place(x=650, y=70, width=785, height=755)
                            selectedquery()
                            attendtreeview.bind("<ButtonRelease>", backfields)

                            rightscroll = ttk.Scrollbar(attendtreeview, orient="vertical", command= attendtreeview.yview)#todo|
                            attendtreeview.configure(yscrollcommand=rightscroll.set)
                            rightscroll.pack(side="right", fill="y")               

                            bottomscroll = ttk.Scrollbar(attendtreeview, orient='horizontal', command= attendtreeview.xview)#todo__
                            attendtreeview.configure(xscrollcommand=bottomscroll.set)
                            bottomscroll.pack(side="bottom", fill="x")

                            markattend = tk.Button(attendfrm , text="Mark Attendance", font=("arial",12), cursor='hand2' , fg="white", activeforeground="white", bg="maroon", activebackground="maroon", bd=5 ,relief='groove',command= lambda: automatic())
                            markattend.place(x=10, y=610, width=630, height=45)    
                            def automatic():
                            
                                 def draw_boundry(img, classifier, scaleFactor, minNeighbours, color, text, clf):

                                     classifier = cv2.CascadeClassifier("C:\\Projectwork\\facealgorithm\\haarcascade_frontalface_default.xml")
                                     gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                                     faces = classifier.detectMultiScale(gray, scaleFactor, minNeighbours)

                                     for x, y, w, h in faces:
                                         cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                                         id, predict = clf.predict(gray[y:y+h, x:x+w])

                                         confidence = int((100*(1-predict/300)))

                                         con = conn.connect(host="localhost", user="root", password="", db="facerecognitionattendancesystem")
                                         cur = con.cursor()


                                         cur.execute("SELECT student_id, student_name, student_rollno FROM student WHERE student_id=%s", (id,))
                                         student_data = cur.fetchone()

                                         #todo Check if data is found
                                         if student_data:
                                             # Unpack the fetched data into individual variables
                                             i, n, r = student_data
                                             # Convert student ID, name, and roll number to strings if needed (might not be necessary)
                                             i = str(i)
                                             n = str(n)
                                             r = str(r)

                                         now = datetime.now()
                                         dt = now.strftime("%Y-%m-%d")
                                         time = now.strftime("%H:%M:%S")
                                         day = now.strftime("%A")
                                         def check_status(in_time, out_time):
                                             late_threshold = now.strptime("9:00:00 AM",  "%H:%M:%S %p")
                                             in_datetime = now.strptime(in_time, "%H:%M:%S %p")

                                             if in_datetime > late_threshold:
                                                 return "Late"
                                             elif in_time and out_time:
                                                 return "Present"
                                             else:
                                                 return "Absent" 

                                         in_time = "08:30:00 AM"
                                         out_time = "14:30:00 PM"
                                         status = check_status(in_time, out_time)

                                         if confidence > 75:
                                             cv2.putText(img, f"Student_ID: {i}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                                             cv2.putText(img, f"Student_Name: {n}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                                             cv2.putText(img, f"Student_RollNo: {r}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                                             mark_attendance(i, n, r, time, dt, status, day)
                                         else:
                                             cv2.rectangle(img, (x,y), (x+w, y+h) ,cv2.FONT_HERSHEY_SIMPLEX, 1.3,(255,255,0),2)
                                             cv2.putText(img, "Unknown Person" , (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

                                 def facedetect(img, clf, faceCascade):
                                     draw_boundry(img, faceCascade, 1.3, 15, (255, 25, 255), "Face", clf)
                                     return img

                                 def mark_attendance(i, n, r, time, dt, status, day):
                                     con = conn.connect(host="localhost", user="root", password="", db="facerecognitionattendancesystem")
                                     cur = con.cursor()

                                     now = datetime.now()
                                     dt = now.strftime("%Y-%m-%d")
                                     time = now.strftime("%H:%M:%S")
                                     day = now.strftime("%A")
                                     def check_status(in_time, out_time):
                                             late_threshold = now.strptime("12:00:00 PM",  "%H:%M:%S %p")
                                             in_datetime = now.strptime(in_time, "%H:%M:%S %p")

                                             if in_datetime > late_threshold:
                                                 return "Late"
                                             elif in_time and out_time:
                                                 return "Present"
                                             else:
                                                 return "Absent"

                                     in_time = "11:30:00 AM"
                                     out_time = "14:30:00 PM"
                                     status = check_status(in_time, out_time)

                                     cur.execute("SELECT * FROM attendance WHERE student_name=%s AND Date=%s AND day=%s", (n, dt, day))
                                     row = cur.fetchone()
                                     if not row:
                                         cur.execute("INSERT INTO attendance (student_id, student_name, student_rollno, Time, Date, Status, day) VALUES (%s, %s, %s, %s, %s, %s, %s)", (i, n, r, time, dt, status, day))
                                         con.commit()
                                         msg.showinfo("Success", "Attendance recorded successfully.")
                                     else:
                                         msg.showerror("Error", "Attendance for This Student Already Recorded For Today.")

                                 faceCascade = cv2.CascadeClassifier("C:\\Projectwork\\facealgorithm\\haarcascade_frontalface_default.xml")
                                 clf = cv2.face.LBPHFaceRecognizer.create()
                                 clf.read("classifier.xml")

                                 # url = 'http://username:password@ip_address/video' # todo <-- ip camera access
                                 webcam = cv2.VideoCapture(0)  #todo: access variable and run complete 
                                 while True:
                                     _, img = webcam.read()
                                     img = facedetect(img, clf, faceCascade)
                                     cv2.imshow("Attendance Pannel", img)
                                     if cv2.waitKey(1) == ord("q"):
                                         break
                                     
                                 webcam.release()
                                 cv2.destroyAllWindows()

                                 attendfrm.mainloop()
                    
                 def help():
                      helpfrm = tk.Tk()
                      
                      helpfrm.geometry('1440x820+0+0')
                      helpfrm.title("Help Page")
                      helpfrm.config(bg='maroon')
                      
                      helpback = tk.Button(helpfrm, text="Back", font=("arial", 12), command= lambda : exithelp(), cursor='hand2')
                      helpback.place(x=15, y=30, width=120, height=50)
                      def exithelp():
                            helpfrm.destroy()
                                   
                       
                      helptitle = tk.Label(helpfrm, text="HELP", font=("times new roman", 30), fg="white", bg='maroon')
                      helptitle.place(x=600, y=30, height=60, width=120) 
                                   
                      helpmessage = tk.Label(helpfrm, text="Email: theapmsdeveloper@gmail.com", font=("times new roman", 30), fg="white", bg='maroon')
                      helpmessage.place(x=10, y=400, height=60, width=1400)
                      
                      
                      
                      
                      helpfrm.mainloop()
                   
                 def aboutus():
                      aboutfrm = tk.Tk()
                      aboutfrm.geometry('1440x820+0+0')
                      aboutfrm.title("About Us")
                      aboutfrm.config(bg="indigo",)
                      
                      aboutlbl = tk.Label(aboutfrm, text="ABOUT US", fg="salmon", font=("times new roman", 30), bg="indigo")
                      aboutlbl.place(x=600, y=30, width=195, height=60)
                      
                      message = tk.Label(aboutfrm, text="The Face Recognition Attendance System is used to automatic taking student attendance and Tracking student.",
                                         font=("times new roman", 20), fg="white", bg="indigo")
                      message.place(x=10, y=720, height=35, width=1400)
                      
                      aboutback = tk.Button(aboutfrm, text="Back", font=("arial", 12), command= lambda : exithelp(), cursor='hand2')
                      aboutback.place(x=15, y=30, width=100, height=50)
                      def exithelp():
                            aboutfrm.destroy()
                            
                      aboutfrm.mainloop()
                      
                   
                 childwindow.mainloop()
                  
                      
               
if __name__ == "__main__":
     childwindows = tk.Tk()
     window = facerecognitionattendancesys()
     window.loginpage()
     childwindows.mainloop()
   