# set_backend_data_structure PRD

## Description
Define the database schema or data models for users, expenses, categories, and reports.


## Conceptual Info

This node converts high‑level functional requirements into concrete database table definitions (SQL DDL statements or ORM model classes) for the core entities of the expense tracker: Users, Expenses, Categories, and Reports. It establishes column types, primary/foreign keys, and necessary constraints to support CRUD operations and reporting.

## Docstring

### Summary
Generate database schema definitions for the expense‑tracker backend based on functional requirements.

### Parameters

- **requirements** (List[str]): High‑level functional requirements produced by the `define_app_functionality_requirements` node.

### Returns

List[str]: A list of strings, each containing a CREATE TABLE statement (or equivalent ORM model) for Users, Expenses, Categories, and Reports.

### Raises

- ValueError: If the `requirements` list is empty or None.
- SchemaGenerationError: If a requirement cannot be mapped to a concrete table or column definition.

### Examples

```python
>>> define_backend_schema([
...     'User registration and authentication',
...     'Expense entry, editing and deletion',
...     'Expense categorization',
...     'Summary reports by period and category'
>>> ])
["CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL, email TEXT);",
 "CREATE TABLE categories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, user_id INTEGER NOT NULL, FOREIGN KEY(user_id) REFERENCES users(id));",
 "CREATE TABLE expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL NOT NULL, date DATE NOT NULL, description TEXT, category_id INTEGER NOT NULL, user_id INTEGER NOT NULL, FOREIGN KEY(category_id) REFERENCES categories(id), FOREIGN KEY(user_id) REFERENCES users(id));",
 "CREATE TABLE reports (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, report_type TEXT NOT NULL, generated_at DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(user_id) REFERENCES users(id));"]
```

```python
>>> define_backend_schema(['User can set a monthly spending limit'])
["CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL, email TEXT, monthly_limit REAL);"]
```
