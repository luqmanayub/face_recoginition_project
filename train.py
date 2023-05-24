from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Reecoginition System")

        # bg image
        img3 = Image.open(
            r"C:\Users\mluqm\OneDrive\Desktop\face_recoginition_system\student_portal\trainmainimg.png")
        img3 = img3.resize((2100, 1030), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=2100, height=1030)

        b1 = Button(self.root, text="TRAIN DATA", cursor="hand2", command=self.train_classifier, font=(
            "times new roman", 30, "bold"), bg="darkblue", fg="white")
        b1.place(x=550, y=500, width=1000, height=60)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Gray Scale Image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # Train Classifier

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset is Completed")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
