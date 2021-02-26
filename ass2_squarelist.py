#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30
import math
l1=[]
for i in range(1,31):
	l1.append(int(math.pow(i,2)))
print(l1)
for i in range(30):
	if i<5 or i>24:
		print(l1[i])
	

