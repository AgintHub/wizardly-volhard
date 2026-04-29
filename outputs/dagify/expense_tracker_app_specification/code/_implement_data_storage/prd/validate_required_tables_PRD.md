# validate_required_tables PRD

## Description
Validates that the supplied database table list contains all tables required for the application to function correctly.


## Conceptual Info

This shim ensures that the backend data structure defined earlier contains every essential table before any database operations are performed, preventing runtime failures caused by missing schema elements.

## Docstring

### Summary
Validate that the required database tables are present in the provided table list.

### Parameters

- **db_tables** (str): A comma‑separated string of table names supplied by the `set_backend_data_structure` node (e.g., `'Users,Expenses,Categories,Reports'`).

### Returns

str: A confirmation message such as `'All required tables are present.'` when validation succeeds.

### Raises

- ValueError: Raised when one or more of the mandatory tables (`Users`, `Expenses`, `Categories`, `Reports`) are missing from `db_tables`. The error message lists the absent tables.
- TypeError: Raised when `db_tables` is not of type `str`.

### Examples

```python
>>> validate_required_tables('Users,Expenses,Categories,Reports')
'All required tables are present.'
```

```python
>>> validate_required_tables('Users,Expenses')
ValueError: Missing required tables: Categories, Reports
```
