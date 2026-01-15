"""
Method Overriding Example

Demonstrates how Python supports method overriding through inheritance,
similar to C++ virtual functions.
"""


class Animal:
    """Base class demonstrating method overriding."""

    def __init__(self, name: str):
        self.name = name

    def make_sound(self) -> str:
        """Base implementation - can be overridden by subclasses."""
        return f"{self.name} makes a generic sound"

    def move(self) -> str:
        """Base implementation - can be overridden by subclasses."""
        return f"{self.name} moves"

    def info(self) -> str:
        """Uses other methods - demonstrates polymorphism."""
        return f"{self.name}: {self.make_sound()}, {self.move()}"


class Dog(Animal):
    """Dog class that overrides parent methods."""

    def make_sound(self) -> str:
        """Override: Dog-specific sound."""
        return f"{self.name} barks: Woof! Woof!"

    def move(self) -> str:
        """Override: Dog-specific movement."""
        return f"{self.name} runs on four legs"


class Cat(Animal):
    """Cat class that overrides parent methods."""

    def make_sound(self) -> str:
        """Override: Cat-specific sound."""
        return f"{self.name} meows: Meow!"

    def move(self) -> str:
        """Override: Cat-specific movement."""
        return f"{self.name} walks gracefully"


class Bird(Animal):
    """Bird class that overrides some methods but not others."""

    def make_sound(self) -> str:
        """Override: Bird-specific sound."""
        return f"{self.name} chirps: Tweet! Tweet!"

    # Note: move() is NOT overridden, so it uses the parent's implementation


class Shape:
    """Another example: Shape hierarchy with method overriding."""

    def area(self) -> float:
        """Base method - must be overridden by subclasses."""
        raise NotImplementedError("Subclass must implement area()")

    def perimeter(self) -> float:
        """Base method - must be overridden by subclasses."""
        raise NotImplementedError("Subclass must implement perimeter()")

    def describe(self) -> str:
        """Uses overridden methods - demonstrates polymorphism."""
        return f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"


class Rectangle(Shape):
    """Rectangle class overriding Shape methods."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Override: Rectangle-specific area calculation."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Override: Rectangle-specific perimeter calculation."""
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle class overriding Shape methods."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Override: Circle-specific area calculation."""
        return 3.14159 * self.radius * self.radius

    def perimeter(self) -> float:
        """Override: Circle-specific perimeter calculation."""
        return 2 * 3.14159 * self.radius


if __name__ == "__main__":
    print("=" * 60)
    print("Method Overriding Example - Animal Hierarchy")
    print("=" * 60)

    # Create instances of different animals
    animals = [
        Animal("Generic Animal"),
        Dog("Buddy"),
        Cat("Whiskers"),
        Bird("Tweety"),
    ]

    # Demonstrate polymorphism - same interface, different behavior
    for animal in animals:
        print(f"\n{animal.info()}")
        print(f"\n{animal.make_sound()}")

    print("\n" + "=" * 60)
    print("Method Overriding Example - Shape Hierarchy")
    print("=" * 60)

    # Create instances of different shapes
    shapes = [
        Rectangle(5.0, 3.0),
        Circle(4.0),
        Rectangle(10.0, 2.0),
    ]

    # Demonstrate polymorphism - same interface, different behavior
    for shape in shapes:
        print(f"\n{shape.describe()}")

    print("\n" + "=" * 60)
    print("Key Points:")
    print("- Python supports method overriding through inheritance")
    print("- Subclasses can override parent class methods")
    print("- Polymorphism works at runtime based on object type")
    print("- Methods not overridden use the parent's implementation")
    print("=" * 60)
