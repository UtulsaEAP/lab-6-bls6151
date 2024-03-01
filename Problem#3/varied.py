#Name: Braden Stanfield  Lab: Fri 3
def process_input(input_string):
      # Split into separate strings
    nums = input_string.split()
    # Convert strings to floats
    i = 0
    j = 1
    k = 0
    while i < len(nums) :
        nums[i] = float(nums[i])
        i += 1

    # Get max and average
    max = nums[0]
    
    while j < len(nums):
        if nums[j] > max:
            max = nums[j]
        j += 1
    max_value = max
    tot = 0
    while k < len(nums):
        tot += nums[k]
        k += 1
    average_value = tot/(len(nums))
    return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
