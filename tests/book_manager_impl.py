import pytest
from pytest_bdd import given, when, then
from pytest_bdd.parsers import cfparse, parse
from src.book import Book
from src.book_manager import Closet
from allure import step


@pytest.fixture
def ctx():
    return {"closet": Closet()}


@given(cfparse('A book with <{name}> name and <{author}> author is added to the <{shelf_type}> shelf'))
@when(cfparse('A book with <{name}> name and <{author}> author is added to the <{shelf_type}> shelf'))
@step('A book with name and author is added to the shelf')
def add_book_to_shelf(ctx, name, author, shelf_type):
    """
    :param ctx: current context fixture
    :param name: str
    :param author: str
    :param shelf_type: read/unread
    :return:
    """
    book = ctx["closet"].take(name, author)
    if shelf_type == "read":
        ctx["closet"].reading(name)
    ctx["f_book"] = book


@given(cfparse('Create book with <{name}> name and <{author}> author'))
@step('Create book with name and author')
def define_book(ctx, name, author):
    """
    :param ctx: current context fixture
    :param name: str
    :param author: str
    :return:
    """
    book = Book(name, author)
    ctx["f_book"] = book


@given(cfparse('No books are added to the <{shelf_type}> shelf'))
@step('Define no books are added to the shelf')
def define_empty_shelf(ctx, shelf_type):
    """
    :param ctx:
    :param shelf_type: str read/unread
    :return:
    """
    if shelf_type == "read":
        assert ctx["closet"].count_read == 0
    if shelf_type == "unread":
        assert ctx["closet"].count_unread == 0


@when(cfparse('<{action}> current book in to closet'))
@when(cfparse('<{action}> current book from closet'))
def action_book_to_closet(ctx, action):
    """
    :param ctx: current context fixture
    :param action: add/retrieve/read
    :return:
    """
    with step(f'<{action}> current book in to closet'):
        book = ctx["f_book"]
        if action == "add":
            ctx["closet"].take(book.name, book.author)
        elif action == "retrieve":
            ctx["closet"].retrieve(book.name)
        elif action == 'read':
            ctx["closet"].reading(book.name)
        else:
            raise KeyError(f'Unknown action: {action}')


@then(cfparse('Current book <{status}> in closet at <{shelf_type}> shelf'))
def verify_book_present_in_shelf(ctx, status, shelf_type):
    """
    :param ctx: current context fixture
    :param status: str present/not_present
    :param shelf_type: str read/unread
    :return:
    """
    with step(f'Current book <{status}> in closet at <{shelf_type}> shelf'):
        book = ctx.get('f_book')

        if shelf_type == 'read':
            shelf = ctx['closet'].read
        else:
            shelf = ctx['closet'].no_read

        if status == 'present':
            assert book in shelf
        else:
            assert book not in shelf


@when(cfparse('Current book is <{status}>'))
@then(cfparse('Current book is <{status}>'))
def verify_book_status(ctx, status):
    """
    :param ctx:
    :param status: str readed/unreaded
    :return:
    """
    with step(f'Current book is <{status}>'):
        if status == "readed":
            assert ctx["f_book"].read is True
        else:
            assert ctx["f_book"].read is False


@then(parse('Closet <{shelf_type}> book counter equal <{value:d}>'))
def verify_closets_counter(ctx, shelf_type, value):
    """
    :param ctx:
    :param shelf_type: str read/unread/total
    :param value: int
    :return:
    """
    with step(f'Closet <{shelf_type}> book counter equal <{value:d}>'):
        closet = ctx["closet"]
        if shelf_type == "read":
            assert closet.count_read == value
        elif shelf_type == "unread":
            assert closet.count_unread == value
        else:
            assert closet.total == value
