import sqlite3
from tkinter import *
from tkinter import messagebox

def create_table():
    #connect to the database
    con = sqlite3.connect("cemetery.db")
    cur = con.cursor()

    #create table
    cur.execute("CREATE TABLE IF NOT EXISTS plots (First_Name TEXT, Last_Name TEXT, DOB TEXT, DOD TEXT, Gender TEXT, Plot_Number INTEGER)")
    con.commit()
    con.close()
    messagebox.showinfo("Info", "Table created successfully.")

def submit_data():
    #connect to the database
    con = sqlite3.connect("cemetery1.db")
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
    elif gender not in ["Male", "Female"]:
        messagebox.showerror("Error", "Invalid Gender. Gender should be Male or Female.")
    else:
        try:
            #convert plot_number to integer
            plot_number = int(plot_number)
            #insert data into the table
            cur.execute("INSERT INTO plots VALUES (?,?,?,?,?,?)",(first_name, last_name, dob, dod, gender, plot_number))
            con.commit()
            messagebox.showinfo("Info", "Data added successfully.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Plot number already exists.")
        except ValueError:
            messagebox.showerror("Error", "Invalid plot number.")

    con.close()

#gui
root = Tk()
root.geometry("400x350")
root.title("Cemetery Data")

#create labels
f_name_label = Label(root, text = "First Name")
l_name_label = Label(root, text = "Last Name")
dob_label = Label(root, text = "DOB (yyyy-mm-dd)")
dod_label = Label(root, text = "DOD (yyyy-mm-dd)")
gender_label = Label(root, text = "Gender")
plot_num_label = Label(root, text = "Plot Number")

#create entries
f_name_entry = Entry(root)
l_name_entry = Entry(root)
dob_entry = Entry(root)
dod_entry = Entry(root)
gender_entry = Entry(root)
plot_num_entry = Entry(root)

#create buttons
create_table
button = Button(root, text = "Create Table", command = create_table)
submit_button = Button(root, text = "Submit", command = submit_data)

#place labels and entries on the gui
f_name_label.place(x = 20, y = 20)
f_name_entry.place(x = 150, y = 20)
l_name_label.place(x = 20, y = 50)
l_name_entry.place(x = 150, y = 50)
dob_label.place(x = 20, y = 80)
dob_entry.place(x = 150, y = 80)
dod_label.place(x = 20, y = 110)
dod_entry.place(x = 150, y = 110)
gender_label.place(x = 20, y = 140)
gender_entry.place(x = 150, y = 140)
plot_num_label.place(x = 20, y = 170)
plot_num_entry.place(x = 150, y = 170)

#place buttons on the gui
button.place(x = 20, y = 200)
submit_button.place(x = 150, y = 200)

root.mainloop()