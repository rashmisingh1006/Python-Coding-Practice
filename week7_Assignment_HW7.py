print("Exercise #1:")
print("*********")
import datetime
class Person:
    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

person = Person(
    "Jane",
    "Doe", datetime.date(1992, 3, 12),  # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age())
"""
1. Person : Here Person is a Class and the scope is global.
2. person : Here, person is an object, an instance of the Person class. The scope is global.
3. surname : It is a parameter passed into the __init__method of Person Class. It has local scope.
4. self : self is the first parameter inside the method definition as whenever we call a method on an object, the
   object itself is automatically passed on as first parameter. Hence, it gives us the way to access the object's
   properties from inside the object's methods. Scope of the self parameter is local to the method in which it is passed.
5. age(the function name): Here age is a custom method that calculates the age of the person using the
   birthdate and the current date. It does not take any parameters except self. It only uses information stored in
   the object's attributes and the current date which it retrieves using the datetime module.
   Scope of age is local to the Person Class.
6. age(the variable used inside the function) : It is a local variable inside the age method and it's scope is limited
   to the age method.
7. self.email : It is a way in which we use attributes inside the method of a class. It is local to the methods in the
   class.
8. person.email : It is an attribute of person object and another way of writing self.email and the scope is global.
"""
print("**********************")
print("Exercise 2:")
import datetime
class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        self.age = 0
        self.recalculate_age()

    def recalculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        self.age = age
        self._age_last_recalculated = today

    def age(self):
        if datetime.date.today() > self._age_last_recalculated:
            self.recalculate_age()
        return self.age


person4 = Person("Cate", "Blanchett", datetime.date(1964, 10, 10),  # year, month, day
                 "Sydeny Australia",
                 "444 666 0808",
                 "cate.blanchett@gmail.com")

print(person4.age)

print("*********************")
print("Exercise 3")
class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

square1 = Square(2)
print(square1.get_area())
square2 = Square(4)
print(square2.get_area())

print("**************************")
print("Exercise 4")

person1 = Person("Sydney", "White", datetime.date(2011, 9, 21), # year, month, day
    "330 400 EAST",
    "999 888 1000",
    "sydney.white@example.com")


print(dir(person1))
print(dir(Person))

print(person1.__str__())
print(str(person1))

"""
1. If I call the __str__ method on the instance, it will give me the pointer of the object. We will get the same result 
if we call the str function with instance as a parameter.
"""

print(type(person1))
print(type(Person))
"""
2. The type of the instance is Person class.
3. The type of the Person is class.
"""
"""
4. The vars() function prints the name and value of all the custom attributes of any object that is passed 
in as a parameter.
"""
print(vars(person))


print("************************")
print("Exercise 5")
class Reverse:
    def __init__(self, str):
        self.str = str
    def reverse_string(self):
        return ' '.join(reversed(self.str.split()))

string = Reverse("I love Python Programming")
print(string.reverse_string())

print("************************")
print("Exercise 6")
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_circle(self):
        return format(pi * (self.radius ** 2),".2f")

    def perimeter(self):
        return format(2 * pi * self.radius,".2f")

NewCircle = Circle(16)
print(NewCircle.area_circle())
print(NewCircle.perimeter())

print("************************")
print("Exercise 7")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area_rectangle(self):
        return format(self.length * self.width, ".2f")

rectangle1 = Rectangle(10,6.8)
print(rectangle1.area_rectangle())


print("************************")
print("Exercise 8")
from math import sqrt
class Line:
    x = 0
    y = 0
    coordinate1 = (x, y)
    coordinate2 = (x, y)
    def __init__(self, coor1, coor2):
        self.coordinate1 = coor1
        self.coordinate2 = coor2
    def distance(self):
        dist = sqrt((self.coordinate2[0]-self.coordinate1[0])**2 + (self.coordinate2[1] - self.coordinate1[1])**2)
        return format(dist,".2f")

    def slope(self):
        slp = (self.coordinate2[1] - self.coordinate1[1])/(self.coordinate2[0] - self.coordinate1[0])
        return format(slp,".1f")

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)
print("The distance between coordinates is:", li.distance())
print("The slope of the given line is:",li.slope())

print("************************")
print("Exercise 9")
# Step 1:
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number / 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result
# Step2:
num = int(input("Please enter an number: "))
while num != 1:
    num = collatz(int(num))






