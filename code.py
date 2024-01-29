class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Expense Tracker:")
            for category, amount in self.expenses.items():
                print(f"{category}: ${amount}")

    def delete_expense(self, category):
        if category in self.expenses:
            del self.expenses[category]
            print(f"Expense in '{category}' deleted.")
        else:
            print(f"No expenses found in '{category}'.")

# Example usage:
expense_tracker = ExpenseTracker()

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        expense_tracker.add_expense(category, amount)
        print("Expense added successfully.")

    elif choice == '2':
        expense_tracker.view_expenses()

    elif choice == '3':
        category = input("Enter category to delete: ")
        expense_tracker.delete_expense(category)

    elif choice == '4':
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
