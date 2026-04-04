# Python Learning Guide

# 1. VARIABLES AND DATA TYPES
print("=== Variables and Data Types ===")
name = "Alice"
age = 25
height = 5.8
is_student = True

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

# 2. BASIC OPERATIONS
print("\n=== Basic Operations ===")
x = 10
y = 3
print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")
print(f"Floor Division: {x // y}")
print(f"Modulo: {x % y}")

# 3. STRINGS
print("\n=== Strings ===")
greeting = "Hello, Python!"
print(greeting)
print(f"Length: {len(greeting)}")
print(f"Uppercase: {greeting.upper()}")
print(f"Lowercase: {greeting.lower()}")

# 4. LISTS
print("\n=== Lists ===")
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
fruits.append("date")
print(f"After adding date: {fruits}")

# 5. TUPLES (immutable)
print("\n=== Tuples ===")
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")

# 6. DICTIONARIES
print("\n=== Dictionaries ===")
student = {"name": "Bob", "age": 22, "grade": "A"}
print(f"Student: {student}")
print(f"Name: {student['name']}")

# 7. IF STATEMENTS
print("\n=== If Statements ===")
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# 8. LOOPS - FOR
print("\n=== For Loops ===")
for i in range(1, 6):
    print(f"Count: {i}")

for fruit in fruits:
    print(f"Fruit: {fruit}")

# 9. LOOPS - WHILE
print("\n=== While Loops ===")
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1

# 10. FUNCTIONS
print("\n=== Functions ===")


def greet(name, greeting="Hello"):
    """This is a docstring - it describes what the function does"""
    return f"{greeting}, {name}!"


print(greet("Alice"))
print(greet("Bob", "Hi"))

# 11. LIST COMPREHENSION
print("\n=== List Comprehension ===")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers: {evens}")

# 12. EXCEPTION HANDLING
print("\n=== Exception Handling ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result: {result}")
finally:
    print("This always executes")

# 13. CLASSES AND OBJECTS
print("\n=== Classes and Objects ===")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"


dog = Dog("Buddy", 3)
print(dog)
print(dog.bark())

# 14. LAMBDA FUNCTIONS
print("\n=== Lambda Functions ===")
square = lambda x: x**2
print(f"Square of 5: {square(5)}")

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")

# 15. USEFUL BUILT-IN FUNCTIONS
print("\n=== Built-in Functions ===")
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Min: {min(nums)}, Max: {max(nums)}, Sum: {sum(nums)}")
print(f"Sorted: {sorted(nums)}")
print(f"Unique: {sorted(set(nums))}")
