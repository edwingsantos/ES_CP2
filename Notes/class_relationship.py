##ES 1 Class relationship notes 
#
##inheritance
##parent class
#class Vehical:
#    def __int__(self, model, brand):
#        self.brand = brand
#        self.model = model
#
#    def move(self):
#        print("Move!")
#
##Child class
#class Car(Vehical):
#    pass
#
#class Boat(Vehical):
#    def move(self):
#        print("sail")
#
#class Plane(Vehical):
#    def move(self):
#        print("Fly")
#
#car = Car("Ford", "Mustang")
#boat = Boat("Ibiza", "Touring 20")
#plane = Plane("Boeing", "747")
#
#print(boat.brand)
#print(boat.model)
#boat.move()


#aggretiong 
class library:
    def __init__(self, name, catalog = []):
        self.name = name
        self.catalog =  catalog
    
    def add_book(self, book):
        self.catalog.append(book)

    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.pop(book)
        else:
            print("hi")

    def view_catalog(self):
        for book in self.catalog:
            print(book)

class Book:
    def __init__(self, title, author):
            self.title =  title
            self.author =  author

    def __str__(self):
        return f"{self.title} by {self.author}"
    

lib = library("Provo Library")

lib.add_book(Book("edwing biography", "me "))

lib.view_catalog()