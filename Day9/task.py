# program_dictionary = {
#     "Bug":"An error",
#     "Function":"A piece of code to call",
#     "Loop":"The action of doing something over and over again",
# }
#To add something to the dictionary
# program_dictionary["While"] = "It's a type of loop"
# print(program_dictionary)

# To edit something to the dictionary
# program_dictionary["Loop"] = "It's a loop."

# To wipe out entire dictionary
# program_dictionary = {}
# print(program_dictionary)

# It's better to create an empty dictionary first, then add values
# empty_dictionary = {}

# Loop through a dictionary
# for task in program_dictionary:
#     print(task)
#     print(program_dictionary[task])
# Nested
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
# Nested List in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }
#print Lille
# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
}

print(travel_log["Germany"]["cities_visited"][2])