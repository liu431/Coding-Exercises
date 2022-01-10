## Notes

[Real Python  - Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)

### OOP
A method of structuring a program by bundling related __properties__ and __behaviors__ into individual objects

#### Classes vs Instances
* Classes: create user-defined data structures; a blueprint for how something should be defined
* Methods: identify the behaviors and actions that an object created from the class can perform with its data. 
* Instance: an object that is built from a class and contains real data.

```python
class Dog:
    # Class attribute (same value for all class instances)
    species = "Canis familiaris"
    
    # Sets the initial state of the object by assigning the values of the object’s properties
    # Self parameter: so that new attributes can be defined on the object
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Special instance method / dunder methods
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    # Instance method 
    def speak(self, sound):
        return f"{self.name} says {sound}"
        
# Instantiate an Object
buddy = Dog("Buddy", 9)
buddy.name # 'Buddy'
# Custom objects are mutable by default and can be altered dynamically
buddy.age = 10 
print(buddy) # 'Buddy is 10 years old'
```

#### Inheritance
* One class takes on the attributes and methods of another.
* Child classes are derived from parent classes.
* Child classes can override or extend the attributes and methods of parent classes.

```python
# Create new class with its own name and then put the name of the parent class in parentheses
class JackRussellTerrier(Dog):
    # Override a method defined on the parent class
    def speak(self, sound="Arf"):
        # Access the parent class from inside a method of a child class 
        return super().speak(sound)
    
miles = JackRussellTerrier("Miles", 4)    
isinstance(miles, Dog) # True
```


#### Polymorphism
* Different object classes can share the same method name

#### Method overriding










