def modify_fruit_list(fruits):
    fruits_set = set(fruits)
    fruits_set.add('pear')
    fruits_set.remove('apple')
    fruits_list = list(fruits_set)
    return fruits_list[1]

fruits = ['apple', 'banana', 'orange']

print(modify_fruit_list(fruits))
