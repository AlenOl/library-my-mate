from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import LiteraryFormat, Book


class ModelsTests(TestCase):
    def test_literary_format_str(self):
        format_ = LiteraryFormat.objects.create(name="test")

        self.assertEqual(str(format_), format_.name)

    def test_author_str(self):
        author = get_user_model().objects.create_user(
            username="test",
            password="test12345",
            first_name="Test first",
            last_name="Test last"
        )

        self.assertEqual(str(author), f"{author.username} ({author.first_name} {author.last_name})")

    def test_book_str(self):
        format_ = LiteraryFormat.objects.create(name="test")
        book = Book.objects.create(
            title="Test",
            price=10.15,
            format=format_
        )

        self.assertEqual(str(book), f"{book.title} (price: {book.price}, format: {format_.name})")

    def test_create_author_with_pseudonym(self):
        username = "test"
        password = "test12345"
        pseudonym = "Test pseudonym"
        author = get_user_model().objects.create_user(
            username=username,
            password=password,
            pseudonym=pseudonym
        )

        self.assertEqual(author.username, username)
        self.assertTrue(author.check_password(password))
        self.assertEqual(author.pseudonym, pseudonym)
