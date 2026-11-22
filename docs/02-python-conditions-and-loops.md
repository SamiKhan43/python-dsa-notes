# Python Conditions and Loops

Conditions choose which code to execute. Loops repeat code while a condition
is true or while iterating over a sequence.

## 1. If Statements

Code inside an `if` block runs only when its condition is `True`.

```python
age = 20

if age >= 18:
    print("Adult")
```

Python uses indentation to identify a code block:

```python
if True:
    print("Inside the if block")

print("Always executed")
```

Use four spaces for indentation.

## 2. If-Else

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## 3. If-Elif-Else

Use `elif` to check additional conditions in order.

```python
marks = 85

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "Fail"

print(grade)
```

Only the first matching block is executed.

## 4. Nested Conditions

Put an `if` statement inside another block for related conditions:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")
```

Nested conditions can become difficult to read. Prefer combining conditions
when possible:

```python
if age >= 18 and has_id:
    print("Entry allowed")
elif age >= 18:
    print("ID required")
else:
    print("Underage")
```

## 5. Logical Conditions

```python
x = 7

if x > 0 and x < 10:
    print("Single-digit positive number")

if x < 0 or x > 10:
    print("Outside the main range")

if not x == 0:
    print("Not zero")
```

Use `!= 0` instead of `not x == 0` when checking inequality.

## 6. Truthy and Falsy Values

An empty or zero value is usually falsy. Non-empty and non-zero values are truthy.

```python
if []:
    print("This will not run")

if [1, 2]:
    print("This will run")

if 0:
    print("This will not run")

if "Python":
    print("This will run")
```

## 7. Ternary Expression

A ternary expression is a short form of `if-else`, useful for assigning one of
two values:

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
```

Keep ternary expressions simple. Use a full `if-else` for complex decisions.

## 8. Match-Case

`match-case` compares a value against several patterns. It requires Python 3.10+.

```python
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")
```

The `_` case is the default case.

## 9. For Loops

A `for` loop iterates over each item in a sequence.

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

It also works with strings:

```python
for character in "Python":
    print(character)
```

### Range

`range(start, stop, step)` generates numbers without creating a list.
The `stop` value is excluded.

| Code | Values |
|---|---|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(1, 6)` | `1, 2, 3, 4, 5` |
| `range(1, 10, 2)` | `1, 3, 5, 7, 9` |
| `range(10, 0, -1)` | `10, 9, 8, ..., 1` |

```python
for i in range(5):
    print(i)
```

## 10. While Loops

A `while` loop repeats while its condition is `True`.

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

Always update the variable that controls a `while` loop, unless the loop is
terminated with `break`.

### Avoiding Infinite Loops

```python
attempts = 0

while attempts < 3:
    print("Try again")
    attempts += 1
```

## 11. Break

`break` immediately ends the loop.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Output:

```text
0
1
2
3
4
```

## 12. Continue

`continue` skips the remaining code in the current iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output:

```text
0
1
3
4
```

## 13. Pass

`pass` performs no action and is useful as a placeholder.

```python
for i in range(5):
    pass
```

## 14. Loop Else

A loop's `else` block executes when the loop ends normally, without `break`.

```python
for i in range(5):
    if i == 10:
        break
else:
    print("No break occurred")
```

`else` can be useful for search operations:

```python
numbers = [10, 20, 30]
target = 25

for number in numbers:
    if number == target:
        print("Found")
        break
else:
    print("Not found")
```

## 15. Nested Loops

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

Pattern example:

```python
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
```

Output:

```text
*
* *
* * *
* * * *
```

## 16. Useful Loop Functions

### enumerate()

Returns the index and value.

```python
names = ["Ali", "Ahmed", "Sara"]

for index, name in enumerate(names):
    print(index, name)
```

### zip()

Iterates over multiple sequences together.

```python
names = ["Ali", "Ahmed"]
ages = [20, 22]

for name, age in zip(names, ages):
    print(name, age)
```

### reversed()

Iterates from the end to the beginning.

```python
for number in reversed([1, 2, 3]):
    print(number)
```

### sorted()

Iterates through values in sorted order.

```python
for number in sorted([4, 1, 3, 2]):
    print(number)
```

## 17. Common DSA Loop Patterns

### Find the maximum

```python
numbers = [4, 8, 2, 10, 5]
maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)
```

### Calculate a sum

```python
numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number

print(total)
```

### Find an element

```python
numbers = [10, 20, 30, 40]
target = 30

for index in range(len(numbers)):
    if numbers[index] == target:
        print("Found at index:", index)
        break
```

### Compare pairs

```python
numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        print(numbers[i], numbers[j])
```

## 18. Time Complexity

| Pattern | Time complexity |
|---|---|
| One loop over `n` items | `O(n)` |
| Two sequential loops | `O(n)` |
| One nested pair of loops | `O(n²)` |
| Three nested loops | `O(n³)` |
| Loop dividing by 2 | `O(log n)` |

```python
# O(n)
for i in range(n):
    print(i)

# O(n²)
for i in range(n):
    for j in range(n):
        print(i, j)

# O(log n)
while n > 1:
    n //= 2
```

## 19. Common Mistakes

1. Forgetting `:` after `if`, `elif`, `else`, `for`, or `while`.
2. Using `=` instead of `==` in a comparison.
3. Forgetting to update the condition variable in a `while` loop.
4. Forgetting that `range()` excludes its stop value.
5. Using `break` when `continue` is required.
6. Indenting code inconsistently.
7. Modifying a collection while iterating over it without care.

## 20. Practice Problems

### Beginner

1. Print numbers from 1 to 100.
2. Print even numbers from 1 to 50.
3. Print a multiplication table.
4. Find the sum of numbers from 1 to `N`.
5. Calculate the factorial of a number.
6. Reverse a number.

### Intermediate

7. Find the largest of three numbers.
8. Check whether a number is prime.
9. Print the Fibonacci sequence.
10. Check whether a number is a palindrome.
11. Print a star pattern.
12. Count the frequency of an element in an array.

### DSA

13. Contains Duplicate.
14. Find Maximum in an Array.
15. Two Sum using brute force.
16. Check whether an Array Is Sorted.
17. Reverse an Array.
18. Move All Zeros to the End.

## Quick Revision

| Concept | Purpose |
|---|---|
| `if` | Execute when a condition is True |
| `elif` | Check another condition |
| `else` | Execute when no condition matched |
| `match-case` | Compare against patterns |
| `for` | Iterate over a sequence |
| `while` | Repeat while a condition is True |
| `range()` | Generate a number sequence |
| `break` | Exit a loop immediately |
| `continue` | Skip to the next iteration |
| `pass` | Placeholder with no action |
| `enumerate()` | Get index and value |
| `zip()` | Combine sequences |
| `reversed()` | Iterate in reverse |
