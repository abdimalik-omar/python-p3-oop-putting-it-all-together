#!/usr/bin/env python3

class Book:
    def __init__ (self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count (self):
        """The page_count property"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        """Page Count must be an integer."""
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print('page_count must be an integer')

    def turn_page(self):
        """Simulate turning a page."""
        print("Flipping the page...wow, you read fast!")


    # Creating a Book instance
try:
    my_book = Book("Python Programming", 250)
    print(my_book.page_count)  # Output: 250
    my_book.turn_page()        # Output: Flipping the page...wow, you read fast!
except Exception as e:
    print(e)

# Testing invalid page_count
try:
    invalid_book = Book("Error Book", "two hundred")
except Exception as e:
    print(e)  # Output: page_count must be an integer.