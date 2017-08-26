
#find the biggest sheep size and shear it:
def find_biggest_shear():
    biggest_sheep = max(sheeps_sizes)
    biggest_sheep_pos = sheeps_sizes.index(max(sheeps_sizes))
    print('Now my biggest sheep is',biggest_sheep,'let\'s shear it')
    sheeps_sizes[biggest_sheep_pos] = 8
    print('After shearing, here is my flock')
    print(sheeps_sizes)

#raise all sheep sizes 50:
def One_month_shear():
    print('One month has passed, now here is my flock')
    i = 0
    for sheep in sheeps_sizes:
        sheeps_sizes[i] = sheeps_sizes[i] +50
        i += 1
    print(sheeps_sizes)

#main program:
print('Hello! My name is Tuan Anh and these are my sheep sizes')
sheeps_sizes = [5, 7, 300, 90, 24, 50, 75]
print(sheeps_sizes)
find_biggest_shear()

for count in range(2):
    print('Month',count+1,':')
    One_month_shear()
    find_biggest_shear()
    print()

count += 1
print('Month',count+1,':')
One_month_shear()

totalsize = sum(sheeps_sizes)
print('My flock has size in total:',totalsize)
print('I would get',totalsize,'* 2$ =',totalsize*2,'$')