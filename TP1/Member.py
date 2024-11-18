

class Member :
    def __init__ (self, nom) :
        self.nom = nom
        self.borrowed_books = []

    def borrow_book (self,livre) :
        if livre.borrow() ==True :
            self.borrowed_books.append (livre)
        else :
            print ("emprunt impossible")

    def return_book (self,livre) :
        livre.return_book()
        if livre in self.borrowed_books :
            self.borrowed_books.remove (livre)
        else :
            print ("livre non emprunté")

    def list_borrowed_books (self) :
        for l in self.borrowed_books :
            print ("titre :", l.titre,"-", "auteur : ", l.auteur)