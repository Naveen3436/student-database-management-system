from tkinter import *
import tkinter.messagebox
import student_backend as pb  # Make sure you have student_backend.py with the right functions

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.root.geometry("1400x585+0+0")
        self.root.config(bg="black")

        # Assign variables
        self.stdId = StringVar()
        self.Firstname = StringVar()
        self.Surname = StringVar()
        self.DoB = StringVar()
        self.Age = StringVar()
        self.Gender = StringVar()
        self.Address = StringVar()
        self.Mobile = StringVar()

        ######## FUNCTIONS ########
        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Catalogs", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()

        def clearData():
            self.txtStdId.delete(0, END)
            self.txtFirstname.delete(0, END)
            self.txtSurname.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtMobile.delete(0, END)

        def addData():
            if len(self.stdId.get()) != 0:
                pb.addStdRec(self.stdId.get(), self.Firstname.get(), self.Surname.get(), self.DoB.get(),
                             self.Age.get(), self.Gender.get(), self.Address.get(), self.Mobile.get())
                self.studentlist.delete(0, END)
                self.studentlist.insert(END, (self.stdId.get(), self.Firstname.get(), self.Surname.get(), self.DoB.get(),
                                              self.Age.get(), self.Gender.get(), self.Address.get(), self.Mobile.get()))

        def DisplayData():
            self.studentlist.delete(0, END)
            for row in pb.viewData():
                self.studentlist.insert(END, row)

        def StudentRec(event):
            if self.studentlist.curselection():
                index = self.studentlist.curselection()[0]
                self.sd = self.studentlist.get(index)
                self.txtStdId.delete(0, END)
                self.txtStdId.insert(END, self.sd[0])
                self.txtFirstname.delete(0, END)
                self.txtFirstname.insert(END, self.sd[1])
                self.txtSurname.delete(0, END)
                self.txtSurname.insert(END, self.sd[2])
                self.txtDoB.delete(0, END)
                self.txtDoB.insert(END, self.sd[3])
                self.txtAge.delete(0, END)
                self.txtAge.insert(END, self.sd[4])
                self.txtGender.delete(0, END)
                self.txtGender.insert(END, self.sd[5])
                self.txtAddress.delete(0, END)
                self.txtAddress.insert(END, self.sd[6])
                self.txtMobile.delete(0, END)
                self.txtMobile.insert(END, self.sd[7])

        def DeleteData():
            if hasattr(self, 'sd'):
                pb.deleteRec(self.sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            self.studentlist.delete(0, END)
            for row in pb.searchData(self.stdId.get(), self.Firstname.get(), self.Surname.get(), self.DoB.get(),
                                     self.Age.get(), self.Gender.get(), self.Address.get(), self.Mobile.get()):
                self.studentlist.insert(END, row)

        def update():
            if hasattr(self, 'sd'):
                pb.deleteRec(self.sd[0])  # Delete old record
                pb.addStdRec(self.stdId.get(), self.Firstname.get(), self.Surname.get(), self.DoB.get(),
                             self.Age.get(), self.Gender.get(), self.Address.get(), self.Mobile.get())  # Add new one
                DisplayData()

        ################## GUI LAYOUT ##################

        MainFrame = Frame(self.root, bg="white")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=1, padx=54, pady=8, bg="sky blue", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'),
                            text="Students Database Management System", bg="sky blue", fg="black")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=1, width=1400, height=70, padx=18, pady=10, bg="sky blue", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=9, width=1400, height=400, padx=20, pady=20, bg="#555", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, font=('arial', 12, 'bold'), bd=1, width=450, height=300,
                                   bg="Ghost White", relief=RIDGE, text="STUDENT INFO\n")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, font=('arial', 12, 'bold'), bd=1, width=450, height=300,
                                    bg="Ghost White", relief=RIDGE, text="STUDENT DETAILS\n")
        DataFrameRight.pack(side=RIGHT)

        # Entry fields
        labels = ["Student ID:", "First Name:", "Surname:", "Date of Birth:", "Age:", "Gender:", "Address:", "Mobile:"]
        vars = [self.stdId, self.Firstname, self.Surname, self.DoB, self.Age, self.Gender, self.Address, self.Mobile]
        entry_refs = []

        for i, (label, var) in enumerate(zip(labels, vars)):
            lbl = Label(DataFrameLeft, font=('arial', 12, 'bold'), text=label, bg="ghost white", padx=2, pady=3)
            lbl.grid(row=i, column=0, sticky=W)
            entry = Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=var, bg="ghost white", width=39)
            entry.grid(row=i, column=1)
            entry_refs.append(entry)

        # Store Entry widgets
        (self.txtStdId, self.txtFirstname, self.txtSurname, self.txtDoB, self.txtAge,
         self.txtGender, self.txtAddress, self.txtMobile) = entry_refs

        # Listbox + scrollbar
        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky='ns')

        self.studentlist = Listbox(DataFrameRight, width=68, height=12, font=('arial', 12, 'bold'),
                                   yscrollcommand=scrollbar.set)
        self.studentlist.bind('<<ListboxSelect>>', StudentRec)
        self.studentlist.grid(row=0, column=0, padx=10)
        scrollbar.config(command=self.studentlist.yview)

        # Buttons
        buttons = [("Add New", addData), ("Display", DisplayData), ("Clear", clearData),
                   ("Delete", DeleteData), ("Search", searchDatabase), ("Update", update), ("Exit", iExit)]

        for idx, (text, cmd) in enumerate(buttons):
            btn = Button(ButtonFrame, text=text, font=('arial', 20, 'bold'), height=1, width=10, bd=4, fg="#555",
                         command=cmd)
            btn.grid(row=0, column=idx)


# Main Entry
if __name__ == "__main__":
    root = Tk()
    application = Student(root)
    root.mainloop()
