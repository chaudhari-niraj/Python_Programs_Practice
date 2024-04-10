'''Implement a program that converts a given number of
minutes into hours and minutes'''

def convert_to_hrs_min(m):
    hr = m//60
    remaining_min = m%60
    return hr, remaining_min
    
_min = int(input("Enter the minutes: "))
_hrs, remaining_min = convert_to_hrs_min(_min)
print(f"{_min} is equal to {_hrs} hours and {remaining_min} minutes")  