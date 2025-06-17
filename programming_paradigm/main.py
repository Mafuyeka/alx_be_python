#!/usr/bin/env python3

from library_system import Library

lib = Library()
lib.add_book("The Alchemist", "Paulo Coelho")
lib.add_book("1984", "George Orwell")
lib.list_books()

lib.borrow_book("1984")
lib.list_books()

lib.return_book("1984")
lib.list_books()
