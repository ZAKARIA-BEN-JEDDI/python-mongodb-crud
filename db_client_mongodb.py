import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

PythonMongodb = myclient["PythonMongodb"]

client_collection = PythonMongodb['clients']

# TODO initialisation des key de document
# id = int(input("enterer un id : "))
# prenom = (input("entrer le prenom de client : ")) 
# tel = (input("entrer le tel de client : ")) 
# adress_laivraison = (input("entrer le adress_laivraison de client : "))

# print("id de client : ", id)
# print("prenom de client : ", prenom)
# print("tel de client : ", tel)
# print("adress laivresson de client : ", adress_laivraison)

# client_collection.insert_one({'_id':id,'prenom':prenom,'tel':tel,'adress_laivraison':adress_laivraison})

def get_all_client_mongo():
  allClient = client_collection.find()
  return allClient

def modifier(nv_nom,nv_prenom,nv_telephone,nv_adress,id):
  client_collection.update_one(
    {'_id': id},
    {'$set': {
        'nom': nv_nom,
        'prenom': nv_prenom,
        'telephone': nv_telephone,
        'adress': nv_adress
    }}
)

def chercher_client(id):
  client = client_collection.find_one({'_id': id})
  return client is not None


def ajouter(id,nom,prenom,telephone,adress):
  client_collection.insert_one({'_id':id,'nom':nom,'prenom':prenom,'telephone':telephone,'adress':adress})

def suprimmer_client(id):
  client_collection.delete_one({'_id':id})

def chercher_client_telephone(telephone):
    result = client_collection.find_one({"telephone": telephone})
    if result: 
        return [result]
    else:
        return []

def chercher_client_nom(nom):
  result = client_collection.find_one({'nom':nom})
  if result :
    return [result]
  else:
    return []
