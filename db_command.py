import sqlite3
import db_client
import db_produit
import tkinter.messagebox

def creer_db_command():
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS commande (
            id_commande INTEGER PRIMARY KEY,
            id_client INTEGER,
            id_produit INTEGER,
            qte INTEGER,
            date_commande TEXT,
            FOREIGN KEY (id_client) REFERENCES client(id_client),
            FOREIGN KEY (id_produit) REFERENCES produit(id_produit)
        )
    ''')
    connexion.close()

def get_all_command():
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('SELECT * FROM commande')
    result = cursor.fetchall()
    connexion.close()
    return result

def get_id_produit():
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT id_produit FROM produit")
    id_produit = cursor.fetchall()
    connexion.close()
    return id_produit
def get_id_client():
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT id_client FROM client")
    id_client = cursor.fetchall()
    connexion.close()
    return id_client

def verifier(id_client,id_produit): #verifier si id_client et id_produit existent dans ses tables 
    connexion = sqlite3.connect('magasin.db')
    cursor1 = connexion.cursor()
    cursor1.execute("SELECT id_client FROM client WHERE id_client = ?",(id_client,))
    result = cursor1.fetchone()
    cursor2 = connexion.cursor()
    cursor2.execute("SELECT id_produit FROM produit WHERE id_produit = ?",(id_produit,))
    result2 = cursor2.fetchone()
    if result != None and result2 != None:
        return True

def ajouter(id_commande,id_client,id_produit,qte,date_commande):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    if verifier(id_client,id_produit) == True and qte > 0:
        cursor.execute('''
                        INSERT INTO commande (id_commande,id_client,id_produit,qte,date_commande) VALUES
                        (?,?,?,?,?)
                    ''',(id_commande,id_client,id_produit,qte,date_commande))
        tkinter.messagebox.showinfo('',"COMMANDE AJOUTE AVEC SUCCES")
        
    else:
        tkinter.messagebox.showerror('',"CLIENT OU PRODUIT NON EXIST")
    connexion.commit()
    connexion.close()

def modifier(nv_id_client ,nv_id_produit ,nv_qte ,nv_date_commande, id_command):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    if verifier(id_client = nv_id_client,id_produit = nv_id_produit) == True and nv_qte>0:
        cursor.execute('''
                        UPDATE commande
                        SET id_client = ?, id_produit = ?, qte = ?, date_commande = ?
                        WHERE id_commande = ?
                    ''',(nv_id_client ,nv_id_produit ,nv_qte ,nv_date_commande, id_command))
        connexion.commit()
        connexion.close()

def chercher_commande_deja_exist(id):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('''
        SELECT COUNT(*) FROM commande WHERE id_commande = ?
    ''', (id,))
    result = cursor.fetchone()
    connexion.close()
    return int(result[0]) > 0

def chercher(id_command):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('SELECT * FROM commande WHERE id_commande = ?',(id_command))
    result = cursor.fetchone()
    connexion.commit()
    connexion.close()
    return result

def suprimmer(id_command):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('DELETE FROM commande WHERE id_commande = ?',(id_command,))
    connexion.commit()
    connexion.close()

def chercher_command_client(id_client):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor1 = connexion.cursor()
    cursor1.execute("SELECT id_client FROM client WHERE id_client = ?",(id_client))
    result1 = cursor1.fetchone()
    if result1 != None:
        cursor.execute("SELECT * FROM commande WHERE id_client = ?",(id_client))
        result2 = cursor.fetchall()
        return result2
    connexion.close()

def chercher_command_date(date):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM commande WHERE date_commande = ?",(date,))
    result = cursor.fetchall()
    connexion.close()
    return result

creer_db_command()