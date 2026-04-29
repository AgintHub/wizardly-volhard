# generate_users_table PRD

## Description
Generates a SQL CREATE TABLE statement for the Users table based on supplied core domain information.


## Conceptual Info

This shim translates the high‑level business domains identified by the system into a concrete Users table definition, forming part of the overall relational schema for the expense‑tracker application.

## Docstring

### Summary
Generate a SQL `CREATE TABLE` statement for the Users table based on a comma‑separated list of core domains.

### Parameters

- **domains** (str): Comma‑separated list of core domain names (e.g., "users,expenses,categories") derived from the requirements analysis.

### Returns

str: A valid SQL `CREATE TABLE` statement for the Users table, including an integer primary key `id`, columns `username`, `email`, `created_at`, and any additional columns inferred from the provided domains.

### Raises

- ValueError: If the `domains` string is empty or does not contain the required "users" domain.
- TypeError: If `domains` is not of type `str`.

### Examples

```python
>>> generate_users_table('users,expenses,categories')
"CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, email TEXT UNIQUE NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
```

```python
>>> generate_users_table('users')
"CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, email TEXT UNIQUE NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
```
