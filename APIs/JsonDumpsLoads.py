'''Python offers great support for JSON through its json library. We can convert lists and
dictionaries to JSON, and vice versa. Our ISS Pass data, for example,
is a dictionary encoded as a string in JSON format.
The JSON library has two main methods:
    dumps — takes in a Python object and converts it to a string
    loads — takes in a JSON string and converts it to a Python object
'''

# Make a list of fast food chains.
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(type(best_food_chains))

# Import the JSON library.
import json

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
print(type(best_food_chains_string))

# Convert best_food_chains_string back to a list.
print(type(json.loads(best_food_chains_string)))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))

# Use the JSON function loads to convert fast_food_franchise_string to a Python object.
# Assign the resulting Python object to fast_food_franchise_2.
fast_food_franchise_2 = json.loads(fast_food_franchise_string)

