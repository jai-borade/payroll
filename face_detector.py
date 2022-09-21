from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os


class face_detector:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1720x860+0+0")
        self.root.title("Face Reco System")

        title_lbl=Label(self.root,text='FACE RECOGNITION', font=('Secuela', 36, "bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1720,height=45)

        left_image=Image.open("E:\Jai\JaiRoll\Face_recog1.jfif")
        left_image=left_image.resize((860,810),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(left_image)

        left_lbl=Label(self.root,image=self.photo1)
        left_lbl.place(x=0,y=50,width=860,height=810)

        right_image=Image.open("E:\Jai\JaiRoll\Face_recog2.jfif")
        right_image=right_image.resize((860,810),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(right_image)

        right_lbl=Label(self.root,image=self.photo2)
        right_lbl.place(x=861,y=50,width=859,height=810)

        btn2=Button(right_lbl,text="Detect Face",command=self.face_reco,font=('Secuela', 30, "bold"),fg="white", bg="Darkgreen",cursor="hand2")
        btn2.place(x=0,y=650,width=859,height=80)

    # ===============================Face Recognition===============================

    def face_reco(self):
        def draw_boundary(img,classifier,scaleFactor,minNeigbors,color,text,clf):
            #print(img)
            #print(cv2.COLOR_BGR2GRAY)
            img = cv2.imread("user1.jpg",1)
            gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            #cv2.imwrite("gray_img.jpg", gray_img)
            #b = color [:,:, 0]
            #g = color [:,:, 1]
            #r = color [:,:, 2]
            #rgba = cv2.merge((b,g,r, g))
            #cv2.imwrite("rgba.png", rgba)
            #gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)           
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeigbors)
            print(gray_img)

            coords=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
                id,predict=clf.predict(gray_img[y:y+h, x:x+w]) 
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Designation from employee_master where Employee_ID="+str(id))
                e=my_cursor.fetchone()
                print(e)
                e="+".join(e) 

                my_cursor.execute("select Department from employee_master where Employee_ID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Email_ID from employee_master where Employee_ID="+str(id))
                c=my_cursor.fetchone()
                c="+".join(c)


                if confidence>77:
                    cv2.putText(img,f"Designation:{e}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Email_ID:{c}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face:",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coords

        def recognize(img, clf, faceCascade):
            coords = draw_boundary(img, faceCascade, 1.1, 10, (255,255,255), "Face", clf)
            return img
        
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
   
        while True:
            ret,img=cap.read()
            img=recognize(img,clf,face_cascade) 
            if not ret:
                print("Not Ret")
                break
            cv2.imshow("Video",img)

            if cv2.waitKey(10)==13:
                break
            cap.release()
            cv2.destroyAllWindows()   
              
                      
        

if __name__=="__main__":
    root=Tk()
    obj=face_detector(root)
    root.mainloop()