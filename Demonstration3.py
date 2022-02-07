# Assignment: HW4
# Exercise #1: Fantasy Game Inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'map fragments' : 3}
total = 0
for key in stuff:
    print(stuff[key], key)
print("Total number of items : ", sum(stuff.values()))

# Exercise #2: Comma Code
characters = ["Thor", "Thanos", "Black Panther", "Iron Man", "Hulk", "Batman", "Captain America"]
c1 = "'"
for i in characters[0:5]:
    c1 += str(i) + ", "
print(c1 + characters[5] + " and " + characters[6] + "'")

# Exercise #3: Create a dictionary of technical terms and allow the user
# to lookup the definitions of these terms from the dictionary.

technical_dict = {
    "dict": "stores a key/value pair",
    "list": "stores a value at each index",
    "map": "see dict",
    "set": "stores unordered unique elements",
    "exit": "Exits the program!"
    }
term = 0
while term != "exit":
    term = input("Please enter a term: ").lower()
    if term in technical_dict:
        print(term, "->", technical_dict[term])
    elif term != "exit":
        print("The given term is not present in the dictionary.")

# Exercise #4: To write an expression that would turn the string
# "Mississippi" into a set of unique letters.

print(set("Mississippi"))

# Exercise #5:
list1 = [1,2,[3,4, "hello"]]
list1[2][2] = "goodbye"
print(list1)

# Exercise #6:
#6a.
d = {'simple key' : "hello"}
print(d['simple key'])
#6b
d = {"k1":{"k2":"hello"}}
print(d["k1"]["k2"])


