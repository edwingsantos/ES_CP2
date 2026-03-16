#Es 

#example 1
class Animal:
    def __init__(self, name, species, age):
       self.name = name
       self.species = species
       self.age = age

    def __str__(self):
        return f"""Namne: {self.name}\nspecies: {self.species}\nage: {self.age}"""

    def birdthday(self):
        self.age += 1

dog = Animal("Coco", "Dog", 4)
bunny = Animal("Judy","Rabbit", 20)
print(dog)
print(bunny)
dog.birdthday()
print(dog)

#  Example 2
class ClassPeriod:
    def __int__(self, subject, teacher = "Ms. LaRose", room = None):
        self.subject = subject.capitilize()
        self.teacher = teacher
        self. room = room 
    def __str__(self):
        return f"Subject: {self.subject}\nTeacher: {self.teacher}\nRoom: {self.room}"
    
first = ClassPeriod("Computer Programing 2", room=200)
second = ClassPeriod("Seminary", "Bro Little", "outside")