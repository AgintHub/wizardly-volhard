# create_database_tables PRD

## Description
Creates the physical database tables based on the provided ORM model definitions and returns a status message.


## Conceptual Info

This shim bridges the high‑level data‑model specification and the physical persistence layer by materializing ORM definitions into actual database tables, enabling downstream API generation.

## Docstring

### Summary
Create database tables from ORM model definitions.

The function parses the provided ORM models, issues the necessary DDL statements to the active database connection, and returns a human‑readable status message.

### Parameters

- **orm_models** (str): A string (e.g., JSON) describing the ORM models where each key is a model name and each value is a column‑definition string compatible with the target SQL dialect.

### Returns

str: A message summarising the outcome, such as "Database tables created successfully." or an error description.

### Raises

- ValueError: If `orm_models` cannot be parsed as valid JSON or lacks required model definitions.
- TypeError: If `orm_models` is not a string.
- RuntimeError: If any underlying database operation fails (e.g., syntax error, connection loss).

### Examples

```python
>>> create_database_tables('{"User": "id INTEGER PRIMARY KEY, name TEXT", "Expense": "id INTEGER PRIMARY KEY, amount REAL, user_id INTEGER"}')
"Database tables created successfully."
```

```python
>>> create_database_tables('invalid json')
"ValueError: orm_models string is not valid JSON."
```
