

'''Question 1. Wonderhood kids love to play with really big numbers. One of the teachers asked
students to find if a given number(let's say X) is divisible by 3 or 9. Can you help out the kid?'''


#Function to find if x is divisible by 3 or 9
def check_divisible(x):
	if x%3==0:
		print("{} is divisible by 3".format(x))
		return "yes"
	elif x%9==0:
		print("{} is divisible by 9".format(x))
		return "yes"
	else:
		print("{} is not divisible by 3 or 9".format(x))
		return "no"


#Given Number x 
x = 18

#check if x is divisble by 3 or 9
print(check_divisible(x))



'''Question 2. Given two unsorted arrays(let's say A and B) of integers of size 'm' and 'n'. Find
any three integers from any array in any order(let's say x,y,z) which when multiplied produces a
number which is divisible by 9. You can choose all numbers from one array or from both arrays.
If no such elements exists return -1
First line of input is the size of the array 'm' and 'n'. Second and third lines are array A of size 'm'
and array B of size 'n' respectively.'''





#Function to check if multiplication of any 3 integers is divisible by 9 in given array or list
def check_integers_divisible(a,b):
	c = a+b   #combine two lists
	l = len(c) #len of combined list
	x = y = z = 0
	
	for i in range(0,l):
			
		for j in range(0,l):
				
			for k in range(0,l):
				if i < l and j < l and k < l:
					if i != j and i!= k and j!=k:
						
						if c[i] != 0 and c[j] != 0 and c[k] != 0:
							mul_three_integers = c[i] * c[j] * c[k]    
						
							if mul_three_integers%9 == 0: #three integers divisible by 9
								
								#Assigning values to x,y,z
								x = c[i]
								y = c[j]
								z = c[k]
	if x and y and z:
		result = x * y * z
		print("{} * {} * {} = {} is divisible by 9".format(x,y,z,result))
		return "{} {} {}".format(x,y,z)
	else:
		return -1


#Given two arrays A and B	
a  = [3, 5 ,3]
b = [7, 4, 7, -1]

#check if any 3 integers is divisible by 9 in givent 2 arrays or lists
print(check_integers_divisible(a,b))							





















		