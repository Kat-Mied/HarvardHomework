def main(): 

    class Book:
        def __init__(self, isbn, title, author, year):
            self.isbn = isbn 
            self.title = title 
            self.author = author
            self.year = year 
        def print_info(self): 
            print(f"Book isbn: {self.isbn  }")
            print(f"Book title: {self.title}")
            print(f"Book author: {self.author}")
            print(f"Book year: {self.year}")

#create books! 
f = Book(isbn="380795272", title="Krondor: The Betrayal", author="Raymond E. Feist", year="1998")



