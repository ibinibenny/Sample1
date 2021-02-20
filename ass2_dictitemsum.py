#Write a Python program to sum all the items in a dictionary.
dict1={1:1,2:4,3:9,4:16}
print(dict1.items())
sum1,sum2=0,0
for i in dict1.keys():
	sum1+=i
	sum2+=dict1[i]
print(sum1,sum2)

