import inflect
p = inflect.engine()

list_names = []

while True:
    try:
        name = input("Name: ")
        list_names.append(name)
    except EOFError:
        print()
        break

Formatted_list = p.join(list_names)    
print("Adieu", "Adieu to " + Formatted_list)
