from tkinter import *
from tkinter import ttk
import sqlite3 
from tkinter import messagebox
import addbuku, addmember, pinjambuku

con=sqlite3.connect('Perpus.db')
cur=con.cursor()



class Main (object):
    def __init__ (self,master):
        self.master = master


        def displayStatistik(evt):
            count_books=cur.execute("SELECT count(book_id)FROM books").fetchall()
            count_members = cur.execute("SELECT count(member_id)FROM members").fetchall()
            taken_books = cur.execute("SELECT count(book_status) FROM books WHERE book_status=1").fetchall()
            print(count_books)
            self.lbl_book_count.config(text='Total :'+ str(count_books[0][0])+' buku di perpustakaan')
            self.lbl_member_count.config(text="Total member :"+ str (count_members[0][0]))
            self.lbl_taken_count.config(text="buku yang dipinjam :" + str (taken_books[0][0]))
            displayBooks(self)


        def displayBooks(self):
            books=cur.execute("SELECT * FROM books").fetchall()
            count=0

            self.list_books.delete(0,END)
            for book in books:
                print(book)
                self.list_books.insert(count,str(book[0])+"-"+(book[1]))
                count +=1

            def bookinfo(evt):
                value = str(self.list_books.get(self.list_books.curselection()))
                id = value.split('-')[0]
                book = cur.execute("SELECT * FROM books WHERE book_id=?",(id,))
                book_info = book.fetchall()
                print(book_info)
                self.list_details.delete(0,'end')

                self.list_details.insert(0,"Judul Buku : "+book_info[0][1])
                self.list_details.insert(1,"Penulis : "+book_info[0][2])
                self.list_details.insert(2,"Halaman : "+book_info[0][3])
                self.list_details.insert(3,"Bahasa : "+book_info[0][4])
                if book_info[0][5] ==  0:
                    self.list_details.insert(4,"Status : Tersedia")
                else :
                    self.list_details.insert(4,"Status : Tidak Tersedia")
                
                
            def doubleClick(evt):
                global given_id
                value=str(self.list_books.get(self.list_books.curselection()))
                given_id=value.split('-')[0]
                give_book=GiveBook()
            
            self.list_books.bind('<<ListboxSelect>>',bookinfo)
            self.tabs.bind('<<NotebookTabChanged>>',displayStatistik)
            #self.tabs.bind('<<ButtonRelease-1>',displayBooks)
            self.list_books.bind('<Double-Button-1>',doubleClick)

        #Frame
        mainFrame=Frame(self.master)
        mainFrame.pack()
        #top frames
        topFrame=Frame(mainFrame,width= 1350, height=70, bg="#EBE5E5", padx=20,relief=SUNKEN, borderwidth=2)
        topFrame.pack(side=TOP,fill=X)
        #CenterFrame
        centerFrame =Frame(mainFrame,width=1350,relief=RIDGE,bg='#e0f0f0',height=680)
        centerFrame.pack(side=TOP)
        #centerleftframe
        centerleftFrame=Frame (centerFrame,width=700,height=700,bg='#e0f0f0',borderwidth=3, relief='sunken')
        centerleftFrame.pack (side=LEFT)
        #center Right Frame
        centerRightFrame=Frame(centerFrame,width=450,height=700,bg='#e0f0f0',borderwidth=3, relief='sunken')
        centerRightFrame.pack()

        #Search bar
        self.ent_search= Entry(topFrame,width=30,bd=10)
        self.ent_search.pack(side=RIGHT)
        self.iconsearch=PhotoImage(file='icons/iconsearch.png')
        self.btn_search=Button(topFrame,image=self.iconsearch, command=self.searchBooks)
        self.btn_search.pack(side=RIGHT,padx=5)


        #list Bar
        List_bar = LabelFrame (centerRightFrame,width=420,height=30,bg="#7CDFDF")
        List_bar.pack(fill=BOTH)
        lbl_list=Label(List_bar,text='Kategori',font='times 16 bold',fg="#31044b",bg='#7CDFDF')
        lbl_list.grid(row=0,column=1)
        self.listPilih=IntVar()
        rbl1= Radiobutton (List_bar,text='Semua Buku',var=self.listPilih,value = 1,bg="#2cff9c")
        rbl2= Radiobutton (List_bar,text='Yang tersedia',var=self.listPilih,value = 2,bg="#00c0e2")
        rbl3= Radiobutton (List_bar,text='Tidak Tersedia',var=self.listPilih,value = 3,bg="#f57226")
        rbl1.grid(row=1,column=0,padx=5)
        rbl2.grid(row=1,column=1,padx=5)
        rbl3.grid(row=1,column=2,padx=5)
        btn_list=Button(List_bar,text='Cek Buku',command=self.listBooks)
        btn_list.grid(row=3,column=2,pady=10,padx=7)


        #Gambar dan judul
        gambar_bar=Frame(centerRightFrame)
        gambar_bar.pack(fill=BOTH)
        style = ttk.Style()

        ###############################################Tab####################################################
        self.tabs= ttk.Notebook(centerleftFrame,width=900,height=660)
        self.tabs.pack()
        self.tab1_icon=PhotoImage(file='icons/Perpus.png')
        self.tab2_icon=PhotoImage(file='icons/Stats.png')
        style = ttk.Style()
        style.theme_use()
        style.configure("TNotebook.tab")
        style.configure("TNotebook.Tab", font=('arial', 13, 'bold'))  
        self.tab1 =ttk.Frame(self.tabs)  
        self.tabs.add(self.tab1, text='Perpustakaan', image=self.tab1_icon, compound=LEFT)
        self.tab2 = ttk.Frame (self.tabs)
        self.tabs.add(self.tab2, text='Statistik', image=self.tab2_icon, compound=LEFT)
        

        
         #selamatdatang
        self.selamatdatang = Label (topFrame,text='SELAMAT DATANG DI PERPUSTAKAAN KAMI :)',font='arial 15 bold',pady=5,bg="#EBE5E5")
        self.selamatdatang.pack()


        #Tambahkan Buku
        kiri=LabelFrame(self.tab1,width=90,height=660)
        kiri.pack(fill=BOTH)
        self.iconbook=PhotoImage(file='icons/TambahBuku.png')
        self.btnbook= Button(kiri,text='Tambahkan Buku',image=self.iconbook,compound='left',font='arial 13 bold',height=30,width=200,padx=5,bg="#ca35f0",command=self.addbuku)
        self.btnbook.pack(side=LEFT,padx=50,anchor="nw")
        

        #TambahUser
        
        self.iconmember=PhotoImage(file='icons/user3.png',height=29)
        self.btnmember = Button(kiri,text='Tambahkan Pengguna',font='arial 15 bold', padx=20,bg="#1bee13",command=self.addMember)
        self.btnmember.configure(image=self.iconmember,compound=LEFT)
        self.btnmember.pack(side=LEFT)

        #Ngasih Buku
        self.icongive=PhotoImage(file='icons/givebook.png')
        self.btngive= Button (kiri,text='Pinjam Buku',font='arial 15 bold',image=self.icongive,bg="#f7b80b")
        self.btngive.configure(image=self.icongive,compound=LEFT,command=self.giveBook)
        self.btngive.pack(side=LEFT,padx =50)

    
        



       #List Book
        self.list_books=Listbox(gambar_bar,width=40,height=28,bd=5,font='times 12 bold')
        self.sb=Scrollbar(gambar_bar,orient=VERTICAL)
        self.list_books.grid(row=0,column=0,padx=(10,0),pady=10,sticky=N)
        self.sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=0,sticky=N+S+E)

        ###### List Details
        self.list_details = Listbox (self.tab1,width=80,height=80,bd=5,font='times 15 bold')
        self.list_details.pack()
################################TAB2###################################################
     #Statistik
        self.lbl_book_count=Label(self.tab2,text="NIGGER",pady=20,font='verdana 14 bold')
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count=Label(self.tab2,text="NIGGER",pady=20,font='verdana 14 bold')
        self.lbl_member_count.grid(row=1,sticky=W)
        self.lbl_taken_count=Label(self.tab2,text="NIGGER",pady=20,font='verdana 14 bold')
        self.lbl_taken_count.grid(row=2,sticky=W)


        ###function
        displayBooks(self)
        displayStatistik(self)


    def addbuku (self):
        add=addbuku.Addbuku()

    def addMember(self):
        member = addmember.AddMember()

    def searchBooks(self):
        value = self.ent_search.get()
        search = cur.execute("SELECT * FROM books WHERE book_name LIKE ?",('%'+value+'%',)).fetchall()
        print(search)
        self.list_books.delete(0,END)
        count = 0
        for book in search:
            self.list_books.insert(count,str(book[0])+"-"+book[1])
            count += 1

    def listBooks(self):
        value = self.listPilih.get()
        if value == 1:
            semuabuku = cur.execute("SELECT * FROM books").fetchall()
            self.list_books.delete(0,END)

            count = 0
            for book in semuabuku:
                self.list_books.insert(count,str(book[0])+"-"+book[1])

        elif value == 2:
            buku_di_perpus = cur.execute("SELECT * FROM books WHERE book_status =?",(0,)).fetchall()
            self.list_books.delete(0,END)

            count = 0
            for book in buku_di_perpus:
                self.list_books.insert(count, str(book[0])+"-"+book[1])
                count +=1

        else :
            tidak_tersedia =cur.execute("SELECT * FROM books WHERE book_status =?",(1,)).fetchall()
            self.list_books.delete(0,END)

            count = 0
            for book in tidak_tersedia:
                self.list_books.insert(count,str(book[0])+"-"+book[1])
                count +=1


    def giveBook(self):
        give_book = pinjambuku.GiveBook()


class GiveBook (Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("600x550+550+200")
        self.title("Peminjaman Buku")
        self.resizable(False,False)
        global given_id
        self.book_id = int(given_id)
        query = "SELECT * FROM books"
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
        self.combo_name.current(self.book_id-1)
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






def main ():
    root=Tk()
    app = Main (root)
    root.title ("Management Sistem Perpustakaan") 
    root.geometry("1350x750+350+200")
    root.iconbitmap
    root.mainloop()

if __name__ == '__main__':
    main()

