filename = "../data/names.txt"

with open(filename, 'r') as f:
    for line in f:
        name = line[:-1]
        print(f"Hello, {name}!")
