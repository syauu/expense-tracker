# add (desc n amount)
# update
# delete
# view all expense
# summary all expense
# summary specific month (current year)
import argparse
import json
import os
from datetime import datetime

expense_file = "expense.json"

def load_file():
    if not os.path.exists(expense_file):
        with open(expense_file, "w") as file:
            json.dump([], file, indent=4)

    with open(expense_file, "r") as file:
        return json.load(file)

def save_file(expenses):
    with open(expense_file, "w") as file:
        json.dump(expenses, file, indent=4)
        
def list_expenses():
    expenses = load_file()

    try:
        if not expenses:
            print("No expenses.")
        else:
            for index, expense in enumerate(expenses, start=1):
                print("List of all expenses:")
                print(f"{index}. {expense['description']}.")
                print(f"Amount: RM{expense['amount']:.2f}")
        return expenses
    except FileNotFoundError:
        print("File not found")
        return []   # return empty list untuk function lain guna
    except json.JSONDecodeError:
        print("Wrong json format")
        return []   # return empty list untuk function lain guna

def add_expense(desc, amount):
    expenses = load_file()

    new_expenses = {
        "description": desc,
        "amount": amount,
        "date": datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    }

    expenses.append(new_expenses)

    save_file(expenses)

def delete_expense(id):
    if id is None:
        print("Please provide an id")
        return
    
    expenses = load_file()
    if not expenses:
        print("No expenses available.")
        return
    try:
        to_delete = id-1    # id is argument get from argparse. id-1 akan dapat index of dict dalm list json yg nak didelete
        deleted = expenses.pop(to_delete)
        save_file(expenses)
        print(f"Expense {deleted['description']} deleted")
    except ValueError:
        print("Please enter valid number")
    except IndexError:
        print("No expense found")

def main():
    parser = argparse.ArgumentParser(description="Expenses Tracker CLI") # first kita create parser object
    subparser = parser.add_subparsers(dest="command")   # then buat subparser untuk multiple command. save it into command variable

    # then create each subparsers and their arguments
    # add subparser
    add_parser = subparser.add_parser("add", help="Add new expense") # "add" tu adalah command untuk tambah expense, then letak help for the help info
    # lepas dah create parser untuk add, buat parser untuk argument dia pula, which are desc and amount
    add_parser.add_argument(
        "-d", "--desc",
        type=str,
        required=True,
        help="Enter description of expense"
        )
    add_parser.add_argument(
        "-a", "--amount",
        type=float,
        required=True,
        help="Enter amount of expense"
        )
    
    # list subparser
    list_all_subparser = subparser.add_parser("list", help="List all expenses")

    # delete subparser
    delete_subparser = subparser.add_parser("delete", help="Delete an expense")
    delete_subparser.add_argument(
        "-i", "--id",
        type=int,
        help="Enter expense id to delete"
    )

    # then store all that parsers in args variable untuk kita call nanti
    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.desc, args.amount)
    elif args.command == "list":
        list_expenses()
    elif args.command == "delete":
        delete_expense(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()