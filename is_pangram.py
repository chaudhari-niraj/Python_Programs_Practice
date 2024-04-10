#Python program to check if given string is pangram

def is_pangram(s):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    # Convert input string to lowercase for case-insensitive comparison
    s = s.lower()
    for char in alphabets:
        # Check if any alphabet is missing in the input string
        if char not in s:
            print('No! the given string is not pangram')
            return False
    print('Yes! the given string is pangram')
    return True

string = input("Enter the sentence: ")
is_pangram(string)