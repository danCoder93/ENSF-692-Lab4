# ENSF 692 Spring 2025
# May 15 Lab 4
# Input With Functions

# Add comments to explain the functionality of this program
# basically it's running a loop a specific number of times asking user an input and then printing it.
# The first part of the code ask users their input
# and return the type of entry along with input value.
# The second part takes the input value and its type and print it.
# The return type of input prompt is default to string type unless converted to specific data type

def get_user_input(n):
    entry = input("Please type any entry #" + str(n + 1) + ": ")
    return entry, type(entry)

def process_user_input(n, entry, type):
    print("This is entry #" + str(n + 1) + ":", entry)
    print("The type of entry #" + str(n + 1) + " is :", str(type.__name__))


print('\n' * 2)
num_of_repeats = 3
results = []
results_types = []

for i in range(num_of_repeats):
    a, b = get_user_input(i)
    results.append(a)
    results_types.append(b)

for i in range(num_of_repeats):
    process_user_input(i,results[i], results_types[i])

