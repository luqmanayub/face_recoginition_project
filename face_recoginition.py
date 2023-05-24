from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Reecoginition System")

        # bg image
        img3 = Image.open(
            r"C:\Users\mluqm\OneDrive\Desktop\face_recoginition_system\student_portal\facerecogmain.png")
        img3 = img3.resize((2100, 1030), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=2100, height=1030)

        b1 = Button(self.root, text="Face Recoginition", cursor="hand2", command=self.face_recog, font=(
            "times new roman", 30, "bold"), bg="darkblue", fg="white")
        b1.place(x=550, y=500, width=1000, height=60)

    # Attendance Mark
    def mark_attendance(self, i, n, d):
        with open("attended.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            namme_list = []
            for line in myDataList:
                entry = line.split((","))
                namme_list.append(entry[0])
            if ((i not in namme_list) and (n not in namme_list) and (d not in namme_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{dtString},{d1},Present")

                # Face Recoginition Function

    def face_recog(self):
        # img3 = Image.open(
        #     r"C:\Users\mluqm\OneDrive\Desktop\face_recoginition_system\student_portal\facerecogmain.png")
        # img3 = img3.resize((2100, 1030), Image.ANTIALIAS)
        # self.photoimg3 = ImageTk.PhotoImage(img3)

        # bg_img = Label(self.root, image=self.photoimg3)
        # bg_img.place(x=0, y=0, width=2100, height=1030)

        # main_frame = Frame(bg_img, bd=2)
        # main_frame.place(x=40, y=170, width=1840, height=850)

        def draw_boundry(img, classifier, scaleFacetor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFacetor, minNeighbors)

            coord = []
            for (x, y, w, h) in features:
                # img3 = Image.open(
                #     r"C:\Users\mluqm\OneDrive\Desktop\face_recoginition_system\student_portal\facerecogmain.png")
                # img3 = img3.resize((2100, 1030), Image.ANTIALIAS)
                # self.photoimg3 = ImageTk.PhotoImage(img3)

                # bg_img = Label(self.root, image=self.photoimg3)
                # bg_img.place(x=0, y=0, width=2100, height=1030)
                identity_label = cv2.rectangle(
                    img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                # main_frame = Frame(bg_img, bd=2)
                # main_frame.place(x=40, y=170, width=1840, height=850)

                id, predict = clf.predict(
                    gray_image[y:y+h, x:x+w])  # prediction formula
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="123", database="face_recoginizer")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "select Name from student where StudentId="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                # my_cursor.execute(
                #     "select StudentId from student where StudentId="+str(id))
                # r = my_cursor.fetchone()
                # r = "+".join(r)

                my_cursor.execute(
                    "select Dept from student where StudentId="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute(
                    "select StudentId from student where StudentId="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                img = cv2.rectangle(img, (0, 0), (0 + 450, 0 + 135),
                                    (208, 208, 208), -1)
                img = cv2.putText(img, f"ID:{i}",
                                  (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3)
                img = cv2.putText(img, f"Name:{n}",
                                  (20, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3)
                img = cv2.putText(img, f"Department:{d}",
                                  (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3)
                # font = cv2.FONT_HERSHEY_SIMPLEX
                datet = str(datetime.now())
                cv2.putText(img, datet, (20, 110),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3)

                if confidence > 77:
                    cv2.putText(
                        img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    # cv2.putText(
                    #     img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, n,  d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(
                        img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundry(img, faceCascade, 1.1, 10,
                                 (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)

        # main_frame = Frame(video_cap)
        # main_frame.place(width=1840, height=850)
        def rescale_frame(img, percent=75):
            width = int(img.shape[1] * percent / 100)
            height = int(img.shape[0] * percent / 100)
            dim = (width, height)
            return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            # frame75 = rescale_frame(img, percent=75)
            # cv2.imshow('frame75', frame75)
            frame150 = rescale_frame(img, percent=180)

            cv2.imshow('frame150', frame150)

            # cv2.imshow("Welcome to Face Recogintion", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()

        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
