import unittest
from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        # print("In setUp")
        self.phonebook: PhoneBook = PhoneBook()

    def tearDown(self) -> None:
        # Still going to be run after the test case causes an exception
        # print("In tearDown")
        pass

    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "12345")
        number: str = self.phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    # @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Anna', '012345')
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Sue', '12345')
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):

        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Sue', '123')
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Sue", "123343")
        self.assertIn("Sue", self.phonebook.get_names())
        self.assertIn("123343", self.phonebook.get_numbers())

# 1. Arrange
#    Set up the object to be tested, and collaborators
# 2. Act
#    Exercise the unit under test.
# 3. Assert
#    Make claims about what happened.
