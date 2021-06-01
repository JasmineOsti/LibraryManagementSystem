from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing System")
        bg_color="#856ff8"
        title=Label(self.root,text="Billing System",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=======variable============
        #=======cosmetics===========
        self.Bath_Soap=IntVar()
        self.Face_Cream=IntVar()
        self.Nailpolish=IntVar()
        self.Lipstick=IntVar()
        self.Eyeliner=IntVar()
        self.Body_Lotion=IntVar()
        #=======grocery===========
        self.Rice=IntVar()
        self.Coffee=IntVar()
        self.Sugar=IntVar()
        self.Cheese=IntVar()
        self.Bread=IntVar()
        self.Eggs=IntVar()
        #=======cosmetics===========
        self.Coke= IntVar()
        self.Sprite= IntVar()
        self.Dew= IntVar()
        self.Pepsi= IntVar()
        self.Red_Bull= IntVar()
        self.Fruit_Juice= IntVar()
        #========Total Products Price and Tax Variables=======
        self.Cosmetic_Price=StringVar()
        self.Grocery_Price=StringVar()
        self.Cold_Drinks_Price=StringVar()

        self.Cosmetic_Tax=StringVar()
        self.Grocery_Tax=StringVar()
        self.Cold_Drinks_Tax=StringVar()

        #==========Customer=============
        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()

        #=======Customer Detail Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="firebrick",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=20)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=20)
        cphn_txt = Entry(F1, width=15,textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=20)
        c_bill_txt = Entry(F1, width=15,textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill, width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #=====Cosmetics Frame======
        F2=LabelFrame(self.root,bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"),fg="firebrick", bg=bg_color)
        F2.place(x=5, y=180,width=325,height=380)

        Bath_Soap_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Bath_Soap_txt=Entry(F2,width=10,textvariable=self.Bath_Soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_Cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_Cream_txt = Entry(F2, width=10,textvariable=self.Face_Cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        Nail_Polish_lbl = Label(F2, text="Nail Polish", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Nail_Polish_txt = Entry(F2, width=10,textvariable=self.Nailpolish, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        Lipstick_lbl = Label(F2, text="Lipstick", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Lipstick_txt = Entry(F2, width=10,textvariable=self.Lipstick, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        Eyeliner_lbl = Label(F2, text="Eyeliner", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Eyeliner_txt = Entry(F2, width=10,textvariable=self.Eyeliner, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        Body_Lotion_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Body_Lotion_txt = Entry(F2, width=10,textvariable=self.Body_Lotion, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        #====Grocery Frame======
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"),fg="firebrick", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10,textvariable=self.Rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl = Label(F3, text="Coffee", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10,textvariable=self.Coffee, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10,textvariable=self.Sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl = Label(F3, text="Cheese", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10,textvariable=self.Cheese, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl = Label(F3, text="Bread", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.Bread, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl = Label(F3, text="Eggs ", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10,textvariable=self.Eggs, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #====Cold Drinks Frame======
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman", 15, "bold"),fg="firebrick", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        c1_lbl = Label(F4, text="Coke", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=10,textvariable=self.Coke, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10,textvariable=self.Sprite, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl = Label(F4, text="Dew", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10,textvariable=self.Dew, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl = Label(F4, text="Pepsi", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10, textvariable=self.Pepsi,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl = Label(F4, text="Red Bull", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=10,textvariable=self.Red_Bull, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl = Label(F4, text="Fruit Juice", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10,textvariable=self.Fruit_Juice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #====Bill Area======
        F5=Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold", bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #====Button Frame======
        F6=LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),fg="firebrick", bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1_lbl=Label(F6,text="Total Cosmetics Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.Cosmetic_Price,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.Grocery_Price,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.Cold_Drinks_Price,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="Cosmetics Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.Cosmetic_Tax,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.Grocery_Tax,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.Cold_Drinks_Tax,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6, bd=7,relief=GROOVE)
        btn_F.place(x=750, width=580,height=105)

        Total_btn=Button(btn_F,command=self.total,text="Total",bg="mediumpurple",fg="white",bd=2,pady=15,width=10,font="arial 15 bold ").grid(row=0,column=0,padx=5,pady=5)
        Make_Bill_btn = Button(btn_F, text="Make Bill",command=self.bill_area, bg="mediumpurple", fg="white", bd=2, pady=15, width=10,font="arial 15  bold ").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear",command=self.clear_data, bg="mediumpurple", fg="white", bd=2, pady=15, width=10,font="arial 15 bold ").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit",command=self.Exit_app, bg="mediumpurple", fg="white", bd=2, pady=15, width=10,font="arial 15 bold ").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p=self.Bath_Soap.get()*40
        self.c_fc_p=self.Face_Cream.get()*200
        self.c_np_p = self.Nailpolish.get() *70
        self.c_ls_p = self.Lipstick.get() *120
        self.c_el_p = self.Eyeliner.get() *100
        self.c_bl_p = self.Body_Lotion.get() *190

        self.Total_Cosmetic_Price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_np_p+
                                    self.c_ls_p+
                                    self.c_el_p+
                                    self.c_bl_p
                                    )
        self.Cosmetic_Price.set("Rs. "+str(self.Total_Cosmetic_Price))
        self.c_tax=round((self.Total_Cosmetic_Price*0.05),2)
        self.Cosmetic_Tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.Rice.get()*450
        self.g_c_p=self.Coffee.get()*300
        self.g_s_p=self.Sugar.get()*170
        self.g_ch_p=self.Cheese.get()*220
        self.g_b_p=self.Bread.get() * 80
        self.g_e_p=self.Eggs.get() * 20
        self.Total_Grocery_Price = float(
                                    self.g_r_p+
                                    self.g_c_p+
                                    self.g_s_p+
                                    self.g_ch_p+
                                    self.g_b_p+
                                    self.g_e_p
                                    )
        self.Grocery_Price.set("Rs. "+str(self.Total_Grocery_Price))
        self.g_tax=round((self.Total_Grocery_Price*0.1),2)
        self.Grocery_Tax.set("Rs. "+str(self.g_tax))

        self.d_c_p=self.Coke.get()*250
        self.d_s_p=self.Sprite.get() * 210
        self.d_d_p=self.Dew.get() * 230
        self.d_p_p=self.Pepsi.get() * 250
        self.d_rb_p=self.Red_Bull.get() * 150
        self.d_fj_p=self.Fruit_Juice.get() * 220
        self.Total_Cold_Drinks_Price = float(
                                    self.d_c_p+
                                    self.d_s_p+
                                    self.d_d_p+
                                    self.d_p_p+
                                    self.d_rb_p+
                                    self.d_fj_p
                                    )
        self.Cold_Drinks_Price.set("Rs. "+str(self.Total_Cold_Drinks_Price))
        self.d_tax=round((self.Total_Cold_Drinks_Price*0.05),2)
        self.Cold_Drinks_Tax.set("Rs. "+str(self.d_tax))

        self.Total_Bill=float(  self.Total_Cosmetic_Price+
                                self.Total_Grocery_Price+
                                self.Total_Cold_Drinks_Price+
                                self.c_tax+
                                self.g_tax+
                                self.d_tax
                                )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to BigHit Mart\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone Number : {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n======================================")
        self.txtarea.insert(END, f"\nProducts\t\tOTY\tPrice")
        self.txtarea.insert(END, f"\n======================================")

    def bill_area(self):
        if self.c_name.get()==""or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are required.")
        elif self.Cosmetic_Price.get()=="Rs. 0.0" and self.Grocery_Price.get()=="Rs. 0.0" and self.Cold_Drinks_Price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No product purchased.")
        else:

            self.welcome_bill()
            #=====Cosmetics=====
            if self.Bath_Soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.Bath_Soap.get()}\t\t{self.c_s_p}")
            if self.Face_Cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.Face_Cream.get()}\t\t{self.c_fc_p}")
            if self.Nailpolish.get()!=0:
                self.txtarea.insert(END,f"\n Nailpolish\t\t{self.Nailpolish.get()}\t\t{self.c_np_p}")
            if self.Lipstick.get()!=0:
                self.txtarea.insert(END,f"\n Lipstick\t\t{self.Lipstick.get()}\t\t{self.c_ls_p}")
            if self.Eyeliner.get()!=0:
                self.txtarea.insert(END,f"\n Eyeliner\t\t{self.Eyeliner.get()}\t\t{self.c_el_p}")
            if self.Body_Lotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.Body_Lotion.get()}\t\t{self.c_bl_p}")

    #=====Grocery=====
            if self.Rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.Rice.get()}\t\t{self.g_r_p}")
            if self.Coffee.get()!=0:
                self.txtarea.insert(END,f"\n Coffee\t\t{self.Coffee.get()}\t\t{self.g_c_p}")
            if self.Sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.Sugar.get()}\t\t{self.g_s_p}")
            if self.Cheese.get()!=0:
                self.txtarea.insert(END,f"\n Cheese\t\t{self.Cheese.get()}\t\t{self.g_ch_p}")
            if self.Bread.get()!=0:
                self.txtarea.insert(END,f"\n Bread\t\t{self.Bread.get()}\t\t{self.g_b_p}")
            if self.Eggs.get()!=0:
                self.txtarea.insert(END,f"\n Eggs\t\t{self.Eggs.get()}\t\t{self.g_e_p}")

    #=====Cold Drinks=====
            if self.Coke.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.Bath_Soap.get()}\t\t{self.c_s_p}")
            if self.Sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.Sprite.get()}\t\t{self.d_s_p}")
            if self.Dew.get()!=0:
                self.txtarea.insert(END,f"\n Dew\t\t{self.Dew.get()}\t\t{self.d_d_p}")
            if self.Pepsi.get()!=0:
                self.txtarea.insert(END,f"\n Pepsi\t\t{self.Pepsi.get()}\t\t{self.d_p_p}")
            if self.Red_Bull.get()!=0:
                self.txtarea.insert(END,f"\n Red Bull\t\t{self.Red_Bull.get()}\t\t{self.d_rb_p}")
            if self.Fruit_Juice.get()!=0:
                self.txtarea.insert(END,f"\n Fruit Juice\t\t{self.Fruit_Juice.get()}\t\t{self.d_fj_p}")

            self.txtarea.insert(END, f"\n-------------------------------------")
            if self.Cosmetic_Tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nCosmetic Tax\t\t\t{self.Cosmetic_Tax.get()}")
            if self.Grocery_Tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nGrocery Tax\t\t\t{self.Grocery_Tax.get()}")
            if self.Cold_Drinks_Tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nCold Drinks Tax\t\t\t{self.Cold_Drinks_Tax.get()}")

                self.txtarea.insert(END, f"\nTotal Bill\t\t\t Rs. {self.Total_Bill}")
                self.txtarea.insert(END, f"\n-------------------------------------")
                self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no: {self.bill_no.get()} saved successfully.")
        else:
            return
    def find_bill(self):
        present="No"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="Yes"
        if present=="No":
            messagebox.showerror("Error","Invalid Bill No.")
    def clear_data(self):
        op=messagebox.askyesno("Clear", "Do you really want to clear the data?")
        if op>0:
            #=======cosmetics===========
            self.Bath_Soap.set(0)
            self.Face_Cream.set(0)
            self.Nailpolish.set(0)
            self.Lipstick.set(0)
            self.Eyeliner.set(0)
            self.Body_Lotion.set(0)
            #=======grocery===========
            self.Rice.set(0)
            self.Coffee.set(0)
            self.Sugar.set(0)
            self.Cheese.set(0)
            self.Bread.set(0)
            self.Eggs.set(0)
            #=======cosmetics===========
            self.Coke.set(0)
            self.Sprite.set(0)
            self.Dew.set(0)
            self.Pepsi.set(0)
            self.Red_Bull.set(0)
            self.Fruit_Juice.set(0)
            #========Total Products Price and Tax Variables=======
            self.Cosmetic_Price.set("")
            self.Grocery_Price.set("")
            self.Cold_Drinks_Price.set("")

            self.Cosmetic_Tax.set("")
            self.Grocery_Tax.set("")
            self.Cold_Drinks_Tax.set("")

            #==========Customer=============
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Are you sure you want to exit?")
        if op>0:
            self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop(
