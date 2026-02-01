#Create and Access Dictionary Elements
print("4.1 Create and Access Dictionary Elements")
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Created Dictionary:", my_dict)

print("Access 'name':", my_dict["name"]) 
print("Access 'age':", my_dict.get("age")) 


#Update Dictionary
print("\n4.2 Update Dictionary")
my_dict["age"] = 26 
print("Updated 'age' to 26:", my_dict)

my_dict["profession"] = "Engineer" 
print("Added 'profession':", my_dict)


#Removing Elements
print("\n4.3 Removing Elements")
removed_value = my_dict.pop("city")
print(f"Removed 'city': {removed_value}")
print("Dictionary After Removing 'city':", my_dict)

del my_dict["name"] 
print("Dictionary After Deleting 'name':", my_dict)

my_dict.clear() 
print("Dictionary After Clearing All Elements:", my_dict)


#Merging Dictionaries
print("\n4.4 Merging Dictionaries")
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5}
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

merged_dict = dict1.copy() 
merged_dict.update(dict2) 
print("Merged Dictionary:", merged_dict)