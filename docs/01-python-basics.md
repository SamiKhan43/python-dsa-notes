# Python Basics

Python is an interpreted, high-level programming language. This guide covers
the core syntax you need before moving to conditions, loops, and data structures.

## 1. Running Python

```bash
python main.py
```

In an interactive Python session:

```bash
python
```

Use `print()` to display values and `input()` to receive text from the user.

```python
name = input("Enter your name: ")
print("Hello,", name)
```

> `input()` always returns a string. Convert it when a number is needed.

```python
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
```

## 2. Variables

A variable is a name that refers to a value. Python creates a variable when it
is assigned; no type declaration is required.

```python
name = "Ali"
age = 20
marks = 90.5
is_student = True
```

Variable names should be descriptive and use lowercase words separated by
underscores (`snake_case`).

```python
# Good
student_name = "Ali"
student_age = 20

# Avoid
x = "Ali"  # unclear
```

### Multiple Assignment

```python
a, b, c = 10, 20, 30
x = y = z = 100
```

Swapping values is easy in Python:

```python
a, b = 10, 20
a, b = b, a
```

## 3. Comments

Comments explain code for humans and are ignored by Python.

```python
# This is a single-line comment

"""
This is a multi-line string.
It is commonly used as a documentation string.
"""
```

## 4. Built-in Data Types

| Data type | Example | Description |
|---|---|---|
| `int` | `10`, `-5` | Whole number |
| `float` | `10.5`, `2.0` | Decimal number |
| `str` | `"Python"` | Text |
| `bool` | `True`, `False` | Boolean value |
| `list` | `[1, 2, 3]` | Ordered, mutable collection |
| `tuple` | `(1, 2, 3)` | Ordered, immutable collection |
| `set` | `{1, 2, 3}` | Unordered collection of unique values |
| `dict` | `{"name": "Ali"}` | Key-value collection |
| `NoneType` | `None` | Represents no value |

Use `type()` and `isinstance()` to inspect values:

```python
value = 10

print(type(value))              # <class 'int'>
print(isinstance(value, int))   # True
```

## 5. String Basics

Strings can use single or double quotes:

```python
name = "Ali"
message = 'Welcome'
```

Use an escape sequence for special characters:

```python
print("Line 1\nLine 2")
print("She said, \"Hello!\"")
```

Strings can be combined or repeated:

```python
print("Hello " + "World")
print("Ha" * 3)
```

Use f-strings to insert values into text:

```python
name = "Ali"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

### String Indexing and Slicing

```python
text = "Python"

print(text[0])    # P
print(text[-1])   # n
print(text[0:3])  # Pyt
print(text[::-1]) # nohtyP
```

In `text[start:stop]`, `start` is included and `stop` is excluded.

## 6. Type Conversion

```python
int("100")       # "100" -> 100
float("10.5")    # "10.5" -> 10.5
str(100)         # 100 -> "100"
bool(1)          # 1 -> True
list("abc")      # "abc" -> ["a", "b", "c"]
tuple([1, 2])    # [1, 2] -> (1, 2)
set([1, 1, 2])   # [1, 1, 2] -> {1, 2}
```

Not every value can be converted:

```python
int("hello")  # Raises ValueError
```

## 7. Operators

### Arithmetic Operators

| Operator | Description | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 2` | `7` |
| `-` | Subtraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | True division | `5 / 2` | `2.5` |
| `//` | Floor division | `5 // 2` | `2` |
| `%` | Remainder | `5 % 2` | `1` |
| `**` | Exponentiation | `5 ** 2` | `25` |

```python
quotient = 10 // 3
remainder = 10 % 3
```

### Comparison Operators

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

```python
print(10 > 5)   # True
print(10 == 5)  # False
```

### Assignment Operators

| Operator | Example | Equivalent |
|---|---|---|
| `=` | `x = 5` | Assign 5 |
| `+=` | `x += 2` | `x = x + 2` |
| `-=` | `x -= 2` | `x = x - 2` |
| `*=` | `x *= 2` | `x = x * 2` |
| `/=` | `x /= 2` | `x = x / 2` |
| `//=` | `x //= 2` | `x = x // 2` |
| `%=` | `x %= 2` | `x = x % 2` |
| `**=` | `x **= 2` | `x = x ** 2` |

## 8. Logical and Membership Operators

Logical operators combine Boolean expressions:

| Operator | Description |
|---|---|
| `and` | True only if both expressions are True |
| `or` | True if at least one expression is True |
| `not` | Reverses a Boolean value |

```python
age = 20

print(age >= 18 and age < 30)
print(age < 18 or age >= 65)
print(not age < 18)
```

Membership operators check whether a value exists in a collection:

| Operator | Description |
|---|---|
| `in` | Value exists |
| `not in` | Value does not exist |

```python
numbers = [1, 2, 3]

print(2 in numbers)       # True
print(5 not in numbers)   # True
print("Py" in "Python")   # True
```

## 9. Operator Precedence

Python follows a precedence order. When in doubt, use parentheses.

```python
result = 10 + 5 * 2       # 20
result = (10 + 5) * 2     # 30
result = 10 > 5 and 3 < 4 # True
```

## 10. Common Mistakes

1. Using `=` instead of `==` to compare values.
2. Adding a number to a string without converting it.
3. Expecting `input()` to return a number directly.
4. Using `text[stop]` when slicing: `stop` is excluded.
5. Confusing integer division `/` with floor division `//`.
6. Misspelling variable names or changing capitalization.

## 11. Practice

1. Ask for a user's name and print a greeting.
2. Ask for two numbers and print their sum.
3. Calculate the area of a rectangle.
4. Convert temperature from Celsius to Fahrenheit.
5. Swap the values of two variables.
6. Print the last three characters of a string.
7. Check whether `100` is greater than `75`.

## Quick Revision

| Concept | Example |
|---|---|
| Variable | `age = 20` |
| Integer | `10` |
| Float | `10.5` |
| String | `"Python"` |
| Boolean | `True` |
| Input | `input("Prompt: ")` |
| Output | `print(value)` |
| F-string | `f"Age: {age}"` |
| Convert to integer | `int("20")` |
| Compare | `x == y` |
| Add and assign | `x += 2` |
| Membership | `x in values` |
