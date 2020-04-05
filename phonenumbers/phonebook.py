class PhoneBook:
    def __init__(self):
        self.numbers = dict()

    def add(self, name: str, number: str):
        self.numbers[name] = number

    def lookup(self, name: str) -> str:
        return self.numbers[name]

    def is_consistent(self) -> bool:
        return True
