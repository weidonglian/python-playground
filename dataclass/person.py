from dataclasses import dataclass


@dataclass
class Person:
    name: str
    address: str
    salary: float

    def total_info(self) -> str:
        return f"{self.name} and {self.address}"

    def calculate(self, new_salary: float) -> float:
        return self.salary + new_salary

