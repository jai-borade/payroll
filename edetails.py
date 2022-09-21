from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np




class Employee_Datails:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1720x860+0+0")
        self.root.title("Employee Details")

        # =======================Text Variables======================
      
        self.var_Name=StringVar()
        self.var_SO=StringVar()
        self.var_EmpID=StringVar()
        self.var_Desig=StringVar()
        self.var_Dep=StringVar()
        self.var_Aadhar=StringVar()
        self.var_PAN=StringVar()
        self.var_Gender=StringVar()
        self.var_UAN=StringVar()
        self.var_ESI=StringVar()
        self.var_Email=StringVar()
        self.var_Contact=StringVar()
        self.var_Bank=StringVar()
        self.var_BankAcc=StringVar()
        self.var_Bkbranch=StringVar()
        self.var_IFSC=StringVar()
        self.var_DOB=StringVar()
        self.var_DOJ=StringVar()
        self.var_Passport=StringVar()
        self.var_Education=StringVar()               
        self.var_CAdd=StringVar()
        self.var_PAdd=StringVar()
        self.var_Photo=StringVar()       
        

        # Frame 1
        img=Image.open("E:\Jai\JaiRoll\Employee1.jfif")
        img=img.resize((600, 130),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img)
       
        f_lbl=Label(self.root,image=self.photo1)
        f_lbl.place(x=0,y=0,width=600,height=130)

        # Frame 2
        img1=Image.open("E:\Jai\JaiRoll\Employee2.jfif")
        img1=img1.resize((520, 130),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img1)
       
        f_lbl=Label(self.root,image=self.photo2)
        f_lbl.place(x=600,y=0,width=520,height=130)

        # Frame 3
        img2=Image.open("E:\Jai\JaiRoll\employee4.jfif")
        img2=img2.resize((600, 130),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photo3)
        f_lbl.place(x=1120,y=0,width=600,height=130)

         # Background Image
        img3=Image.open("E:\Jai\JaiRoll\J6.jfif")
        img3=img3.resize((1720, 730),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photo4)
        bg_img.place(x=0,y=130,width=1720,height=730)

        title_lbl=Label(bg_img,text='Employee Management System', font=('Secuela', 36, "bold"),bg="white", fg="Dark Blue")
        title_lbl.place(x=0,y=0,width=1580,height=45)

        # Main Frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=50,width=1650,height=680)

        # Left Side Label Frame

        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee Details",font=("Secuela",18, "bold"))
        left_frame.place(x=10,y=10, width=825, height=650)

        emp_name=LabelFrame(left_frame,bd=2)
        emp_name.place(x=2,y=0,width=820,height=50)

        
        emp_info=LabelFrame(left_frame,bd=2)
        emp_info.place(x=2,y=50,width=820,height=380)

        emp_info1=LabelFrame(left_frame,bd=2)
        emp_info1.place(x=2,y=400,width=820,height=140)

        btn_frame=LabelFrame(left_frame,bd=2)
        btn_frame.place(x=2,y=510,width=820,height=60)

        btn_frame1=LabelFrame(left_frame,bd=2)
        btn_frame1.place(x=2,y=563,width=820,height=50)

         

        # Right Side Label Frame

        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee Details",font=("Secuela",18, "bold"))
        right_frame.place(x=840,y=10, width=790, height=650)

        # Name Label:
        lbl_Name=Label(emp_name,text='Employee_Full_ Name : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_Name.grid(row=0, column=1,sticky=W, padx=2, pady=7)

        txt_name=ttk.Entry(emp_name,textvariable=self.var_Name,width=54, font=('secuela', 10, 'bold'))
        txt_name.grid(row=0,column=3,padx=2, pady=7)

        # Father's Name
        lbl_FN=Label(emp_name,text='Son_of : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_FN.grid(row=0, column=4,sticky=W, padx=2, pady=7)
        
        txt_FN=ttk.Entry(emp_name,textvariable=self.var_SO,width=30, font=('secuela', 10, 'bold'))
        txt_FN.grid(row=0,column=5,padx=2, pady=7)



        # Employee Information Table

        # Employee ID:
        lbl_EmpId=Label(emp_info,text='Employee_ID : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_EmpId.grid(row=0, column=1,sticky=W, padx=2, pady=7)
        
        txt_EmpId=ttk.Entry(emp_info,textvariable=self.var_EmpID,width=30, font=('secuela', 10, 'bold'))
        txt_EmpId.grid(row=0,column=2,padx=2, pady=7)

        # Employee Designation:
        lbl_Desig=Label(emp_info,text='Designation : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_Desig.grid(row=0, column=3,sticky=W, padx=2, pady=7)
        
        txt_Desig=ttk.Entry(emp_info,textvariable=self.var_Desig,width=30, font=('secuela', 10, 'bold'))
        txt_Desig.grid(row=0,column=4,padx=2, pady=7)

        # Employee Department:
        lbl_Dep=Label(emp_info,text='Department : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_Dep.grid(row=2, column=1,sticky=W, padx=2, pady=7)

        com_txt_Dep=ttk.Combobox(emp_info,textvariable=self.var_Dep,state='readonly', font=('secuela', 10, 'bold'),width=30)
        com_txt_Dep['value']=('Select Department', 'HR', 'Talent Aquision', 'Accounts', 'Audit', 'Finance', 'Legal', 'Software Engineer', 'System Architect')
        com_txt_Dep.current(0)
        com_txt_Dep.grid(row=2,column=2,sticky=W,padx=2, pady=7)

        # Aadhar No.:      
        lbl_Aadhar=Label(emp_info,text='Aadhar_Number : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_Aadhar.grid(row=2, column=3,sticky=W, padx=2, pady=7)
        
        txt_Aadhar=ttk.Entry(emp_info,textvariable=self.var_Aadhar,width=30, font=('secuela', 10, 'bold'))
        txt_Aadhar.grid(row=2,column=4,padx=2, pady=7)

        #PAN No.:
        lbl_PAN=Label(emp_info,text='PAN : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_PAN.grid(row=3, column=1,sticky=W, padx=2, pady=7)
        
        txt_PAN=ttk.Entry(emp_info,textvariable=self.var_PAN,width=30, font=('secuela', 10, 'bold'))
        txt_PAN.grid(row=3,column=2,padx=2, pady=7)

        # Gender
        lbl_Gender=Label(emp_info,text='Gender : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_Gender.grid(row=3, column=3,sticky=W, padx=2, pady=7)

        com_txt_Gender=ttk.Combobox(emp_info,textvariable=self.var_Gender,state='readonly', font=('secuela', 10, 'bold'),width=30)
        com_txt_Gender['value']=('Select Gender','Male','Female','Others')
        com_txt_Gender.current(0)
        com_txt_Gender.grid(row=3,column=4,sticky=W,padx=2, pady=7)        
        
        # UAN No.
        lbl_UAN=Label(emp_info,text='UAN : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_UAN.grid(row=4, column=1,sticky=W, padx=2, pady=7)
        
        txt_UAN=ttk.Entry(emp_info,textvariable=self.var_UAN,width=30, font=('secuela', 10, 'bold'))
        txt_UAN.grid(row=4,column=2,padx=2, pady=7)

        # ESI No.
        lbl_ESI=Label(emp_info,text='ESI_Number : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_ESI.grid(row=4, column=3,sticky=W, padx=2, pady=7)
        
        txt_ESI=ttk.Entry(emp_info,textvariable=self.var_ESI,width=30, font=('secuela', 10, 'bold'))
        txt_ESI.grid(row=4,column=4,padx=2, pady=7)
        

        # Contact No.
        lbl_Contact=Label(emp_info,text='Contact_Number : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_Contact.grid(row=5, column=3,sticky=W, padx=2, pady=7)
        
        txt_Contact=ttk.Entry(emp_info,textvariable=self.var_Contact,width=30, font=('secuela', 10, 'bold'))
        txt_Contact.grid(row=5,column=4,padx=2, pady=7)

        # Email ID
        lbl_EmailID=Label(emp_info,text='Email_ID : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_EmailID.grid(row=5, column=1,sticky=W, padx=2, pady=7)
        
        txt_EmailID=ttk.Entry(emp_info,textvariable=self.var_Email,width=30, font=('secuela', 10, 'bold'))
        txt_EmailID.grid(row=5,column=2,padx=2, pady=7)

        # Bank Name
        lbl_BkName=Label(emp_info,text='Bank_Name : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_BkName.grid(row=6, column=1,sticky=W, padx=2, pady=7)
        
        txt_lbl_BkName=ttk.Entry(emp_info,textvariable=self.var_Bank,width=30, font=('secuela', 10, 'bold'))
        txt_lbl_BkName.grid(row=6,column=2,padx=2, pady=7)

        # Bank A/C No.
        lbl_AcNo=Label(emp_info,text='Account_Number : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_AcNo.grid(row=6, column=3,sticky=W, padx=2, pady=7)
        
        txt_AcNo=ttk.Entry(emp_info,textvariable=self.var_BankAcc,width=30, font=('secuela', 10, 'bold'))
        txt_AcNo.grid(row=6,column=4,padx=2, pady=7)

        # Bank Branch
        lbl_BkName=Label(emp_info,text='Branch_Name : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_BkName.grid(row=7, column=1,sticky=W, padx=2, pady=7)
        
        txt_lbl_BkName=ttk.Entry(emp_info,textvariable=self.var_Bkbranch,width=30, font=('secuela', 10, 'bold'))
        txt_lbl_BkName.grid(row=7,column=2,padx=2, pady=7)

        # IFSC Code.
        lbl_IFSC=Label(emp_info,text='IFSC : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_IFSC.grid(row=7, column=3,sticky=W, padx=2, pady=7)
        
        txt_IFSC=ttk.Entry(emp_info,textvariable=self.var_IFSC,width=30, font=('secuela', 10, 'bold'))
        txt_IFSC.grid(row=7,column=4,padx=2, pady=7)

        # DOB :
        lbl_DOB=Label(emp_info,text='DOB : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_DOB.grid(row=8, column=1,sticky=W, padx=2, pady=7)
        
        txt_lbl_DOB=ttk.Entry(emp_info,textvariable=self.var_DOB,width=30, font=('secuela', 10, 'bold'))
        txt_lbl_DOB.grid(row=8,column=2,padx=2, pady=7)

        # DOJ :
        lbl_DOJ=Label(emp_info,text='DOJ : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_DOJ.grid(row=8, column=3,sticky=W, padx=2, pady=7)
        
        txt_DOJ=ttk.Entry(emp_info,textvariable=self.var_DOJ,width=30, font=('secuela', 10, 'bold'))
        txt_DOJ.grid(row=8,column=4,padx=2, pady=7)

        # Passprot No. :
        lbl_Passport=Label(emp_info,text='Passport_Number : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_Passport.grid(row=9, column=1,sticky=W, padx=2, pady=7)
        
        txt_lbl_Passport=ttk.Entry(emp_info,textvariable=self.var_Passport,width=30, font=('secuela', 10, 'bold'))
        txt_lbl_Passport.grid(row=9,column=2,padx=2, pady=7)

        # Educational Qualification:
        lbl_EduQ=Label(emp_info,text='Education : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_EduQ.grid(row=9, column=3,sticky=W, padx=2, pady=7)
        
        txt_EduQ=ttk.Entry(emp_info,textvariable=self.var_Education,width=30, font=('secuela', 10, 'bold'))
        txt_EduQ.grid(row=9,column=4,padx=2, pady=7)

        
        # Employee Current Address :
        lbl_CAddress=Label(emp_info1,text='Current_Address : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_CAddress.grid(row=0, column=1,sticky=W, padx=2, pady=7)
        
        txt_lbl_CAddress=ttk.Entry(emp_info1,textvariable=self.var_CAdd,width=85, font=('secuela', 10, 'bold'))
        txt_lbl_CAddress.grid(row=0,column=2,padx=2, pady=7)

        # Employee Permanent Address :
        lbl_PAddress=Label(emp_info1,text='Permanent_Address : ', font=('secuela', 10, 'bold'), bg='white')
        lbl_PAddress.grid(row=1, column=1,sticky=W, padx=2, pady=7)
        
        txt_lbl_PAddress=ttk.Entry(emp_info1,textvariable=self.var_PAdd,width=85, font=('secuela', 10, 'bold'))
        txt_lbl_PAddress.grid(row=1,column=2,padx=2, pady=7)

        # Radio Buttons
        self.var_radio1=StringVar()
        radio_btn1=ttk.Radiobutton(emp_info1,variable=self.var_radio1,text="Take_Photo",value='Yes')
        radio_btn1.grid(row=2,column=1)

        radio_btn2=ttk.Radiobutton(emp_info1,variable=self.var_radio1,text="No_Photo",value='No')
        radio_btn2.grid(row=2,column=2)


        # Button Frame
        save_btn=Button(btn_frame, text='Save',command=self.add_data,font=('secuela', 12, 'bold'), bg='blue',fg="white", width=24)
        save_btn.grid(row=0, column=1,sticky=W, padx=2, pady=7)

        update_btn=Button(btn_frame, text='Update',command=self.update_data,font=('secuela', 12, 'bold'), bg='blue',fg="white", width=24)
        update_btn.grid(row=0, column=2,sticky=W, padx=2, pady=7)

        delete_btn=Button(btn_frame, text='Delete',command=self.delete_data,font=('secuela', 12, 'bold'), bg='blue',fg="white", width=24)
        delete_btn.grid(row=0, column=3,sticky=W, padx=2, pady=7)

        reset_btn=Button(btn_frame, text='Reset',command=self.reset_data,font=('secuela', 12, 'bold'), bg='blue',fg="white", width=23)
        reset_btn.grid(row=0, column=4,sticky=W, padx=2, pady=7)

        takephoto_btn=Button(btn_frame1, text='Take a Photo',command=self.generate_dataset,font=('secuela', 12, 'bold'), bg='blue',fg="white", width=49)
        takephoto_btn.grid(row=1, column=1,sticky=W, padx=2, pady=5)

        updatephoto_btn=Button(btn_frame1, text='Update Photo',font=('secuela', 12, 'bold'), bg='blue',fg="white", width=49)
        updatephoto_btn.grid(row=1, column=2,sticky=W, padx=2, pady=5)

        # ========================Search System =======================

        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search Tab",font=("Secuela",10, "bold"),bg='white',fg='red')
        search_frame.place(x=0,y=0, width=780, height=70)

        search_by=Label(search_frame,font=('secuela', 12, 'bold'), text='Search by:',fg='white', bg='red')
        search_by.grid(row=0,column=1,sticky=W,padx=5)

        search_employee=ttk.Combobox(search_frame,state='readonly', font=('secuela', 10, 'bold'),width=15)
        search_employee['value']=('Search by','Aadhar','Contact No.','Email Id')
        search_employee.current(0)
        search_employee.grid(row=0,column=2,sticky=W,padx=5)

        txt_lbl_searchby=ttk.Entry(search_frame,width=28, font=('secuela', 10, 'bold'))
        txt_lbl_searchby.grid(row=0,column=3,padx=2, pady=7)

        search_btn=Button(search_frame, text='Search',font=('secuela', 10, 'bold'), bg='blue',fg="white", width=20)
        search_btn.grid(row=0, column=4,sticky=W, padx=4, pady=5)

        showAll_btn=Button(search_frame, text='ShowAll',font=('secuela', 10, 'bold'), bg='blue',fg="white", width=20)
        showAll_btn.grid(row=0, column=5,sticky=W, padx=4, pady=5)

        # =====================Table Frame ============================
       
        table_frame=Frame(right_frame,bd=2,bg='white',relief=RIDGE)
        table_frame.place(x=2,y=75,width=780,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("Name","SO","EmpID","Desig","Dep","Aadhar","PAN","Gender","UAN","ESI","Email","Contact","Bank","BankAcc","Bkbranch","IFSC","DOB","DOJ","Passport","Education","CAdd","PAdd","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("Name",text="Employee_Full_Name")
        self.employee_table.heading("SO",text="Son_of")
        self.employee_table.heading("EmpID",text="Employee_ID")
        self.employee_table.heading("Desig",text="Designation")
        self.employee_table.heading("Dep",text="Department")
        self.employee_table.heading("Aadhar",text="Aadhar_Number")
        self.employee_table.heading("PAN",text="PAN")
        self.employee_table.heading("Gender",text="Gender")
        self.employee_table.heading("UAN",text="UAN")
        self.employee_table.heading("ESI",text="ESI_Number")
        self.employee_table.heading("Email",text="Email_ID")
        self.employee_table.heading("Contact",text="Contact_Number")
        self.employee_table.heading("Bank",text="Bank_Name")
        self.employee_table.heading("BankAcc",text="Account_Number")
        self.employee_table.heading("Bkbranch",text="Branch_Name")
        self.employee_table.heading("IFSC",text="IFSC")
        self.employee_table.heading("DOB",text="DOB")
        self.employee_table.heading("DOJ",text="DOJ")
        self.employee_table.heading("Passport",text="Passport_Number")
        self.employee_table.heading("Education",text="Education")                
        self.employee_table.heading("CAdd",text="Current_Address")
        self.employee_table.heading("PAdd",text="Permanent_Address")
        self.employee_table.heading("Photo",text="Take_Photo") 
               
        self.employee_table["show"]='headings' 


        self.employee_table.column("Name",width=150)
        self.employee_table.column("SO",width=100)
        self.employee_table.column("EmpID",width=100)
        self.employee_table.column("Desig",width=100)
        self.employee_table.column("Dep",width=100)
        self.employee_table.column("Aadhar",width=150)
        self.employee_table.column("PAN",width=100)
        self.employee_table.column("Gender",width=100)
        self.employee_table.column("UAN",width=100)
        self.employee_table.column("ESI",width=100)
        self.employee_table.column("Email",width=100)
        self.employee_table.column("Contact",width=100)
        self.employee_table.column("Bank",width=100)
        self.employee_table.column("BankAcc",width=150)
        self.employee_table.column("Bkbranch",width=100)
        self.employee_table.column("IFSC",width=100)
        self.employee_table.column("DOB",width=100)
        self.employee_table.column("DOJ",width=100)
        self.employee_table.column("Passport",width=150)
        self.employee_table.column("Education",width=100)                
        self.employee_table.column("CAdd",width=200)
        self.employee_table.column("PAdd",width=200)
        self.employee_table.column("Photo",width=100)
        
           

        self.employee_table.pack(fill=BOTH,expand=1) 
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data() 

    # ======================fuction Declaration==========================

    def add_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_Gender.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee_master values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                                                    self.var_Name.get(),
                                                                                                                                                    self.var_SO.get(),
                                                                                                                                                    self.var_EmpID.get(),
                                                                                                                                                    self.var_Desig.get(),
                                                                                                                                                    self.var_Dep.get(),
                                                                                                                                                    self.var_Aadhar.get(),
                                                                                                                                                    self.var_PAN.get(),
                                                                                                                                                    self.var_Gender.get(),
                                                                                                                                                    self.var_UAN.get(),
                                                                                                                                                    self.var_ESI.get(),
                                                                                                                                                    self.var_Email.get(),
                                                                                                                                                    self.var_Contact.get(),
                                                                                                                                                    self.var_Bank.get(),
                                                                                                                                                    self.var_BankAcc.get(),
                                                                                                                                                    self.var_Bkbranch.get(),
                                                                                                                                                    self.var_IFSC.get(),
                                                                                                                                                    self.var_DOB.get(),
                                                                                                                                                    self.var_DOJ.get(),
                                                                                                                                                    self.var_Passport.get(),
                                                                                                                                                    self.var_Education.get(),                                                                                                                                                                                                                                                                                                       
                                                                                                                                                    self.var_CAdd.get(),
                                                                                                                                                    self.var_PAdd.get(),
                                                                                                                                                    self.var_radio1.get() 
                                                                                                                                                    

                                                                                                                                                ))
    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Employee Data added successfully",parent=self.root)
            except Exception as es: 
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)


    # ===================== Fetch Data =======================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from employee_master")
        data=my_cursor.fetchall()

        if len(data)!=0:
            #self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # =======================Get Cursor====================
    def get_cursor(self,event):
        cursor_focus=self.employee_table.focus()
        content=self.employee_table.item(cursor_focus)
        data=content["values"]
        self.var_Name.set(data[0])
        self.var_SO.set(data[1])
        self.var_EmpID.set(data[2])
        self.var_Desig.set(data[3])
        self.var_Dep.set(data[4])
        self.var_Aadhar.set(data[5])
        self.var_PAN.set(data[6])
        self.var_Gender.set(data[7])
        self.var_UAN.set(data[8])
        self.var_ESI.set(data[9])
        self.var_Email.set(data[10])
        self.var_Contact.set(data[11])
        self.var_Bank.set(data[12])
        self.var_BankAcc.set(data[13])
        self.var_Bkbranch.set(data[14])
        self.var_IFSC.set(data[15])
        self.var_DOB.set(data[16])
        self.var_DOJ.set(data[17])
        self.var_Passport.set(data[18])
        self.var_Education.set(data[19])             
        self.var_CAdd.set(data[20])
        self.var_PAdd.set(data[21])
        self.var_radio1.set(data[22]) 
        

    def update_data(self):
        if self.var_Name.get()=="" or self.var_Gender.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else: 
            try:
                update=messagebox.askyesno('Update','are you sure?',parent=self.root)
                if update>0:                                                 
                    conn=mysql.connector.connect(host='localhost', username='root',password='root', database='face_recognition')
                    my_cursor=conn.cursor() 
                    my_cursor.execute("update employee_master set Employee_Full_Name=%s,Son_of=%s,Employee_ID=%s,Department=%s,Aadhar_Number=%s,PAN=%s,Gender=%s,UAN=%s,ESI_Number=%s,Email_ID=%s,Contact_Number=%s,Bank_Name=%s,Account_Number=%s,Branch_Name=%s,IFSC=%s,DOB=%s,DOJ=%s,Passport_Number=%s,Education=%s,Current_Address=%s,Permanent_Address=%s,Take_Photo=%s where Designation=%s",(
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Name.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_SO.get(),                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_EmpID.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Dep.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Aadhar.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_PAN.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Gender.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_UAN.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_ESI.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Email.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Contact.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Bank.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_BankAcc.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Bkbranch.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_IFSC.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_DOB.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_DOJ.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Passport.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Education.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_CAdd.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_PAdd.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Desig.get()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

                                                                                                                                                                                                                                                                                                                                                                                                            ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee Successfully Updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root) 


    # Delete

    def delete_data(self):
        if self.var_PAN.get()=="":
            messagebox.showerror('Error','All Fields are Required')

        else:
            try:
                delete=messagebox.askyesno('Delete','are you sure to delete this employee',parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host='localhost', username='root',password='root', database='face_recognition')
                    my_cursor=conn.cursor()
                    sql='delete from employee_master where PAN=%s' 
                    value=(self.var_PAN.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee has been deleted Sucessfully!',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
    def reset_data(self):
        
        self.var_Name.set("")
        self.var_SO.set("")
        self.var_EmpID.set("")
        self.var_Desig.set("")
        self.var_Dep.set("Select Department")
        self.var_Aadhar.set("")
        self.var_PAN.set("")
        self.var_Gender.set("Select Gender")
        self.var_UAN.set("")
        self.var_ESI.set("")
        self.var_Email.set("")
        self.var_Contact.set("")
        self.var_Bank.set("")
        self.var_BankAcc.set("")
        self.var_Bkbranch.set("")
        self.var_IFSC.set("")
        self.var_DOB.set("")
        self.var_DOJ.set("")
        self.var_Passport.set("")
        self.var_Education.set("")             
        self.var_CAdd.set("")
        self.var_PAdd.set("")
        self.var_radio1.set("")


    # ====================Generate Dataset or Take a Photo Sample===========================
    def generate_dataset(self):
        if self.var_Name.get()=="" or self.var_Gender.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else: 
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='root', database='face_recognition')
                my_cursor=conn.cursor() 
                my_cursor.execute("select * from employee_master")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update employee_master set Employee_Full_Name=%s,Son_of=%s,Designation=%s,Department=%s,Aadhar_Number=%s,PAN=%s,Gender=%s,UAN=%s,ESI_Number=%s,Email_ID=%s,Contact_Number=%s,Bank_Name=%s,Account_Number=%s,Branch_Name=%s,IFSC=%s,DOB=%s,DOJ=%s,Passport_Number=%s,Education=%s,Current_Address=%s,Permanent_Address=%s,Take_Photo=%s where Employee_ID=%s",(
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Name.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_SO.get(),                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Desig.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Dep.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Aadhar.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_PAN.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Gender.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_UAN.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_ESI.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Email.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Contact.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Bank.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_BankAcc.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Bkbranch.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_IFSC.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_DOB.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_DOJ.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Passport.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_Education.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_CAdd.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_PAdd.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                                                                                                                                                                                                            self.var_EmpID.get()==id+1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

                                                                                                                                                                                                                                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close

                # ===========================Load - Predefined Data - Front Face- From OpenCV ===============================
               
                face_classifier=cv2.CascadeClassifier("E:\Jai\JaiRoll\haarcascade_frontalface_default.xml")

                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_crop(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(my_frame,(250,250), Image.ANTIALIAS)
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_Path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_Path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Processed Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==20:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Datasets Completed")

            except Exception as es:                
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)









    


     
       













         
        







        
       

       

       



       






        

      
      















































if __name__=="__main__":
    root=Tk()
    obj=Employee_Datails(root)
    root.mainloop()