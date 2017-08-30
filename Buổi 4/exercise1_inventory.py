inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
# inventory["pocket"] = ["seashell" , "strange berry" , "lint" ]

inventory.update({'pocket':['seashell','strange berry','lint']})
print("pocket :", inventory["pocket"])

inventory["backpack"].sort()
print("backpack :", inventory["backpack"])

inventory["backpack"].remove("dagger")
print("backpack :", inventory["backpack"])

inventory["gold"] += 50
print("gold after add 50 :", inventory["gold"])

# Add a key to inventory called 'pocket'.
# Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
# .sort()the items in the list stored under the 'backpack' key.
# Then .remove('dagger') from the list of items stored under the 'backpack' key.
# Add 50 to the number stored under the 'gold' key.
