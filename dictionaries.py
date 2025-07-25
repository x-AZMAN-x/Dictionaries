#blank/ empty dictionary
blank_dict = {}
print(blank_dict)

#dictionary with mixed keys
mixed_dictionary = {
    "name": "Azman",
    "age": 12,
    1: [10, 20, 50]
}
print(mixed_dictionary["name"])
print(mixed_dictionary.get("name"))

#updating a key in dictionary
mixed_dictionary["age"] = 25
print(mixed_dictionary)

#how to add a new key value
mixed_dictionary["Address"] = "Dhaka"
print(mixed_dictionary)

#how to remove a key value
mixed_dictionary.pop(1)
print(mixed_dictionary)