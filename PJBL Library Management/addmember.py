from tkinter import *
from tkinter import messagebox
import sqlite3
con = sqlite3.connect("Perpus.db")
cur = con.cursor()



class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("600x550+550+200")
        self.title("Tambahkan Pengguna")
        self.resizable(False,False)

        ##################Frame####################

        #Topframe
        self.topFrame= Frame (self,height=150,bg="white")
        self.topFrame.pack(fill=X)
        #Button Frame
        self.bottomFrame=Frame(self,height=400,bg="#fcc324")
        self.bottomFrame.pack(fill=X)
        #Heading Foto dan tanggal
        self.top_image = PhotoImage (file="icons/PenggunaBIG1.png")
        top_image_lbl = Label (self.topFrame,image=self.top_image,bg="white")
        top_image_lbl.place(x=40,y=-27)
        heading= Label(self.topFrame,text="Tambahkan Pengguna",font="arial 22 bold",fg="#003f8a",bg='white')
        heading.place(x=260,y=60)


        ############################# Masuk Dan Label #########################

        #Member Name
        self.lbl_name=Label(self.bottomFrame,text="Pengguna :",font="arial 15 bold",fg="white",bg="#fcc324")
        self.lbl_name.place(x=40,y=40)
        self.masuk_name = Entry (self.bottomFrame,width=30,bd=3)
        self.masuk_name.insert(0,"Masukan Nama Pengguna")
        self.masuk_name.place(x=150,y=45)

        # phone
        self.lbl_phone=Label(self.bottomFrame,text="Phone :",font="arial 15 bold",fg="white",bg="#fcc324")
        self.lbl_phone.place(x=40,y=80)
        self.masuk_phone = Entry (self.bottomFrame,width=30,bd=3)
        self.masuk_phone.insert(0,"Masukan No Pengguna")
        self.masuk_phone.place(x=150,y=85)

        #Button
        button = Button(self.bottomFrame,text="Tambahkan phone",command=self.addMember)
        button.place(x=240,y=120)

    def addMember(self):
        nama = self.masuk_name.get().strip()
        phone = self.masuk_phone.get().strip()

        if (nama and phone):

            try:
                phone = int (phone)
                query = "INSERT INTO members (member_name, member_phone) VALUES (?, ?)"
                cur.execute(query, (nama, phone))
                con.commit()
                messagebox.showinfo("Berhasil", "Pengguna berhasil ditambahkan.", icon="info")
            except :
        
                messagebox.showerror("Terjadi Error", f"Tidak dapat ditambahkan Phone Harus berupa angka", icon="warning")
        else:
             messagebox.showerror("Terjadi Error", "Semua tabel wajib diisi.", icon="warning")