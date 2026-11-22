# Python Data Structures

Data structures are ways of organizing and storing data so we can access and modify it efficiently.

Python has several built-in data structures:

1. Lists
2. Tuples
3. Sets
4. Dictionaries
5. Strings

---

# 1. Lists

A list is an ordered, mutable collection that allows duplicate elements.

### Creating a List

```python
nums = [10, 20, 30, 40, 50]
```

### Accessing Elements

```python
nums[0]     # 10
nums[-1]    # 50
nums[1:3]   # [20, 30]
nums[::-1]  # Reverse list
```

### List Methods

| Method | Description |
|---|---|
| `append(x)` | Add element at the end |
| `extend(iterable)` | Add multiple elements |
| `insert(i, x)` | Insert at a specific index |
| `remove(x)` | Remove first occurrence |
| `pop()` | Remove last element |
| `pop(i)` | Remove element at index |
| `clear()` | Remove all elements |
| `index(x)` | Find element index |
| `count(x)` | Count occurrences |
| `sort()` | Sort the list |
| `reverse()` | Reverse the list |
| `copy()` | Create a shallow copy |

### List Operations

```python
nums = [10, 20, 30, 40]

len(nums)       # Length
max(nums)       # Maximum
min(nums)       # Minimum
sum(nums)       # Sum
20 in nums      # Check existence
sorted(nums)    # Return sorted list
```

### List Traversal

```python
# Values
for num in nums:
    print(num)

# Indexes
for i in range(len(nums)):
    print(nums[i])

# Index and value
for i, num in enumerate(nums):
    print(i, num)
```

### List Comprehension

```python
squares = [x * x for x in range(5)]

evens = [x for x in range(10) if x % 2 == 0]
```

### List Time Complexity

| Operation | Complexity |
|---|---|
| Access by index | O(1) |
| Search | O(n) |
| Append | O(1) amortized |
| Insert at beginning | O(n) |
| Remove by value | O(n) |
| Pop last element | O(1) |
| Sorting | O(n log n) |

### DSA Applications

- Array traversal
- Searching
- Sorting
- Two pointers
- Sliding window
- Stack implementation

---

# 2. Tuples

A tuple is an ordered and immutable collection that allows duplicates.

### Creating a Tuple

```python
nums = (10, 20, 30, 40)
```

### Tuple Methods

| Method | Description |
|---|---|
| `count(x)` | Count occurrences |
| `index(x)` | Find element index |

### Tuple Operations

```python
nums[0]       # First element
nums[-1]      # Last element
len(nums)     # Length
20 in nums    # Check existence
nums[1:3]     # Slicing
```

### Important Points

- Ordered collection.
- Allows duplicate values.
- Cannot be modified after creation.
- Can be used as dictionary keys if all elements are hashable.

### DSA Applications

- Store fixed values.
- Represent coordinates.
- Store pairs such as `(value, index)`.
- Use as keys in dictionaries.

---

# 3. Sets

A set is an unordered collection of unique elements.

### Creating a Set

```python
nums = {1, 2, 3, 4, 5}

empty_set = set()
```

Note: `{}` creates an empty dictionary, not an empty set.

### Set Methods

| Method | Description |
|---|---|
| `add(x)` | Add an element |
| `update(iterable)` | Add multiple elements |
| `remove(x)` | Remove element; error if absent |
| `discard(x)` | Remove element without error if absent |
| `pop()` | Remove an arbitrary element |
| `clear()` | Remove all elements |
| `copy()` | Create a shallow copy |

### Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # Union
a & b    # Intersection
a - b    # Difference
a ^ b    # Symmetric difference

3 in a   # Membership check
len(a)   # Length
```

### DSA Example: Contains Duplicate

```python
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
```

### DSA Applications

- Finding duplicates.
- Removing duplicates.
- Fast membership checking.
- Finding common elements.
- Tracking visited elements.

---

# 4. Dictionaries

A dictionary stores data in key-value pairs.

### Creating a Dictionary

```python
student = {
    "name": "Ali",
    "age": 20,
    "marks": 90
}
```

### Dictionary Methods

| Method | Description |
|---|---|
| `get(key)` | Get value safely |
| `keys()` | Return all keys |
| `values()` | Return all values |
| `items()` | Return key-value pairs |
| `update()` | Update dictionary |
| `pop(key)` | Remove a specific key |
| `popitem()` | Remove last inserted pair |
| `setdefault()` | Get value or insert default |
| `clear()` | Remove all elements |
| `copy()` | Create a shallow copy |

### Dictionary Operations

```python
student = {"name": "Ali", "age": 20}

student["name"]             # Access
student["city"] = "Karachi" # Add
student["age"] = 21         # Update

"age" in student            # Check key
student.get("marks", 0)     # Safe access
```

### Dictionary Traversal

```python
# Keys
for key in student:
    print(key)

# Values
for value in student.values():
    print(value)

# Key-value pairs
for key, value in student.items():
    print(key, value)
```

### DSA Example: Frequency Counter

```python
nums = [1, 2, 2, 3, 3, 3]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(freq)
```

Output:

```python
{1: 1, 2: 2, 3: 3}
```

### DSA Applications

- Two Sum.
- Frequency counting.
- Grouping elements.
- Anagram problems.
- Fast lookups.
- Memoization.

---

# 5. Strings

A string is an immutable sequence of characters.

### Creating a String

```python
s = "Python Programming"
```

### String Operations

```python
s[0]       # First character
s[-1]      # Last character
s[1:5]     # Slicing
s[::-1]    # Reverse
len(s)     # Length
"Python" in s
```

### String Methods

| Method | Description |
|---|---|
| `lower()` | Convert to lowercase |
| `upper()` | Convert to uppercase |
| `capitalize()` | Capitalize first character |
| `title()` | Capitalize each word |
| `strip()` | Remove surrounding whitespace |
| `replace(a, b)` | Replace text |
| `split()` | Split into a list |
| `join()` | Join strings |
| `find(x)` | Find substring index |
| `count(x)` | Count occurrences |
| `startswith(x)` | Check starting text |
| `endswith(x)` | Check ending text |
| `isdigit()` | Check whether all characters are digits |
| `isalpha()` | Check whether all characters are letters |

### DSA Applications

- Palindrome problems.
- Anagram problems.
- String reversal.
- Character frequency.
- Substring searching.
- Two pointers.

---

# 6. Important Built-in Functions

These functions are useful across different data structures.

| Function | Description |
|---|---|
| `len()` | Get length |
| `max()` | Get maximum |
| `min()` | Get minimum |
| `sum()` | Calculate sum |
| `sorted()` | Return sorted list |
| `reversed()` | Return reverse iterator |
| `enumerate()` | Get index and value |
| `zip()` | Combine iterables |
| `range()` | Generate number sequence |
| `any()` | Check if any element is True |
| `all()` | Check if all elements are True |
| `abs()` | Absolute value |

---

# 7. Data Structure Comparison

| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Ordered | Yes | Yes | No guaranteed order | Yes |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No | Keys: No |
| Indexed | Yes | Yes | No | By key |
| Syntax | `[]` | `()` | `{}` | `{key: value}` |

---

# 8. Time Complexity Comparison

Average-case complexities:

| Operation | List | Set | Dictionary |
|---|---|---|---|
| Access | O(1) by index | N/A | O(1) by key |
| Search | O(n) | O(1) | O(1) by key |
| Insert | O(1) append* | O(1) | O(1) |
| Delete | O(n) | O(1) | O(1) |

*List append is amortized O(1). Set and dictionary operations can be O(n) in the worst case.*

---

# 9. Which Data Structure Should You Use?

| Problem | Recommended Structure |
|---|---|
| Contains Duplicate | Set |
| Two Sum | Dictionary |
| Frequency Counter | Dictionary |
| Remove Duplicates | Set |
| Reverse Array | List |
| Find Maximum | List |
| Valid Anagram | Dictionary / Counter |
| Store Unique Elements | Set |
| Key-Value Mapping | Dictionary |
| Fixed Collection | Tuple |
| Palindrome Check | String |

---

# 10. Practice Problems

### Lists
1. Find maximum element.
2. Find minimum element.
3. Reverse a list.
4. Find the second-largest element.
5. Remove duplicates.

### Sets
6. Contains Duplicate.
7. Find common elements between two lists.
8. Find the union of two lists.
9. Find the intersection of two lists.

### Dictionaries
10. Count frequency of elements.
11. Two Sum.
12. Find the most frequent element.
13. Valid Anagram.

### Strings
14. Reverse a string.
15. Valid Palindrome.
16. Count vowels.
17. Find the first non-repeating character.
18. Check whether two strings are anagrams.