from django.test import TestCase
from bookstore.models import Book, Category


class InventoryModelTest(TestCase):

    def test_book_is_related_to_category(self):
        test_category = Category.objects.create()
        books = Book()
        books.category = test_category
        books.save()
        self.assertIn(books, test_category.books_set.all())

    def test_string_representation_of_categories(self):
        category = Category.objects.create(name="health", description="health category")
        self.assertEqual(category.name, 'health')


    def test_string_representation_of_books(self):
        test_category2 = Category.objects.create()
        book = Book(name='some text', category=test_category2)
        self.assertEqual(str(book), 'some text')

