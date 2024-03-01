#Name: Braden Stanfield  Lab: Fri 3
def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
    i = 0
    nums = ""
    while i < len(input_list):
        if int(input_list[i]) >= min_val:
            if int(input_list[i]) <= max_val:
                nums += input_list[i] + ","
        i += 1
    print(nums)
if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = user_input.split()

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    user_input = user_input.split()
    min_val, max_val = int(user_input[0]), int(user_input[1])

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(integer_list, min_val, max_val)
