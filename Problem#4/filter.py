#Name: Braden Stanfield  Lab: Fri 3
def process_and_print(input_string):
      # Split into separate strings
    nums = input_string.split()
    i = 0
    # Convert strings to integers and filter out negative values
    input_data = []
    while i < len(nums):
        if int(nums[i]) < 0:
            input_data.append(int(nums[i])) 
        i += 1

    # Sort integers in reverse order
    input_data.sort(reverse=True)
    #input_data.reverse()
    # Print sorted integers
    j = 0
    printed = ""
    while j < len(input_data) :
        printed += (str(input_data[j]) + " ")
        j += 1
    print(printed[:-1])

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    (process_and_print(user_input))
