'''Create a function to count the number of vowels in a
given string'''

def count_no_of_vowels(s):
    vowels='aeiouAEIOU'
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count
    
input_str = input('Enter the string: ')
print('No of vowels:', count_no_of_vowels(input_str)) 