from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os




class training:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1720x860+0+0")
        self.root.title("Face Reco System")

        title_lbl=Label(self.root,text='TRAIN DATASETS', font=('Secuela', 36, "bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1720,height=45)

        upper_image=Image.open("E:\Jai\JaiRoll\J3.jfif")
        upper_image=upper_image.resize((1720, 380),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(upper_image)

        upper_lbl=Label(self.root,image=self.photo3)
        upper_lbl.place(x=0,y=50,width=1720,height=380)

        lower_image=Image.open("E:\Jai\JaiRoll\J2.jfif")
        lower_image=lower_image.resize((1720, 380),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(lower_image)

        bottom_lbl=Label(self.root,image=self.photo4)
        bottom_lbl.place(x=0,y=510,width=1720,height=380)

        btn2=Button(self.root,text="TRAIN DATA",command=self.train_classifier,font=('Secuela', 30, "bold"),fg="white", bg="Darkblue",cursor="hand2")
        btn2.place(x=0,y=430,width=1720,height=80)

    def train_classifier(self):
        data_dir=('data')
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,"uint8")
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training_1",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        # =======================Train the classifier and Save==========================
        clf=cv2.face.LBPHFaceRecognizer_create()    
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed") 




       

        










if __name__=="__main__":
    root=Tk()
    obj=training(root)
    root.mainloop()