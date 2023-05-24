from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Reecoginition System")

    # Variable
        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

    # bg image
        img3 = Image.open(
            r"C:\Users\mluqm\OneDrive\Desktop\face_recoginition_system\student_portal\attendancemainimg.png")
        img3 = img3.resize((2100, 1030), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=2100, height=1030)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=40, y=190, width=1840, height=850)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details", font=(
            "times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=900, height=500)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE)
        left_inside_frame.place(x=40, y=30, width=780, height=400)

        #label and entry

        # attendance ID

        attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=(
            "times new roman", 12, "bold"))
        attendanceId_label.grid(row=0, column=0, padx=4, pady=10)

        attendanceId_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_id, width=20, font=(
            "times new roman", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=4, pady=10)

        # Name

        nameLabel = Label(left_inside_frame, text="Name:", font=(
            "comicsansns", 12, "bold"))
        nameLabel.grid(row=0, column=2, padx=4, pady=10)

        atten_name = ttk.Entry(left_inside_frame, textvariable=self.var_atten_name,  width=20, font=(
            "comicsansns", 12, "bold"))
        atten_name.grid(row=0, column=3, padx=4, pady=10)

        # Dept

        depLabel = Label(left_inside_frame, text="Department:", font=(
            "comicsansns", 12, "bold"))
        depLabel.grid(row=1, column=0, padx=4, pady=10)

        atten_dep = ttk.Entry(left_inside_frame, textvariable=self.var_atten_dep,  width=20, font=(
            "comicsansns", 12, "bold"))
        atten_dep.grid(row=1, column=1, padx=4, pady=10)

        # Time

        timeLabel = Label(left_inside_frame, text="Time:", font=(
            "comicsansns", 12, "bold"))
        timeLabel.grid(row=1, column=2, padx=4, pady=10)

        atten_time = ttk.Entry(left_inside_frame, textvariable=self.var_atten_time,  width=20, font=(
            "comicsansns", 12, "bold"))
        atten_time.grid(row=1, column=3, padx=4, pady=10)

        # Date

        dateLabel = Label(left_inside_frame, text="Date:", font=(
            "comicsansns", 12, "bold"))
        dateLabel.grid(row=2, column=0, padx=4, pady=10)

        atten_date = ttk.Entry(left_inside_frame, textvariable=self.var_atten_date,  width=20, font=(
            "comicsansns", 12, "bold"))
        atten_date.grid(row=2, column=1, padx=4, pady=10)

        # Attendance

        attendanceLabel = Label(left_inside_frame, text="Attendance Satus:", font=(
            "comicsansns", 12, "bold"))
        attendanceLabel.grid(row=3, column=0, padx=4, pady=10)

        self.atten_status = ttk.Combobox(
            left_inside_frame, textvariable=self.var_atten_attendance, width=20, font=("comicsansns", 12, "bold"))
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, padx=4, pady=10)
        self.atten_status.current(0)

        # button  frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=300, width=817, height=37)

        import_btn = Button(btn_frame, text="Import CSV", command=self.importCsv, width=22, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export CSV", command=self.exportCSV, width=21, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame,  text="Update", width=22, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=22, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details", font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=920, y=10, width=900, height=500)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=30, width=750, height=370)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(
            table_frame, column=("id", "name", "Dept",  "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="StudentID")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("Dept", text="Department")
        # self.AttendanceReportTable.heading("course", text="Course")
        # self.AttendanceReportTable.heading("year", text="Year")
        # self.AttendanceReportTable.heading("sem", text="Semester")

        # self.AttendanceReportTable.heading("Sec", text="Section")
        # self.AttendanceReportTable.heading("gender", text="Gender")
        # self.AttendanceReportTable.heading("email", text="Email")
        # self.AttendanceReportTable.heading("phone", text="Phone")
        # self.AttendanceReportTable.heading("address", text="Address")
        # self.AttendanceReportTable.heading("dob", text="DOB")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        # self.AttendanceReportTable.heading("teacher", text="Teacher Name")
        # self.AttendanceReportTable.heading("photo", text="PhotoSampleStatus")
        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("Dept", width=100)
        # self.AttendanceReportTable.column("course", width=100)
        # self.AttendanceReportTable.column("year", width=100)
        # self.AttendanceReportTable.column("sem", width=100)
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("name", width=100)
        # self.AttendanceReportTable.column("Sec", width=100)
        # self.AttendanceReportTable.column("gender", width=100)
        # self.AttendanceReportTable.column("email", width=100)
        # self.AttendanceReportTable.column("phone", width=100)
        # self.AttendanceReportTable.column("address", width=100)
        # self.AttendanceReportTable.column("dob", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
        # self.AttendanceReportTable.column("teacher", width=100)
        # self.AttendanceReportTable.column("photo", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        # self.fetchData()

    # Fetch Data

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File", "*.csv"), ("ALl File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # Export Csv

    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "Error", "No data Found", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
                ("CSV File", "*.csv"), ("ALl File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data is exported")
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to:{str(es)}", parent=self.root)

    # get cursor

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_attendance.set(rows[5])

    # reset function
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set(""),
        self.var_atten_dep.set(""),
        self.var_atten_time.set(""),
        self.var_atten_date.set(""),
        self.var_atten_attendance.set(""),


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
