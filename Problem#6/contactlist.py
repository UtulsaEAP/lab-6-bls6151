#Name: Braden Stanfield  Lab: Fri 3
def process_user_contacts(user_input):
    i = 0
    user_contacts = ""
    list = user_input.split()
    # Put word pairs into a dictionary
    
    # Get contact name from input, output contact's phone number
    num = "Contact not found."
    Contact_name = input("Enter the contact name: ")
    while i < len(list):
        a = list[i].split(',')
        if a[0] == Contact_name:
            if len(a) > 1:
                num = a[1]
                i = len(list)
        i += 1
    if num == "Contact not found.":
        i = 0
        while i < len(list):
            a = list[i]
            if a == Contact_name:
                if len(list) > 1:
                    num = list[i + 1]
                    i = len(list)
            i += 1
    print(num)
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    (process_user_contacts(user_input))
