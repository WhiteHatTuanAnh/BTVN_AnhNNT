items = ['T-Shirt', 'Sweater']

def show_items():
    print('Our items: ',end='')
    for i in items:
        if i == items[-1]:
            print(i)
            break
        print(i,',',end='')
    print()

while True:
    act = list(input('Welcome to our shop, what do you want (C, R, U, D)? '))
    # Xóa các khoảng trắng:
    while act[0] == ' ' or act[-1] == ' ':
        act.remove(' ')

    if (act[0] == 'C') or (act[0] == 'c'):
        new_item = str(input('Enter new item: '))
        items.append(new_item)
        show_items()
    elif (act[0] == 'R') or (act[0] == 'r'):
        show_items()
    elif (act[0] == 'U') or (act[0] == 'u'):
        show_items()
        position = int(input('Update position? '))
        new_item = str(input('New item? '))
        items.insert(position,new_item)
    elif (act[0] == 'D') or (act[0] == 'd'):
        show_items()
        del_position = int(input('Delete position? '))
        items.pop(del_position-1)
        show_items()
    else:
        print('Wrong input.')
