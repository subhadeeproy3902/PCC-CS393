a = int(input("Enter a number1 : "))
b = int(input("Enter a number2 : "))

def prime(i):
	if i==0 or i==1:
		return 0
	elif i==2:
		return 1
	else:
		for j in range(2,i):
			if i%j==0:
				return 0
		return 1
		
y = []
for i in range(a,b+1):
	x = prime(i)
	if x == 1:
		y.append(i)

if y == []:
	print("No prime numbers in the range")
else:
	print("Prime numbers are:", end = " ")
	for p in y:
		print(p,end = " ")
	print("\n")
