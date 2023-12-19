def load_transactions():
    try:
        with open('transactions.txt', 'r') as file:
            lines = file.readlines()
            transactions = {'income': [], 'expenses': []}
            for line in lines:
                category, amount, transaction_type = line.strip().split(',')
                if transaction_type == 'income':
                    transactions['income'].append({'category': category, 'amount': float(amount)})
                elif transaction_type == 'expense':
                    transactions['expenses'].append({'category': category, 'amount': float(amount)})
            return transactions
    except FileNotFoundError:
        return {'income': [], 'expenses': []}

def save_transactions(transactions):
    with open('transactions.txt', 'w') as file:
        for income in transactions['income']:
            file.write(f"{income['category']},{income['amount']},income\n")
        for expense in transactions['expenses']:
            file.write(f"{expense['category']},{expense['amount']},expense\n")

def add_income(transactions):
    income_categories = ['Salary', 'Business', 'Others']
    print("Income Categories: ")
    for index, category in enumerate(income_categories, start=1):
        print(f"{index}. {category}")

    print("4. Add New Category")

    while True:
        try:
            choice = int(input("Select income category (1-4): "))
            if 1 <= choice <= 3:
                break
            elif choice == 4:
                new_category = input("Enter new income category: ")
                income_categories.append(new_category)
                print(f"New category '{new_category}' added successfully!")
                break
            else:
                print("Invalid choice. Please enter a valid category number.")
        except ValueError:
            print("Invalid input. Please enter a valid category number.")

    income_category = income_categories[choice - 1]
    income_amount = float(input("Enter income amount in INR: "))
    transactions['income'].append({'category': income_category, 'amount': income_amount})
    save_transactions(transactions)
    print("Income added successfully!")

def add_expense(transactions):
    expense_categories = ['Food', 'Home', 'Work', 'Entertainment']
    print("Expense Categories: ")
    for index, category in enumerate(expense_categories, start=1):
        print(f"{index}. {category}")

    print("5. Add New Category")

    while True:
        try:
            choice = int(input("Select expense category (1-5): "))
            if 1 <= choice <= 4:
                break
            elif choice == 5:
                new_category = input("Enter new expense category: ")
                expense_categories.append(new_category)
                print(f"New category '{new_category}' added successfully!")
                break
            else:
                print("Invalid choice. Please enter a valid category number.")
        except ValueError:
            print("Invalid input. Please enter a valid category number.")

    expense_category = expense_categories[choice - 1]
    expense_amount = float(input("Enter expense amount in INR: "))
    transactions['expenses'].append({'category': expense_category, 'amount': expense_amount})
    save_transactions(transactions)
    print("Expense added successfully!")

def calculate_budget(transactions):
    total_income = sum(income['amount'] for income in transactions['income'])
    total_expenses = sum(expense['amount'] for expense in transactions['expenses'])
    remaining_budget = total_income - total_expenses
    print(f"Total Income: ₹{total_income:.2f}")
    print(f"Total Expenses: ₹{total_expenses:.2f}")
    print(f"Remaining Budget: ₹{remaining_budget:.2f}")

def analyze_expenses(transactions):
    expense_categories = {'Food': 0, 'Home': 0, 'Work': 0, 'Entertainment': 0}
    
    for expense in transactions['expenses']:
        category = expense['category']
        amount = expense['amount']
        if category in expense_categories:
            expense_categories[category] += amount
    
    print("Expense Analysis:")
    for category, amount in expense_categories.items():
        print(f"{category}: ₹{amount:.2f}")

def main():
    transactions = load_transactions()

    while True:
        print("\n=== Budget Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Expense Analysis")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_income(transactions)
        elif choice == '2':
            add_expense(transactions)
        elif choice == '3':
            calculate_budget(transactions)
        elif choice == '4':
            analyze_expenses(transactions)
        elif choice == '5':
            save_transactions(transactions)
            print("Exiting the Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).")

if __name__ == "__main__":
    main()
