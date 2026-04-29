# generate_reports_table PRD

## Description
Generates the SQL statement to create the Reports table based on core domain identifiers.


## Conceptual Info

This shim produces the database schema definition for the Reports table, linking it to other core domain tables identified earlier in the pipeline, enabling downstream code to create the necessary reporting infrastructure.

## Docstring

### Summary
Create the SQL statement for the Reports table based on identified core domains.

### Parameters

- **domains** (str): A comma‑separated string of core domain names (e.g., "Users,Expenses,Categories") that the Reports table should reference.

### Returns

str: A valid SQL CREATE TABLE statement defining the Reports table with appropriate columns and foreign‑key constraints to the supplied domains.

### Raises

- ValueError: If the domains string is empty or does not contain any recognizable core domain.
- TypeError: If the provided `domains` argument is not of type `str`.

### Examples

```python
>>> generate_reports_table('Users,Expenses,Categories')
"CREATE TABLE Reports (\n    report_id SERIAL PRIMARY KEY,\n    user_id INTEGER NOT NULL,\n    expense_id INTEGER NOT NULL,\n    category_id INTEGER NOT NULL,\n    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n    FOREIGN KEY (user_id) REFERENCES Users(user_id),\n    FOREIGN KEY (expense_id) REFERENCES Expenses(expense_id),\n    FOREIGN KEY (category_id) REFERENCES Categories(category_id)\n);"
```

```python
>>> generate_reports_table('Users')
"CREATE TABLE Reports (\n    report_id SERIAL PRIMARY KEY,\n    user_id INTEGER NOT NULL,\n    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n    FOREIGN KEY (user_id) REFERENCES Users(user_id)\n);"
```
