from tkinter import *
from tkinter import ttk
import sqlite3 
from tkinter import messagebox

con=sqlite3.connect('Perpus.db')
cur=con.cursor()


class GiveBook (Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("600x550+550+200")
        self.title("Peminjaman Buku")
        self.resizable(False,False)

        query = "SELECT * FROM books WHERE book_status=0"
        books = cur.execute(query).fetchall()
        book_list = []
        for book in books:
            book_list.append(str(book[0])+ "-"+book[1])
            
        query2="SELECT * FROM members"
        members = cur.execute(query2).fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0])+"-"+member[1])

        
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
        heading= Label(self.topFrame,text="Pinjam Buku",font="arial 22 bold",fg="#003f8a",bg='white')
        heading.place(x=260,y=60)


        ############################# Masuk Dan Label #########################

        #Judul Buku
        self.book_name = StringVar()
        self.lbl_name=Label(self.bottomFrame,text="Buku :" ,font="arial 15 bold",fg="white",bg="#fcc324")
        self.lbl_name.place(x=40,y=40)
        self.combo_name = ttk.Combobox(self.bottomFrame,textvariable=self.book_name)
        self.combo_name ['values']=book_list
        self.combo_name.place(x=180,y=45)


        # Nama Peminjam / Pengguna
        self.member_name = StringVar()
        self.lbl_phone=Label(self.bottomFrame,text="Pengguna :",font="arial 15 bold",fg="white",bg="#fcc324")
        self.lbl_phone.place(x=40,y=80)
        self.combo_member = ttk.Combobox(self.bottomFrame,textvariable=self.member_name)
        self.combo_member['values']= member_list
        self.combo_member.place(x=180,y=85)

        #Button
        button = Button(self.bottomFrame,text="Pinjam Buku",command=self.pinjambuku)
        button.place(x=240,y=120)

    def pinjambuku(self):
        book_name =self.book_name.get()
        self.book_id=book_name.split('-')[0]
        member_name = self.member_name.get()
        
        if (book_name and member_name !=""):
            try:
                query="INSERT INTO 'borrows' (bbook_id,bmember_id) VALUES(?,?)"
                cur.execute(query,(book_name,member_name))
                con.commit()
                messagebox.showinfo("Berhasil","Berhasil Meminjam",icon='info')
                cur.execute("UPDATE books SET book_status =? WHERE book_id=?",[1,self.book_id])
                con.commit()
            

            except:
              messagebox.showerror("Error","Gagal Meminjam",icon='warning')

        else:
            messagebox.showerror("Error","Tabel tidak boleh kosong",icon='warning')
