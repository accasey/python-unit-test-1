from typing import List


class PhoneBook:
    def __init__(self):
        self.numbers = dict()

    def add(self, name: str, number: str):
        self.numbers[name] = number

    def lookup(self, name: str) -> str:
        return self.numbers[name]

    def is_consistent(self) -> bool:
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True

    def get_names(self) -> List[str]:
        return [k for k in self.numbers.keys()]

    def get_numbers(self) -> List[str]:
        return [*self.numbers.values()]
