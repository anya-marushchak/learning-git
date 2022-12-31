#Task 1
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
triples = [number**3 for number in list]
print(triples)
formula = [number**3 for number in list if number % 2]
print(formula)
print(11%2)
for number in list:
  if "9":
    print(number)
print()

#Task 2
my_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
print(my_list)
print(my_list[1:4])
print(my_list[5:10])
print(my_list[-2:])
print(my_list[0])
print(my_list[4])
print(my_list[10:12])
print()
#another method of task 2 using append function
my_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
new_list = []
new_list_2 = []
for number in my_list:
  new_list.append(my_list[1:4])
  new_list.append(my_list[5:10])
  new_list.append(my_list[-2:])
  new_list_2.append(my_list[0])
  new_list_2.append(my_list[4])
  new_list_2.append(my_list[10:12])
  break
print(my_list)
print(new_list)
print(new_list_2)

