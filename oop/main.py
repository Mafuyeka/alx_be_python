# main.py

from library_system import Book, EBook, PrintBook, Library
from shape_hierarchy import Circle, Rectangle

def test_library():
    print("\n📚 Library Test:")
    my_library = Library()
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()


def test_shapes():
    print("\n🔷 Shape Test:")
    shapes = [
        Circle(5),
        Rectangle(4, 6)
    ]
    for shape in shapes:
        print(f"{type(shape).__name__} - Area: {shape.area()}, Perimeter: {shape.perimeter()}")


def main():
    test_library()
    test_shapes()

if __name__ == "__main__":
    main()
