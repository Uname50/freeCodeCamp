# Lambda functions can be valuably combined with the map() function, which executes a specified function for each element in a collection of objects, such as a list:
# -> map(lambda x: x * 2, [1, 2, 3])
# The result of the example above would be [2, 4, 6], where each item in the list passed to map() has been doubled by the action of the lambda function.

# The filter() function allows you to select items from an iterable, such as a list, based on the output of a function:
# -> filter(my_function, my_list)
# filter() returns an iterator in which the elements of my_list are included, for which my_function returns True. An iterator is a special object that enables you to iterate over the elements of a collection, like a list.

# The amount of the expense needs to be converted before performing any calculation. The float() function takes a string or an integer number as argument and returns a floating point number.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('Exiting the program.')
            break
        
if __name__ == '__main__':
    main()