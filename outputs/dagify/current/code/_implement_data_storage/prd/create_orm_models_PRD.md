# create_orm_models PRD

## Description
Creates ORM model definitions from a string representation of database tables.


## Conceptual Info

This shim converts a plain‑text description of database tables into ORM model metadata, enabling downstream steps to create actual model classes, database tables, and CRUD handlers without hard‑coding schema details.

## Docstring

### Summary
Generate ORM model specifications from a textual table definition.

The function parses `db_tables`, validates its format, and returns a stringified Python dictionary where each key is a table name and each value is a mapping of field names to generic ORM types (e.g., Integer, String, Float). The output can be fed directly to code generators that produce SQLAlchemy or similar ORM classes.

### Parameters

- **db_tables** (str): Newline‑separated table definitions. Each line must follow the pattern `TableName:field1:type1,field2:type2,...` where `type` is one of `int`, `str`, `float`, or `bool`.

### Returns

str: A string representation of a dictionary `{table_name: {field_name: orm_type, ...}, ...}` where `orm_type` is a generic ORM type name (e.g., "Integer", "String", "Float", "Boolean").

### Raises

- ValueError: If any line in `db_tables` does not conform to the required `TableName:field:type` syntax or contains an unsupported field type.
- TypeError: If `db_tables` is not a string.

### Examples

```python
>>> create_orm_models('User:id:int,name:str,email:str\nExpense:id:int,amount:float,user_id:int')
'{'User': {'id': 'Integer', 'name': 'String', 'email': 'String'}, 'Expense': {'id': 'Integer', 'amount': 'Float', 'user_id': 'Integer'}}'
```

```python
>>> create_orm_models('Category:id:int,title:str')
'{'Category': {'id': 'Integer', 'title': 'String'}}'
```
