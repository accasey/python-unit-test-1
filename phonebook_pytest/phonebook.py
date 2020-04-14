from typing import Dict, Set
import os


class Phonebook():

    def __init__(self, cache_directory) -> None:
        self.numbers: Dict[str, str] = {}
        self.filename = os.path.join(cache_directory, "phonebook.txt")
        self.cache = open(self.filename, "w")

    def add(self, name: str, number: str) -> None:
        self.numbers[name] = number

    def lookup(self, name: str) -> str:
        return self.numbers[name]

    def names(self) -> Set[str]:
        return set(self.numbers.keys())

    def clear(self):
        self.cache.close()
        os.remove(self.filename)
