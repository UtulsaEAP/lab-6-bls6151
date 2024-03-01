#Name: Braden Stanfield  Lab: Fri 3
def check_palindrome(user_input):
 #type your code here
    back = ""
    leng = len(user_input)
    i = leng - 1
    while i > -1:
        back += user_input[i]
        i -= 1
    if user_input == back:
        print("palindrome: " + user_input)
    else:
        print("not a palindrome: " + user_input)
    
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
