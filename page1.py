from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from tkinter import font
import db_produit

class page1:

    def afficher_interface(self):
        #TODO insitialisation de la page
        self.page = Tk()
        self.page.config(background="#006666")
        #TODO font
        self.nouvelle_police = font.Font(family="Calibri", size=14, weight="bold")
        self.font_champ = font.Font(family="Calibri", size=14, weight="bold",slant="italic")
        self.font_button = font.Font(family="Calibri", size=13, weight="bold",slant="italic")
        self.font_button_table_1_2 = font.Font(family="Calibri", size=10, weight="bold",slant="italic")

        #TODO geometry
        self.page.geometry("1200x600")
        #TODO title
        self.page.title("PRODUIT")
        #TODO self.page not resizable
        self.page.resizable(False,False)

        #! CHAMP DE SAISIE
        self.ID_label = Label(self.page,text="ID:",background="#006666",fg="#fff",font=self.font_champ)
        self.ID_entrer = Entry(self.page,border=1,width=20)
        self.NOM_label = Label(self.page,text="NOM:",background="#006666",fg="#fff",font=self.font_champ)
        self.NOM_entrer = Entry(self.page,border=1,width=20)
        self.PRIX_label = Label(self.page,text="PRIX:",background="#006666",fg="#fff",font=self.font_champ)
        self.PRIX_entrer = Entry(self.page,border=1,width=20)
        self.QUANTITE_label = Label(self.page,text="QUANTITE:",background="#006666",fg="#fff",font=self.font_champ)
        self.QUANTITE_entrer = Entry(self.page,border=1,width=20)
        self.DESCRIPTION_label = Label(self.page,text="DESCRIPTION:",background="#006666",fg="#fff",font=self.font_champ)
        self.DESCRIPTION_entrer = Entry(self.page,border=1,width=35)
        
        self.option_trier_asc = ['id','prix','quantite']
        self.option_trier_desc = ['id','prix','quantite']
        self.asc = tk.StringVar()
        self.desc = tk.StringVar()

        self.filtrer_label = Label(self.page,text="TRIER ASC",background="#006666",fg="#fff",font=self.font_champ)
        self.filtrer_label.place(x=180 ,y=20)
        self.combobox_asc = ttk.Combobox(self.page,textvariable=self.asc,values=self.option_trier_asc)
        self.combobox_asc.place(x=180, y=50)

        self.filtrer_label_desc = Label(self.page,text="TIER DESC",background="#006666",fg="#fff",font=self.font_champ)
        self.filtrer_label_desc.place(x=180 ,y=80)
        self.combobox_desc = ttk.Combobox(self.page,textvariable=self.desc,values=self.option_trier_desc)
        self.combobox_desc.place(x=180, y=110)

        self.filtrer = Label(self.page ,text='FILTRE PRIX',background="#006666",fg="#fff",font=self.font_champ)
        self.filtrer.place(x=410, y=25)
        self.filtrer_min = Label(self.page ,text='MIN',background="#006666",fg="#fff",font=self.font_champ)
        self.filtrer_min.place(x=380 , y=60)
        self.filtrer_min_entre = Entry(self.page,border=1,width=5)
        self.filtrer_min_entre.place(x=420 , y=65)
        self.filtrer_max = Label(self.page ,text='-  MAX',background="#006666",fg="#fff",font=self.font_champ)
        self.filtrer_max.place(x=460 , y=60)
        self.filtrer_max_entre = Entry(self.page,border=1,width=5)
        self.filtrer_max_entre.place(x=520 , y=65)
        self.btn_filtrer = Button(self.page,text="filtrer",padx= 10,pady=1,command=self.filtrer_prix, fg="#000",cursor='hand2')
        self.btn_filtrer.place(x= 440,y=100)
        self.btn_effacer = Button(self.page,text="effacer",padx= 10,pady=1,command=self.clear_All_input,background='#ff073a', fg="#000", font=self.font_button,cursor='hand2')

        # self.b1 = Button(self.page,text="ajouter",padx= 20,command=self.show_input, fg="#000", font=self.font_button,cursor='hand2')
        self.b1 = Button(self.page,text="ajouter",padx= 20,command=self.ajouter, fg="#000", font=self.font_button,cursor='hand2')
        self.b1.place(x=25, y=25)
        self.b2 = Button(self.page,text="modifier",padx= 15,pady=1,command=self.modifier, fg="#000", font=self.font_button,cursor='hand2')
        self.b2.place(x=25, y=80)
        self.b3 = Button(self.page,text="suprimmer",padx= 10,pady=1,command=self.suprimmer, fg="#000", font=self.font_button,cursor='hand2')
        self.b3.place(x=25, y=135)
        self.b3 = Button(self.page,text="afficher tous",padx= 10,pady=1,command=self.ajouter_au_table1, fg="#000", font=self.font_button,cursor='hand2')
        self.b3.place(x=25, y=190)
        self.b5 = Button(self.page,text="afficher client",padx= 10,pady=2,command=self.changer_page_to_table2, fg="#000",font=self.font_button_table_1_2,cursor='hand2')
        self.b5.place(x=900, y=570)
        self.table1()
        self.table.bind('<ButtonRelease>',p1.placer_donne_pour_modifier_suprimmer)#il faut le appeler apres l'apelle de la fonction table1()
        self.combobox_asc.bind("<<ComboboxSelected>>", self.choix_triage_asc)
        self.combobox_desc.bind("<<ComboboxSelected>>", self.choix_triage_desc)
        self.hover_button()
        self.show_input()
        self.ajouter_au_table1()
        self.page.mainloop()

    def show_input(self):
        self.clear_All_input()
        self.ID_label.place(x=650,y=25)
        self.ID_entrer.place(x=700,y=30)
        self.NOM_label.place(x=650,y=60)
        self.NOM_entrer.place(x=700,y=65)
        self.PRIX_label.place(x=900,y=25)
        self.PRIX_entrer.place(x=950,y=30)
        self.QUANTITE_label.place(x=860,y=60)
        self.QUANTITE_entrer.place(x=950,y=65)
        self.DESCRIPTION_label.place(x=650,y=100)
        self.DESCRIPTION_entrer.place(x=770,y=105)
        self.btn_effacer.place(x=830, y=150)
        # self.btn_valider.place(x=870, y=150)

    def hide_input(self):
        self.clear_All_input()
        self.ID_label.place(x=-25,y=-60)
        self.ID_entrer.place(x=-60,y=-65)
        self.NOM_label.place(x=-200,y=-60)
        self.NOM_entrer.place(x=-250,y=-65)
        self.PRIX_label.place(x=-380,y=-60)
        self.PRIX_entrer.place(x=-430,y=-65)
        self.QUANTITE_label.place(x=-555,y=-60)
        self.QUANTITE_entrer.place(x=-645,y=-65)
        self.DESCRIPTION_label.place(x=-735,y=-60)
        self.DESCRIPTION_entrer.place(x=-850,y=-65)
        self.btn_effacer.place(x=-490, y=-120)
        # self.btn_valider.place(x=-350, y=-120)

    def clear_All_input(self):
        self.ID_entrer.delete(0, END)
        self.NOM_entrer.delete(0, END)
        self.PRIX_entrer.delete(0, END)
        self.QUANTITE_entrer.delete(0, END)
        self.DESCRIPTION_entrer.delete(0, END)

    def changer_page_to_table2(self):
        self.page.destroy()
        from page2 import Class_page2
        p2 = Class_page2()
        p2.afficher_interface2()

    def on_enter1(self,e):
        self.b1['background'] = '#006666'  # Change la couleur au survol
        self.b1['fg'] = '#fff'
        self.b1['font'] = self.font_button
    def on_enter2(self,e):
        self.b2['background'] = '#006666'
        self.b2['fg'] = '#fff'
        self.b2['font'] = self.font_button
    def on_enter3(self,e):
        self.b3['background'] = '#006666'
        self.b3['fg'] = '#fff'
        self.b3['font'] = self.font_button

    def on_leave1(self,e):
        self.b1['background'] = '#fff'  # Revient à la couleur normale
        self.b1['fg'] = '#000'
        self.b1['font'] = self.font_button
    def on_leave2(self,e):
        self.b2['background'] = '#fff'
        self.b2['fg'] = '#000'
        self.b2['font'] = self.font_button
    def on_leave3(self,e):
        self.b3['background'] = '#fff'
        self.b3['fg'] = '#000'
        self.b3['font'] = self.font_button

    def hover_button(self):
        self.b1.bind("<Enter>", self.on_enter1)
        self.b1.bind("<Leave>", self.on_leave1)
        self.b2.bind("<Enter>", self.on_enter2)
        self.b2.bind("<Leave>", self.on_leave2)
        self.b3.bind("<Enter>", self.on_enter3)
        self.b3.bind("<Leave>", self.on_leave3)

    def ajouter(self):
        self.id_x = (self.ID_entrer.get())
        self.nom = self.NOM_entrer.get()
        self.prix = (self.PRIX_entrer.get())
        self.quantite = (self.QUANTITE_entrer.get())
        self.desciprtion = self.DESCRIPTION_entrer.get()
        if self.id_x == '' or self.nom == '' or self.prix =='' or self.quantite == '' or self.desciprtion == '':
            tkinter.messagebox.showerror('',"CHAMP VIDE")
        elif db_produit.chercher_produit(self.id_x):
            tkinter.messagebox.showerror('','PRODUIT DEJA EXIST !')
        else:
            self.id_x = int(self.id_x)
            self.prix =  float(self.prix)
            self.quantite =  float(self.quantite)
            if type(self.id_x) == int and type(self.prix) == float and type(self.quantite) == float :
                db_produit.ajouter_produit(self.id_x,self.nom,self.prix,self.quantite,self.desciprtion)
                self.ajouter_au_table1()
                tkinter.messagebox.showinfo('','PRODUIT AJOUTE AVEC SUCCES')
                self.clear_All_input()

    def placer_donne_pour_modifier_suprimmer(self,event):
        self.show_input()
        produit_choisi = self.table.focus() #row selectionne
        if produit_choisi: #si un row selectionne 
            produit = self.table.item(produit_choisi)['values']
            self.clear_All_input()
            self.ID_entrer.insert(0,produit[0])
            self.NOM_entrer.insert(0,produit[1])
            self.PRIX_entrer.insert(0,produit[2])
            self.QUANTITE_entrer.insert(0,produit[3])
            self.DESCRIPTION_entrer.insert(0,produit[4])

    def modifier(self):
        produit_selecionner = self.table.focus()
        if produit_selecionner:
            nv_nom = self.NOM_entrer.get()
            nv_prix = self.PRIX_entrer.get()
            nv_quantite = self.QUANTITE_entrer.get()
            nv_description= self.DESCRIPTION_entrer.get()
            id = self.ID_entrer.get()
            db_produit.modifier_produit(nv_nom,nv_prix,nv_quantite,nv_description,id)
            self.ajouter_au_table1()
            tkinter.messagebox.showinfo('','PRODUIT BIEN MODIFIER')
            self.clear_All_input()
        else:
            tkinter.messagebox.showerror('',"SELECTIONNER D'ABBORD PRODUIT")

    def suprimmer(self):
        produit_choisi = self.table.focus()
        if produit_choisi:
            produit = self.table.item(produit_choisi)['values']
            self.clear_All_input()
            self.ID_entrer.insert(0,produit[0])
            self.NOM_entrer.insert(0,produit[1])
            self.PRIX_entrer.insert(0,produit[2])
            self.QUANTITE_entrer.insert(0,produit[3])
            self.DESCRIPTION_entrer.insert(0,produit[4])
            db_produit.suprimmer_produit(id=produit[0])
            self.ajouter_au_table1()
            self.clear_All_input()
            tkinter.messagebox.showinfo('','PRODUIT BIEN SUPRIMMER')
        else:
            tkinter.messagebox.showerror('',"SELECTIONNER D'ABBORD PRODUIT")
    def filtrer_desc_id(self):
        produit_trier_desc = db_produit.filtre_produit_par_ID_DESC()
        self.table.delete(*self.table.get_children())
        for p_desc in produit_trier_desc:
            self.table.insert('',END,values=p_desc)

    def filtrer_asc_prix(self):
        produit_trier = db_produit.filtre_produit_par_prix_ASC()
        self.table.delete(*self.table.get_children())
        for produit in produit_trier:
            self.table.insert('',END,values=produit)

    def filtrer_desc_prix(self):
        produit_trier_desc = db_produit.filtre_produit_par_prix_DESC()
        self.table.delete(*self.table.get_children())
        for p_desc in produit_trier_desc:
            self.table.insert('',END,values=p_desc)

    def filtrer_asc_quantite(self):
        produit_trier = db_produit.filtre_produit_par_quantite_ASC()
        self.table.delete(*self.table.get_children())
        for produit in produit_trier:
            self.table.insert('',END,values=produit)

    def filtrer_desc_quantite(self):
        produit_trier_desc = db_produit.filtre_produit_par_prix_DESC()
        self.table.delete(*self.table.get_children())
        for p_desc in produit_trier_desc:
            self.table.insert('',END,values=p_desc)

    def choix_triage_asc(self,event):
        print("Sélection : ", self.asc.get())
        if self.asc.get() == 'id':
            self.ajouter_au_table1()
        elif self.asc.get() == 'prix':
            self.filtrer_asc_prix()
        else:
            self.filtrer_asc_quantite()
    
    def choix_triage_desc(self,event):
        print("Sélection : ", self.desc.get())
        if self.desc.get() == 'id':
            self.filtrer_desc_id()
        elif self.desc.get() == 'prix':
            self.filtrer_desc_prix()
        else:
            self.filtrer_desc_quantite()
    def filtrer_prix(self):
        min = self.filtrer_min_entre.get()
        max = self.filtrer_max_entre.get()
        produit_encadrer = db_produit.encadrement_produit(min=min,max=max)
        self.table.delete(*self.table.get_children())
        for p_encadrer in produit_encadrer:
            self.table.insert('',END,values=p_encadrer)
    def table1(self):
        #TODO TABLE
        self.table = ttk.Treeview(self.page,height=15)
        self.table['columns'] = ('ID','NOM','PRIX','QUANTITE','DESCRIPTON')
        self.table.column('#0',stretch=tk.NO,width=0)
        self.table.column('ID',anchor=tk.CENTER,width=250)
        self.table.column('NOM',anchor=tk.CENTER,width=250)
        self.table.column('PRIX',anchor=tk.CENTER,width=250)
        self.table.column('QUANTITE',anchor=tk.CENTER,width=250)
        self.table.column('DESCRIPTON',anchor=tk.CENTER,width=250)
        self.table.heading('ID',text='ID')
        self.table.heading('NOM',text='NOM')
        self.table.heading('PRIX',text='PRIX')
        self.table.heading('QUANTITE',text='QUANTITE')
        self.table.heading('DESCRIPTON',text='DESCRIPTON')
        self.table.place(x=0, y=240)

    def ajouter_au_table1(self):
        all_produits = db_produit.get_all_produit()
        self.table.delete(*self.table.get_children())
        for produit in all_produits:
            self.table.insert('',END,values= produit)

p1 = page1()
p1.afficher_interface()