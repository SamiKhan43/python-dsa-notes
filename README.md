# DSA Python Journey

My learning log for Data Structures and Algorithms in Python. The goal is not to finish a roadmap. The goal is to be able to look at an unfamiliar problem, understand it, pick an approach, write the solution on my own, analyze its efficiency, and improve it. Long term, I am preparing to work as a backend engineer.

---

## How I study

For every topic I follow the same loop:

1. Learn the concept: what it is, why it exists, how it works.
2. Write the note **in my own words**, from memory.
3. Solve one problem on my own: understand, dry run, brute force, analyze, optimize, test edge cases.
4. Commit with a clear message.

## Progress

### Phase 1: Problem-solving foundations

- [x] [Lesson 1: Thinking like a programmer](phase-1-foundations/01-thinking-like-a-programmer.md)
- [ ] [Lesson 2: Analyzing loops and reading constraints](phase-1-foundations/02-analyzing-loops-and-reading-constraints.md)
- [ ] [Lesson 3: Understanding input, output, and constraints](phase-1-foundations/03-understanding-input-output-and-constraints.md)
- [ ] Lesson 4: Dry running code
- [ ] Lesson 5: Big O and analyzing loops
- [ ] Lesson 6: Space complexity
- [ ] Lesson 7: Comparing solutions

### Phase 2: Fundamental data structures

- [ ] Arrays and lists, strings, hashing, dictionaries and sets
- [ ] Frequency counting, prefix sums, two pointers, sliding window
- [ ] Stacks, queues and deques, linked lists

### Phase 3: Essential algorithms

- [ ] Linear and binary search, sorting, recursion, backtracking, greedy

### Phase 4: Trees and graphs

- [ ] Trees, BST, traversals, heaps, tries, graphs, BFS, DFS, topological sort, shortest paths

### Phase 5: Advanced problem-solving

- [ ] Dynamic programming, divide and conquer, Union Find, monotonic stacks, bit manipulation

## Problems solved

| Problem | Concepts | Best time | Best space | File |
|---|---|---|---|---|
| Contains Duplicate | brute force, sets, trade-offs | O(n) | O(n) | [contains-duplicate.py](problems/contains-duplicate.py) |
| Pair Sum | brute force, hash set, complements | O(n) | O(n) | [Two-Sum-problem.py](problems/Two-Sum-problem.py) |

## Repository structure

```
python-dsa-notes/
├── README.md
├── phase-1-foundations/
│   ├── 01-thinking-like-a-programmer.md
│   ├── 02-analyzing-loops-and-reading-constraints.md
│   └── 03-understanding-input-output-and-constraints.md
├── docs/
│   ├── 01-python-basics.md
│   ├── 02-python-conditions-and-loops.md
│   └── 03-python-data-structures.md
└── problems/
    └── contains-duplicate.py
```