# set_backend_data_structure PRD

## Description
Define the database schema or data models for users, expenses, categories, and reports.


## Conceptual Info

Creates a relational database schema for the expense‑tracker application based on the high‑level functional requirements. It defines the Users, Expenses, Categories, and Reports tables, their columns, data types, primary/foreign keys, and inter‑table relationships, returning ready‑to‑execute CREATE TABLE statements.

## Docstring

### Summary
Generates SQL CREATE TABLE statements for the core data model of the expense‑tracker app from functional requirements.

### Parameters

- **requirements** (List[str]): High‑level functional requirements produced by the define_app_functionality_requirements node.

### Returns

List[str]: SQL CREATE TABLE statements (as strings) for Users, Expenses, Categories, and Reports.

### Raises

- ValueError: If the requirements list is empty or lacks any core domain needed to infer the schema.

### Examples

```python
>>> generate_schema(['User authentication', 'Expense entry', 'Reporting'])
["CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password_hash TEXT NOT NULL);", "CREATE TABLE Categories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);", "CREATE TABLE Expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, category_id INTEGER NOT NULL, amount REAL NOT NULL, date TEXT NOT NULL, description TEXT, FOREIGN KEY(user_id) REFERENCES Users(id), FOREIGN KEY(category_id) REFERENCES Categories(id));", "CREATE TABLE Reports (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, report_type TEXT NOT NULL, generated_at TEXT NOT NULL, FOREIGN KEY(user_id) REFERENCES Users(id));"]
```

```python
>>> generate_schema([])
ValueError: Requirements list cannot be empty.
```
