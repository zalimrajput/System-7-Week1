# System-7 — Week 1

A week-wise record of my Python learning journey.

## Day 01 — Python Basics (`day-01-python-basics/`)

### What's covered

| # | Topic | Status |
|---|-------|--------|
| 1 | Variables & Data Types (str, int, float, bool) | ✅ Complete |
| 2 | Checking types with `type()` | ✅ Complete |
| 3 | Operators (arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`) | ✅ Complete |
| 4 | User Input & Output (`input()`, type conversion) | ✅ Complete |
| 5 | Simple calculator (sum & product of two numbers) | ✅ Complete |

### Files

- `day-01-python-basics/basics.py` — runnable script covering all of the above.

### Run it

```bash
python day-01-python-basics/basics.py
```

The script prints the variables and their data types, shows operator results, then prompts
for your name, age, and two numbers to calculate.

## Day 02 — Control Flow & Functions (`day-02-control-flow-functions/`)

### What's covered

| # | Topic | Status |
|---|-------|--------|
| 1 | Conditions (`if`, `else`, `elif`) | ✅ Complete |
| 2 | Loops (`for`, `while`) | ✅ Complete |
| 3 | Loop control (`break`, `continue`) | ✅ Complete |
| 4 | `range()` — with start/end, step, and reverse | ✅ Complete |
| 5 | Functions — no params, with params, and `return` | ✅ Complete |
| 6 | Combining conditions, loops, and functions | ✅ Complete |

### Files

- `day-02-control-flow-functions/loops.py` — runnable script covering all of the above.
- `day-02-control-flow-functions/Task_1/calculator.py` — interactive calculator using functions and `match`/`case`.
- `day-02-control-flow-functions/Task_1/num_guessing_game.py` — number guessing game (1–100) with attempt counting.

### Run it

```bash
python day-02-control-flow-functions/loops.py
python day-02-control-flow-functions/Task_1/calculator.py
python day-02-control-flow-functions/Task_1/num_guessing_game.py
```

`loops.py` prints condition, loop, `range()`, and function examples. The calculator prompts
for an operation and two numbers (type `end` to exit), and the guessing game asks you to
guess a secret number until you get it or type `end`.

## Day 03 — Data Structures (`day-03-data-structures/`)

### What's covered

| # | Topic | Status |
|---|-------|--------|
| 1 | Lists — `append`, `extend`, `insert`, `remove`, `pop`, `clear`, `index`, `count`, `sort`, `reverse`, `copy` | ✅ Complete |
| 2 | List operations — `len`, `max`, `min`, `sum`, `sorted`, `in`, indexing & slicing | ✅ Complete |
| 3 | Tuples — `count`, `index`, and read-only operations | ✅ Complete |
| 4 | Dictionaries — `keys`, `values`, `items`, `get`, `update`, `pop`, `popitem`, `setdefault`, `copy`, `clear`, `dict.fromkeys` | ✅ Complete |
| 5 | Sets — `add`, `update`, `remove`, `discard`, `pop`, `clear` | ✅ Complete |
| 6 | Set math — `union`, `intersection`, `difference`, `symmetric_difference`, `issubset`, `issuperset`, `isdisjoint`, `intersection_update` | ✅ Complete |

### Files

- `day-03-data-structures/data_structures.py` — runnable script covering all of the above.

### Run it

```bash
python day-03-data-structures/data_structures.py
```

The script prints a labelled section for every method and operation, so you can see exactly
what each one does to the sample data.

## Day 04 — Files, Exceptions, Modules & OOP (`day-04-files-oop/`)

### What's covered

| # | Topic | Status |
|---|-------|--------|
| 1 | File handling — opening modes (`r`, `w`, `a`), `with` statement, `read`, `read(n)`, `readline`, `readlines`, `write` | ✅ Complete |
| 2 | Exception handling — `try` / `except` / `else` / `finally` | ✅ Complete |
| 3 | Built-in modules — `math`, `random`, `datetime` | ✅ Complete |
| 4 | Basic OOP — classes, `__init__`, methods, modifying object properties | ✅ Complete |
| 5 | Inheritance, polymorphism, encapsulation (public / protected / private) | ✅ Complete |
| 6 | Task 2 — small OOP projects (bank account, library, student records) | ✅ Complete |

### Files

- `day-04-files-oop/advanced_operations.py` — runnable script covering all of the above.
- `day-04-files-oop/demofile.txt`, `day-04-files-oop/data.txt` — sample files the script reads and writes.
- `day-04-files-oop/Task_2/bank_account.py` — `BankAccount` class with deposit, withdraw, and balance check (private `__balance`).
- `day-04-files-oop/Task_2/library.py` — `Library` class with add, show, borrow, and return book.
- `day-04-files-oop/Task_2/student_record.py` — menu-driven student record manager persisted to `students.json` (add / show / search).

### Run it

```bash
cd day-04-files-oop
python advanced_operations.py   # prompts for two numbers in the exception-handling demo

cd Task_2
python bank_account.py
python library.py
python student_record.py       # interactive menu, choose 4 to exit
```

> Note: the scripts use relative file paths, so run each one from its own folder.
> `advanced_operations.py` deliberately accesses a private attribute (`print(p1.__age)`) in the
> encapsulation demo and ends with an `AttributeError` — that is the teaching example, and the
> two demos after that line never run.

## Progress — Week 1 Plan

| Day | Topics | Folder | Status |
|-----|--------|--------|--------|
| Day 1 | Python syntax, variables, data types, operators, input/output | `day-01-python-basics` | ✅ Complete |
| Day 2 | Conditions, loops, `range()`, functions | `day-02-control-flow-functions` | ✅ Complete |
| Day 3 | Lists, tuples, dictionaries, sets | `day-03-data-structures` | ✅ Complete |
| Day 4 | File handling, exceptions, modules, basic OOP | `day-04-files-oop` | ✅ Complete |
| Day 5 | NumPy: arrays, indexing, mathematical operations | `day-05-numpy` | ⬜ Pending |
| Day 6 | Pandas: Series, DataFrames, filtering, sorting, missing values | `day-06-pandas` | ⬜ Pending |
| Day 7 | Matplotlib, Seaborn, TensorFlow intro, CSV analysis task | `day-07-visualization-tensorflow` | ⬜ Pending |
