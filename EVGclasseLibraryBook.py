class LibraryBook (object):   
    def __init__(self, title, author, pub_year, call_no):
      self.title = title
      self.author = author
      self.year = pub_year
      self.call_number = call_no
      self.checked_out = False

      my_book = LibraryBook()

      my_book.title = "Harry Potter and the Philosopher's Stone"
      my_book.author = ('Rowling', 'J.K.')
      my_book.year = 1998
      my_book.call_number = "PZ7.R79835"

      # new_book = LibraryBook("Harry Potter and the Sorcerer's Stone", 
      #                  ("Rowling","J.K."), 1998, "PZ7.R79835")

      
       # Retorna o título e as informações do autor do livro como uma string
    def title_and_author(self):
            return "{self.author[0]}: {self.title[0]}" 
        
        # Imprime todas as informações associadas a um livro neste formato
    def __str__(self): # certifique-se de que __str__ retorna uma string!
            return "{} {} ({}): {}".format(self.author[1], self.author[0], self.year, self.title)

        # Retorna uma representação de string do livro com o título e call_number     
    def __repr__(self): 
            return "<Book: {} ({})>".format(self.title, self.call_number)
            print(my_book)  
            my_book.title_and_author()
            
            

print(LibraryBook)
print(LibraryBook.title_and_author)
print(LibraryBook.__repr__)


              