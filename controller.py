from typing import List

from model import Book
from repository import Repository
from utils import logger


class BookController:
    """
    Controller class for handling operations related to books.
    """

    def __init__(self) -> None:
        """Initializes the BookController with a repository instance."""
        self.repository = Repository()

    def getall(self) -> List[Book]:
        """
        Fetches all books from the repository.

        Returns:
            List[Book]: A list of Book objects.
        """
        try:
            return self.repository.fetchall_books()
        except Exception as e:
            logger.error(f"Failed to fetch all books: {e}")
            return []

    def add_book(self, title: str, author: str, publisher: int, isbn: str, year_published: int) -> None:
        """
        Adds a new book to the repository.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            publisher (int): The publisher ID.
            isbn (str): The ISBN of the book.
            year_published (int): The publication year of the book.
        """
        book = Book(
            id = 0,  # Placeholder for auto-generated ID
            title = title,
            author = author,
            publisher_id = publisher,
            isbn = isbn,
            year_published = year_published
        )
        try:
            self.repository.add_book(book = book)
            logger.info(f"Book '{title}' added successfully.")
        except Exception as e:
            logger.error(f"Failed to add book '{title}': {e}")
            raise RuntimeError("Failed to add book.")

    def delete_by_id(self, book_id: int) -> None:
        """
        Deletes a book by its ID.

        Args:
            book_id (int): The ID of the book to be deleted.
        """
        try:
            self.repository.delete_book_by_id(book_id)
            logger.info(f"Book with ID {book_id} deleted successfully.")
        except Exception as e:
            logger.error(f"Failed to delete book with ID {book_id}: {e}")
            raise RuntimeError("Failed to delete book.")

    def update_book(self, bid: int, title: str, author: str, publisher_id: int, isbn: str, year: int) -> None:
        """
        Updates the details of a book in the repository.

        Args:
            bid (int): The ID of the book to be updated.
            title (str): The updated title of the book.
            author (str): The updated author of the book.
            publisher_id (int): The updated publisher ID.
            isbn (str): The updated ISBN.
            year (int): The updated publication year.
        """
        book = Book(
            id = bid,
            title = title,
            author = author,
            publisher_id = publisher_id,
            isbn = isbn,
            year_published = year
        )
        try:
            self.repository.update_book(book)
            logger.info(f"Book with ID {bid} updated successfully.")
        except Exception as e:
            logger.error(f"Failed to update book with ID {bid}: {e}")
            raise RuntimeError("Failed to update book.")


class QueryController:
    """
    Controller class for handling queries related to authors, publishers, members, and loans.
    """

    def __init__(self) -> None:
        """Initializes the QueryController with a repository instance."""
        self.repository = Repository()

    def get_book_by_author(self, author_name: str) -> List[Book]:
        """
        Fetches books by the given author.

        Args:
            author_name (str): The name of the author.

        Returns:
            List[Book]: A list of Book objects written by the given author.
        """
        try:
            return self.repository.get_books_by_author_name(author_name)
        except Exception as e:
            logger.error(f"Failed to fetch books by author '{author_name}': {e}")
            return []

    def get_all_publishers(self) -> List:
        """
        Fetches all publishers from the repository.

        Returns:
            List[Publisher]: A list of Publisher objects.
        """
        try:
            return self.repository.get_publishers()
        except Exception as e:
            logger.error(f"Failed to fetch publishers: {e}")
            return []

    def get_all_members(self) -> List:
        """
        Fetches all members from the repository.

        Returns:
            List[Member]: A list of Member objects.
        """
        try:
            return self.repository.get_all_members()
        except Exception as e:
            logger.error(f"Failed to fetch members: {e}")
            return []

    def get_all_member_by_book(self, book_name: str) -> List[tuple]:
        """
        Fetches all members who have borrowed the specified book.

        Args:
            book_name (str): The title of the book.

        Returns:
            List[tuple]: A list of tuples containing member and loan information.
        """
        try:
            return self.repository.get_all_members_by_book(book_name)
        except Exception as e:
            logger.error(f"Failed to fetch members by book '{book_name}': {e}")
            return []

    def get_all_loans(self) -> List[tuple]:
        """
        Fetches all loan records from the repository.

        Returns:
            List[tuple]: A list of tuples containing loan information.
        """
        try:
            return self.repository.get_all_loans()
        except Exception as e:
            logger.error(f"Failed to fetch loan records: {e}")
            return []
