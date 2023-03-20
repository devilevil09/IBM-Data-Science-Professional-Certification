# List and tuples

# TUPLES
Ratings = (10,9,8,7,6,5,4,3,2,1)

print(Ratings)

tuple1 = ('disco',10,4.7)


print(tuple1)
print(type(tuple1))
print(tuple1[1])
print(tuple1[2])
print(tuple1[-1])
print(tuple1[-2])
print(tuple1[-3])

say_what=('say',' what', 'you', 'will')
print(say_what[-1])

tuple2 = tuple1+('Hey', 23,99.99,'germs')
print(tuple2)

# Tuple slicing

print(tuple2[1:4])
print(len(tuple2))

'''
# Tuple is immutable
Rating = Ratings
print(Rating)
Rating[2]=56
print(Rating)
'''
Rating = (1,45,65,56,23,'hello')
print(Rating)
print(sorted(Ratings))

# Tuple Nesting
Nested_tuple = (6,9,('xoxo','hehe'),(2,5,7),('Hello', 'mello'))
print(Nested_tuple)
print(Nested_tuple[0])
print(Nested_tuple[1])
print(Nested_tuple[2])
print(Nested_tuple[2][0])
print(Nested_tuple[2][1])
print(Nested_tuple[3])
print(Nested_tuple[4])

# LIST
l = ['Chutiya Jackson', 12, 10.32, ('qw','ty',1,56),[7,9]]
print(l)

l1 = l+ [1,23,234,543,'free','rfnjs']
print(l1)
l1.extend(['poop','lol'])
l1.extend('lol')
l1.append([9,90,909])
print(l1)
del(l[3])
print(l)

# String to List
print('chutiya jackson'.split())
print('chutiya,jackson,hrhe,ndjg,eihied'.split(','))
print('1,2,3,4,5,6,7'.split(","))
print("1 2 3 4 5 6 7 8 9".split(" "))

# Cloning the list 
Clone_list = l1[:]
print(Clone_list)
#help(Clone_list)

