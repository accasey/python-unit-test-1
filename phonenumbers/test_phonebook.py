import unittest
from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        print("In setUp")
        self.phonebook: PhoneBook = PhoneBook()

    def tearDown(self) -> None:
        # Still going to be run after the test case causes an exception
        print("In tearDown")

    def test_lookup_by_name(self):
        # phonebook: PhoneBook = PhoneBook()
        self.phonebook.add("Bob", "12345")
        number: str = self.phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
        # phonebook: PhoneBook = PhoneBook()
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    # @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        # phonebook: PhoneBook = PhoneBook
        self.assertTrue(self.phonebook.is_consistent())
