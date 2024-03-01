#Name: Braden Stanfield  Lab: Fri 3
def process_user_contacts(user_input):
    i = 0
    user_contacts = ""
    list = user_input.split()
    
 
    
    tokens = 0

    # Put word pairs into a dictionary
    
    # Get contact name from input, output contact's phone number
    
    contact_name = input("Enter the contact name: ")
    while i < len(list):
        a = list[i].split(',')
        if a[0] == contact_name:
            if len(a) > 1:
                user_contacts = a[1]
        i += 1
    print(user_contacts)
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    (process_user_contacts(user_input))
