#to print and find sum of odd no.s b/w 1 & 50

sum1=0
for i in range(1,50,2):
	print(i)
	sum1+=i
print("the sum of above numbers=%d" %sum1)


a=1
b=50
s=0
print("odd numbers between",a, 'and',b,"are", end=" ")
for num in range(a,b+1):
	if num%2!=0:
		print(num,end=" ")
		s=s+num
print("\nsum",s)
