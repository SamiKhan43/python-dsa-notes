# Lesson 4: Dry Running Code

A dry run means executing code by hand, one step at a time, and writing down how each variable changes. This lesson is for beginners who want to find bugs and verify solutions without guessing.

## Quick summary

- A dry run is a table: one row per step, one column per variable you care about.
- Use a tiny input (3 to 4 items), so the table stays short.
- Always add an edge case: empty list, one item, duplicates.
- A dry run shows **how** code behaves. Running it shows only the final output.
- A wrong program can print the right answer by luck, and the table still shows the flaw.
- In Python, `nums[-1]` is the last item, so an off-by-one bug can give no error and a wrong answer.


## 1. How to dry run

1. Pick a tiny input.
2. List the variables that change (loop variable, counters, results).
3. Write one row per loop step. Fill each cell by hand, without running the code.
4. At the end, compare your result with the answer you expect.

Why by hand: if you only run the code, you see the output but not the reasoning. The table forces you to follow what the code really does, not what you assume it does.

## 2. Worked example: find the maximum

```python
def find_max(nums):
    best = nums[0]
    for num in nums:
        if num > best:
            best = num
    return best
```

Dry run with `[3, 9, 4]`:

| step | num | num > best? | best |
|------|-----|-------------|------|
| start | - | - | 3 |
| 1 | 3 | no | 3 |
| 2 | 9 | yes | 9 |
| 3 | 4 | no | 9 |

It returns 9, which is correct. Now the edge case `[]`: the first line, `nums[0]`, raises `IndexError`. The happy-path test missed this, and the edge case found it.

## 3. Worked example: a bug that hides

The goal: count how many numbers are bigger than the number directly before them.

```python
# BUGGY
def count_increases(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
    return count
```

Dry run with `[5, 3, 4]`. The real answer is 1, because only 3 to 4 is an increase.

| i | nums[i] | nums[i-1] | nums[i] > nums[i-1]? | count |
|---|---------|-----------|----------------------|-------|
| 0 | 5 | 4 | yes | 1 |
| 1 | 3 | 5 | no | 1 |
| 2 | 4 | 3 | yes | 2 |

The function returns 2, which is wrong. Row `i = 0` is the cause: `nums[-1]` is the **last** item, so the first item (5) is compared with the last item (4). The first item has nothing before it, so it should never be compared.

The bug only shows when the first item is bigger than the last. For `[1, 2, 3]` the first item is smaller, so the function returns the correct 2 by luck. This is why one passing test proves little.

The fix: start the loop where a left neighbor exists, at index 1.

```python
# FIXED
def count_increases(nums):
    count = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
    return count
```

Dry run of the fixed version with `[5, 3, 4]`:

| i | nums[i] | nums[i-1] | nums[i] > nums[i-1]? | count |
|---|---------|-----------|----------------------|-------|
| 1 | 3 | 5 | no | 0 |
| 2 | 4 | 3 | yes | 1 |

It returns 1, which is correct. For `[]` and `[7]` the loop does not run, so it returns 0.

## 4. When to dry run

- When code gives a wrong answer and you don't know why.
- Before submitting, with a tiny input and an edge case.
- When a bug involves positions versus values (`i` versus `nums[i]`).
- When checking an idea before writing it.

Backend link: tracing a bug through a request handler is the same habit. You follow one value as it changes from step to step.

## 5. Checklist: things to remember

1. Use a tiny input, so the table stays short.
2. One row per step, one column per changing variable.
3. Fill the table by hand, because running the code hides the steps.
4. Always test an edge case (empty, one item, duplicates).
5. Say whether you are using a position (`i`) or a value (`nums[i]`).
6. Remember `nums[-1]` is valid in Python and is the last item.

## 6. Common pitfalls and interview questions

**Pitfalls**

- Dry running only the happy path, so edge-case bugs survive.
- Trusting a correct output from one test. It may be luck.
- Skipping rows, so a mistake hides in the part you skipped.
- Confusing `i` with `nums[i]`.

**Interview questions**

- *Why dry run instead of just running the code?* It shows how the code behaves at each step, so you can find where it goes wrong, even when the output looks right.
- *What does `nums[-1]` do in Python?* It returns the last item. Other languages would raise an error, which is why this bug can be silent.