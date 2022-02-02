#Week4 In class exercise2

#1.1 Create Dictionaries : Use any names and birthdays you want to create a birthday dictionary that has four entries.
# The name is the key and the value is the birth date.  Print each birth date by using the key to access each entry.

birthday = {
    "Annie": 1994,
    "Katie": 1998,
    "Sydney": 2000,
    "Amy": 2002
}
for key in birthday:
    print(key, "->", birthday[key])

#1.2 Update Dictionaries : Using the dictionary from above, update the last entry and change the birth date to 06/06/1980.

birthday = {
    "Annie": 1994,
    "Katie": 1998,
    "Sydney": 2000,
    "Amy": 2002
}
birthday["Amy"] = "06/06/1980"
print(birthday)

#1.3 Dictionary With Lists : Create a dictionary of the seasons Fall, Spring and Summer where the name of the season is
# the key and the value is a list of the months in that season. Print the value of "Fall".

seasons = {
    "Fall": ["September", "October", "November"],
    "Spring": ["March", "April", "May"],
    "Summer": ["June", "July", "August"]
}
print(seasons["Fall"])

#1.4 Dictionary Merge : Create the same dictionary as in exercise 3 but also create a second dictionary with only the season of Winter.
# Use the dictionary.update method to merge the winter dictionary into the seasons dictionary.  Print the seasons dictionary.

seasons = {
    "Fall": ["September", "October", "November"],
    "Spring": ["March", "April", "May"],
    "Summer": ["June", "July", "August"]
}
print(seasons)
winter_season = {"Winter": ["December", "January", "February"]}
seasons.update(winter_season)
print(seasons)

