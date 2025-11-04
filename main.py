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

def save_file(expense):
    with open(expense_file, "w") as file:
        json.dump(expense, file, indent=4)

def add_expense(desc, amount):
    expenses = load_file()

    new_expenses = {
        "description": desc,
        "amount": amount,
        "date": datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    }

    expenses.append(new_expenses)

    save_file(expenses)

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

    # then store all that parsers in args variable untuk kita call nanti
    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.desc, args.amount)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()