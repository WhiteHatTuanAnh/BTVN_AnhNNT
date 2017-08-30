
def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory.keys():
        inventory[fruit] += quantity
    else :
        inventory[fruit] = quantity
    return

new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print("strawberries" in new_inventory)
print(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory["strawberries"] == 35)

