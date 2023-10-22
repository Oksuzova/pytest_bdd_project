"""Book_manager feature tests."""

from tests.book_manager_impl import *
from pytest_bdd import scenario

@scenario('book_manager.feature', 'New book should be add to unread shelf')
def test_new_book_should_be_add_to_unread_shelf():
    """New book should be add to unread shelf."""


@scenario('book_manager.feature', 'Book should have read status after reading')
def test_book_should_have_read_status_after_reading():
    """Book should have read status after reading."""


@scenario('book_manager.feature', 'Counting read books')
def test_counting_read_books():
    """Counting read books."""


@scenario('book_manager.feature', 'Counting the total number of books')
def test_counting_the_total_number_of_books():
    """Counting the total number of books."""


@scenario('book_manager.feature', 'Counting unread books')
def test_counting_unread_books():
    """Counting unread books."""


@scenario('book_manager.feature', 'Retrieve a book from read shelf')
def test_retrieving_a_book_should_work_for_both_read_and_unread_shelves():
    """Retrieving a book should work for both read and unread shelves."""


@scenario('book_manager.feature', 'Retrieve a book from unread shelf')
def test_retrieving_a_book_should_work_for_both_read_and_unread_shelves():
    """Retrieving a book should work for both read and unread shelves."""
