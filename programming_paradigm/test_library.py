import unittest
from library_system import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.add_book("Test Book", "Test Author")

    def test_add_book(self):
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Book")

    def test_borrow_book(self):
        self.library.borrow_book("Test Book")
        self.assertFalse(self.library.books[0].available)

    def test_return_book(self):
        self.library.borrow_book("Test Book")
        self.library.return_book("Test Book")
        self.assertTrue(self.library.books[0].available)

if __name__ == '__main__':
    unittest.main()
