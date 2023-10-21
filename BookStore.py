import BinaryHeap
import Book
import ArrayList
import ChainedHashTable
import BinarySearchTree
import SLLQueue
import algorithms
"""
import AdjacencyList
"""
import time


class BookStore:
    """
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart.
    """

    def __init__(self):
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.bookCatalog = None
        self.shoppingCart = SLLQueue.SLLQueue()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        """
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key,
                title, group, rank (number of copies sold) and similar books
        """
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                # self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)
                # self.bookIndices.add(key, self.bookCatalog.size() - 1)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = SLLQueue.SLLQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting ShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        """
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input:
            i: positive integer
        """
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        """
        addBookByIndex: Inserts into the playlist the song of the list at index i
        input:
            i: positive integer
        """
        # Validating the index, otherwise it  crashes
        if 0 <= i and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str, cnt: int):
        """
        searchBookByInfix: Search all the books that contains infix
        input:
            infix: A string
            cnt: An int
        """
        start_time = time.time()
        print(*[b for b in self.bookCatalog if infix in b.title][:cnt])
        '''
        This is faster and probably what you were looking for, but uglier
        a = 0
        for book in self.bookCatalog:
            if a >= cnt:
                break
            if infix in book.title:
                a += 1
                print(book)
        '''
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        """
        removeFromShoppingCart: remove one book from the shopping cart
        """
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        print('getCartBestSeller returned')
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            print(self.shoppingCart.max().title)
            elapsed_time = time.time() - start_time
            print(f"Completed in {elapsed_time} seconds")

    def addBookByKey(self, key):
        start_time = time.time()
        result = self.bookIndices.find(key)
        if result is not None:
            b = self.bookCatalog.get(result)
            self.shoppingCart.add(b)
            print(f'Added title: {b.title}')
        else:
            print('Book not found...')
        elapsed_time = time.time() - start_time
        print(f"addBookByKey Completed in {elapsed_time} seconds")

    def addBookByPrefix(self, prefix):
        if prefix != '':
            x = self.sortedTitleIndices.find_key(prefix)
            if (prefix <= x.k) and (x.k[0:len(prefix)] == prefix):
                b = self.bookCatalog.get(x.v)
                self.shoppingCart.add(b)
                return b.title
        return None

    def bestsellers_with(self, infix: str, structure: int, n: int = 0):
        """
        if structure == 1:
            best_sellers = BinarySearchTree.BinarySearchTree()
        elif structure == 2:
            best_sellers = BinaryHeap.BinaryHeap()
        else:
            return print('Invalid data structure.')
        if infix == '':
            return print('Invalid infix.')
        if n < 0:
            return print('Invalid number of titles.')
        start_time = time.time()
        sent = 0

        for book in self.bookCatalog:
            if infix in book.title:
                book.rank *= -1
                if structure == 1:
                    best_sellers.add(book.rank, book)
                elif structure == 2:
                    best_sellers.add(book)
        if structure == 1:
            for book in best_sellers.in_order():
                if n == 0 or sent < n:
                    sent += 1
                    print(book)
        elif structure == 2:
            while best_sellers.size() > 0 and (sent < n or n == 0):
                sent += 1
                print(best_sellers.remove())
        elapsed_time = time.time() - start_time
        print(f'Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds')
        """
        best_sellers = None
        if structure == 1:
            best_sellers = BinarySearchTree.BinarySearchTree()
        elif structure == 2:
            best_sellers = BinaryHeap.BinaryHeap()
        else:
            print("Invalid data structure.")
        if best_sellers is not None:
            if infix == "":
                print("Invalid infix.")
            else:
                start_time = time.time()
                # books = []
                if n < 0:
                    print("Invalid number of titles.")
                for book in self.bookCatalog:
                    if infix in book.title:
                        book.rank *= -1
                        if structure == 1:
                            best_sellers.add(book.rank, book)
                        elif structure == 2:
                            best_sellers.add(book)
                # elif n == 0:
                #     for book in books:
                #         best_sellers.add(book.rank)
                counter = 0
                if structure == 1:
                    for book in best_sellers.in_order():
                        if counter < n or n == 0:
                            counter += 1
                            print(book)
                elif structure == 2:
                    while best_sellers.size() > 0 and (n == 0 or counter < n):
                        counter += 1
                        book = best_sellers.remove()
                        print(book)
                elapsed_time = time.time() - start_time
                print(f"Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds")

    def sort_catalog(self, s: int):
        start_time = time.time()
        if s == 1:
            algorithms.merge_sort(self.bookCatalog)
            elapsed_time = time.time() - start_time
            # print(f"Sorted bookCatalog using merge sort in {elapsed_time} seconds")
            return True
        elif s == 2:
            algorithms.quick_sort(self.bookCatalog, False)
            elapsed_time = time.time() - start_time
            # print(f"Sorted bookCatalog using quick sort first element pivot in {elapsed_time} seconds")
            return True
        elif s == 3:
            algorithms.quick_sort(self.bookCatalog)
            elapsed_time = time.time() - start_time
            # print(f"Sorted bookCatalog using quick sort random element pivot in {elapsed_time} seconds")
            return True
        else:
            return False

    def display_catalog(self, n: int):
        for i in range(n):
            print(self.bookCatalog.get(i))

