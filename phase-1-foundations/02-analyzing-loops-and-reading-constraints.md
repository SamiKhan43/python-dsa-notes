# Lesson 2: Analyzing Loops and Reading Constraints

Constraints describe the size and shape of valid inputs. They help determine
whether an algorithm will finish in time. To use them, estimate how many times
the important parts of the code run.

## 1. Read the constraints first

Look for limits such as:

- The number of items, often written as `n`
- The range of values
- Whether values can repeat
- Whether the input is sorted
- The number of test cases

These details affect both correctness and performance. For example, an algorithm
that checks every pair may work for a list of 100 items but be too slow for
100,000 items.

## 2. Count loop iterations

The number of iterations matters more than the exact statements inside the loop.

### One loop

```python
for item in items:
    process(item)
```

If `items` has `n` elements, the body runs `n` times. The work grows linearly:
O(n).

### Nested loops

```python
for i in range(n):
    for j in range(n):
        process(i, j)
```

For each of the `n` outer iterations, the inner loop runs `n` times. The body
runs `n * n` times, or O(n²).

If `n = 1,000`, that is about one million iterations.

### A loop over pairs

```python
for i in range(n):
    for j in range(i + 1, n):
        process(i, j)
```

The inner loop gets shorter each time. The total is
`(n - 1) + (n - 2) + ... + 1`, which equals `n * (n - 1) / 2`.
This is still O(n²).

### Sequential loops

```python
for item in items:
    process(item)

for item in items:
    process_again(item)
```

Each loop runs `n` times, so the total is `2n`. Drop the constant: O(n), not
O(n²).

### A loop that halves or doubles

```python
value = n
while value > 1:
    value //= 2
```

The value halves each time, so the loop runs about `log₂(n)` times: O(log n).
The same growth occurs when a counter starts at 1 and doubles until it reaches
`n`.

## 3. Match the estimate to the constraints

Use the input limit to estimate the work of a candidate solution:

| Input size | O(n) work | O(n²) work |
|---:|---:|---:|
| 100 | 100 | 10,000 |
| 1,000 | 1,000 | 1,000,000 |
| 100,000 | 100,000 | 10,000,000,000 |

This table is a rough comparison, not a time guarantee. Actual runtime depends
on the operations, language, hardware, and time limit. Still, it makes clear why
a nested-loop solution is risky for very large `n`.

For multiple test cases, include all cases in the estimate. If there are `t`
cases and each case processes `n` items, total linear work is O(t * n).

## 4. Use constraints to choose an approach

Consider checking every pair to find whether two values add to a target:

```python
for i in range(n):
    for j in range(i + 1, n):
        if values[i] + values[j] == target:
            return True
```

This takes O(n²) time. At `n = 100,000`, it may inspect about five billion
pairs, so it is likely too slow. A method that remembers previously seen values
can solve the same task in O(n) average time, using O(n) extra space.

The decision process is:

1. Find the largest possible input size.
2. Count the operations the candidate algorithm performs.
3. Estimate the work at that maximum size.
4. If the estimate is too large, look for repeated work or a better algorithm.
5. Remember that memory limits and operation costs matter too.

## 5. Common counting mistakes

- **Treating all nested loops as O(n²):** check each loop's range. A loop that
  halves its value is logarithmic, not linear.
- **Multiplying sequential loops:** loops one after another add their work; they
  do not multiply it.
- **Ignoring changing bounds:** a pair loop may do fewer operations than `n²`,
  but still has O(n²) growth.
- **Ignoring early exits:** an early `return` can make some inputs finish
  sooner, but estimate the worst case unless asked for another case.
- **Ignoring test cases:** multiply the per-case work by the number of cases.
- **Assuming the example is the maximum:** use the stated constraints instead.

## Practice checklist

- [ ] Identify the maximum input size and number of test cases
- [ ] Write down how many times each loop can run
- [ ] Add work for sequential sections and multiply work for nested sections
- [ ] Check whether loop bounds change, halve, or double
- [ ] Estimate operations at the maximum input size
- [ ] Decide whether the time and memory use are reasonable

Next: Lesson 3: Understanding input, output, and constraints in depth
