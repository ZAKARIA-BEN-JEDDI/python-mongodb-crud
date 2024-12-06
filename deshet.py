from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from tkinter import font
# from page1 import afficher_interface
# from page2 import *
import db_command
# import db_product
import db_command


class Commande:

    def afficher_interface3(self):
        #TODO insitialisation de la page
        self.page3 = Tk()
        self.page3.config(background="#253342")
        #TODO font
        self.p3_nouvelle_police = font.Font(family="Calibri", size=14, weight="bold")
        self.p3_font_champ = font.Font(family="Calibri", size=12, weight="bold",slant="italic")
        self.p3_font_button = font.Font(family="Calibri", size=13, weight="bold",slant="italic")
        self.p3_font_button_chercher = font.Font(family="Calibri", size=12, weight="bold",slant="italic")
        self.p3_font_button_table_1_2_3 = font.Font(family="Calibri", size=10, weight="bold",slant="italic")

        #TODO geometry
        self.page3.geometry("1200x600")
        #TODO title
        self.page3.title("client")
        #TODO self.page3 not resizable
        self.page3.resizable(False,False)
        #TODO titre de la self.page3
        self.p3_titre_brand = Label(self.page3,pady=0,text="COMMANDES",font=self.p3_nouvelle_police)
        self.p3_titre_brand.pack()

        #! CHAMP DE SAISIE
        self.id_commande_label = Label(self.page3,text="id commande",background="#253342",fg="#fff",font=self.p3_font_champ)
        self.id_commande_entrey = Entry(self.page3,border=1,width=20)
        self.id_client_label = Label(self.page3,text="id client",background="#253342",fg="#fff",font=self.p3_font_champ)
        self.id_client_entrer = Entry(self.page3,border=1,width=20)
        self.id_produit_label = Label(self.page3,text="id produit",background="#253342",fg="#fff",font=self.p3_font_champ)
        self.id_produit_entrer = Entry(self.page3,border=1,width=20)
        self.qte_label = Label(self.page3,text="quantite",background="#253342",fg="#fff",font=self.p3_font_champ)
        self.qte_entrey = Entry(self.page3,border=1,width=20)
        self.date_commande_label = Label(self.page3,text="date de laivraison",background="#253342",fg="#fff",font=self.p3_font_champ)
        self.date_commande_entry = Entry(self.page3,border=1,width=35)
        self.p3_btn_valider = Button(self.page3,text="valider",padx= 10,pady=1,command=self.ajouter,background='#00c04b', fg="#000", font=self.p3_font_button,cursor='hand2')
        self.p3_btn_vider = Button(self.page3,text="effacer",padx= 10,pady=1,command=self.clear_All_input,background='#ff073a', fg="#000", font=self.p3_font_button,cursor='hand2')
        self.p3_b1 = Button(self.page3,text="ajouter",padx= 23,pady=1,command=self.show_input, fg="#000", font=self.p3_font_button,cursor='hand2')
        self.p3_b1.place(x=25, y=25)
        self.p3_b2 = Button(self.page3,text="modifier",padx= 20,pady=1,command=self.modifier, fg="#000", font=self.p3_font_button,cursor='hand2')
        self.p3_b2.place(x=25, y=80)
        self.p3_b3 = Button(self.page3,text="suprimmer",padx= 10,pady=1,command=self.suprimmer, fg="#000", font=self.p3_font_button,cursor='hand2')
        self.p3_b3.place(x=25, y=135)
        self.p3_b3_prime = Button(self.page3,text="afficher tous",padx= 6,pady=1,command=self.remplir_tableau, fg="#000", font=self.p3_font_button,cursor='hand2')
        self.p3_b3_prime.place(x=25, y=190)
        self.date_commande_label = Label(self.page3,text="date de laivraison",background="#253342",fg="#fff",font=self.p3_font_champ)
        self.date_commande_entry = Entry(self.page3,border=1,width=35)

        self.client_command_entry = Entry(self.page3,border=1,width=20)
        self.p3_b4 = Button(self.page3,text="afficher command d'un client",padx= 2,pady=1,command=self.afficher_command_client, fg="#000", font=self.p3_font_button_chercher,highlightbackground="red",cursor='hand2')
        self.chercher_nom_client_entrer = Entry(self.page3,border=1,width=20)
        self.p3_command_chercher_date = Button(self.page3,text="chercher par date",padx= 9,pady=1,command=self.afficher_commande_par_date, fg="#000", font=self.p3_font_button_chercher,highlightbackground="red",cursor='hand2')
        self.p3_b5 = Button(self.page3,text="afficher produit",padx= 10,pady=2,command=self.changer_page_to_table1, fg="#000",font=self.p3_font_button_table_1_2_3,cursor='hand2')
        self.p3_b5.place(x=420, y=570)
        self.p3_b5 = Button(self.page3,text="afficher client",padx= 10,pady=2,command=self.changer_page_to_table2, fg="#000",font=self.p3_font_button_table_1_2_3,cursor='hand2')
        self.p3_b5.place(x=570, y=570)
        # self.client_command_entry.place(x=180 ,y=25)
        # self.p3_b4.place(x=180, y=55)
        # self.chercher_nom_client_entrer.place(x=180 ,y=110)
        # self.p3_command_chercher_date.place(x=180, y=140)
        self.table3()
        self.remplir_tableau()
        self.p3_table3.bind('<ButtonRelease>',self.selected_row) #la fonction sans parenthese
        self.afficher_autre_option()
        self.hover_button()
        self.page3.mainloop()

    def desafficher(self):
        #! si je le remplace place par destroy quand je veut les afficher ==> erreur (car il sont suprimmer totalement)
        self.client_command_entry.place(x=-180 ,y=-25)
        self.p3_b4.place(x=-180, y=-55)
        self.chercher_nom_client_entrer.place(x=-180 ,y=-110)
        self.p3_command_chercher_date.place(x=-180, y=-140)

    def afficher_autre_option(self):
        self.client_command_entry.place(x=180 ,y=25)
        self.p3_b4.place(x=180, y=55)
        self.chercher_nom_client_entrer.place(x=180 ,y=110)
        self.p3_command_chercher_date.place(x=180, y=140)

    def show_input(self):
        self.desafficher()
        self.id_commande_label.place(x=180,y=25)
        self.id_commande_entrey.place(x=300,y=30)
        self.id_produit_label.place(x=180,y=70)
        self.id_produit_entrer.place(x=300,y=75)
        self.id_client_label.place(x=180,y=115)
        self.id_client_entrer.place(x=300,y=115)
        self.date_commande_label.place(x=450,y=25)
        self.date_commande_entry.place(x=590,y=30)
        self.qte_label.place(x=450,y=70)
        self.qte_entrey.place(x=590,y=75)
        self.p3_btn_valider.place(x=550, y=150)
        self.p3_btn_vider.place(x=450, y=150)

    def desafficher_input(self):
        self.id_commande_label.place(x=-180,y=-25)
        self.id_commande_entrey.place(x=-300,y=-30)
        self.id_produit_label.place(x=-180,y=-70)
        self.id_produit_entrer.place(x=-300,y=-75)
        self.id_client_label.place(x=-180,y=-115)
        self.id_client_entrer.place(x=-300,y=-115)
        self.date_commande_label.place(x=-450,y=-25)
        self.date_commande_entry.place(x=-590,y=-30)
        self.qte_label.place(x=-450,y=-70)
        self.qte_entrey.place(x=-590,y=-75)
        self.p3_btn_valider.place(x=-550, y=-150)
        self.p3_btn_vider.place(x=-450, y=-150)

    def ajouter(self):
        self.show_input()
        id_command = self.id_commande_entrey.get()
        id_client = self.id_client_entrer.get()
        id_produit = self.id_produit_entrer.get()
        qte = int(self.qte_entrey.get())
        date = self.date_commande_entry.get()
        if id_command == '' or id_client == '' or id_produit == '' or qte == '' or date == '':
            tkinter.messagebox.showerror('',"CHAMP VIDE")
        elif db_command.chercher_commande_deja_exist(id=id_command):
            tkinter.messagebox.showerror('',"COMMANDE DEJA EXIST")
        else:
            db_command.ajouter(id_commande=id_command,id_client=id_client,id_produit=id_produit,qte=qte,date_commande=date)
            self.remplir_tableau()
            self.clear_All_input()
            self.desafficher_input()
            self.afficher_autre_option()

    def remplir_tableau(self):
        all_commande = db_command.get_all_command()
        self.p3_table3.delete(*self.p3_table3.get_children())
        for commande in all_commande:
            self.p3_table3.insert('',END,values=commande)

    def selected_row(self,event):
        self.show_input()
        self.p3_btn_valider.place(x=-50,y=-50)#pour le desafficher #! le cas de la selection d'un ranger il faut clique soit sur modi ou supp
        self.p3_btn_vider.place(x=450,y=135)                       #! il faut disparu valider
        self.clear_All_input()
        client_selectionne = self.p3_table3.focus()
        if client_selectionne:
            info_client = self.p3_table3.item(client_selectionne)['values']
            self.id_commande_entrey.insert(0,info_client[0])
            self.id_client_entrer.insert(0,info_client[1])
            self.id_produit_entrer.insert(0,info_client[2])
            self.qte_entrey.insert(0,info_client[3])
            self.date_commande_entry.insert(0,info_client[4])

    def modifier(self):
        id_command = int(self.id_commande_entrey.get())
        id_client = int(self.id_client_entrer.get())
        id_produit = int(self.id_produit_entrer.get()) #! IDE return int(result[0]) != 0
        nv_qte = int(self.qte_entrey.get())
        nv_date = self.date_commande_entry.get()
        db_command.modifier(nv_id_client=id_client,nv_id_produit=id_produit,nv_qte=nv_qte,nv_date_commande=nv_date,id_command=id_command)
        tkinter.messagebox.showinfo('',"CLIENT MODIFIER AVEC SUCCES")
        self.clear_All_input()
        self.desafficher_input()
        self.afficher_autre_option()
        self.remplir_tableau()

    def suprimmer(self):
        id = int(self.id_commande_entrey.get())
        db_command.suprimmer(id_command=id)
        self.remplir_tableau()
        tkinter.messagebox.showinfo('',"CLIENT SUPRIMMER AVEC SUCCES")
        self.clear_All_input()
        self.desafficher_input()
        self.afficher_autre_option()

    def afficher_command_client(self):
        self.remplir_tableau()
        id_client = self.client_command_entry.get()
        results = db_command.chercher_command_client(id_client=id_client)
        self.p3_table3.delete(*self.p3_table3.get_children())
        for result in results:
            self.p3_table3.insert('',END,values=result)
        self.client_command_entry.delete(0,END)

    def afficher_commande_par_date(self):
        self.remplir_tableau()
        date = self.date_commande_entry.get()
        date_commandes = db_command.chercher_command_date(date)
        self.p3_table3.delete(*self.p3_table3.get_children())
        for date_commande in date_commandes:
            self.p3_table3.insert('',END,values=date_commande)
        self.chercher_nom_client_entrer.delete(0,END)

    def clear_All_input(self):
        self.id_commande_entrey.delete(0, END)  # Deletes all characters
        self.id_client_entrer.delete(0, END)
        self.id_produit_entrer.delete(0, END)
        self.qte_entrey.delete(0, END)
        self.date_commande_entry.delete(0, END)

    def on_enter1(self,e):
        self.p3_b1['background'] = '#253342'  # Change la couleur au survol
        self.p3_b1['fg'] = '#fff'
        self.p3_b1['font'] = self.p3_font_button
    def on_enter2(self,e):
        self.p3_b2['background'] = '#253342'
        self.p3_b2['fg'] = '#fff'
        self.p3_b2['font'] = self.p3_font_button
    def on_enter3(self,e):
        self.p3_b3['background'] = '#253342'
        self.p3_b3['fg'] = '#fff'
        self.p3_b3['font'] = self.p3_font_button

    def on_leave1(self,e):
        self.p3_b1['background'] = '#fff'  # Revient à la couleur normale
        self.p3_b1['fg'] = '#000'
        self.p3_b1['font'] = self.p3_font_button
    def on_leave2(self,e):
        self.p3_b2['background'] = '#fff'
        self.p3_b2['fg'] = '#000'
        self.p3_b2['font'] = self.p3_font_button
    def on_leave3(self,e):
        self.p3_b3['background'] = '#fff'
        self.p3_b3['fg'] = '#000'
        self.p3_b3['font'] = self.p3_font_button

    def hover_button(self):
        self.p3_b1.bind("<Enter>", self.on_enter1)
        self.p3_b1.bind("<Leave>", self.on_leave1)
        self.p3_b2.bind("<Enter>", self.on_enter2)
        self.p3_b2.bind("<Leave>", self.on_leave2)
        self.p3_b3.bind("<Enter>", self.on_enter3)
        self.p3_b3.bind("<Leave>", self.on_leave3)

    def changer_page_to_table1(self):
        self.page3.destroy()
        from page1 import afficher_interface
        import page1
        p1 = page1()
        # p1.afficher_interface()

    def changer_page_to_table2(self):
        self.page3.destroy()
        import page2
        from page2 import Class_page2
        p2 = Class_page2()
        p2.afficher_interface2()

    def table3(self):
        self.p3_table3 = ttk.Treeview(self.page3,height=15)
        self.p3_table3['columns'] = ('ID COMMANDE','ID CLIENT','ID PRODUIT','QUANTITE','DATE DE LAIVRAISON')
        self.p3_table3.column('#0',stretch=tk.NO,width=0)
        self.p3_table3.column('ID COMMANDE',anchor=tk.CENTER,width=250)
        self.p3_table3.column('ID CLIENT',anchor=tk.CENTER,width=250)
        self.p3_table3.column('ID PRODUIT',anchor=tk.CENTER,width=250)
        self.p3_table3.column('QUANTITE',anchor=tk.CENTER,width=250)
        self.p3_table3.column('DATE DE LAIVRAISON',anchor=tk.CENTER,width=250)
        self.p3_table3.heading('ID COMMANDE',text='ID COMMANDE')
        self.p3_table3.heading('ID CLIENT',text='ID CLIENT')
        self.p3_table3.heading('ID PRODUIT',text='ID PRODUIT')
        self.p3_table3.heading('QUANTITE',text='QUANTITE')
        self.p3_table3.heading('DATE DE LAIVRAISON',text='DATE DE LAIVRAISON')
        self.p3_table3.place(x=0, y=240)

p3 = Commande()
p3.afficher_interface3()
