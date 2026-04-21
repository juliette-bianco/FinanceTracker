# Juliette Bianco
# 8/2/24

import datetime

# Main function
def main():
    print("Welcome to the Personal Finance Tracker")
    print("You can add expenses, view all expenses, and save the data to a file.")
    
    tasks = []  # List to store tasks

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Save Expenses to File")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            addExpense(tasks)
        elif choice == '2':
            viewExpenses(tasks)
        elif choice == '3':
            saveExpensesToFile(tasks)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to add an expense
def addExpense(tasks):
    task_name = input("Enter the expense name: ")  # String input for expense name
    task_priority = float(input("Enter the expense amount: "))  # Floating-point input for expense amount
    task_due_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current date and time
    
    task = {
        'name': task_name,
        'amount': task_priority,
        'date': task_due_date
    }
    
    tasks.append(task)  # Add the expense dictionary to the expenses list
    print(f"Expense '{task_name}' added.")

# Function to view expenses
def viewExpenses(tasks):
    if tasks:
        print("\nExpenses List:")
        for task in tasks:
            print(f"Name: {task['name']}, Amount: ${task['amount']:.2f}, Date: {task['date']}")
    else:
        print("No expenses recorded.")

# Function to save expenses to a file
def saveExpensesToFile(tasks):
    filename = "expenses.txt"
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task['name']},{task['amount']},{task['date']}\n")
    print(f"Expenses saved to {filename}")

# Run the main function
if __name__ == "__main__":
    main()
