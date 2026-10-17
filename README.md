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

## Day 05 — NumPy (`day-05-numpy/`)

### What's covered

| # | Topic | Status |
|---|-------|--------|
| 1 | NumPy vs Python lists — `np.array` | ✅ Complete |
| 2 | Array dimensions — 0D, 1D, 2D, 3D and `.shape` | ✅ Complete |
| 3 | Array properties — `ndim`, `shape`, `size`, `dtype` | ✅ Complete |
| 4 | Indexing — 1D / 2D / 3D, negative indexing | ✅ Complete |
| 5 | Slicing (`arr[1:5]`, `arr[4:]`, `arr[:4]`) | ✅ Complete |
| 6 | Data types — `dtype='S'`, `dtype='i4'` | ✅ Complete |
| 7 | Copy vs view — `copy()`, `view()` | ✅ Complete |
| 8 | Reshaping & iterating (`reshape`, `for` loops) | ✅ Complete |
| 9 | Joining & splitting — `concatenate`, `array_split`, `axis` | ✅ Complete |
| 10 | Searching, sorting, filtering — `where`, `sort`, boolean masks | ✅ Complete |
| 11 | Task 3 — matrix indexing & mathematical/statistical operations | ✅ Complete |

### Files

- `day-05-numpy/num_py.py` — runnable script covering all of the above.
- `day-05-numpy/Task_3/num_py_operations.py` — 3×3 matrix demo: properties, indexing,
  slicing, arithmetic, `sum`/`mean`/`max`/`min`, row/column sums, and `arr[arr > 50]` filtering.

### Run it

```bash
python day-05-numpy/num_py.py
python day-05-numpy/Task_3/num_py_operations.py
```

> Requires `numpy` (`pip install numpy`).

## Day 06 — Pandas (`day-06-pandas/`)

### What's covered

| # | Topic | Status |
|---|-------|--------|
| 1 | Series — plain and with a custom index | ✅ Complete |
| 2 | DataFrame creation from a dictionary | ✅ Complete |
| 3 | Useful commands — `head`, `tail`, `shape`, `columns`, `info`, `describe` | ✅ Complete |
| 4 | Filtering — single and combined boolean conditions | ✅ Complete |
| 5 | Sorting — `sort_values` | ✅ Complete |
| 6 | Missing values — `isnull`, `isnull().sum()`, `dropna`, `fillna` (mean & constant) | ✅ Complete |
| 7 | Task 4 — cleaning a real clinical-trials CSV | ✅ Complete |

### Files

- `day-06-pandas/panda_s.py` — runnable script covering all of the above.
- `day-06-pandas/Task_4/dataset_cleaning.py` — cleaning pipeline: normalizes blank /
  placeholder strings to `NA`, median-fills numeric columns, fills categoricals with
  `"Unknown"`, verifies nothing is left missing, then writes the cleaned CSV and a
  before/after missing-values chart.
- `day-06-pandas/Task_4/clinical_trials_2025_2026.csv` — raw dataset.
- `day-06-pandas/Task_4/clinical_trials_2025_2026_cleaned.csv` — cleaned output.
- `day-06-pandas/Task_4/missing_values_before_after.png` — before/after comparison plot.

### Run it

```bash
python day-06-pandas/panda_s.py
python day-06-pandas/Task_4/dataset_cleaning.py
```

> Requires `pandas` and `matplotlib` (`pip install pandas matplotlib`). Task 4 uses
> script-relative paths, so it can be run from any directory.

## Day 07 — Matplotlib, Seaborn & CSV Analysis (`day-07-visualization-tensorflow/`)

### What's covered

| # | Topic | Status |
|---|-------|--------|
| 1 | Matplotlib — bar chart with `title`, `xlabel`, `ylabel`, `show` | ✅ Complete |
| 2 | Seaborn — `sns.barplot` on the same data | ✅ Complete |
| 3 | Task 5 — load a messy CSV, inspect with `head`/`shape`/`info`/`describe` | ✅ Complete |
| 4 | Cleaning — strip column whitespace, title-case categories, coerce `$`-prefixed numerics | ✅ Complete |
| 5 | Data quality — missing values, duplicates, invalid quantities/prices | ✅ Complete |
| 6 | Derived totals — `Quantity * Price` for valid rows only | ✅ Complete |
| 7 | Charts — orders by status, average price by category, missing values, correlation heatmap | ✅ Complete |

### Files

- `day-07-visualization-tensorflow/ploting.py` — Matplotlib and Seaborn bar-chart examples.
- `day-07-visualization-tensorflow/Task_5/csv_visualization.py` — full CSV analysis pipeline.
- `day-07-visualization-tensorflow/Task_5/messy_ecommerce_sales_data.csv` — raw input dataset.
- `day-07-visualization-tensorflow/Task_5/ecommerce_analyzed.csv` — analysis-ready output.
- `day-07-visualization-tensorflow/Task_5/orders_by_status.png`, `average_price_by_category.png`,
  `missing_values.png`, `correlation_heatmap.png` — generated charts.

### Run it

```bash
python day-07-visualization-tensorflow/ploting.py

cd day-07-visualization-tensorflow/Task_5
python csv_visualization.py   # opens each chart in a window; also saved as PNG
```

> Requires `pandas`, `matplotlib`, and `seaborn`. `Task_5` reads its CSV with a relative
> path, so run it from inside the `Task_5` folder.

## Progress — Week 1 Plan

| Day | Topics | Folder | Status |
|-----|--------|--------|--------|
| Day 1 | Python syntax, variables, data types, operators, input/output | `day-01-python-basics` | ✅ Complete |
| Day 2 | Conditions, loops, `range()`, functions | `day-02-control-flow-functions` | ✅ Complete |
| Day 3 | Lists, tuples, dictionaries, sets | `day-03-data-structures` | ✅ Complete |
| Day 4 | File handling, exceptions, modules, basic OOP | `day-04-files-oop` | ✅ Complete |
| Day 5 | NumPy: arrays, indexing, mathematical operations | `day-05-numpy` | ✅ Complete |
| Day 6 | Pandas: Series, DataFrames, filtering, sorting, missing values | `day-06-pandas` | ✅ Complete |
| Day 7 | Matplotlib, Seaborn, TensorFlow intro, CSV analysis task | `day-07-visualization-tensorflow` | ✅ Complete |

All 7 days of Week 1 are complete. 🎉
