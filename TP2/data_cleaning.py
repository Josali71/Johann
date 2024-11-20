class DataCleaning :
    def clean_data(data) : # création d'une fonction clean_date qui récupère les infos sur le site pokemon
        dictionnaire = {    #  crée un dictionnaire qui récupère uniquement les données voulues
            "id" : data['id'], #identifiant du pokemon
            "name" : data ['name'], # son nom
            "height" : data ['height'], # sa taille
            "weight" : data ['weight'], # son poids
            "types" : [t['type'] for t in data['types']] # l'ensemble de ses types et leur url
            }

        return dictionnaire # retourne les informations trouvés sous forme de dictionnaire

