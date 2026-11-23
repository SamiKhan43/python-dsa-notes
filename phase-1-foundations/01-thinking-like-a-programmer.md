# Lesson 1: Thinking Like a Programmer

Programming problems are solved by converting a clear requirement into exact steps.
The goal is not to produce Python immediately. It is to understand the problem,
choose a correct approach, and then improve it.

## 1. Understand the problem

Before writing code, identify:

- **Input:** What data is given?
- **Output:** What must be returned or printed?
- **Rules:** How is the input processed?
- **Constraints:** How large or unusual can the input be?
- **Edge cases:** What happens with empty, repeated, or minimum-sized input?

Restate the problem in simple terms. If it cannot be explained clearly, it is not
yet understood.

### Example

Given a list of numbers and a target, decide whether two different positions in
the list contain values that add to the target.

| Item | Definition |
|---|---|
| Input | A list `nums` and an integer `target` |
| Output | `True` or `False` |
| Rule | The pair must use two different positions |
| Edge case | An empty or single-element list has no valid pair |

## 2. Work through an example

A **dry run** means following the proposed steps manually and recording each
changed value. A correct dry run is the basis of an algorithm.

For `nums = [2, 7, 11, 15]` and `target = 9`:

1. Inspect `2`.
2. Compare it with `7`.
3. Calculate `2 + 7 = 9`.
4. Return `True`.

Dry run a small case and an edge case. Do not rely only on the provided example.

## 3. Develop a brute-force solution

Brute force checks possibilities directly. It is the best starting solution when
the goal is to establish correctness.

```python
def has_pair_with_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False
```

This solution checks every pair. It may be slow, but it is easy to test and reason
about. A slow correct solution is more useful than a fast incorrect solution.

## 4. Find repeated work

Optimization starts with a specific inefficiency. In the brute-force solution,
the nested loops test many pairs more than once.

| Input size `n` | Approximate pairs checked |
|---|---:|
| 10 | 45 |
| 100 | 4,950 |
| 1,000 | 499,500 |

Doubling or tripling the input makes this work grow much faster than the input.
Look for information that could be remembered instead of recalculated.

## 5. Improve the solution

For Pair Sum, store the values already seen. For each value, calculate whether
the matching value was seen earlier.

```python
def has_pair_with_sum(nums, target):
    seen = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)

    return False
```

The set does not replace the original list. It records additional information:
which values have already been visited.

### Why not always use the shortcut

For a problem such as Contains Duplicate, the shortcut
`len(nums) != len(set(nums))` is correct, but it is not always the best choice.

**Shortcut weakness:** it always builds the whole set, so it cannot stop early.
The loop version can stop at the first duplicate.

```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

| Case | Loop version | Shortcut |
|---|---|---|
| Best (duplicate at the start) | Looks at about 2 numbers | Processes all `n` numbers |
| Worst (no duplicates) | Looks at all `n` numbers | Processes all `n` numbers |

Both are O(n), but the loop can never be slower because it can exit early.

## 6. Analyze the solution

### Time complexity

Time complexity describes how the number of operations grows as the input grows.
It does not describe exact execution seconds.

| Pattern | Big O | Growth |
|---|---|---|
| One direct operation | O(1) | Constant |
| One loop | O(n) | Linear |
| One loop inside another loop | O(n²) | Quadratic |

The set solution visits each value once, so it takes O(n) average time.

### Space complexity

Space complexity describes additional memory used as input size grows.
The set solution stores up to `n` values, so it takes O(n) space.

This is a time-space trade-off: extra memory makes the solution faster.

## 7. Test the solution

Test more than one normal example:

```python
assert has_pair_with_sum([2, 7, 11, 15], 9) is True
assert has_pair_with_sum([2, 7, 11, 15], 23) is True
assert has_pair_with_sum([1, 2, 3], 7) is False
assert has_pair_with_sum([], 0) is False
assert has_pair_with_sum([5], 10) is False
assert has_pair_with_sum([3, 3], 6) is True
```

Include:

- A successful case
- An unsuccessful case
- Empty input
- One element
- Repeated values
- The smallest and largest expected values

## 8. Use a repeatable process

1. Read and restate the problem.
2. Identify input, output, constraints, and edge cases.
3. Dry run a small example by hand.
4. Write a brute-force solution.
5. Test it against normal and edge cases.
6. Find the repeated work.
7. Choose a better data structure or algorithm.
8. Explain the time and space complexity.
9. Test the optimized solution again.

## 9. Big O shortcuts

- Remove constants: `n + 100` becomes O(n).
- Keep the fastest-growing term: `n² + n` becomes O(n²).
- Usually estimate the worst case unless the problem specifies otherwise.
- Big O answers “how does work grow?” rather than “how long does it run?”

## Practice checklist

- [ ] Restate the problem
- [ ] Define inputs and outputs
- [ ] List edge cases
- [ ] Dry run an example
- [ ] Write a brute-force solution
- [ ] Verify with tests
- [ ] Identify repeated work
- [ ] Write an optimized solution
- [ ] State time and space complexity

Related: [Contains Duplicate](../problems/contains-duplicate.py)
