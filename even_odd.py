# Write a program to check if a number is even or odd

def even_odd(n):
    if (n%2)==0:
        print(n,"is even number")
    else:
        print(n,"is odd number")
    
number=int(input("Enter the number: "))
even_odd(number) 