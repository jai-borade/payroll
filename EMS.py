from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from edetails import Employee_Datails
from training import training
from face_detector import face_detector
import os




class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1720x860+0+0")
        self.root.title("Face Recognition System") 

        # Frame 1
        img=Image.open("E:\Jai\JaiRoll\P1.jfif")
        img=img.resize((600, 130),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img)
       
        f_lbl=Label(self.root,image=self.photo1)
        f_lbl.place(x=0,y=0,width=600,height=130)

        # Frame 2
        img1=Image.open("E:\Jai\JaiRoll\J2.jfif")
        img1=img1.resize((520, 130),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img1)
       
        f_lbl=Label(self.root,image=self.photo2)
        f_lbl.place(x=600,y=0,width=520,height=130)

        # Frame 3
        img2=Image.open("E:\Jai\JaiRoll\J3.jfif")
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

        title_lbl=Label(bg_img,text='FACE RECOGNITION ATTENDANCE SYSTEM', font=('Secuela', 36, "bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1580,height=45)

        # Employee Details Button
        img4=Image.open("E:\Jai\JaiRoll\EMS3.jfif")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photo5=ImageTk.PhotoImage(img4)

        btn1=Button(bg_img,image=self.photo5,command=self.EIS,cursor="hand2")
        btn1.place(x=200,y=100,width=220,height=220)

        btn2=Button(bg_img,text="Employee Details",command=self.EIS,font=('Secuela', 18, "bold"),fg="white", bg="Darkblue",cursor="hand2")
        btn2.place(x=200,y=280,width=220,height=40)

        # Face Detector Button
        img5=Image.open("E:\Jai\JaiRoll\FR2.jfif")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photo6=ImageTk.PhotoImage(img5)

        btn1=Button(bg_img,image=self.photo6,cursor="hand2",command=self.face_data)
        btn1.place(x=520,y=100,width=220,height=220)

        btn2=Button(bg_img,text="Face Detector",font=('Secuela', 18, "bold"),fg="white", bg="Darkblue",cursor="hand2",command=self.face_data)
        btn2.place(x=520,y=280,width=220,height=40)

        # Attendance Button
        img6=Image.open("E:\Jai\JaiRoll\J8.jfif")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photo7=ImageTk.PhotoImage(img6)

        btn1=Button(bg_img,image=self.photo7,cursor="hand2")
        btn1.place(x=840,y=100,width=220,height=220)

        btn2=Button(bg_img,text="Attendance",font=('Secuela', 18, "bold"),fg="white", bg="Darkblue",cursor="hand2")
        btn2.place(x=840,y=280,width=220,height=40)


        # Help Desk Button
        img7=Image.open("E:\Jai\JaiRoll\Help Desk.jfif")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photo8=ImageTk.PhotoImage(img7)

        btn1=Button(bg_img,image=self.photo8,cursor="hand2")
        btn1.place(x=1160,y=100,width=220,height=220)

        btn2=Button(bg_img,text="Help Desk",font=('Secuela', 18, "bold"),fg="white", bg="Darkblue",cursor="hand2")
        btn2.place(x=1160,y=280,width=220,height=40)


        # Train Face Button
        img8=Image.open("E:\Jai\JaiRoll\J9.jfif")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photo9=ImageTk.PhotoImage(img8)

        btn1=Button(bg_img,image=self.photo9,cursor="hand2",command=self.training_data)
        btn1.place(x=200,y=400,width=220,height=220)

        btn2=Button(bg_img,text="Train Data",font=('Secuela', 18, "bold"),fg="white", bg="Darkblue",cursor="hand2",command=self.training_data)
        btn2.place(x=200,y=580,width=220,height=40)


        # Photos Button
        img9=Image.open("E:\Jai\JaiRoll\photos.jfif")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photo10=ImageTk.PhotoImage(img9)

        btn1=Button(bg_img,image=self.photo10,cursor="hand2",command=self.open_img)
        btn1.place(x=520,y=400,width=220,height=220)

        btn2=Button(bg_img,text="Photos",font=('Secuela', 18, "bold"),fg="white", bg="Darkblue",cursor="hand2",command=self.open_img)
        btn2.place(x=520,y=580,width=220,height=40)

        # Developer Button
        img10=Image.open("E:\Jai\JaiRoll\J10.jfif")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photo11=ImageTk.PhotoImage(img10)

        btn1=Button(bg_img,image=self.photo11,cursor="hand2")
        btn1.place(x=840,y=400,width=220,height=220)

        btn2=Button(bg_img,text="Developer",font=('Secuela', 18, "bold"),fg="white", bg="Darkblue",cursor="hand2")
        btn2.place(x=840,y=580,width=220,height=40)

        # Exit Button
        img11=Image.open("E:\Jai\JaiRoll\Exit.jfif")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photo12=ImageTk.PhotoImage(img11)

        btn1=Button(bg_img,image=self.photo12,cursor="hand2")
        btn1.place(x=1160,y=400,width=220,height=220)

        btn2=Button(bg_img,text="Exit",font=('Secuela', 18, "bold"),fg="white", bg="Darkblue",cursor="hand2")
        btn2.place(x=1160,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("Data")
        







        # ========================Fuction buttons=======================
    def EIS(self):
        self.new_window=Toplevel(self.root)
        self.app=Employee_Datails(self.new_window)

    def training_data(self):
        self.new_window=Toplevel(self.root)
        self.app=training(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_detector(self.new_window)      




   








if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

