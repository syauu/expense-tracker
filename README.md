**Expense Tracker CLI**

A simple CLI program written in Python to manage daily expenses. This program can **add, list, delete and summarize** expenses.
All expenses are stored locally in **expense.json** file.
This program is using **argparse** to get command from CLI.

**Features**
- Add new expense with description and amount
- List all expenses
- Delete an expense by its ID
- View total expense for current year or specific month in the current year

**Usage**
1. Add new expense:
  - python main.py add --desc "Lunch" --amount 12.50
2. List expenses:
  - python main.py list
3. Delete an expense:
  - python main.py delete --id {indexNumber}
4. Summary current year:
  - python main.py summary
5. Summary for specific month:
  - python main.py summary --month {monthNumber}

**How It Works**
- All data is stored in **expense.json** as a list of dictionaries.
- Each expense entry includes:
    {
    "description": "Lunch",
    "amount": 12.5,
    "date": "04-11-2025, 15:42:00"
    }
- The program reads and writes to this file using Python's built in json module.
- The argparse library is used to handle CLI commands and options.

**Example Help Menu**
python main.py -h

output:
  usage: main.py [-h] {add,list,delete,summary} ...
  
  Expenses Tracker CLI
  
  positional arguments:
    {add,list,delete,summary}
      add       Add new expense
      list      List all expenses
      delete    Delete an expense
      summary   Summary of total expenses for current year
  
  optional arguments:
    -h, --help  show this help message and exit
