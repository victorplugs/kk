def prime_number(num):
	for x in range(2, num+1):
		if all(x%i!=0 for i in range(2,x)):
	         print (x)
prime_number(100)
