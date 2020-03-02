inventory = {
    'fruit': {
        'apple': 250,
        'pear': 500,
        'orange': 10
    },
    'vegetable': {
        'cucumber': 300,
        'broccoli': 100
    }
}


def category_adder():
    category_prompt1 = input("what is the Category you are trying to add:")  # inpu goes here for addition of category
    if category_prompt1 in inventory.keys():
        print("this category is already accounted for.\nCannot be added.")
    if category_prompt1 not in inventory.keys():
        inventory[category_prompt1] = {}
    return inventory


def category_deleter():
    print(inventory, '\n.This is the inventory of interest. \nPlease choose a category that is present to delete.')
    category_chooser_del = input("What category are you trying to delete: ")
    if category_chooser_del in inventory:
        del inventory[category_chooser_del]
        print(inventory)
    else:
        print(inventory, '\nThis is the inventory of interest. \nPlease choose a category that is present.')
    return inventory
# Item adder


def item_adder():
    category_chooser_item_add = input('Which category is the item you want to add:')           # input goes for key addition
    item_add, quantity_added = input("What is the item of interest to add and quantity added (add values with space between):").split()
    if category_chooser_item_add in inventory.keys():
        inventory[category_chooser_item_add][item_add] = quantity_added
    return inventory


def item_deleter():
    print(inventory)
    category_chooser_item_del = input("Which category is the item located in: ")
    item_del = input('Which item is being deleted: ')
    if category_chooser_item_del in inventory.keys():
        del (inventory[category_chooser_item_del][item_del])
    return inventory


def item_modifier():
    category_chooser_item_modifier = input('Input which category is the item located in: ')
    item_chooser_modifier = input('Which item are you trying to modify')
    new_value_for_item = input('What is the new value for this item: ')
    if category_chooser_item_modifier in inventory.keys():
        inventory[category_chooser_item_modifier][item_chooser_modifier] = int(new_value_for_item)
    return inventory


def inventory_printer():
    print(inventory)


def main():

    print(''' Program to change inventory: Type in corresponding number.
    1. Add Category
    2. Delete Category
    3. Add Item
    4. Change Item
    6. Print Inventory
    0 or Exit to Leave Program''')
    print(inventory)
    while True:
        try:
            prompter = input('What is the respective prompt:')
            if 0 <= int(prompter)<= 6:
                if int(prompter) == 1:
                    category_adder()
                if int(prompter) == 2:
                    category_deleter()
                if int(prompter) == 3:
                    item_adder()
                if int(prompter) == 4:
                    item_deleter()
                if int(prompter) == 5:
                    item_modifier()
                if int(prompter) == 6:
                    inventory_printer()
                elif prompter == '0' or prompter == 'Exit':
                    print('function terminated.')
                    break
        except ValueError:
            print('Not a Valid Input.')


main()