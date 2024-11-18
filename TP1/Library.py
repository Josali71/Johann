from Book import Book
from RegularMember import RegularMember
from PremiumMember import PremiumMember

class Library :
    def __init__ (self) :
        self.livres = []
        self.membres = []

    def add_book (self, titre, auteur) :
        self.livres.append (Book(titre, auteur))

    def add_member (self, type, nom) :
        if type == "regular" :
            self.membres.append (RegularMember(nom))
        elif type == "premium" :
            self.membres.append (PremiumMember(nom))
        else :
            print ("Statut inexistant")

    def list_books (self) :
        for l in self.livres :
            print ("titre :", l.titre,"-", "auteur : ", l.auteur)

    def find_book (self, titre) :
        for l in self.livres :
            if l.titre == titre :
                return l
        return None

    def find_member (self, nom) :
        for m in self.membres :
            if m.nom == nom :
                return m
        return None