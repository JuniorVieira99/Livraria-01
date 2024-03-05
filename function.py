
id_book = 0
lib_index = ""
class Book:
    
    def Book_Cons(self,name,author,year,genre,pages):
        global id_book
        id_book += 1
        self.Name = name
        self.Author = author
        self.Year = year
        self.Genre = genre
        self.Pages = pages
        self.Id = id_book
        self.Name = self.Name.capitalize()  
        self.Author = self.Author.capitalize() 
        self.Genre = self.Genre.capitalize() 
        
class Library:
    def __init__(self):
        global lib_index
        lib_index = input("Insira o nome da Livraria: ").title()
        self.lib = {}
        
    def AddBook(self,Book):
        if Book.Id in self.lib.keys():
            print("\nEsse livro já perterce a livraria.")
        else:
            self.lib.update({Book.Id:{
                'Name' : Book.Name ,
                'Author' : Book.Author ,
                'Year': Book.Year ,
                'Genre' : Book.Genre ,
                'Pages' : Book.Pages
            }}) 
            
    def RemoveBooks(self,Book):
        if not self.lib == {}:
            print("A Livraria esta vazia")            
        elif Book.Id in self.lib.keys():
            del self.lib[Book.Id]                 
        else:
            print("\nEsse livro não está na livraria.")
    
   
    def User_RemoveBooks(self):
        if self.lib == {}:
            print("A Livraria esta vazia ")
        else:
         book_i =""
         book_id=""   
         Book_Name = input("Insira o nome do Livro: ").title()        
         for keys in self.lib.keys():
            for k,v in self.lib[keys].items():
                if Book_Name == v:
                    book_id = keys  
                    print("\n" + str(k) + " : " + str(v) + " Foi deletado.")  
                    book_i = 1     
                    break
                else:
                    print("\n" + str(Book_Name) + " Não está na livraria.")
                    break       
         if book_i == 1:
           del self.lib[book_id]               
                  
        
    def ShowAllBooks(self):
      if self.lib == {}:
         print("A Livraria esta vazia")     
      else: 
       for keys in self.lib.keys():
           print("Book Id: " + str(keys))
           for k,v in self.lib[keys].items():
               print("\t" + str(k) + " : " + str(v))
                    
    def User_ShowOneBook(self,Book_Name):
         if self.lib == {}:
            print("A Livraria esta vazia")
         else:                
          for keys in self.lib.keys():
            for k,v in self.lib[keys].items(): 
                 if Book_Name in self.lib[keys].values():  
                       book_id_SOB = keys
                       break  
                 else :
                       print("O livro" +str(Book_Name)+ "não está na livraria.")
                       break  
          print (book_id_SOB)
          for k,v in self.lib[book_id_SOB].items():   
                        print("\t" + str(k) + " : " + str(v))  
    def Save(self):
     if self.lib == {}:
        print("A Livraria esta vazia")
     else:   
        global lib_index
        Livraria_Book_id =""
        Livraria_Body =""
        Livraria =(f"{lib_index} : ")
        lib_index_f = lib_index.replace(" ","_")
        try:   
         # Inserir o local de salvamento   
         Lib_arquivo = open(f"C:...........\\Livraria_{lib_index_f}.txt", "w")
            
         for Keys in self.lib.keys():
            Livraria_Book_id = ("\nBook Id: " + str(Keys))
            for k,v in self.lib[Keys].items():
                Livraria_Body += ("\t\n" + str(k) + " : " + str(v))
            Livraria += ("\n" +Livraria_Book_id +"\n\t" + Livraria_Body)
            Livraria_Book_id = ""
            Livraria_Body = ""
            
         Lib_arquivo.write(Livraria)
        
        except:
            print("Caminho não encontrado")
        
    
     
#book1 = Book()
#book1.Book_Cons("Harry","J.K",1998,"Fiction",475)

#ibrary1 = Library()
#Library1.AddBook(book1)
#Library1.ShowAllBooks()
#Library1.ShowOneBook(book1)

