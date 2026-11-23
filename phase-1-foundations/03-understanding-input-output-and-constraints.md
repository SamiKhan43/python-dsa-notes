# Lesson 3: Understanding Input, Output, and Constraints

Correct code is not only about passing examples. It must read the input format,
produce the exact output format, and handle every valid input within the stated
constraints.

## 1. Understand the input format

Before writing code, identify how much input is given and how it is separated.

Common formats include:

| Input format | Example |
|---|---|
| One integer | `5` |
| One integer and one line | `5\n1 2 3 4 5\n` |
| A fixed number of values | `10 20 30` |
| One line per test case | `3\n6\n9\n` |
| Until the end of input | `1 2 3\n4 5 6\n` |

The input format determines how the values are read. Do not invent a format that
the problem statement does not provide.

## 2. Read input safely

Use `input()` for interactive input or one line at a time.

```python
n = int(input())
numbers = list(map(int, input().split()))
```

Use `sys.stdin.readline()` or `sys.stdin.read()` when there is enough input that
calling `input()` repeatedly could be slow.

```python
import sys

data = sys.stdin.readline().split()
n = int(data[0])
numbers = list(map(int, data[1:]))
```

For a complete input stream:

```python
import sys

values = list(map(int, sys.stdin.read().split()))
n = values[0]
numbers = values[1:n + 1]
```

This approach is useful for competitive-programming problems, but only when the
input structure is known first.

## 3. Handle test cases

When a problem gives the number of test cases, read that count and process each
case separately.

```python
import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
index = 1

for _ in range(t):
    n = data[index]
    index += 1
    numbers = data[index:index + n]
    index += n

    print(sum(numbers))
```

Keep all test-case state separate. Do not accidentally reuse a variable or
accumulator from one test case in the next.

## 4. Produce the exact output format

The output must match the problem statement exactly. This can include:

- A number on one line
- `Yes` or `No`
- A list of values
- Multiple lines
- One answer per test case
- No extra text or prompts

```python
answers = [10, 20, 30]
print(*answers)
```

This prints:

```text
10 20 30
```

For multiple answers, build a list of strings and print it once:

```python
import sys

answers = ["2", "8", "15"]
sys.stdout.write("\n".join(answers))
```

Do not add labels such as `"Answer:"` unless the problem asks for them.

## 5. Read the constraints

Constraints describe valid input sizes and value ranges. Common examples are:

- `1 <= n <= 100`
- `1 <= nums[i] <= 10^9`
- `n` is the number of array elements
- The input has `t` test cases
- The sum of `n` across test cases may have a limit
- Strings contain lowercase English letters

Always check:

1. The maximum number of elements.
2. The minimum and maximum value.
3. Whether zero or negative values are allowed.
4. Whether duplicates are allowed.
5. Whether the input is sorted.
6. Whether empty input is allowed.

## 6. Choose types carefully

Python integers have arbitrary precision, so they do not overflow in the same
way as fixed-width integers in many languages. However, very large numbers can
still be expensive to read and calculate.

Use an appropriate collection:

| Need | Common choice |
|---|---|
| Preserve order and duplicates | List |
| Remove duplicates or check membership | Set |
| Count values or map keys to values | Dictionary |
| Work with a fixed collection | Tuple |
| Process characters | String |

If the constraints allow a value up to `10^9`, the sum of many values may exceed
`10^9`, even though each individual value does not. Use Python's integer type,
and consider overflow only when using other languages.

## 7. Time and input limits

The problem's input limit determines whether parsing and processing are efficient
enough.

For `n` elements:

| Complexity | Reasonable as a starting estimate |
|---|---|
| O(n) | Usually suitable for up to hundreds of thousands |
| O(n log n) | Common for sorting and ordered operations |
| O(n²) | Usually risky for `n > 10,000` |

These are guidelines, not guarantees. Time limits can vary. The constraints,
language, and number of test cases should decide the final approach.

For `t` test cases, analyze the total input size. If each test case can contain
`n` elements, O(t * n) may be too slow. If the statement gives a limit on the sum
of `n`, use that total limit when estimating work.

## 8. Avoid input assumptions

Do not assume that:

- Input is sorted unless the statement says so.
- Values are positive unless the constraint says so.
- Duplicates do not exist unless the statement says so.
- `n` is the first line if the statement has a different format.
- The array is non-empty if `n` can be zero.
- A dictionary lookup will always find a key.
- Printing a list with brackets matches the required format.

## 9. A complete reading example

Given:

```text
T = number of test cases
N = number of integers in the test case
N integers follow
```

Read and output the sum for each test case:

```python
import sys

data = list(map(int, sys.stdin.read().split()))

t = data[0]
index = 1
answers = []

for _ in range(t):
    n = data[index]
    index += 1

    numbers = data[index:index + n]
    index += n

    answers.append(str(sum(numbers)))

sys.stdout.write("\n".join(answers))
```

This solution:

- Reads all input once.
- Keeps an independent slice for each test case.
- Calculates O(n) work for each case.
- Uses O(n) memory for the current slice and O(t) memory for the answers.

## 10. Edge cases

Create a checklist from the constraints:

- Minimum valid input
- Maximum valid input
- Empty input, if allowed
- Repeated values
- Zero
- Negative values
- A single element
- Large values
- Multiple test cases
- Large totals

Example:

```python
def sum_of_values(values):
    return sum(values)

assert sum_of_values([]) == 0
assert sum_of_values([5]) == 5
assert sum_of_values([0, 0, 0]) == 0
assert sum_of_values([-3, 8]) == 5
assert sum_of_values([10**9, 10**9]) == 2 * 10**9
```

## 11. Common mistakes

- Forgetting to read `n` before reading `n` values.
- Reading an extra or missing test case.
- Printing prompts instead of only the required output.
- Retaining state between test cases.
- Using `input()` inefficiently for very large input.
- Using `n` as the value count but mistakenly indexing the wrong position.
- Ignoring trailing newlines or whitespace.
- Using `O(n²)` work for an input that should require O(n) or O(n log n).
- Testing only the examples from the statement.
- Returning a Python list instead of the requested string or format.

## Practice checklist

- [ ] Identify the input format
- [ ] Identify the output format
- [ ] Read all constraints and limits
- [ ] Check whether test cases share or reset state
- [ ] Choose the required data types
- [ ] Estimate time and memory at the maximum input size
- [ ] Test minimum, maximum, empty, repeated, and invalid assumptions
- [ ] Match the output exactly

Next: Lesson 4: Dry running code
