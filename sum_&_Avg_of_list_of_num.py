# Find sum and average of List in Python

num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

count = 0

for i in num_list:
    count += i
 
avg = count/len(num_list)

total = print("sum of given list of numbers is ", count)
average = print("Average of given list of numbers is ", avg)



'''num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

count = sum(num_list)
 
avg = count/len(num_list)

total = print("sum of given list of numbers is ", count)
average = print("Average of given list of numbers is ", avg)
'''


'''
import statistics
num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

count = sum(num_list)
 
avg = statistics.mean(num_list)

total = print("sum of given list of numbers is ", count)
average = print("Average of given list of numbers is ", avg)
'''


'''
import numpy as np
num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

count = np.sum(num_list)
 
avg = np.average(num_list)

total = print("sum of given list of numbers is ", count)
average = print("Average of given list of numbers is ", avg)
'''