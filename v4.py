import sqlite3
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                             FUNCTIONS
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def create_table():
    #connect to the database
    con = sqlite3.connect("cemetery.db")
    cur = con.cursor()

    #create table
    cur.execute("CREATE TABLE IF NOT EXISTS burials (Entry_Number TEXT, First_Name TEXT, Other_names TEXT, Last_Name TEXT, Gender TEXT, Description TEXT, DOB TEXT, DOD TEXT, Age INTEGER, Place of death TEXT, Date_Of_Burial TEXT, Sector TEXT, Plot_Number INTEGER)")
    con.commit()
    con.close()
    messagebox.showinfo("Info", "Table created successfully.")

def submit_data():
    #connect to the database
    con = sqlite3.connect("cemetery.db")
    cur = con.cursor()

    #get data from the form
    first_name = f_name_entry.get()
    last_name = l_name_entry.get()
    dob = dob_entry.get()
    dod = dod_entry.get()
    gender = gender_entry.get()
    plot_number = plot_num_entry.get()

    #check for presence of all fields
    if first_name == "" or last_name == "" or dob == "" or dod == "" or gender == "" or plot_number == "":
        messagebox.showerror("Error", "Please fill in all fields.")

    elif gender not in ["Male", "Female", "Unknown"]:
        messagebox.showerror("Error", "Invalid Gender. Gender should be Male or Female. Use 'Unknown if unsure'. ")

    else:
        try:
            #convert plot_number to integer
            plot_number = int(plot_number)
            #insert data into the table
            cur.execute("INSERT INTO burials VALUES (?,?,?,?,?,?)",(first_name, last_name, dob, dod, gender, plot_number))
            con.commit()
            messagebox.showinfo("Info", "Data added successfully.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Plot number already exists.")
        except ValueError:
            messagebox.showerror("Error", "Invalid plot number.")

    con.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                              GUI
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#gui
root = Tk()
root.geometry("400x350")
root.title("Cemetery Data")

create_table

#create and place labels
entry_number = Label(root, text = "Entry Number").place(x = 20, y = 20)
entry_number_entry = Entry(root).place(x = 150, y = 20)

f_name_label = Label(root, text = "First Name").place(x = 20, y = 50)
f_name_entry = Entry(root)
f_name_entry.place(x = 150, y = 50)

o_name_label = Label(root, text = "Other Name(s)").place(x = 20, y = 80)
o_name_entry = Entry(root).place(x = 150, y = 80)

l_name_label = Label(root, text = "Last Name").place(x = 20, y = 110)
l_name_entry = Entry(root).place(x = 150, y = 110)

gender_label = Label(root, text = "Gender").place(x = 20, y = 140)
gender_entry = Entry(root).place(x = 150, y = 140)

description_label = Label(root, text = "Description").place(x = 20, y = 170)
description_entry = Entry(root).place(x = 150, y = 170)

dob_label = Label(root, text = "DOB (dd-mm-yy)").place(x = 20, y = 200)
dob_entry = DateEntry(root, selectmode = "day").place(x = 150, y = 200)

dod_label = Label(root, text = "DOD (dd-mm-yy)").place(x = 20, y = 230)
dod_entry = DateEntry(root, selectmode = "day").place(x = 150, y = 230)

age_label = Label(root, text = "Age at Death:").place(x = 20, y = 260)
q = "50"
age_entry = Label(root, text = "Age at death:" + q)
age_entry.place(x = 150, y = 260)

place_of_death_label = Label(root, text = "Place of Death").place(x = 20, y = 290)
place_of_death_entry = Entry(root).place(x = 150, y = 290)

date_of_burial_label = Label(root, text = "Date of burial").place(x = 20, y = 320)
date_of_burial_entry = Entry(root).place(x = 150, y = 320)

sector_label = Label(root, text = "Sector").place(x = 20, y = 350)
sector_entry = Entry(root).place(x = 150, y = 350)

plot_num_label = Label(root, text = "Plot Number").place(x = 20, y = 380)
plot_num_entry = Entry(root).place(x = 150, y = 380)

is_consecrated = Label(root, text = "In Consecrated ground").place(x = 20, y = 410)

#create buttons
#button = Button(root, text = "Create Table", command = create_table)
submit_button = Button(root, text = "Submit", command = submit_data)


#place buttons on the gui
#button.place(x = 20, y = 200)
submit_button.place(x = 150, y = 440)



root.mainloop()