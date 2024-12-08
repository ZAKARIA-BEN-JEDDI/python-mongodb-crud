import sqlite3
# this will be mongodb import
def creer_db_produit():
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor() #?curseur est utilisé pour exécuter des requêtes SQL et récupérer les résultats.

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produit (
            id_produit INTEGER PRIMARY KEY,
            nom_produit TEXT NOT NULL,
            prix INTEGER NOT NULL,
            quantite INTEGER NOT NULL,
            description TEXT NOT NULL
        )
    ''')
    connexion.commit()
    connexion.close()

def get_all_produit():
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('SELECT * FROM produit')
    produit = cursor.fetchall()
    connexion.close()
    return produit

def ajouter_produit(id,nom,prix,quantite,description):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('''
        INSERT INTO produit (id_produit,nom_produit,prix,quantite,description)
                            values(?,?,?,?,?)
    ''',(id,nom,prix,quantite,description))
    connexion.commit()
    connexion.close()

def modifier_produit(nv_nom,nv_prix,nv_quantite,nv_description,id):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute(
        "UPDATE produit SET nom_produit = ?, prix = ?, quantite = ?, description = ? WHERE id_produit = ?",
                        (nv_nom,nv_prix,nv_quantite,nv_description,id))
    print('les donnes sont modifier dans la base de donnes')
    connexion.commit()
    connexion.close()

def chercher_produit(id):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('''
        SELECT COUNT(*) FROM produit WHERE id_produit = ?
    ''', (id,))
    result = cursor.fetchone()  # Utiliser fetchone() pour obtenir une seule ligne
    connexion.close()
    return int(result[0]) > 0

def suprimmer_produit(id):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('DELETE FROM produit WHERE id_produit =?',(id,))
    connexion.commit()
    connexion.close()


def filtre_produit_par_ID_DESC():
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('SELECT * FROM produit ORDER BY id_produit DESC')
    connexion.commit()
    produit_desc = cursor.fetchall()
    connexion.close()
    return produit_desc

def filtre_produit_par_prix_ASC():
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM produit ORDER BY prix")
    connexion.commit()
    produit_trie = cursor.fetchall()
    connexion.close()
    return produit_trie

def filtre_produit_par_prix_DESC():
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('SELECT * FROM produit ORDER BY prix DESC')
    connexion.commit()
    produit_desc = cursor.fetchall()
    connexion.close()
    return produit_desc

def filtre_produit_par_quantite_ASC():
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM produit ORDER BY quantite")
    connexion.commit()
    produit_trie = cursor.fetchall()
    connexion.close()
    return produit_trie

def filtre_produit_par_quantite_DESC():
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('SELECT * FROM produit ORDER BY quantite DESC')
    connexion.commit()
    produit_desc = cursor.fetchall()
    connexion.close()
    return produit_desc
def encadrement_produit(min,max):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('SELECT * FROM produit WHERE prix >= ? AND prix <= ?', (min, max))
    produit_filtrer = cursor.fetchall()
    connexion.close()
    return produit_filtrer
creer_db_produit()