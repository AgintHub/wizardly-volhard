# generate_expenses_table PRD

## Description
Generates the SQL CREATE TABLE statement for the Expenses table based on the supplied core domain identifiers.


## Conceptual Info

This shim creates the database schema for the Expenses entity; it translates high‑level domain information into a concrete SQL CREATE TABLE command that will be incorporated into the overall backend data structure for the expense‑tracker application.

## Docstring

### Summary
Generate the SQL CREATE TABLE statement for the Expenses table using core domain information.

### Parameters

- **domains** (str): A comma‑separated string of core domain identifiers (e.g., "finance,user,category") that influence column selection and naming conventions for the Expenses table.

### Returns

str: A single string containing a valid SQL CREATE TABLE statement for the Expenses table, including appropriate columns, data types, primary keys, foreign keys, and any domain‑driven constraints.

### Raises

- ValueError: If the `domains` string is empty or does not contain any recognized domain keywords required to build the table.
- TypeError: If `domains` is not of type `str`.

### Examples

```python
>>> generate_expenses_table('finance,user,category')
'CREATE TABLE Expenses (expense_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, category_id INTEGER NOT NULL, amount REAL NOT NULL, expense_date DATE NOT NULL, description TEXT, FOREIGN KEY(user_id) REFERENCES Users(user_id), FOREIGN KEY(category_id) REFERENCES Categories(category_id));'
```

```python
>>> generate_expenses_table('finance')
'CREATE TABLE Expenses (expense_id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL NOT NULL, expense_date DATE NOT NULL, description TEXT);'
```
