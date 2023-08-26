#1st example of method
class Try: #a class
        def __init__(self):
                pass
        def printhello(self,name): #a method
                print(f"Hello, {name}")
                return name
obj=Try()
obj.printhello('Ayushi')


#2nd example of method
class Animal: #class
       def __init__(self,species,gender): #a method
                 self.species=species
                 self.gender=gender
fluffy=Animal('Lion','Male')
print(fluffy.gender)