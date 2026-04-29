# generate_crud_operation_tests PRD

## Description
Generates a list of CRUD operation test identifiers based on provided backend API endpoint definitions.


## Conceptual Info

This shim creates the CRUD‑operation test suite required for validating backend API endpoints; it translates endpoint definitions into standardized test identifiers that can be later used by the testing framework.

## Docstring

### Summary
Generate CRUD operation test identifiers from a string of API endpoint definitions.

### Parameters

- **api_endpoints** (str): A single string containing one or more API endpoint paths, separated by commas (e.g., "/expenses,/users").

### Returns

List[str]: A list of test case identifiers for create, read, update, and delete actions for each endpoint, formatted as "test_<action>_<resource>".

### Raises

- ValueError: If the input string is empty or does not contain any valid endpoint paths.
- TypeError: If the provided api_endpoints argument is not of type str.

### Examples

```python
>>> generate_crud_operation_tests('/expenses,/users')
['test_create_expense', 'test_read_expense', 'test_update_expense', 'test_delete_expense', 'test_create_user', 'test_read_user', 'test_update_user', 'test_delete_user']
```

```python
>>> generate_crud_operation_tests('/reports')
['test_create_report', 'test_read_report', 'test_update_report', 'test_delete_report']
```
