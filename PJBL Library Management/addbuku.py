from tkinter import *
from tkinter import messagebox
import sqlite3
con = sqlite3.connect("Perpus.db")
cur = con.cursor()



class Addbuku(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("600x550+550+200")
        self.title("Tambahkan Buku")
        self.resizable(False,False)

        ##################Frame####################

        #Topframe
        self.topFrame= Frame (self,height=150,bg="white")
        self.topFrame.pack(fill=X)
        #Button Frame
        self.bottomFrame=Frame(self,height=400,bg="#fcc324")
        self.bottomFrame.pack(fill=X)
        #Heading Foto dan tanggal
        self.top_image = PhotoImage (file="icons/TambahBukuBIG.png")
        top_image_lbl = Label (self.topFrame,image=self.top_image,bg="white")
        top_image_lbl.place(x=50,y=-55)
        heading= Label(self.topFrame,text="Tambahkan Buku",font="arial 22 bold",fg="#003f8a",bg='white')
        heading.place(x=320,y=60)


        ############################# Masuk Dan Label #########################

        #home
        self.lbl_name=Label(self.bottomFrame,text="Judul :",font="arial 15 bold",fg="white",bg="#fcc324")
        self.lbl_name.place(x=40,y=40)
        self.masuk_name = Entry (self.bottomFrame,width=30,bd=3)
        self.masuk_name.insert(0,"Masukan Judul Buku")
        self.masuk_name.place(x=150,y=45)

        # author
        self.lbl_penulis=Label(self.bottomFrame,text="Penulis :",font="arial 15 bold",fg="white",bg="#fcc324")
        self.lbl_penulis.place(x=40,y=80)
        self.masuk_penulis = Entry (self.bottomFrame,width=30,bd=3)
        self.masuk_penulis.insert(0,"Masukan Nama Penulis Buku")
        self.masuk_penulis.place(x=150,y=85)

        #Halaman
        self.lbl_halaman=Label(self.bottomFrame,text="Halaman :",font="arial 15 bold",fg="white",bg="#fcc324")
        self.lbl_halaman.place(x=40,y=120)
        self.masuk_halaman = Entry (self.bottomFrame,width=30,bd=3)
        self.masuk_halaman.insert(0,"Masukan Halaman Buku")
        self.masuk_halaman.place(x=150,y=125)

         #Bahasa
        self.lbl_bahasa=Label(self.bottomFrame,text="Bahasa :",font="arial 15 bold",fg="white",bg="#fcc324")
        self.lbl_bahasa.place(x=40,y=160)
        self.masuk_bahasa = Entry (self.bottomFrame,width=30,bd=3)
        self.masuk_bahasa.insert(0,"Masukan Bahasa Buku")
        self.masuk_bahasa.place(x=150,y=165)
        #Button
        button = Button(self.bottomFrame,text="Tambahkan Buku",command=self.addBuku)
        button.place(x=240,y=200)

    def addBuku(self):
        nama = self.masuk_name.get().strip()
        penulis = self.masuk_penulis.get().strip()
        halaman = self.masuk_halaman.get().strip()
        bahasa = self.masuk_bahasa.get().strip()

        if (nama and penulis and halaman and bahasa):
            try:
                
                halaman = int(halaman)

    
                query = "INSERT INTO books (book_name, book_author, book_page, book_language) VALUES (?, ?, ?, ?)"
                cur.execute(query, (nama, penulis, halaman, bahasa))
                con.commit()
                con.close()

                messagebox.showinfo("Berhasil", "Buku berhasil ditambahkan.", icon="info")
                self.destroy()
            except Exception as e:
                   messagebox.showerror("Terjadi Error", f"Tidak dapat ditambahkan:\n{str(e)}", icon="warning")
        else:
            messagebox.showerror("Terjadi Error", "Semua Tabel wajib diisi.", icon="warning")