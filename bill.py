from tkinter import *

root=Tk()                         #created an instance of the tkinter.Tk class
root.geometry("1000x500")
root.title("BILL MANAGEMENT")
root.resizable(False,False)


def Reset():
    entry_daltadka.delete(0,END)
    entry_paneermasala.delete(0,END)
    entry_methimatar.delete(0,END)
    entry_bhindimasala.delete(0,END)
    entry_matarpaneer.delete(0,END)
    entry_kajucurry.delete(0,END)
    entry_matkiusal.delete(0,END)

def Total():
    try:a1=int(daltadka.get())
    except: a1=0

    try:a2=int(paneermasala.get())
    except: a2=0

    try:a3=int(methimatar.get())
    except: a3=0

    try:a4=int(bhindimasala.get())
    except: a4=0

    try:a5=int(matarpaneer.get())
    except: a5=0

    try:a6=int(kajucurry.get())
    except: a6=0

    try:a7=int(matkiusal.get())
    except: a7=0

    c1=80*a1
    c2=120*a2
    c3=180*a3
    c4=100*a4
    c5=220*a5
    c6=210*a6
    c7=50*a7

    lb1_total=Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="lavender",bg="black")
    lb1_total.place(x=0,y=50)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="plum1")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)

Label(text="BILL MANAGEMENT",bg="black",fg="MistyRose4",font=("calibri bold",33),width="300",height="2").pack()

f=Frame(root,bg="gray",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="MENU",font=("Gabriola",40,"bold"),fg="black",bg="gray").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Dal Tadka.............Rs.80",fg="black",bg="gray").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Panner Masala.....Rs.120",fg="black",bg="gray").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Methi Matar.......Rs.180",fg="black",bg="gray").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Bhindi Masala....Rs.100",fg="black",bg="gray").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Matar Panner......Rs.220",fg="black",bg="gray").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Kaju Curry..........Rs.210",fg="black",bg="gray").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Matki Usal.........Rs.50",fg="black",bg="gray").place(x=10,y=260)

f2=Frame(root,bg="lavender",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=('calibri',20),bg="lavender")
Bill.place(x=120,y=10)

f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

daltadka=StringVar()
paneermasala=StringVar()
methimatar=StringVar()
bhindimasala=StringVar()
matarpaneer=StringVar()
kajucurry=StringVar()
matkiusal=StringVar()
Total_bill=StringVar()

lb1_daltadka=Label(f1,font=("aria",20,'bold'),text="Dal Tadka",width=12,fg="blue4")
lb1_paneermasala=Label(f1,font=("aria",20,'bold'),text="Panner Masala",width=12,fg="blue4")
lb1_methimatar=Label(f1,font=("aria",20,'bold'),text="Methi Matar",width=12,fg="blue4")
lb1_bhindimasala=Label(f1,font=("aria",20,'bold'),text="Bhindi Masala",width=12,fg="blue4")
lb1_matarpaneer=Label(f1,font=("aria",20,'bold'),text="Matar Panner",width=12,fg="blue4")
lb1_kajucurry=Label(f1,font=("aria",20,'bold'),text="Kaju Curry",width=12,fg="blue4")
lb1_matkiusal=Label(f1,font=("aria",20,'bold'),text="Matki Usal",width=12,fg="blue4")

lb1_daltadka.grid(row=1,column=0)
lb1_paneermasala.grid(row=2,column=0)
lb1_methimatar.grid(row=3,column=0)
lb1_bhindimasala.grid(row=4,column=0)
lb1_matarpaneer.grid(row=5,column=0)
lb1_kajucurry.grid(row=6,column=0)
lb1_matkiusal.grid(row=7,column=0)

entry_daltadka=Entry(f1,font=("aria",20,'bold'),textvariable=daltadka,bd=6,width=8,bg="AntiqueWhite3")
entry_paneermasala=Entry(f1,font=("aria",20,'bold'),textvariable=paneermasala,bd=6,width=8,bg="AntiqueWhite3")
entry_methimatar=Entry(f1,font=("aria",20,'bold'),textvariable=methimatar,bd=6,width=8,bg="AntiqueWhite3")
entry_bhindimasala=Entry(f1,font=("aria",20,'bold'),textvariable=bhindimasala,bd=6,width=8,bg="AntiqueWhite3")
entry_matarpaneer=Entry(f1,font=("aria",20,'bold'),textvariable=matarpaneer,bd=6,width=8,bg="AntiqueWhite3")
entry_kajucurry=Entry(f1,font=("aria",20,'bold'),textvariable=kajucurry,bd=6,width=8,bg="AntiqueWhite3")
entry_matkiusal=Entry(f1,font=("aria",20,'bold'),textvariable=matkiusal,bd=6,width=8,bg="AntiqueWhite3")

entry_daltadka.grid(row=1,column=1)
entry_paneermasala.grid(row=2,column=1)
entry_methimatar.grid(row=3,column=1)
entry_bhindimasala.grid(row=4,column=1)
entry_matarpaneer.grid(row=5,column=1)
entry_kajucurry.grid(row=6,column=1)
entry_matkiusal.grid(row=7,column=1)

btn_reset=Button(f1,bd=5,fg="black",bg="light slate gray",font=("ariel",16,"bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="light slate gray",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()
