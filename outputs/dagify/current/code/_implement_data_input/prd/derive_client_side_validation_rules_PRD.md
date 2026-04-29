# derive_client_side_validation_rules PRD

## Description
Generates client‑side validation rule definitions based on the provided database table specifications.


## Conceptual Info

This shim translates backend data‑model definitions into a set of client‑side validation constraints, enabling UI forms to enforce the same rules as the database without hard‑coding them.

## Docstring

### Summary
Derive client‑side validation rules from a textual representation of database tables.

### Parameters

- **db_tables** (str): A string describing one or more database tables and their columns, e.g., "Users(id:int,name:str,email:str),Expenses(id:int,amount:float,date:date)".

### Returns

str: A JSON‑encoded dictionary where each top‑level key is a table name and each value is a mapping of column names to validation rule dictionaries (e.g., type, required, max_length, format).

### Raises

- ValueError: If `db_tables` is empty or does not contain any parsable table definitions.
- TypeError: If `db_tables` is not a string.

### Examples

```python
>>> derive_client_side_validation_rules('Users(id:int,name:str,email:str)')
'{"Users": {"id": {"type": "int", "required": true}, "name": {"type": "str", "required": true, "max_length": 255}, "email": {"type": "str", "required": true, "format": "email"}}}'
```

```python
>>> derive_client_side_validation_rules('Expenses(id:int,amount:float,date:date)')
'{"Expenses": {"id": {"type": "int", "required": true}, "amount": {"type": "float", "required": true, "min": 0}, "date": {"type": "date", "required": true}}}'
```
