def main():
    print(f"Running Expense Tracker!")

    #Get user input for expense details
    get_user_expense()

    #Write their expense to a file
    save_expense_to_file()

    #Read file and summarize expenses.
    summarize_expenses()
    

def get_user_expense():
    print(f"Getting User Expense")

def write_expense_to_file(expense):
    print(f"Saving User Expense.")

def summarize_expenses():
    print(f"Summarizing User Expenses")

if __name__ == "__main__":
    main()
    