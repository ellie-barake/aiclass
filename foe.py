class library:
    def __init__(self,books):
        self.books=books

    def borrow_books(self,tittle):
        for i in self.books:
            if tittle.lower()== i.lower():
                return "available"
            else:
                return "not available"    
books=['biology','physics','chesmistry']            
documents=library(books)
documents.borrow_books('chemistry')
print(documents.borrow_books('chemistry'))
