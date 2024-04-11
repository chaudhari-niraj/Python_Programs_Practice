'''Given a list of numbers, find the maximum and minimum
values'''

def find_max_min(numbers):
    if not numbers:
        return None, None
    
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    
    return maximum, minimum

def main():
    input_str = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(x) for x in input_str.split()]
    max_value, min_value = find_max_min(numbers)
    if max_value is not None and min_value is not None:
        print("Maximum value:", max_value)
        print("Minimum value:", min_value)
    else:
        print("No numbers provided.")

if __name__ == "__main__":
    main()
