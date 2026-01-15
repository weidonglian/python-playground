"""
Function Overloading Example

Demonstrates different techniques to achieve function overloading behavior
in Python, since Python doesn't have compile-time overloading like C++.
"""

from functools import singledispatch, singledispatchmethod
from typing import overload, Union


# ============================================================================
# Technique 1: Default Parameters (Most Common)
# ============================================================================

def calculate_v1(a: float, b: float, operation: str = "add") -> float:
    """
    Simulates overloading using default parameters.
    Different behaviors based on the operation parameter.
    """
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    elif operation == "subtract":
        return a - b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
    else:
        raise ValueError(f"Unknown operation: {operation}")


# ============================================================================
# Technique 2: Using *args and **kwargs
# ============================================================================

def process_data(*args, **kwargs) -> Union[int, float, str]:
    """
    Simulates overloading using *args and **kwargs.
    Behavior changes based on number and type of arguments.
    """
    if len(args) == 1:
        # Single argument - double it
        value = args[0]
        if isinstance(value, (int, float)):
            return value * 2
        elif isinstance(value, str):
            return value * 2  # String repetition
        else:
            return f"Processed: {value}"

    elif len(args) == 2:
        # Two arguments - add them
        return args[0] + args[1]

    elif len(args) == 3:
        # Three arguments - multiply all
        return args[0] * args[1] * args[2]

    elif "multiply" in kwargs:
        # Keyword argument handling
        return kwargs["multiply"] * 2

    else:
        raise ValueError(f"Unsupported arguments: args={args}, kwargs={kwargs}")


# ============================================================================
# Technique 3: Using @functools.singledispatch (Type-based Dispatch)
# ============================================================================

@singledispatch
def process(value):
    """Base function for singledispatch - handles unregistered types."""
    return f"Processing unknown type: {type(value).__name__}"


@process.register
def _(value: int) -> str:
    """Handle integer values."""
    return f"Processing integer: {value * 2}"


@process.register
def _(value: str) -> str:
    """Handle string values."""
    return f"Processing string: {value.upper()}"


@process.register
def _(value: list) -> str:
    """Handle list values."""
    return f"Processing list with {len(value)} items: {value}"


@process.register
def _(value: dict) -> str:
    """Handle dictionary values."""
    return f"Processing dict with {len(value)} keys: {list(value.keys())}"


# ============================================================================
# Technique 4: Using @typing.overload (Type Hints Only)
# ============================================================================

@overload
def add(x: int, y: int) -> int:
    """Type hint for int + int -> int."""
    ...


@overload
def add(x: str, y: str) -> str:
    """Type hint for str + str -> str."""
    ...


@overload
def add(x: float, y: float) -> float:
    """Type hint for float + float -> float."""
    ...


def add(x, y):
    """
    Actual implementation.
    Type checkers understand the overloads above, but runtime uses this.
    """
    return x + y


# ============================================================================
# Technique 5: Method Overloading with @singledispatchmethod
# ============================================================================

class Calculator:
    """Example class using singledispatchmethod for method overloading."""

    @singledispatchmethod
    def compute(self, value):
        """Base method - handles unregistered types."""
        raise TypeError(f"Unsupported type: {type(value).__name__}")

    @compute.register
    def _(self, value: int) -> int:
        """Handle integer - square it."""
        return value * value

    @compute.register
    def _(self, value: float) -> float:
        """Handle float - cube it."""
        return value * value * value

    @compute.register
    def _(self, value: str) -> str:
        """Handle string - reverse it."""
        return value[::-1]

    @compute.register
    def _(self, value: list) -> int:
        """Handle list - return sum."""
        return sum(value)


# ============================================================================
# Main Demonstration
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Function Overloading Techniques in Python")
    print("=" * 70)

    print("\n1. Default Parameters:")
    print("-" * 70)
    print(f"calculate_v1(5, 3) = {calculate_v1(5, 3)}")
    print(f"calculate_v1(5, 3, 'multiply') = {calculate_v1(5, 3, 'multiply')}")
    print(f"calculate_v1(10, 2, 'divide') = {calculate_v1(10, 2, 'divide')}")

    print("\n2. *args and **kwargs:")
    print("-" * 70)
    print(f"process_data(5) = {process_data(5)}")
    print(f"process_data(3, 4) = {process_data(3, 4)}")
    print(f"process_data(2, 3, 4) = {process_data(2, 3, 4)}")
    print(f"process_data('hello') = {process_data('hello')}")
    print(f"process_data(multiply=10) = {process_data(multiply=10)}")

    print("\n3. @singledispatch (Type-based Dispatch):")
    print("-" * 70)
    print(f"process(42) = {process(42)}")
    print(f"process('hello') = {process('hello')}")
    print(f"process([1, 2, 3, 4]) = {process([1, 2, 3, 4])}")
    print(f"process({{'a': 1, 'b': 2}}) = {process({'a': 1, 'b': 2})}")
    print(f"process(3.14) = {process(3.14)}")  # Uses base function

    print("\n4. @typing.overload (Type Hints Only):")
    print("-" * 70)
    result1: int = add(5, 3)
    result2: str = add("hello", "world")
    result3: float = add(3.14, 2.71)
    print(f"add(5, 3) = {result1} (type: {type(result1).__name__})")
    print(f"add('hello', 'world') = {result2} (type: {type(result2).__name__})")
    print(f"add(3.14, 2.71) = {result3} (type: {type(result3).__name__})")
    print("Note: @overload only helps type checkers, runtime behavior is the same")

    print("\n5. @singledispatchmethod (Class Methods):")
    print("-" * 70)
    calc = Calculator()
    print(f"calc.compute(5) = {calc.compute(5)}")
    print(f"calc.compute(3.0) = {calc.compute(3.0)}")
    print(f"calc.compute('python') = {calc.compute('python')}")
    print(f"calc.compute([1, 2, 3, 4, 5]) = {calc.compute([1, 2, 3, 4, 5])}")

    print("\n" + "=" * 70)
    print("Key Points:")
    print("- Python doesn't have compile-time function overloading like C++")
    print("- Default parameters are the most common approach")
    print("- *args/**kwargs provide flexibility but less type safety")
    print("- @singledispatch enables type-based dispatch at runtime")
    print("- @overload provides type hints for static type checkers only")
    print("- @singledispatchmethod works for class methods")
    print("=" * 70)
