prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

purchased_items = [
    {"banana": 5},
    {"orange": 3}
]

total = 0

for item in purchased_items :
    for key in item :
        print ( "{0}, quantity: {1}, unit price: {2}".format( key, item[key], prices[key] ) )
        purchased_item = item[key] * prices[key]
        print("The amount of {0} is: {1}$".format( key, purchased_item ))
        total += purchased_item
        print()

print ("Total: {0}$".format(total))