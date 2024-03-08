#Name: Braden Stanfield  Lab: Fri 3
def calculate_car_wash_price(service_choice1, service_choice2):
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    base_wash = 10
    total = 10
    output = "ZyCar Wash\nBase car wash - $10"
   #type your code here 
    if service_choice1 == "Air freshener":
        output += "\nAir freshener - $1"
        total += 1
    elif service_choice1 == "Rain repellent":
        output += "\nRain repellent - $2"
        total += 2
    elif service_choice1 == "Tire shine":
        output += "\nTire shine - $2"
        total += 2
    elif service_choice1 == "Wax":
        output += "\nWax - $3"
        total += 3
    elif service_choice1 == "Vaccum":
        output += "\nVaccum - $5"
        total += 5
    
    if service_choice2 == "Air freshener":
        output += "\nAir freshener - $1"
        total += 1
    elif service_choice2 == "Rain repellent":
        output += "\nRain repellent - $2"
        total += 2
    elif service_choice2 == "Tire shine":
        output += "\nTire shine - $2"
        total += 2
    elif service_choice2 == "Wax":
        output += "\nWax - $3"
        total += 3
    elif service_choice2 == "Vaccum":
        output += "\nVaccum - $5"
        total += 3
    
    
    
    output += ("\n-----\nTotal price: $" + str(total))
    print(output)
if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)
