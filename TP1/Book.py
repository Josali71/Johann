class Book :
    def __init__ (self, titre, auteur) :
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def __str__ (self) :
        return f' {self.titre}, {self.auteur}, {self.disponible}'

    def borrow(self) :
        if self.disponible ==True :
            self.disponible =False
            return True
        else :
            return False


    def return_book(self) :
        if self.disponible ==False :
            self.disponible =True
            return True
        else :
            return False



livre1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
livre2 = Book("1984", "George Orwell")
livre3 = Book("To Kill a Mockingbird", "Harper Lee")

print(livre1)
print(livre1.borrow())
print(livre1)
print(livre1.borrow())
print(livre1)
print(livre1.return_book())
print(livre1)