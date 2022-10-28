### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_other_list = [29, 1.77, 'Juan', 'Camou']

print(my_other_list)

print(my_other_list[0])

print(my_other_list[-1])

print(my_other_list.count(29))

age, height, name, lastname = my_other_list

print(age)

my_list.append("a")

my_list.append("c")

print(my_list)

my_list.insert(1, "b")
print(my_list)

my_list.remove("b")
print(my_list)

print(my_list.pop())
print(my_list)

# del my_list[2]