# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os


# class Developer:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Reecoginition System")

#         # bg image
#         img3 = Image.open(
#             r"C:\Users\mluqm\OneDrive\Desktop\face_recoginition_system\student_portal\developertab.png")
#         img3 = img3.resize((2100, 1030), Image.ANTIALIAS)
#         self.photoimg3 = ImageTk.PhotoImage(img3)

#         bg_img = Label(self.root, image=self.photoimg3)
#         bg_img.place(x=0, y=0, width=2100, height=1030)

#         main_frame = Frame(bg_img, bd=2)
#         main_frame.place(x=1100, y=200, width=600, height=780)

#         # developer info
#         dev_Label = Label(main_frame, text="Developer:", font=(
#             "comicsansns", 12, "bold"))
#         dev_Label.place(row=1, column=0, padx=4, pady=10)


# if __name__ == "__main__":
#     root = Tk()
#     obj = Developer(root)
#     root.mainloop()
# --------------------------------------------------------------------------


# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# import numpy as np
# from time import strftime
# from datetime import datetime

# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from tkcalendar import *
from tkcalendar import Calendar, DateEntry
import calendar
import datetime
import psycopg2


# class Developer:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Reecoginition System")

#         self.var_atten_id = StringVar()
#         self.var_atten_name = StringVar()
#         self.var_atten_dep = StringVar()

#         # bg image
#         img3 = Image.open(
#             r"C:\Users\mluqm\OneDrive\Desktop\face_recoginition_system\student_portal\facerecogmain.png")
#         img3 = img3.resize((2100, 1030), Image.ANTIALIAS)
#         self.photoimg3 = ImageTk.PhotoImage(img3)

#         bg_img = Label(self.root, image=self.photoimg3)
#         bg_img.place(x=0, y=0, width=2100, height=1030)

#         b1 = Button(self.root, text="Face Recoginition", cursor="hand2",  font=(
#             "times new roman", 30, "bold"), bg="darkblue", fg="white", command=self.open_win)
#         b1.place(x=550, y=500, width=1000, height=60)

#     def mark_attendance(self, i, n, d):
#         with open("attended.csv", "r+", newline="\n") as f:
#             myDataList = f.readlines()
#             namme_list = []
#             for line in myDataList:
#                 entry = line.split((","))
#                 namme_list.append(entry[0])
#             if ((i not in namme_list) and (n not in namme_list) and (d not in namme_list)):
#                 now = datetime.now()
#                 d1 = now.strftime("%d/%m/%Y")
#                 dtString = now.strftime("%H:%M:%S")
#                 f.writelines(f"\n{i},{n},{d},{dtString},{d1},Present")

#     def open_win(self):
#         new = Toplevel(root)
#         new.geometry("750x250")
#         new.title("New Window")
#         # Create a Label in New window
#         Label(new, text="Hey, Howdy?", font=(
#             'Helvetica 17 bold')).pack(pady=30)

#         main_frame = Frame(new, bd=2)
#         main_frame.place(x=40, y=170, width=1840, height=850)
#         b2 = Button(main_frame, text="Face Recoginition", cursor="hand2",  font=(
#             "times new roman", 30, "bold"), bg="darkblue", fg="white", command=self.face_recog)
#         b2.place(x=550, y=500, width=1000, height=60)

#         # left label frame
#         Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",  font=(
#             "times new roman", 12, "bold"))
#         Left_frame.place(x=10, y=10, width=900, height=800)

#         # Right Frame
#         Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details", font=(
#             "times new roman", 12, "bold"))
#         Right_frame.place(x=920, y=10, width=900, height=500)

#     def face_recog(self):
#         def draw_boundry(img, classifier, scaleFacetor, minNeighbors, color, text, clf):
#             gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(
#                 gray_image, scaleFacetor, minNeighbors)

#             coord = []
#             for (x, y, w, h) in features:

#                 identity_label = cv2.rectangle(
#                     img, (x, y), (x+w, y+h), (0, 255, 0), 3)

#                 id, predict = clf.predict(
#                     gray_image[y:y+h, x:x+w])  # prediction formula
#                 confidence = int((100*(1-predict/300)))

#                 conn = mysql.connector.connect(
#                     host="localhost", username="root", password="123", database="face_recoginizer")
#                 my_cursor = conn.cursor()
#                 my_cursor.execute(
#                     "select Name from student where StudentId="+str(id))
#                 n = my_cursor.fetchone()
#                 n = "+".join(n)
#                 self.var_atten_name = n

#                 my_cursor.execute(
#                     "select Dept from student where StudentId="+str(id))
#                 d = my_cursor.fetchone()
#                 d = "+".join(d)
#                 self.var_atten_dep = d

#                 my_cursor.execute(
#                     "select StudentId from student where StudentId="+str(id))
#                 i = my_cursor.fetchone()
#                 i = "+".join(i)
#                 self.var_atten_id = i
#                 # --------Working
#                 # cv2.rectangle(img, (x, x), (x + w, y + h), (0, 0, 0), -1)

#                 img = cv2.rectangle(img, (0, 0), (0 + 450, 0 + 135),
#                                     (208, 208, 208), -1)
#                 img = cv2.putText(img, f"ID:{i}",
#                                   (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3)
#                 img = cv2.putText(img, f"Name:{n}",
#                                   (20, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3)
#                 img = cv2.putText(img, f"Department:{d}",
#                                   (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3)
#                 font = cv2.FONT_HERSHEY_SIMPLEX
#                 datet = str(datetime.now())
#                 cv2.putText(img, datet, (20, 110),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3)
#                 if confidence > 77:
#                     cv2.putText(
#                         img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#                     cv2.putText(
#                         img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                     cv2.putText(
#                         img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                     self.mark_attendance(i, n,  d)
#                 else:
#                     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
#                     cv2.putText(
#                         img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                 coord = [x, y, w, h]

#             return coord

#         def recognize(img, clf, faceCascade):
#             coord = draw_boundry(img, faceCascade, 1.1, 10,
#                                  (255, 25, 255), "Face", clf)
#             return img

#         faceCascade = cv2.CascadeClassifier(
#             "haarcascade_frontalface_default.xml")
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.read("classifier.xml")

#         video_cap = cv2.VideoCapture(0)

#         def rescale_frame(img, percent=75):
#             width = int(img.shape[1] * percent / 100)
#             height = int(img.shape[0] * percent / 100)
#             dim = (width, height)
#             return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
#         while True:
#             ret, img = video_cap.read()
#             img = recognize(img, clf, faceCascade)
#             # frame75 = rescale_frame(img, percent=75)
#             # cv2.imshow('frame75', frame75)
#             frame150 = rescale_frame(img, percent=180)

#             cv2.imshow('frame150', frame150)

#             # cv2.imshow("Welcome to Face Recogintion", img)

#             if cv2.waitKey(1) == 13:
#                 break
#         video_cap.release()

#         cv2.destroyAllWindows()

import re


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Reecoginition System")

        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_sec = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # bg image
        img3 = Image.open(
            r"C:\Users\mluqm\OneDrive\Desktop\face_recoginition_system\student_portal\mainimg.png")
        img3 = img3.resize((2100, 1030), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=2100, height=1030)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=40, y=170, width=1840, height=850)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=900, height=800)

        # current course

        current_course_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Current Course Information", font=(
            "times new roman", 12, "bold"))
        current_course_frame.place(x=30, y=50, width=835, height=150)

        # Department
        conn = mysql.connector.connect(
            host="localhost", username="root", password="123", database="face_recoginizer")
        cursor = conn.cursor()
        cursor.execute('SELECT department_degree FROM department')
        values = []
        for row in cursor:
            values.append(row[0])
        cursor.close()
        conn.close()

        dept_label = Label(current_course_frame, text="Department", font=(
            "times new roman", 12, "bold"))
        dept_label.grid(row=0, column=0)

        dept_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dept, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        dept_combo["values"] = values
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=4, pady=10)

        # Course

        course_label = Label(current_course_frame, text="Course", font=(
            "times new roman", 12, "bold"))
        course_label.grid(row=0, column=2)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        course_combo["values"] = ("Select Course",
                                  "CS", "IT", "SE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=4, pady=10)

        # Year

        year_label = Label(current_course_frame, text="Year", font=(
            "times new roman", 12, "bold"))
        year_label.grid(row=1, column=0)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        year_combo["values"] = ("Select Year",
                                "2020-21", "2021-22", "2022-23")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=4, pady=10)

        # Semester
        # conn = psycopg2.connect(
        # "dbname=face_recoginizer user=root password=123")
        # username="root", password="123", database="face_recoginizer"
        # cur = conn.cursor()
        # cur.execute("SELECT id, name FROM student")
        # student = cur.fetchall()

        semester_label = Label(current_course_frame, text="Semester", font=(
            "times new roman", 12, "bold"))
        semester_label.grid(row=1, column=2)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        semester_combo["values"] = ("Select Course", "IT", "CS")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=4, pady=10)

        # student information

        # Right_framestudent_information_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Student Information", font=(
        #     "times new roman", 12, "bold"))
        # student_information_frame.place(x=30, y=200, width=835, height=400)

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=920, y=10, width=900, height=800)

        # student ID

        studentId_label = Label(Right_frame, text="Dep ID:", font=(
            "times new roman", 12, "bold"))
        studentId_label.grid(row=0, column=0, padx=4, pady=10)

        studentId_entry = ttk.Entry(Right_frame, textvariable=self.var_std_id, width=20, font=(
            "times new roman", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=4, pady=10)

        # student name

        # studentname_label = Label(Right_frame, text="Student name:",  font=(
        #     "times new roman", 12, "bold"))
        # studentname_label.grid(row=0, column=2, padx=4, pady=10)

        # studentname_entry = ttk.Entry(Right_frame, textvariable=self.var_std_name, width=20, font=(
        #     "times new roman", 12, "bold"))
        # studentname_entry.grid(row=0, column=3, padx=4, pady=10)

        # student-section class

        # section_label = Label(Right_frame, text="Section:", font=(
        #     "times new roman", 12, "bold"))
        # section_label.grid(row=1, column=0, padx=4, pady=10)

        # section_entry = ttk.Entry(student_information_frame, textvariable=self.var_sec, width=20, font=(
        #     "times new roman", 12, "bold"))
        # section_entry.grid(row=1, column=1, padx=4, pady=10)

        # section_combo = ttk.Combobox(Right_frame, textvariable=self.var_sec, font=(
        #     "times new roman", 12, "bold"), width=17, state="readonly")
        # section_combo["values"] = ("Select Section",
        #                            "A", "B", "C")
        # section_combo.current(0)
        # section_combo.grid(row=1, column=1, padx=4, pady=10)

        # gender class

        # gender_label = Label(Right_frame, text="Gender:", font=(
        #     "times new roman", 12, "bold"))
        # gender_label.grid(row=1, column=2, padx=4, pady=10)

        # gender_entry = ttk.Entry(student_information_frame, textvariable=self.var_gender, width=20, font=(
        #     "times new roman", 12, "bold"))
        # gender_entry.grid(row=1, column=3, padx=4, pady=10)

        # gender_combo = ttk.Combobox(Right_frame, textvariable=self.var_gender, font=(
        #     "times new roman", 12, "bold"), width=17, state="readonly")
        # gender_combo["values"] = ("Select Gender",
        #                           "Male", "Female", "Other")
        # gender_combo.current(0)
        # gender_combo.grid(row=1, column=3, padx=4, pady=10)

        # Email class
        # def validate_entry(P):
        #     # Check the length of the entry
        #     if email_entry.get().isnumeric():
        #         # Set the entry's background to red to indicate an error
        #         email_entry.configure(bg='red')
        #         # Return False to prevent the value from being stored
        #         return False
        #     else:
        #         # Set the entry's background to white to indicate success
        #         email_entry.configure(bg='white')
        #         # Return True to allow the value to be stored
        #         return True

        # .
        # root = tk.Tk()

        email_label = Label(Right_frame, text="Department Name:", font=(
            "times new roman", 12, "bold"))
        email_label.grid(row=2, column=0, padx=4, pady=10)

        email_entry = ttk.Entry(Right_frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 12, "bold"))
        # email_entry.config(validate='focusout',
        #    validatecommand=vcmd, invalidcommand=ivcmd)
        email_entry.grid(row=2, column=1, padx=4, pady=10)

        # def validate(self, value):
        #     # """
        #     # Validat the email entry
        #     # :param value:
        #     # :return:
        #     # """
        #     pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        #     if re.fullmatch(pattern, value) is None:
        #         return False

        #     self.show_message()
        #     return True

        # def on_invalid(self):
        #     # """
        #     # Show the error message if the data is not valid
        #     # :return:
        #     # """
        #     self.show_message('Please enter a valid email', 'red')

        # Contact class

        contact_label = Label(Right_frame, text="Department Course:", font=(
            "times new roman", 12, "bold"))
        contact_label.grid(row=2, column=2, padx=4, pady=10)

        contact_entry = ttk.Entry(Right_frame, textvariable=self.var_phone, width=20, font=(
            "times new roman", 12, "bold"))
        contact_entry.grid(row=2, column=3, padx=4, pady=10)

        # Address class

        address_label = Label(Right_frame, text="Deparmtment ABC:", font=(
            "times new roman", 12, "bold"))
        address_label.grid(row=3, column=0, padx=4, pady=10)

        address_entry = ttk.Entry(Right_frame, textvariable=self.var_address, width=20, font=(
            "times new roman", 12, "bold"))
        address_entry.grid(row=3, column=1, padx=4, pady=10)

        # DOB class
        DOB_label = Label(Right_frame, text="Degree:", font=(
            "times new roman", 12, "bold"))
        DOB_label.grid(row=3, column=2, padx=4, pady=10)

        DOB_entry = ttk.Entry(Right_frame, textvariable=self.var_dob, width=20, font=(
            "times new roman", 12, "bold"))
        DOB_entry.grid(row=3, column=3, padx=4, pady=10)
        # DOB_entry = DateEntry(Right_frame, textvariable=self.var_dob, width=12, year=2019, month=6, day=22,
        #                       background='darkblue', foreground='white', borderwidth=2)
        # DOB_entry.grid(row=3, column=3, padx=4, pady=10)
        # DOB_label = Label(Right_frame, text="DOB:", font=(
        #     "times new roman", 12, "bold"))
        # DOB_label.grid(row=3, column=2, padx=4, pady=10)

        # DOB_entry = ttk.Entry(student_information_frame, textvariable=self.var_dob, width=20, font=(
        #     "times new roman", 12, "bold"))
        # DOB_entry.grid(row=3, column=3, padx=4, pady=10)

        # radio button

        # self.var_radio1 = StringVar()
        # radiobtn1 = ttk.Radiobutton(
        #     student_information_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        # radiobtn1.grid(row=6, column=0)

        # radiobtn2 = ttk.Radiobutton(
        #     student_information_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        # radiobtn2.grid(row=6, column=1)

        # button  frame
        btn_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=6, y=230, width=817, height=37)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=22, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        # update_btn = Button(btn_frame,  text="Update", command=self.update_data, width=22, font=(
        #     "times new roman", 12, "bold"), bg="blue", fg="white")
        # update_btn.grid(row=0, column=1)

        # delete_btn = Button(btn_frame, text="Delete", command=self.delete_data,  width=21, font=(
        #     "times new roman", 12, "bold"), bg="blue", fg="white")
        # delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=22, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # # button  frame
        # btn_frame1 = Frame(student_information_frame, bd=2, relief=RIDGE)
        # btn_frame1.place(x=6, y=265, width=817, height=37)

        # takephoto_btn = Button(btn_frame1, text="Take Photo Sample", command=self.generate_dataset, width=45, font=(
        #     "times new roman", 12, "bold"), bg="blue", fg="white")
        # takephoto_btn.grid(row=0, column=0)

        # updatephoto_btn = Button(btn_frame1, text="Update Photo Sample", width=45, font=(
        #     "times new roman", 12, "bold"), bg="blue", fg="white")
        # updatephoto_btn.grid(row=0, column=1)

        # # right label frame
        # Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
        #     "times new roman", 12, "bold"))
        # Right_frame.place(x=920, y=10, width=900, height=800)

        # Search System

#         search_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search System", font=(
#             "times new roman", 12, "bold"))
#         search_frame.place(x=30, y=50, width=835, height=70)

#         search_label = Label(search_frame, text="Search By:", font=(
#             "times new roman", 15, "bold"))
#         search_label.grid(row=0, column=0, padx=4, pady=10)

#         search_combo = ttk.Combobox(search_frame, font=(
#             "times new roman", 12, "bold"), width=17, state="readonly")
#         search_combo["values"] = ("Select",
#                                   "Roll No", "Phone No")
#         search_combo.current(0)
#         search_combo.grid(row=0, column=1, padx=4, pady=10)

#         search_entry = ttk.Entry(search_frame, width=20, font=(
#             "times new roman", 12, "bold"))
#         search_entry.grid(row=0, column=2, padx=4, pady=10)

#         search_btn = Button(search_frame, text="Search", width=18, font=(
#             "times new roman", 12, "bold"), bg="blue", fg="white")
#         search_btn.grid(row=0, column=3, padx=4)

#         showall_btn = Button(search_frame, text="Show All", width=18, font=(
#             "times new roman", 12, "bold"), bg="blue", fg="white")
#         showall_btn.grid(row=0, column=4, padx=4)

# # table frame

#         table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
#         table_frame.place(x=30, y=140, width=835, height=250)

#         scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
#         scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

#         self.student_table = ttk.Treeview(
#             table_frame, column=("Dept", "course", "year", "sem", "id", "name", "Sec", "gender", "email", "phone", "address", "dob",  "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

#         scroll_x.pack(side=BOTTOM, fill=X)
#         scroll_y.pack(side=RIGHT, fill=Y)
#         scroll_x.config(command=self.student_table.xview)
#         scroll_y.config(command=self.student_table.yview)

#         self.student_table.heading("Dept", text="Department")
#         self.student_table.heading("course", text="Course")
#         self.student_table.heading("year", text="Year")
#         self.student_table.heading("sem", text="Semester")
#         self.student_table.heading("id", text="StudentID")
#         self.student_table.heading("name", text="Name")
#         self.student_table.heading("Sec", text="Section")
#         self.student_table.heading("gender", text="Gender")
#         self.student_table.heading("email", text="Email")
#         self.student_table.heading("phone", text="Phone")
#         self.student_table.heading("address", text="Address")
#         self.student_table.heading("dob", text="DOB")
#         # self.student_table.heading("teacher", text="Teacher Name")
#         self.student_table.heading("photo", text="PhotoSampleStatus")
#         self.student_table["show"] = "headings"
#         self.student_table.column("Dept", width=100)
#         self.student_table.column("course", width=100)
#         self.student_table.column("year", width=100)
#         self.student_table.column("sem", width=100)
#         self.student_table.column("id", width=100)
#         self.student_table.column("name", width=100)
#         self.student_table.column("Sec", width=100)
#         self.student_table.column("gender", width=100)
#         self.student_table.column("email", width=100)
#         self.student_table.column("phone", width=100)
#         self.student_table.column("address", width=100)
#         self.student_table.column("dob", width=100)
#         # self.student_table.column("teacher", width=100)
#         self.student_table.column("photo", width=100)

#         self.student_table.pack(fill=BOTH, expand=1)
#         self.student_table.bind("<ButtonRelease>", self.get_cursor)
#         self.fetch_data()

    # Function Declaration

    def add_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Field are Required.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="123", database="face_recoginizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into department values(%s,%s,%s,%s,%s)", (
                    # self.var_dept.get(),
                    # self.var_course.get(),
                    # self.var_year.get(),
                    # self.var_semester.get(),
                    self.var_std_id.get(),
                    # self.var_std_name.get(),
                    # self.var_sec.get(),
                    # self.var_gender.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_dob.get(),
                    # self.var_radio1.get()


                ))
                conn.commit()
                # self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    # Function Declaration for FrontEnd
    # def fetch_data(self):
    #     conn = mysql.connector.connect(
    #         host="localhost", username="root", password="123", database="face_recoginizer")
    #     my_cursor = conn.cursor()
    #     my_cursor.execute("Select * from department")
    #     data = my_cursor.fetchall()

    #     if len(data) != 0:
    #         self.student_table.delete(*self.student_table.get_children())
    #         for i in data:
    #             self.student_table.insert("", END, values=i)
    #         conn.commit()
    #     conn.close()

    # get cursor
    # def get_cursor(self, event=""):
    #     cursor_focus = self.student_table.focus()
    #     content = self.student_table.item(cursor_focus)
    #     data = content['values']
    #     self.var_dept.set(data[0])
    #     self.var_course.set(data[1])
    #     self.var_year.set(data[2])
    #     self.var_semester.set(data[3])
    #     self.var_std_id.set(data[4])
    #     self.var_std_name.set(data[5])
    #     self.var_sec.set(data[6])
    #     self.var_gender.set(data[7])
    #     self.var_email.set(data[8])
    #     self.var_phone.set(data[9])
    #     self.var_address.set(data[10])
    #     self.var_dob.set(data[11])
    #     self.var_radio1.set(data[12])

    # update Function
    # def update_data(self):
    #     if self.var_dept.get() == "Select Deparment" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
    #         messagebox.showerror(
    #             "Error", "All Field are Required.", parent=self.root)
    #     else:
    #         try:
    #             Update = messagebox.askyesno(
    #                 "Update", "Do you want to update this student details", parent=self.root)
    #             if Update > 0:
    #                 conn = mysql.connector.connect(
    #                     host="localhost", username="root", password="123", database="face_recoginizer")
    #                 my_cursor = conn.cursor()
    #                 my_cursor.execute(
    #                     "UPDATE department SET Email=%s, Phone=%s, Address=%s, Dob=%s WHERE StudentId=%s", (
    #                         # self.var_dept.get(),
    #                         # self.var_course.get(),
    #                         # self.var_year.get(),
    #                         # self.var_semester.get(),
    #                         # self.var_std_name.get(),
    #                         # self.var_sec.get(),
    #                         # self.var_gender.get(),
    #                         self.var_email.get(),
    #                         self.var_phone.get(),
    #                         self.var_address.get(),
    #                         self.var_dob.get(),
    #                         # self.var_radio1.get(),
    #                         self.var_std_id.get()
    #                     ))
    #             else:
    #                 if not Update:
    #                     return
    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()
    #             messagebox.showinfo(
    #                 "Success", "Student details is successfully updated.", parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror(
    #                 "Error", f"Due to:{str(es)}", parent=self.root)
    # delete function

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete", "Do you want to delete student record.", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="123", database="face_recoginizer")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM department Where StudentId=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully Deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    # reset function
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        # self.var_std_name.set(""),
        # self.var_sec.set("Select Section"),
        # self.var_gender.set("Select Gender"),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_dob.set(""),
        # self.var_radio1.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
