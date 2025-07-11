# DAY - 7
# This code snippet demonstrates the use of dictionaries in Python.
#making a dictionary to store information about a person
person = {
    "name" : "Pratyush", #key-value pair for name
    "age" : 18,
    "gender" : "male",
    "student" : True,
}
print(f"person information : {person}")
print(f"name : {person["name"]}\n age : {person["age"]}\n")
print(f"keys : {person.keys()}")
print(f"values : {person.values()}\n")
# Modification of dictionary
person["city"] = "Mumbai"
person["age"] = 19
person.pop("student")
print(f"Modified person information : {person}")
