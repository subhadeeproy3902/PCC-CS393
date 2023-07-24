s = 0
count = 0
while 1:
	a = int(input("Enter a number : "))
	s+=a
	count +=1
	if a == 0:
		print("The sum is : ",s)
		if count>1:
			print("The average is : ",s/(count-1))
		else:
			print("Division by 0 is not possible")
		break
		
