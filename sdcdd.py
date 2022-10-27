from dataclasses import dataclass, field, asdict


@dataclass
class User:
    name: str
    age: int

class qqq:
    name: str
    age: int
    def __init__(self, name, age):
        self.user = User(name, age)

    def get_dataclass(self):
        return asdict(self.user)

a = qqq('waq', 3)
print(a.get_dataclass())