# Initialize an empty dictionary to store expenditures Name
expenditures = {}

# Function to add the expenditure name and price
def add_expenditure():
    # Ask the name of the expenditure
    name = input("Enter expenditure name: ")
    # Ask the cost of the expenditure
    amount = float(input("Enter expenditure amount: "))
    expenditures[name] = amount

# Function to calculate and display the total expenditure
def calculate_total():
    total = sum(expenditures.values())
    print(f"Total monthly expenditure: Rs{total:.2f}")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add an expenditure")
    print("2. Calculate total expenditure")
    print("3. Quit")
    
    #Take the user s choice and give a default case
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        add_expenditure()
    elif choice == '2':
        calculate_total()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the monthly expenditure calculator!")
