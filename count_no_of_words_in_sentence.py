print(len(input("Enter the sentence: ").split()))

# Another method using numpy:
'''
import numpy as np
 
# initializing string
test_string = "Geeksforgeeks is best Computer Science Portal"
 
# printing original string
print("The original string is : " + test_string)
 
# using numpy to count words in string
res = np.char.count(test_string, ' ') + 1
 
# printing result
print("The number of words in string are : " + str(res))
'''