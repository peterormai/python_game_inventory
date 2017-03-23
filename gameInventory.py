# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

firstInv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['ruby', 'gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']

# Displays the inventory.
def display_inventory(inv):
    print("Inventory:")
    for k, v in inv.items():
        print(v,k)
    print("Total number of items: " + str(sum(inv.values())) + "\n")
    
# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inv, added_items):
    for i in added_items:
        if i in inv:
            inv[i] += 1
        else:
            inv.update({i:1})   

  


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inv, order=None):
    print("Inventory:")

  

    # countos sort is b és c szerint írja ki, utána total number, mért nem jó az item name??
    
    b = max(len(x) for x in inv) + 10
    asdf = []
    for i in inv:
        asdf.append(inv[i])
    c = len(str(max(asdf)))

    placeholder1 = '{count:>{0}} {item:>' + str(b-3) + '}'
    print(placeholder1.format(str(c),count="count", item="item name"))
    print('-'*(b+c+1))

    if order == "count,desc":
        a = sorted(inv, key=inv.get, reverse=True)
        for i in a:
            placeholder = '{count:>{0}} {item:>' + str(b) + '}'
            print(placeholder.format(str(c),count=str(inv[i]), item=i))
    elif order == "count,asc":
        a = sorted(inv, key=inv.get)
        for i in a:
            print(str(inv[i]) + " " + i)
    elif None:
        pass
    else:
        pass
    print('-'*(b+c+1))

 


add_to_inventory(firstInv,dragon_loot)
display_inventory(firstInv) 
print_table(firstInv, "count,desc")

    


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    import filename
    print(filename)
    pass


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    pass
