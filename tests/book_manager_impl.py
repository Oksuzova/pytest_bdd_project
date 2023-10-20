import pytest
from pytest_bdd import given, when, then
from pytest_bdd.parsers import cfparse


@pytest.fixture
def ctx():
    return {}


@given(cfparse('A book with <{name}> name and <{author}> author is added to the <{shelf_type}> shelf'))
@when(cfparse('A book with <{name}> name and <{author}> author is added to the <{shelf_type}> shelf'))
def add_book_to_shelf(request, ctx, name, author, shelf_type):
    """
    :param ctx: current context fixture
    :param name: str
    :param author: str
    :param shelf_type: read/unread
    :return:
    """
    pass


@given(cfparse('Create book with <{name}> name and <{author}> author'))
def define_book(ctx, name, author):
    """
    :param ctx: current context fixture
    :param name: str
    :param author: str
    :return:
    """
    pass


@given(cfparse('No books are added to the <{shelf_type}> shelf'))
def define_empty_shelf(ctx, shelf_type):
    """
    :param ctx:
    :param shelf_type: str read/unread/all shelf
    :return:
    """
    pass


@when(cfparse('<{action}> current book in to closet'))
@when(cfparse('<{action}> current book from closet'))
def add_book_to_closet(ctx, action):
    """
    :param ctx: current context fixture
    :param action: add/retrieve/read
    :return:
    """
    pass


@then(cfparse('Current book <{status}> in closet at <{shelf_type}> shelf'))
def verify_book_present_in_shelf(ctx, status, shelf_type):
    """
    :param ctx: current context fixture
    :param status: str present/not present
    :param shelf_type: str read/unread
    :return:
    """
    assert  42==42


@when(cfparse('Current book is <{status}>'))
@then(cfparse('Current book is <{status}>'))
def verify_book_status(ctx, status):
    """
    :param ctx:
    :param status: str readed/unreaded
    :return:
    """
    pass


@then(cfparse('Closet <{shelf_type}> book counter equal <{value}>'))
def verify_closets_counter(ctx, shelf_type, value):
    """
    :param ctx:
    :param shelf_type: str read/unread
    :param value: int
    :return:
    """
    pass

