import Calculator
import BookStore
from DLList import DLList


def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option != '0':
        print("""
        1 Check mathematical expression 
        2 Store variable values
        3 Print expression with values
        4 Evaluate expression
        0 Return to main menu
        """)
        """
        calculator.set_variable('alpha12', 3)
        calculator.set_variable('beta2', 5)
        exp = '(alpha12+beta2)'
        expres = calculator.print_expression(exp)
        error_found = False
        for char in expres:
            if char.isalpha():
                error_found = True
                print('Result: Error - Not all variable values are defined.')
                break
        if not error_found:
            # print(f'Evaluating expression: {expres}')
            print(f'Result: {calculator.evaluate(exp)}')
        option = '0'
        """
        option = input()
        if option == "1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression):
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")
        elif option == '2':
            choice = ''
            while choice.lower() != 'n':
                var = input('Enter a variable: ')
                val = float(input('Enter its value: '))
                calculator.set_variable(var, val)
                choice = input('Enter another variable? Y/N')
        elif option == '3':
            exp = input('Introduce the mathematical expression: ')
            if calculator.matched_expression(exp):
                print(calculator.print_expression(exp))
            else:
                print('Invalid expression')
        elif option == '4':
            exp = input('Enter the expression: ')
            try:
                print(f'Result: {calculator.evaluate(exp)}')
            except ValueError:
                print('Result: Error - Not all variable values are defined.')
        ''' 
        Add the menu options when needed
        '''


def menu_bookstore_system():
    bookStore = BookStore.BookStore()
    option = ""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Get cart best-seller
        7 Add a book by key to shopping cart
        8 Add a book by title prefix to shopping cart
        9 Search best-sellers with infix
        10 Sort the catalog
        11 Display the first n books of catalog
        0 Return to main menu
        """)
        """
        bookStore.loadCatalog('books.txt')
        bookStore.bestsellers_with('', 1)
        bookStore.bestsellers_with('World of Po', 1)
        # bookStore.bestsellers_with('World of Po', 2)
        # bookStore.bestsellers_with('World of Po', 2, 5)
        option = '0'
        """
        option = input()
        if option == "r":
            bookStore.setRandomShoppingCart()
        elif option == "s":
            bookStore.setShoppingCart()
        elif option == "1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name)
            # bookStore.pathLength(0, 159811)
        elif option == "2":
            i = int(input("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option == "3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option == "4":
            bookStore.removeFromShoppingCart()
        elif option == "5":
            infix = input("Introduce the query to search: ")
            cnt = int(input("Enter max number of results: "))
            bookStore.searchBookByInfix(infix, cnt)
        elif option == '6':
            bookStore.getCartBestSeller()
        elif option == '7':
            inp = input('Enter book key: ')
            bookStore.addBookByKey(inp)
        elif option == '8':
            inp = input('Enter a prefix: ')
            result = bookStore.addBookByPrefix(inp)
            if result is not None:
                print(f'Added first matched title: {result}')
            else:
                print('Error: Prefix was not found.')
        elif option == '9':
            infix = input('Enter infix: ')
            strc_int = int(input('Enter structure (1 or 2): '))
            max_titles = int(input('Enter max number of titles: '))
            bookStore.bestsellers_with(infix, strc_int, max_titles)
        elif option == '10':
            print('Choose an algorithm:')
            print('\t1 - Merge Sort')
            print('\t2 - Quick Sort (first element pivot)')
            print('\t3 - Quick Sort (random element pivot)')
            inp = int(input('Your selection: '))
            if inp not in [1, 2, 3]:
                print('Invalid algorithm')
            else:
                bookStore.sort_catalog(inp)
        elif option == '11':
            bookStore.display_catalog(int(input('Enter the number of books to display: ')))
        ''' 
        Add the menu options when needed
        '''


def menu_palindrome():
    palin = DLList()
    [palin.add(0, char) for char in input('Enter a word/phrase: ')]
    print(f'Result: {"Palindrome" if palin.isPalindrome() else "Not a palindrome"}')


# main: Create the main menu
def main():
    option = ""
    while option != '0':
        print("""
        1 Calculator
        2 Bookstore System
        3 Palindrome Test
        0 Exit/Quit
        """)
        option = input()

        if option == "1":
            menu_calculator()
        elif option == "2":
            menu_bookstore_system()
        elif option == '3':
            menu_palindrome()


if __name__ == "__main__":
    main()
