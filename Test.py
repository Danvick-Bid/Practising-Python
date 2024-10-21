MAKOTI DANVICK BIDAHA
M24B65/004
B28738
TEST

Question a

def get_even_numbers(numbers):
	even_numbers = [num for num in numbers if num % 2 == 0]
    	return even_numbers

input_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
even_list = get_even_numbers(input_list)
print("Even numbers:", even_list)


Question b

def multiplication_table(n):
	for i in range(1, 13):
        	print(f"{n} x {i} = {n * i}")

number = int(input("Enter a number to print its multiplication table: "))
multiplication_table(number)

Question c

def find_largest(numbers):
    	largest = numbers[0]
    	for num in numbers:
        	if num > largest:
            		largest = num
   	return largest

input_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
largest_number = find_largest(input_list)
print("The largest number is:", largest_number)

Question d

def is_same_string(input_string, check_string):
    	return input_string == check_string

input_str = input("Enter the input string: ")
check_str = input("Enter the string to check: ")

if is_same_string(input_str, check_str):
    	print("The strings are the same.")
else:
    	print("The strings are different.")