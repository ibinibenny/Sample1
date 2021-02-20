#to print and find sum of odd no.s b/w 1 & 50
a=1
b=50
s=0
print("odd numbers between",a, 'and',b,"are", end=" ")
for num in range(a,b+1):
	if num%2!=0:
		print(num,end=" ")
		s=s+num
print("\nsum",s)
