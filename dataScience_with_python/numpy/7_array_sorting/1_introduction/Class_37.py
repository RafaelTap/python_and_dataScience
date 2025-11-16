
# Python has some functions to sort lists and others objects.
x = [1, 3, 5, 2, 9, 22, 15]
print(x, '\n')

#the function sorted() accept a list and return a sorted copy of the same list.
l = sorted(x)
print(l, '\n')

# on the other hand, the method .sort() sort the same list without return a copy.
x.sort()
print(x, '\n')

#the sort methods in Python are very flexible and can work with any iterated object.
l = 'python'
print(l, '\n')
sorted_l = sorted(l)
print(sorted_l, '\n')

l_1 = ['r', 's', 'a']
sorted_l1 = sorted(l_1)
print(sorted_l1)
