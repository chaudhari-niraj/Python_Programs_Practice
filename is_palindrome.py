# Python program to check the input is palindrome or not

def is_palindrome(s):
    s=s.replace(" ","").lower()
    return s == s[::-1]
    
string = input("Enter something: ")

if is_palindrome(string):
    print("This is a palindrome")
else:
    print("This is not a palindrome")



'''def is_palindrome(s):
    s = s.replace(" ", "").lower()
    if(s == s[::-1]):
        print("S is palindrome")
    else:
        print("S is not palindrome")
    
input_str = input("Enter something: ")
is_palindrome(input_str)'''