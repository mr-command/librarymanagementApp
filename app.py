import tkinter as tk
import numpy as np
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import sqlite3
import time
# main window
root = tk.Tk()
root.title("Library Management App")
root.geometry("800x550")
root.resizable(False,False)


# +=== Data Base ===+ #
db = sqlite3.connect("library.db")

cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY , name VARGHAR(255) ,subject VARCHAR(255))")

db.commit()
db.close()

# ===== varables ===== #
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales_data = {month: 0 for month in months}
x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = list(sales_data.values())

var = False

# commands =====================================================

def addbook_panel():
    SidebarLabelRight = tk.Label(width=40,height=18,bg='#000a65',fg='#0277BD',font=5,border=0).place(relx=0.32,rely=0.15)
    Title_Label = tk.Label(bg='#000a65',fg='#0277BD',text="Add Panel",font=5,width=20).place(rely=0.18,relx=0.46)
    title_hr1 = tk.Label(bg='#0277BD',width=50).place(relx=0.38,rely=0.231)
    title_hr2 = tk.Label(bg='#000a65',width=50).place(relx=0.38,rely=0.229)

    #ENTRY === === === ===
    IdEntry = tk.Entry(root,bg='#8e8e8e',border=0,width=35)
    IdEntry.place(relx=0.5,rely=0.3)
    NameEntry = tk.Entry(root,bg='#8e8e8e',border=0,width=35)
    NameEntry.place(relx=0.5,rely=0.4)
    SubjectEntry = tk.Entry(root,bg='#8e8e8e',border=0,width=35)
    SubjectEntry.place(relx=0.5,rely=0.5)
    
    def add_book():
        try:
            GetId = IdEntry.get()
            GetName = NameEntry.get()
            GetSubject = SubjectEntry.get()

            query = "INSERT INTO book(id ,name , subject) VALUES(? , ? , ?)"
            value = (GetId, GetName , GetSubject)

            db = sqlite3.connect("library.db")

            cur = db.cursor()
            cur.execute(query , value)

            db.commit()
            db.close()

            result_lbl = tk.Label(text=f'You Added {GetName}',bg='#000a65',fg='#0277BD')
            result_lbl.place(relx=0.5,rely=0.7)

        except:
            messagebox.showerror("error","error happend")

    #ENTRYS LABEL == == == ==
    IdLabel = tk.Label(bg='#000a65',fg='#0277BD',text='Book Id :').place(relx=0.38,rely=0.3)
    IdLabel = tk.Label(bg='#000a65',fg='#0277BD',text='Book Name :').place(relx=0.38,rely=0.4)
    IdLabel = tk.Label(bg='#000a65',fg='#0277BD',text='Book Subject :').place(relx=0.38,rely=0.5)

    # Button = = = = = = = = =
    Add_btn = tk.Button(width=30,height=1,text=" ..Add.. ",fg="black",bg='#0277BD',border=0,command=add_book).place(relx=0.505,rely=0.6)
    canvas.get_tk_widget().place(relx=12,rely=0.15)
    
def Delete_panel():
    global y , x

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sales_data = {month: 1 for month in months}
    SidebarLabelRight = tk.Label(width=40,height=18,bg='#000a65',fg='#0277BD',font=5,border=0).place(relx=0.32,rely=0.15)
    Title_Label = tk.Label(bg='#000a65',fg='#0277BD',text="Delete Panel",font=5,width=20).place(rely=0.18,relx=0.46)
    title_hr1 = tk.Label(bg='#0277BD',width=50).place(relx=0.38,rely=0.231)
    title_hr2 = tk.Label(bg='#000a65',width=50).place(relx=0.38,rely=0.229)

    #ENTRY === === === ===
    IdEntry = tk.Entry(root,bg='#8e8e8e',border=0,width=35)
    IdEntry.place(relx=0.5,rely=0.3)
    NameEntry = tk.Entry(root,bg='#8e8e8e',border=0,width=35)
    NameEntry.place(relx=0.5,rely=0.4)
    SubjectEntry = tk.Entry(root,bg='#8e8e8e',border=0,width=35)
    SubjectEntry.place(relx=0.5,rely=0.5)
    
    def delete_book():
        try:
            if IdEntry.get() and NameEntry.get() and SubjectEntry.get():
                GetId = IdEntry.get()
                GetName = NameEntry.get()
                GetSubject = SubjectEntry.get()

                query = "DELETE FROM book WHERE id=?"
                value = (GetId,)

                db = sqlite3.connect("library.db")

                cur = db.cursor()
                cur.execute(query , value)

                db.commit()
                db.close()

                current_month = month_menu.get()
                if current_month == "Jan":
                    y[0] += 1
                elif current_month == "Feb":
                    y[1] += 1
                elif current_month == "Mar":
                    y[2] += 1
                elif current_month == "Apr":
                    y[3] += 1
                elif current_month == "May":
                    y[4] += 1
                elif current_month == "Jun":
                    y[5] += 1
                elif current_month == "Jul":
                    y[6] += 1
                elif current_month == "Aug":
                    y[7] += 1
                elif current_month == "Sep":
                    y[8] += 1
                elif current_month == "Oct":
                    y[9] += 1
                elif current_month == "Nov":
                    y[10] += 1
                elif current_month == "Dec":
                    y[-1] += 1

                update()

                result_lbl = tk.Label(text=f'You deleted {GetName}',bg='#000a65',fg='#0277BD')
                result_lbl.place(relx=0.5,rely=0.8)

            else:
                messagebox.showerror("Error","please fill all fields")
        except:
            messagebox.showerror("error","book Not Found")

    def update():
        global sales_data
        if not hasattr(update, "fig_window") or not update.fig_window.winfo_exists():
            update.fig_window = tk.Toplevel(root)
            update.fig_window.geometry("700x500")
            update.fig_window.title("Figure Window")

            fig = Figure(figsize=(7,5),dpi=100)
            plot = fig.add_subplot(111)
            plot.set_facecolor('#00031e')
            plot.set_ylim(1,12)
            plot.set_title("Sell Chart")

            # change Figure color them
            plot.clear()
            fig.patch.set_facecolor('#00031e')
            plot.spines['top'].set_color('#00031e')
            plot.spines['right'].set_color('#00031e')

            if y[-1]<4:
                plot.spines['left'].set_color("red")
                plot.spines['bottom'].set_color("red")
                plot.bar(sales_data.keys(), y ,color="#EC407A")

            elif y[-1] == 4:
                plot.spines['left'].set_color("lightyellow")
                plot.spines['bottom'].set_color("lightyellow")
                plot.bar(sales_data.keys(), y ,color="lightyellow")
            else:
                plot.spines['left'].set_color("lightgreen")
                plot.spines['bottom'].set_color("lightgreen")
                plot.bar(sales_data.keys(), y ,color="lightgreen")

            # change numbers color
            plot.set_xticklabels(months,color='blue')
            plot.set_yticklabels(x,color='blue')
            plot.set_yticklabels(np.arange(0,13,2))

            # input canvas in tkinter
            canvas = FigureCanvasTkAgg(fig, master=update.fig_window)
            canvas.draw()
            canvas.get_tk_widget().place(relx=0,rely=0)

        else:
            # plot settings
            fig = Figure(figsize=(7,5),dpi=100)
            plot = fig.add_subplot(111)
            plot.set_facecolor('#00031e')
            plot.set_ylim(1,12)
            plot.set_title("Sell Chart")

            # change Figure color them
            plot.clear()
            fig.patch.set_facecolor('#00031e')
            plot.spines['top'].set_color('#00031e')
            plot.spines['right'].set_color('#00031e')

            if y[-1]<4:
                plot.spines['left'].set_color("red")
                plot.spines['bottom'].set_color("red")
                plot.bar(sales_data.keys(), y ,color="#EC407A")

            elif y[-1] == 4:
                plot.spines['left'].set_color("lightyellow")
                plot.spines['bottom'].set_color("lightyellow")
                plot.bar(sales_data.keys(), y ,color="lightyellow")
            else:
                plot.spines['left'].set_color("lightgreen")
                plot.spines['bottom'].set_color("lightgreen")
                plot.bar(sales_data.keys(), y ,color="lightgreen")

            # change numbers color
            plot.set_xticklabels(months,color='blue')
            plot.set_yticklabels(x,color='blue')
            plot.set_yticklabels(np.arange(0,13,2))

            # input canvas in tkinter
            canvas = FigureCanvasTkAgg(fig, master=update.fig_window)
            canvas.draw()
            canvas.get_tk_widget().place(relx=0,rely=0)



    #ENTRYS LABEL == == == ==
    IdLabel = tk.Label(bg='#000a65',fg='#0277BD',text='Book Id :').place(relx=0.38,rely=0.3)
    IdLabel = tk.Label(bg='#000a65',fg='#0277BD',text='Book Name :').place(relx=0.38,rely=0.4)
    IdLabel = tk.Label(bg='#000a65',fg='#0277BD',text='Book Subject :').place(relx=0.38,rely=0.5)
    IdLabel = tk.Label(bg='#000a65',fg='#0277BD',text='Select the month :').place(relx=0.38,rely=0.6)

    # Button = = = = = = = = =
    Add_btn = tk.Button(width=30,height=1,text=" ..delete.. ",fg="black",bg='#0277BD',border=0,command=delete_book).place(relx=0.505,rely=0.7)
    canvas.get_tk_widget().place(relx=12,rely=0.15)

    month_menu = tk.StringVar(root)
    month_menu.set("Select a month")
    month_options = tk.OptionMenu(root, month_menu, *months)
    month_options.config(bg='#000a65', fg='#0277BD',borderwidth=0,border=0)
    month_options["menu"].configure(bg='#000a65',fg='#0277BD')
    month_options.place(relx=0.5, rely=0.6)
    
def FInd_Panel():

    SidebarLabelRight = tk.Label(width=40,height=18,bg='#000a65',fg='#0277BD',font=5,border=0).place(relx=0.32,rely=0.15)
    Title_Label = tk.Label(bg='#000a65',fg='#0277BD',text="Find Panel",font=5,width=20).place(rely=0.18,relx=0.46)
    title_hr1 = tk.Label(bg='#0277BD',width=50).place(relx=0.38,rely=0.231)
    title_hr2 = tk.Label(bg='#000a65',width=50).place(relx=0.38,rely=0.229)

    #ENTRY === === === ===
    SubjectEntry = tk.Entry(root,bg='#8e8e8e',border=0,width=35)
    SubjectEntry.place(relx=0.5,rely=0.4)

    
    def Find_book():
        try:    
            get_subject = SubjectEntry.get()
            if get_subject != "":
                query = "SELECT id , name , subject FROM book"
                result = ""

                db = sqlite3.connect("library.db")

                cur = db.cursor()
                items = cur.execute(query)

                for item in items:
                    result += 'name:  ' + item[1] + ', subject:  ' + item[2] + """
"""
                db.commit()
                db.close()
                
                messagebox.showinfo("books found",result)
            else:
                messagebox.showerror("error","plaese fill all fields")
        except:
            messagebox.showerror("error","book not found")

    #ENTRYS LABEL == == == ==
    IdLabel = tk.Label(bg='#000a65',fg='#0277BD',text='Book Subject :').place(relx=0.38,rely=0.4)

    # Button = = = = = = = = =
    Add_btn = tk.Button(width=30,height=1,text=" ..find.. ",fg="black",bg='#0277BD',border=0,command=Find_book).place(relx=0.5,rely=0.5)
    canvas.get_tk_widget().place(relx=12,rely=0.15)


def UpdateBook_Panel():

    SidebarLabelRight = tk.Label(width=40,height=18,bg='#000a65',fg='#0277BD',font=5,border=0).place(relx=0.32,rely=0.15)
    Title_Label = tk.Label(bg='#000a65',fg='#0277BD',text="Update Panel",font=5,width=20).place(rely=0.18,relx=0.46)
    title_hr1 = tk.Label(bg='#0277BD',width=50).place(relx=0.38,rely=0.231)
    title_hr2 = tk.Label(bg='#000a65',width=50).place(relx=0.38,rely=0.229)

    #ENTRY === === === ===
    IdEntry = tk.Entry(root,bg='#8e8e8e',border=0,width=35)
    IdEntry.place(relx=0.5,rely=0.3)
    NameEntry = tk.Entry(root,bg='#8e8e8e',border=0,width=35)
    NameEntry.place(relx=0.5,rely=0.4)
    SubjectEntry = tk.Entry(root,bg='#8e8e8e',border=0,width=35)
    SubjectEntry.place(relx=0.5,rely=0.5)
    
    def update_book():
        try:
            if IdEntry.get() and NameEntry.get() and SubjectEntry.get():

                get_id = IdEntry.get()
                get_subject = SubjectEntry.get()
                get_name = NameEntry.get()

                query = "UPDATE book SET id=? ,name=? ,subject=? WHERE id=?"
                values = (get_id,get_name,get_subject,get_id,)
                db = sqlite3.connect("library.db")

                cur = db.cursor()
                cur.execute(query , values)

                db.commit()
                db.close()

            else:
                messagebox.showerror("error","please fill all fields")
        except:
            messagebox.showerror("error","book not found")
        
        result_lbl = tk.Label(text=f'Your book Updated !',bg='#000a65',fg='#0277BD')
        result_lbl.place(relx=0.5,rely=0.8)

    #ENTRYS LABEL == == == ==
    IdLabel = tk.Label(bg='#000a65',fg='#0277BD',text='Book Id :').place(relx=0.38,rely=0.3)
    IdLabel = tk.Label(bg='#000a65',fg='#0277BD',text='New Name :').place(relx=0.38,rely=0.4)
    IdLabel = tk.Label(bg='#000a65',fg='#0277BD',text='New Subject :').place(relx=0.38,rely=0.5)

    # Button = = = = = = = = =
    Add_btn = tk.Button(width=30,height=1,text=" ..update.. ",fg="black",bg='#0277BD',border=0,command=update_book).place(relx=0.505,rely=0.6)
    canvas.get_tk_widget().place(relx=12,rely=0.15)


# layout ======================================================
SideBarFrameLeft = tk.Frame(root,width=200,height=550,bg='#00063e')
SideBarFrameLeft.pack(side=tk.LEFT)

SideBarFrameRight = tk.Frame(root,width=600,height=550,bg='#00031e')
SideBarFrameRight.pack(side=tk.RIGHT)

SidebarLabelRight = tk.Label(SideBarFrameRight,bg='#00031e')
SidebarLabelRight.place(relx=0.099,rely=0.15)
# Figure =========================================================

# Insert Figure
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
main_x = [1,2,3,4,5,6,7,8,9,10,11,12]
main_y = [0,1,2,3,9,8,7,5,9,11,10,2]

fig = Figure(figsize=(7,5),dpi=85)
plot = fig.add_subplot(111)
plot.set_facecolor('#00031e')
plot.set_xlim(0,12)
# change Figure color them
fig.patch.set_facecolor('#00031e')
plot.spines['top'].set_color('#00031e')
plot.spines['right'].set_color('#00031e')

plot.spines['left'].set_color("red")
plot.spines['bottom'].set_color("red")
plot.plot(main_x,main_y ,color="#EC407A")

# change numbers color
plot.set_xticklabels(months,color='blue')
plot.set_yticklabels(main_y,color='blue')
plot.set_xticklabels(months[0::])
plot.set_yticklabels(np.arange(0,13,2))

# input canvas in tkinter
canvas = FigureCanvasTkAgg(fig, master=SideBarFrameRight)
canvas.draw()
canvas.get_tk_widget().place(relx=0,rely=0.15)

# Titles ==========================================================
title = tk.Label(SideBarFrameRight,font=5,fg='#0277BD',bg='#00063e',text="Library Management App")
title.place(rely=0,relx=0.3)
hr = tk.Label(bg='#0277BD',width=30)
hr.place(rely=0.08,relx=0.48)
hr2 = tk.Label(bg='#00031e',width=30)
hr2.place(rely=0.09,relx=0.48)

title = tk.Label(SideBarFrameLeft,font=2,fg='#0277BD',bg='#00063e',text="sideBar")
title.place(rely=0,relx=0.3)
hr1 = tk.Label(SideBarFrameLeft,bg='#0277BD',width=15)
hr1.place(rely=0.08,relx=0.23)
hr22 = tk.Label(SideBarFrameLeft,bg='#00063e',width=15)
hr22.place(rely=0.09,relx=0.23)

# Panels title ==========================================================

AddPanel = tk.Button(SideBarFrameLeft,text="Add Your book",width=15,fg='#0277BD',bg='#00063e',borderwidth=0,command=addbook_panel)
AddPanel.place(rely=0.15,relx=0.23)

DeletePanel = tk.Button(SideBarFrameLeft,text="Delete Your book",width=15,fg='#0277BD',bg='#00063e',borderwidth=0,command=Delete_panel)
DeletePanel.place(rely=0.25,relx=0.23)

SearchPanel = tk.Button(SideBarFrameLeft,text="Find Your book",width=15,fg='#0277BD',bg='#00063e',borderwidth=0,command=FInd_Panel)
SearchPanel.place(rely=0.35,relx=0.23)

UpdatePanel = tk.Button(SideBarFrameLeft,text="Update Your book",width=15,fg='#0277BD',bg='#00063e',borderwidth=0,command=UpdateBook_Panel)
UpdatePanel.place(rely=0.45,relx=0.23)


root.mainloop()