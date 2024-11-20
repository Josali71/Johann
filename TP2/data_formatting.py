class DataFormatting :
    def format_data(cleaned_data) : # crée un module qui gère un nouveau champ dépendant de 2 autres et le formatage des infos "types"
        if cleaned_data ['weight'] != 0 and cleaned_data ['height'] != 0 : # conditionne la possibilité de calculer l'IMC du pokemon
            cleaned_data['bmi'] = cleaned_data ['weight']/(cleaned_data ['height']**2) # si les conditions le permettent, calcul de l'IMC
        else :
            print ('BMI ne peut être calculée') # les conditions ne le permettent pas : message renvoyé

#formatage des types
        list_type = [] # création d'une liste vide
        for t in cleaned_data['types'] : # boucle : traite les types trouvés dans cleaned_data
            list_type.append(t['name']) #implémente la liste du nom du/des types trouvés
        
        concat = ", ".join(list_type) # sépare les données types par une virgule
        print (concat) # imprime le résultat obtenu

        cleaned_data['types'] = concat # remplace le contenu initial de types par les données nom séparés d'une virgule
          
       

        return cleaned_data # retourne le nouveau résultat pour l'ensembles des infos (id, nom... et types avec le nouveau format)
