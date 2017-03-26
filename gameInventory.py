# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Displays the inventory.


def display_inventory(inventory):
    print("Inventory:")
    for keys, values in inventory.items():
        print(values, keys)
    print("Total number of items: " + str(sum(inventory.values())) + "\n")

# Adds to the inventory dictionary a list of items from added_items.


def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory.update({i: 1})
    return inventory

# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order


def right_ordered_column(firstColumnLength, secondColumnLength, firstColumnContent, secondColumnContent):
    placeholder = '{count:>{0}} {item:>' + str(secondColumnLength) + '}'
    print(placeholder.format(str(firstColumnLength), count=str(firstColumnContent), item=str(secondColumnContent)))


def lengthOfFirstColumn(inventory):
    if inventory != {}:
        listOfValues = []
        for i in inventory:
            listOfValues.append(inventory[i])
        maxLengthOfValues = len(str(max(listOfValues))) + 5
    else:
        maxLengthOfValues = len("count")
    return maxLengthOfValues


def lengthOfSecondColumn(inventory):
    if inventory != {}:
        maxLengthOfKeys = max(len(x) for x in inventory) + 5
    else:
        maxLengthOfKeys = len("item name")
    return maxLengthOfKeys


def print_table(inventory, order=None):
    print("Inventory:")
    maxLengthOfValues = lengthOfFirstColumn(inventory)
    maxLengthOfKeys = lengthOfSecondColumn(inventory)
    right_ordered_column(maxLengthOfValues, maxLengthOfKeys, "count", "item name")
    print('-' * (maxLengthOfKeys + maxLengthOfValues + 1))
    if order == "count,desc":
        sortedInventory = sorted(inventory, key=inventory.get, reverse=True)
        for i in sortedInventory:
            right_ordered_column(maxLengthOfValues, maxLengthOfKeys, inventory[i], i)
    elif order == "count,asc":
        sortedInventory = sorted(inventory, key=inventory.get)
        for i in sortedInventory:
            right_ordered_column(maxLengthOfValues, maxLengthOfKeys, inventory[i], i)
    else:
        for i in inventory:
            right_ordered_column(maxLengthOfValues, maxLengthOfKeys, inventory[i], i)
    print('-' * (maxLengthOfKeys + maxLengthOfValues + 1))
    print("Total number of items: " + str(sum(inventory.values())) + "\n")

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).


def import_inventory(inventory, filename="import_inventory.csv"):
    file = open(filename, 'r')
    read_new_loot = file.read()
    file.close()
    form_new_loot = read_new_loot.strip().split(',')

    new_loot = add_to_inventory(inventory, form_new_loot)
    return new_loot

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).


def export_inventory(inventory, filename="export_inventory.csv"):
    file = open(filename, 'w')
    for i in inventory:
        file.write((i + ',') * inventory[i])
    file.close()
    import os
    with open(filename, 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()


inv = add_to_inventory(inv, dragon_loot)
import_inventory(inv)
display_inventory(inv)
print_table(inv, "count,desc")
export_inventory(inv)
