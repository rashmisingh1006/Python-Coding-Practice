print("Exercise #1")
print("*********************")
class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + " " + self.incantation + "\n" + self.get_description()

    def get_description(self):
        return "No description"

    def execute(self):
        print(self.incantation)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, "Accio", "Summoning Charm")

    def get_description(self):
        return "This charm summons an object to the caster, potentially over a significant distance."

class Confundo(Spell):

    def __init__(self):
        Spell.__init__(self, "Confundo", "Confundus Charm")

    def  get_description(self):
        return "Causes the victim to become confused and befuddled."

def study_spell(spell):
    print(spell)

spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())
print(Accio())


"""
1. What are the parent and child classes here?
Ans : The parent class is Spell and the child classes are Accio and Confundo.
2. What does the code print out? (Try figuring it out without running it in Python)
Ans : The code will print out the following.
Accio
Summoning Charm Accio
No description
Confundus Charm Confundo
Causes the victim to become confused and befuddled.

3. Which get description method is called when ‘study spell(Confundo())’ is executed? Why?
Ans: The get_description method under Confundo class is called as the method in the child class will override the method in the
parent class if the same method exists in both the class which is called as method overriding and is part of inheritance
mechanism.

4. What do we need to do so that ‘print Accio()’ will print the appropriate description 
  (‘This charm summons an object to the caster, potentially over a significant distance’)? 
  Write down the code that we need to add and/or change.
Ans: In the code we need to add the get_description method to the Accio class.
     def get_description(self):
         return "This charm summons an object to the caster, potentially over a significant distance."
"""

print("Exercise #2")
print("**************************")
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        Vehicle.__init__(self, name, max_speed, mileage)

    def display_desc(self):
        print("Vehicle name:", self.name + "  Speed:", str(self.max_speed) + "  Mileage:", str(self.mileage))

bus = Bus("Volvo", 180, 12)
bus.display_desc()

print("Exercise #3:")
print("****************************")
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, mileage, capacity):
        Vehicle.__init__(self, name, mileage, capacity)

    def fare(self):
        total_fare = self.capacity * 100 + 0.1 * self.capacity * 100
        return total_fare

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

print("Exercise #4:")
print("********************************")

class Numbers:
    # Create a class attribute called MULTIPLIER
    MULTIPLIER = 5
    def __init__(self, x, y):
        self.x = x
        self.y = y
#1. Write a method called add which returns the sum of the attributes x and y.
    def add(self):
        return self.x + self.y
#2. Write a class method called multiply, which takes a single number parameter
#   and returns the product of a and MULTIPLIER.
    # return the attribute MULTIPLIER * by a.
    def multiply(self, a):
        return self.MULTIPLIER * a
#3. Write a static method called subtract, which takes two number parameters, b and c, and returns b - c.

    @staticmethod
    def subtract(b, c):
        return b-c

#4. Write a method called value which returns a tuple containing the values of x and y. Make this
# method into a property, and write a setter and deleter for manipulating the values of x and y.

    @property
    def value(self):
        return self.x + self.y

    # Create a setter and a deleter for value.


    @value.setter
    def value(self, val_tuple):
        self.x, self.y = val_tuple

    @value.deleter
    def value(self):
        del self.x
        del self.y

#test the class.
num = Numbers(5,6)
print(num.add())
print(num.multiply(2))
print(num.subtract(4, 4))

print("********************************")
print("Exercise #5: Abstract Classes")
print("Part 1:")
print("********************************")

class Box:
    def add(self, *items):
        raise NotImplementedError()

    def empty(self):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class ListBox(Box):
    def __init__(self):
        self._items = []

    def add(self, *items):
        self._items.extend(items)

    def empty(self):
        items = self._items
        self._items = []
        return items

    def count(self):
        return len(self._items)


class DictBox(Box):
    def __init__(self):
        self._items = {}

    def add(self, *items):
        self._items.update(dict((i, i) for i in items))

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items

    def count(self):
        return len(self._items)


print("Part 2:")


def repack_boxes(*boxes):
    items = []
    for box in boxes:
        items.extend(box.empty())

    while items:
        for box in boxes:
            try:
                box.add(items.pop())
            except IndexError:
                break


box1 = ListBox()
for i in range(20):
    item = Item(str(i), i)
    box1.add(item)

box2 = ListBox()
for i in range(9):
    item = Item(str(i), i)
    box2.add(item)

box3 = DictBox()
for i in range(5):
    item = Item(str(i), i)
    box3.add(item)

repack_boxes(box1, box2, box3)
print(box1.count())
print(box2.count())
print(box3.count())













