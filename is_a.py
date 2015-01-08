## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    """ pass the number of legs, then the things the animal eats.                                  """
    def __init__(self, legs, **diet):
        self.diet = diet
        self.legs = legs
        self.health = 10
        self.poison = []
    
    def meal(self, food):
        if food in self.diet:
            self.health += self.diet[food] 
            
        else:
            print ( "I can't eat that")
        
        if self.health <= 0:
            print ( "The %r has died" %(self) )
            
            
    
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name attribute
        self.name = name
        self.eats = ['meat', 'dog food']
        self.legs = 4

## Cat is an animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has a name attribute
        self.name = name

## Person is-an objects
class Person(object):

    def __init__(self, name):
        ## Person has-a name attribute
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass


## The instance rover is-a Dog with the name "Rover".
rover = Dog("Rover")

## The instance of satan is-a Cat with the name "Satan".
satan = Cat("Satan")

## The instance "Mary" is-a Person with the name "Mary"
mary = Person("Mary")

## marry has-a pet attribute satan. Which happens to be the name 
## of a Cat.

mary.pet = satan

## frank is-a Employee with a name and salary parameters.
frank = Employee("Frank", 120000)

## the instance of frank has-a pet rover
frank.pet = rover

## flipper is-a fish! A fish is an object!
flipper = Fish()

## Salmon is-a fish.
crouse = Salmon()

## Harry is a Halibut
harry = Halibut()
