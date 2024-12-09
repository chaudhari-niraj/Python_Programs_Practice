# Given a list of integers, find all the even numbers and store them in a new list:

# num = [1,2,3,4,5,6,7,8,9,10,16,24,23,39,99,100]

num = list(map(int, input("Enter the integer numbers separated by space: ").split()))
print("List of numbers is: ", num)
even = []
for i in num:
	if i % 2 == 0:
	    even.append(i)
print("List of even numbers is: ",even)
		
