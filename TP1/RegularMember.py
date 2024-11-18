from Member import Member

class RegularMember (Member) :

    def __init__ (self, nom) :
        super().__init__(nom)
        self.borrow_limit = 2
        
    def borrow_book (self, livre) :
        if len(self.borrowed_books) < self.borrow_limit :
            super().borrow_book (livre)
        else :
            print ("Limite d\'emprunt atteinte")
