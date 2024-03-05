from function import Book
from function import Library
def Menu():
    Choice_a = ""
    Choice_b = ""    
    while Choice_a != "3":
     Choice_a = input("\n1. Criar Livraria."
                      "\n2. Sair.\n")
     match Choice_a:
         case "": 
             print("Insira um comando")  
         case "1":
             Library1 = Library()
             while Choice_b != "6": 
                Choice_b = input(
        "\nLivraria"            
        "\n1. Adicionar Livro:  "
        "\n2. Remover Livro: "
        "\n3. Mostrar Todos os Livros: "
        "\n4. Procurar um Livro: "
        "\n5. Salvar Livraria: "
        "\n6. Sair: \n"
            )
                match Choice_b:
                    case "":
                            print("Insira um comando")
                    case "1":
                            name = input("Nome: ").title()
                            author = input("Author: ").title()
                            year = input("Year: ")
                            genre = input("Genre: ").title()
                            pages = input("Page: ")
                            Book1 = Book()
                            Book1.Book_Cons(name,author,year,genre,pages)
                            Library1.AddBook(Book1)
                    case "2":
                            Library1.User_RemoveBooks()
                    case "3":
                            Library1.ShowAllBooks()
                    case "4":
                            Book_nameSK = input("Insira o nome do Livro: ").title()
                            Library1.User_ShowOneBook(Book_nameSK)       
                    case "5":
                            Library1.Save()
                    case "6":
                            break   
                    case _:
                            print("\nInsira um numero de 1 a 4: ") 
                
         case "2":
             break    
         case _: 
             print("Insira um numero de 1 a 3")     
Menu()              