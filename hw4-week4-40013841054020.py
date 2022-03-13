#Mohammad Javad Esmkhani	4001341054020	hm4-week4
#Unintentional infinite loop
MAX = 20 
n = 1
while n <= MAX :
	factor = 0
	print (str(n) + ' : ' )
	while factor <= n:
		factor+=1
		if n%factor==0:
			print (factor)
	print()
	n+=1
#Iteration examples
max_value = int (input ('Display Primes up to what value : '))
value = 2
while value <= max_value :
	is_prime = True
	trail_factor = 2
	while trail_factor < value :
		if value%trail_factor==0:
			is_prime = False
			break
		trail_factor+=1
	if is_prime :
		print(value , end = '\n')
	value+=1
