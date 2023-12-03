people = ["Alice", "Bob", "Carl", "Debbie", "Edward", "Florence"]
search = input("Input an element to search for: ")
found = False

for i in range(len(people)):
    if people[i] == search:
        found = True

if found:
    print(search, "was found in the list")
else:
    print(search, "was not found in the list")