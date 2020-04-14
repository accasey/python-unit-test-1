import pytest
from typing import Generator, Iterator
from phonebook import Phonebook


@pytest.fixture
# def phonebook() -> Iterator[Phonebook]:
def phonebook(tmpdir) -> Phonebook:
    """
    Provides an empty Phonebook object
    """
    # return Phonebook()

    # Use 'yield' and not 'return' so that we can run clear at the end of every test case
    # phonebook = Phonebook()
    # yield phonebook
    # phonebook.clear()

    # With the tmpdir built-in pytest fixture, you can revert to the return
    # You can run 'pytest --fixtures' to get a list of the pytest fixtures
    # and their docstrings
    return Phonebook(tmpdir)


def test_lookup_by_name(phonebook):
    # phonebook = Phonebook()
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")


def test_phonebook_contains_all_names(phonebook):
    # phonebook = Phonebook()
    phonebook.add("Bob", "1234")
    # assert phonebook.names() == {"Bob", "Missing"}
    assert "Bob" in phonebook.names()


def test_missing_name_raises_error(phonebook):
    # phonebook: Phonebook = Phonebook()
    # phonebook.add("Bob", "1234")
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
