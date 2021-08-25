from tkinter.ttk import Label, Entry, Button, Frame, Scrollbar, Style
from tkinter import Listbox, StringVar, Tk, Text
from tkinter.constants import *
from contact_funcs import delete, insert, convert, connect, update, view, search

win = Tk()
win.geometry('700x550')
win.title('Contact NoteBook')
win.resizable(width=False, height=False)
connect()

def clear_command():
    txt_id.delete(0, END)
    txt_name.delete(0, END)
    txt_family.delete(0, END)
    txt_email.delete(0, END)
    txt_phone.delete(0, END)
    txt_fax.delete(0, END)
    txt_addrress.delete(0, END)
    txt_fact_phone.delete(0, END)
    txt_home_phone.delete(0, END)
    txt_work_phone.delete(0, END)
    txt_desc.delete('1.0', END)


def clear_list():
    contact_listbox.delete(0, END)


def fill_list(contacts):
    for cont in contacts:
        contact_listbox.insert(END, cont)


def exit_app():
    win.destroy()


# ================== Variables =====================
c_id = StringVar()
c_name = StringVar()
c_family = StringVar()
c_email = StringVar()
c_phone = StringVar()
c_fax = StringVar()
c_addr = StringVar()
c_fact_phone = StringVar()
c_home_phone = StringVar()
c_work_phone = StringVar()
c_desc = StringVar()


# ================== Labels ========================
lbl_id = Label(win, text="Id : ")
lbl_id.grid(row=0, column=0, pady=10, padx=10)
# --------------------------------------------------

lbl_name = Label(win, text="Name : ")
lbl_name.grid(row=1, column=0, pady=10, padx=10)
# --------------------------------------------------

lbl_family = Label(win, text="Family : ")
lbl_family.grid(row=2, column=0, pady=10, padx=10)
# --------------------------------------------------

lbl_email = Label(win, text="Email : ")
lbl_email.grid(row=3, column=0, pady=10, padx=10)
# --------------------------------------------------

lbl_phone = Label(win, text="Phone : ")
lbl_phone.grid(row=4, column=0, pady=10, padx=10)
# --------------------------------------------------

lbl_fax = Label(win, text="Fax : ")
lbl_fax.grid(row=5, column=0, pady=10, padx=10)
# --------------------------------------------------

lbl_addrress = Label(win, text="Addrress : ")
lbl_addrress.grid(row=6, column=0, pady=10, padx=10)
# --------------------------------------------------

lbl_fact = Label(win, text="Factory Phone-Number : ")
lbl_fact.grid(row=7, column=0, pady=10, padx=10)
# --------------------------------------------------

lbl_fact = Label(win, text="Home Phone-Number : ")
lbl_fact.grid(row=8, column=0, pady=10, padx=10)
# --------------------------------------------------

lbl_fact = Label(win, text="Work Phone-Number : ")
lbl_fact.grid(row=9, column=0, pady=10, padx=10)
# --------------------------------------------------

lbl_desc = Label(win, text="Description : ")
lbl_desc.grid(row=10, column=0, pady=10, padx=10)
# ================== TextBoxes =====================
txt_id = Entry(win, textvariable=c_id)
txt_id.grid(row=0, column=1, pady=10, padx=10)

txt_name = Entry(win, textvariable=c_name)
txt_name.grid(row=1, column=1, pady=10, padx=10)

txt_family = Entry(win, textvariable=c_family)
txt_family.grid(row=2, column=1, pady=10, padx=10)

txt_email = Entry(win, textvariable=c_email)
txt_email.grid(row=3, column=1, pady=10, padx=10)

txt_phone = Entry(win, textvariable=c_phone)
txt_phone.grid(row=4, column=1, pady=10, padx=10)

txt_fax = Entry(win, textvariable=c_fax)
txt_fax.grid(row=5, column=1, pady=10, padx=10)

txt_addrress = Entry(win, textvariable=c_addr)
txt_addrress.grid(row=6, column=1, pady=10, padx=10)

txt_fact_phone = Entry(win, textvariable=c_fact_phone)
txt_fact_phone.grid(row=7, column=1, pady=10, padx=10)

txt_home_phone = Entry(win, textvariable=c_home_phone)
txt_home_phone.grid(row=8, column=1, pady=10, padx=10)

txt_work_phone = Entry(win, textvariable=c_work_phone)
txt_work_phone.grid(row=9, column=1, pady=10, padx=10)

txt_desc = Text(win, width=20, height=5)
txt_desc.grid(row=10, column=1, pady=10, padx=10)
# ================== ListBox =======================
s = Style()
s.configure('My.TFrame', background='red')
mail1 = Frame(win, style='My.TFrame')
mail1.place(height=230, width=200, x=460, y=20)
mail1.config()

sb1 = Scrollbar(win)
sb1.place(x=660, y=20, height=230)
sb1.config()

sb2 = Scrollbar(win, orient='horizontal')
sb2.place(x=450, y=250, width=225)
sb2.config()

contact_listbox = Listbox(mail1, width=33, height=15)
contact_listbox.configure(yscrollcommand=sb1.set, xscrollcommand=sb2.set)
contact_listbox.pack()
sb1.configure(command=contact_listbox.yview)
sb2.configure(command=contact_listbox.xview)

def get_selected_row(event):
    global selected_contact

    if len(contact_listbox.curselection()) > 0:
        index = contact_listbox.curselection()[0]
        selected_contact = contact_listbox.get(index)
        # title
        txt_id.delete(0, END)
        txt_id.insert(END, selected_contact[1])
        # title
        txt_name.delete(0, END)
        txt_name.insert(END, selected_contact[2])
        # author
        txt_family.delete(0, END)
        txt_family.insert(END, selected_contact[3])
        # year
        txt_email.delete(0, END)
        txt_email.insert(END, selected_contact[4])
        # isbn
        txt_phone.delete(0, END)
        txt_phone.insert(END, selected_contact[5])
        # isbn
        txt_fax.delete(0, END)
        txt_fax.insert(END, selected_contact[6])
        # isbn
        txt_addrress.delete(0, END)
        txt_addrress.insert(END, selected_contact[7])
        # isbn
        txt_fact_phone.delete(0, END)
        txt_fact_phone.insert(END, selected_contact[8])
        # isbn
        txt_home_phone.delete(0, END)
        txt_home_phone.insert(END, selected_contact[9])
        # isbn
        txt_work_phone.delete(0, END)
        txt_work_phone.insert(END, selected_contact[10])
        # isbn
        txt_desc.delete('1.0', END)
        txt_desc.insert(END, selected_contact[11])


contact_listbox.bind("<<ListboxSelect>>", get_selected_row)


def view_command():
    clear_list()
    contacts = view()
    fill_list(contacts)
# ================== Buttons =======================


def add_command():
    insert(txt_id.get(),
           txt_name.get(),
           txt_family.get(),
           txt_email.get(),
           txt_email.get(),
           txt_fax.get(),
           txt_addrress.get(),
           txt_fact_phone.get(),
           txt_home_phone.get(),
           txt_work_phone.get(),
           convert(txt_desc))
    clear_command()
    view_command()


btn_insert = Button(win, text='Insert')
btn_insert.place(x=440, y=270)
btn_insert.configure(command=add_command)
# --------------------------------------------------


def delete_command():
    delete(str(selected_contact[0]))
    clear_command()
    view_command()


btn_delete = Button(win, text='Delete')
btn_delete.place(x=525, y=270)

btn_delete.configure(command=delete_command)
# --------------------------------------------------


def update_command():
    update(txt_id.get(),
           txt_name.get(),
           txt_family.get(),
           txt_email.get(),
           txt_phone.get(),
           txt_fax.get(),
           txt_addrress.get(),
           txt_fact_phone.get(),
           txt_home_phone.get(),
           txt_work_phone.get(),
           convert(txt_desc))
    view_command()


btn_update = Button(win, text='Update')
btn_update.place(x=610, y=270)
btn_update.configure(command=update_command)
# --------------------------------------------------


def search_command():
    clear_list()
    contacts = search(txt_id.get(), txt_name.get(),
                      txt_family.get(), txt_phone.get())
    fill_list(contacts)


btn_search = Button(win, text='Search')
btn_search.place(x=440, y=305)
btn_search.configure(command=search_command)
# --------------------------------------------------
btn_exit = Button(win, text='Exit')
btn_exit.place(x=525, y=305)
btn_exit.configure(command=exit_app)
# --------------------------------------------------
btn_exit = Button(win, text='Clear all')
btn_exit.place(x=610, y=305)
btn_exit.configure(command=clear_command)
# ==================================================
view_command()
win.mainloop()
