# List compression
list1 = []

# Regular Code to get even numbers in a list without manually typing them
for x in range(0,11):
    if x % 2 == 0:
        list1.append(x)
print(list1)

# List Compression 1
list3 = [i for i in range(0,12,2)]
print(list1)

# List Compression 2
list3 = [x for x in range(0,11) if x % 2 == 0]
print(list3)

# Create a List from 6-27, 27 inclusive
# Which has multiples of 3 and values should be cubed 9*9*3 or 9**3

list4 = [x**3 for x in range(6, 28) if x%3==0]
#or 
list4 = [x*3*3 for x in range(6, 28) if x%3==0]
print(list4)

#[(x,y)] => Create pairs but catch is that they should not be similar.... (1,2), 
x_list = [1,2,3,4]
y_list = [2,6,1,7]

# 1st Method:
list4 = [(x,y) for x in x_list for y in y_list if x != y]
print(list4)

# 2nd Method:
list_pair = [(x, y) for x, y in zip(x_list, y_list) if x != y]
print(list4)