class Item():
    def __init__(self, name: str, amount: str):
        self._name = name
        self._amount = amount

    def set_name(self, name: str):
        self._name = name

    def set_amount(self, amount: str):
        self._amount = amount

    def get_name(self):
        return self._name

    def get_amount(self):
        return self._amount

    name = property(get_name, set_name)
    amount = property(get_amount, set_amount)
