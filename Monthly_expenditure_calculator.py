# Initialize an empty dictionary to store expenditures
expenditures = {}

# Function to add an expenditure
def add_expenditure():
    name = input("Enter expenditure name: ")
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