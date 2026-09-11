import json
try:
    with open('save.json','r') as f:
        expenses = json.load(f)
except json.decoder.JSONDecodeError:
    expenses = []
except FileNotFoundError:
    expenses = []
def add_expense():
    while True:
        name = input("Name of the expense? ")
        while True:
            try:
                price = float(input("And how much does it cost? "))
                break
            except ValueError:
                print("Please make sure what you entered only contains numbers")
        category = input("And what category does it fall under? ")

        new_dictionary = {
            'Name':name,
            'Price':float(price),
            'Category':category
        }
        
        expenses.append(new_dictionary)
        answer = input("Would you like to add anything else? Yes[Y] / No[N] ")
        if answer.lower() == 'n':
            break
    
def view_expenses():
    print("===Current Expenses===")
    for i in expenses:
        for key,value in i.items():
            print(f'{key}: {value}')
        print("= = = =")

def view_expenses_category():
    category = input("What category would you like to see? ")
    total_expense = 0
    for i in expenses:
        if i["Category"].lower() == category.lower():
            total_expense += i["Price"]
    print(f"Total expenses in the {category} category is {total_expense}")

def save():
    with open('save.json','w') as f:
        json.dump(expenses,f)
    print("Saved!")

def remove():
    removal = input("What would you like to remove? ")
    for i in expenses:
        if i["Name"].lower() == removal.lower():
            expenses.remove(i)
            print('Deleted! ')
            break
        

actions = {
    '1': add_expense,
    '2': view_expenses,
    '3': view_expenses_category,
    '4': save,
    '5': remove
    
}

while True:
    choice = input("What would you like to do? \n [1] Add expense \n [2] View expenses \n [3] View expenses by category \n [4] Save \n [5] Remove \n [6] Quit \n")
    if choice == '6':
        break
    elif choice in actions:
        actions[choice]()
    else:
        print("Please type either 1,2,3,4,5 or 6")