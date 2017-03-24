# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['ruby', 'gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']

# Displays the inventory.
def display_inventory(inventory):
    print("inventory:")
    for k, v in inventory.items():
        print(v,k)
    print("Total number of items: " + str(sum(inventory.values())) + "\n")
    
# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory.update({i:1})
    return inventory   

  


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    print("inventory:")
    b = max(len(x) for x in inventory) + 5
    asdf = []
    for i in inventory:
        asdf.append(inventory[i])
    c = len(str(max(asdf))) + 5

    placeholder1 = '{count:>{0}} {item:>' + str(b) + '}'
    print(placeholder1.format(str(c),count="count", item="item name"))
    print('-'*(b+c+1))

    if order == "count,desc":
        a = sorted(inventory, key=inventory.get, reverse=True)
        for i in a:
            placeholder = '{count:>{0}} {item:>' + str(b) + '}'
            print(placeholder.format(str(c),count=str(inventory[i]), item=i))
    elif order == "count,asc":
        a = sorted(inventory, key=inventory.get)
        for i in a:
            print(str(inventory[i]) + " " + i)
    elif None:
        pass
    else:
        pass
    print('-'*(b+c+1))
    print("Total number of items: " + str(sum(inventory.values())) + "\n")




    


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    file = open(filename, 'r')
    new_loot = file.read()
    file.close()

    newStuff = new_loot.strip().split(',')
    return newStuff




# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).

def export_inventory(inventory, filename="export_inventory.csv"):
    file = open(filename, 'w')
    for i in inventory:
        file.write((i + ",") * inventory[i])

    file.close()


inv = add_to_inventory(inv,dragon_loot)
inv = add_to_inventory(inv,import_inventory(inv))
display_inventory(inv) 
print_table(inv, "count,desc")
export_inventory(inv)