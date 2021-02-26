#Write a program to implement all built-in methods of list.
tup=[1,2,3,4,5,6,6,7,7,8,8,9]
print(tup[0])
print(tup[:5])
print(tup[5]+tup[6])
tupl=['hello','HAAI','           spect      ']
print(tupl*3)
print('hello'in tupl)
print(len(tup))
print(tupl[1].lower())
print(tupl[0].upper())
print(tupl[0].title())
print(tupl[0].capitalize())
print(tupl[2].strip())
print(tupl[1].startswith('H'))
print(tupl[1].endswith('I'))
print("--------------------------")
print(tup)
print("count of 8=",tup.count(8))

print("appending 10")
tup.append(10)
print(tup)

print("inserting 11 @5th index",tup.insert(5,11))

print("removing 1")
tup.remove(10)
print(tup)

print("sorting..")
tup.sort()
print(tup)
print("min and max values in the list are:",min(tup),max(tup))

print("list after popping...")
print(tup.pop())
tup.reverse()
print("list reversed=",tup)
tup.clear()
print("clearing the list",tup)

