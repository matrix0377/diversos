class LibraryBook (object):   
    def __init__(self, title, author, pub_year, call_no):
      self.title = title
      self.author = author
      self.year = pub_year
      self.call_number = call_no
      self.checked_out = False

      
       # Retorna o título e as informações do autor do livro como uma string
    def title_and_author(self):
        return (f"Autor: {self.author}    : Título : {self.title}") 
        
        
        # Imprime todas as informações associadas a um livro neste formato
        # certifique-se de que __str__ retorna uma string!
    def __str__(self): 
        return "{} --->> {} ({}): {}".format(self.call_number, self.author, self.year, self.title)


        # Retorna uma representação de string do livro com o título e call_number     
    def __repr__(self): 
        return ("Book     : {},\nCall_Number: {}".format(self.title, self.call_number))
        
            
            
my_book=LibraryBook(
    "Harry Potter and the Philosopher's Stone",
    "Rowling, J.K",
    1998,
    "PZ7.R79835"
    )

my_book2 = LibraryBook(
    "Learning Perl",
    "Schuwartz, Randal L.",
    2008,
    "QA76.73.P22"
)


# my_book.title = "Harry Potter and the Philosopher's Stone"
# my_book.author = ('Rowling', 'J.K.')
# my_book.year = 1998
# my_book.call_number = "PZ7.R79835"

# new_book = LibraryBook("Harry Potter and the Sorcerer's Stone",
#                  ("Rowling","J.K."), 1998, "PZ7.R79835")

# my_book1 e my_book2
print('\n')

print('-=' * 35, "\n")
print('----- Função title_and_author  ------\n')
print(my_book.title_and_author())
print(my_book2.title_and_author())
print('\n')

print('-=' * 35, "\n")
print('----- Função __repr___  ------\n')
print(my_book.__repr__())
print('\n')
print(my_book2.__repr__())

print('-=' * 35, "\n")
print('----- Função __str__  ------\n')
print(my_book.__str__())
print('\n')
print(my_book2.__str__())
print('\n')
