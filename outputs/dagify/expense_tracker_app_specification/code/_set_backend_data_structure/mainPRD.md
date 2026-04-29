# _set_backend_data_structure - Complete PRD Documentation

## Overview
PRDs for nodes in the '_set_backend_data_structure' module.

## Table of Contents

- [validate_requirements](#validate_requirements)

- [identify_core_domains](#identify_core_domains)

- [generate_users_table](#generate_users_table)

- [generate_categories_table](#generate_categories_table)

- [generate_expenses_table](#generate_expenses_table)

- [generate_reports_table](#generate_reports_table)



---

## validate_requirements

### Description
Validates and normalizes a list of functional requirement strings, ensuring proper formatting, removing duplicates, and raising errors for invalid inputs.

### Conceptual Info

This shim ensures that downstream data‑pipeline stages receive a clean, well‑structured set of functional requirements by enforcing syntactic rules and eliminating redundancies.

### Docstring

**Summary:** Validate and normalize a list of functional requirement strings.

**Parameters:**

- requirements (List[str]): A list of high‑level functional requirement strings produced by the previous node.
**Returns:** List[str] - A cleaned list of requirement strings with leading/trailing whitespace removed and duplicates eliminated.

**Raises:**

- TypeError: If `requirements` is not a list or contains non‑string elements.
- ValueError: If any requirement string is empty after stripping whitespace.
**Examples:**

```python
>>> validate_requirements(['Track expenses', '  Track expenses ', 'Generate reports'])
['Track expenses', 'Generate reports']
```

```python
>>> validate_requirements('Track expenses')
TypeError: requirements must be a list of strings
```



---

## identify_core_domains

### Description
Extracts the core domain names from a high‑level functional requirements string.

### Conceptual Info

This shim isolates the business‑level concepts that drive the data model, allowing downstream nodes to generate appropriate database tables based on the identified core domains.

### Docstring

**Summary:** Identify core domain names from a textual description of functional requirements.

**Parameters:**

- requirements (str): A single string containing high‑level functional requirements; items may be separated by commas, semicolons, newlines, or the word "and".
**Returns:** list[str] - A list of distinct core domain identifiers (lower‑case, whitespace‑trimmed) that were recognized in the input.

**Raises:**

- ValueError: If the input string is empty or does not contain any recognizable domain keywords.
- TypeError: If the supplied `requirements` argument is not of type `str`.
**Examples:**

```python
>>> identify_core_domains('Users can register, create expenses, and view reports')
['users', 'expenses', 'reports']
```

```python
>>> identify_core_domains('Manage categories; track expenses; generate summary reports')
['categories', 'expenses', 'reports']
```



---

## generate_users_table

### Description
Generates a SQL CREATE TABLE statement for the Users table based on supplied core domain information.

### Conceptual Info

This shim translates the high‑level business domains identified by the system into a concrete Users table definition, forming part of the overall relational schema for the expense‑tracker application.

### Docstring

**Summary:** Generate a SQL `CREATE TABLE` statement for the Users table based on a comma‑separated list of core domains.

**Parameters:**

- domains (str): Comma‑separated list of core domain names (e.g., "users,expenses,categories") derived from the requirements analysis.
**Returns:** str - A valid SQL `CREATE TABLE` statement for the Users table, including an integer primary key `id`, columns `username`, `email`, `created_at`, and any additional columns inferred from the provided domains.

**Raises:**

- ValueError: If the `domains` string is empty or does not contain the required "users" domain.
- TypeError: If `domains` is not of type `str`.
**Examples:**

```python
>>> generate_users_table('users,expenses,categories')
"CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, email TEXT UNIQUE NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
```

```python
>>> generate_users_table('users')
"CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, email TEXT UNIQUE NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
```



---

## generate_categories_table

### Description
This shim generates the SQL command string for creating a categories table based on core domains derived from functional requirements.

### Conceptual Info

The generate_categories_table shim constructs the SQL statement for creating a categories table tailored to the application's core domains, facilitating database setup.

### Docstring

**Summary:** Generates an SQL command string for creating a categories table based on specified core domains.

**Parameters:**

- domains (str): A comma-separated string of core domain names that influence the table structure.
**Returns:** str - An SQL command string for creating the categories table, customized for the provided core domains.

**Raises:**

- ValueError: Raised if 'domains' is empty or not a valid string representing core domains.
- TypeError: Raised if 'domains' is not of type str.
**Examples:**

```python
>>> generate_categories_table('finance,budget')
'CREATE TABLE IF NOT EXISTS Categories (id INTEGER PRIMARY KEY, name TEXT, domain TEXT);'
```

```python
>>> generate_categories_table('personal,work')
'CREATE TABLE IF NOT EXISTS Categories (id INTEGER PRIMARY KEY, name TEXT, domain TEXT);'
```



---

## generate_expenses_table

### Description
Generates the SQL CREATE TABLE statement for the Expenses table based on the supplied core domain identifiers.

### Conceptual Info

This shim creates the database schema for the Expenses entity; it translates high‑level domain information into a concrete SQL CREATE TABLE command that will be incorporated into the overall backend data structure for the expense‑tracker application.

### Docstring

**Summary:** Generate the SQL CREATE TABLE statement for the Expenses table using core domain information.

**Parameters:**

- domains (str): A comma‑separated string of core domain identifiers (e.g., "finance,user,category") that influence column selection and naming conventions for the Expenses table.
**Returns:** str - A single string containing a valid SQL CREATE TABLE statement for the Expenses table, including appropriate columns, data types, primary keys, foreign keys, and any domain‑driven constraints.

**Raises:**

- ValueError: If the `domains` string is empty or does not contain any recognized domain keywords required to build the table.
- TypeError: If `domains` is not of type `str`.
**Examples:**

```python
>>> generate_expenses_table('finance,user,category')
'CREATE TABLE Expenses (expense_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, category_id INTEGER NOT NULL, amount REAL NOT NULL, expense_date DATE NOT NULL, description TEXT, FOREIGN KEY(user_id) REFERENCES Users(user_id), FOREIGN KEY(category_id) REFERENCES Categories(category_id));'
```

```python
>>> generate_expenses_table('finance')
'CREATE TABLE Expenses (expense_id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL NOT NULL, expense_date DATE NOT NULL, description TEXT);'
```



---

## generate_reports_table

### Description
Generates the SQL statement to create the Reports table based on core domain identifiers.

### Conceptual Info

This shim produces the database schema definition for the Reports table, linking it to other core domain tables identified earlier in the pipeline, enabling downstream code to create the necessary reporting infrastructure.

### Docstring

**Summary:** Create the SQL statement for the Reports table based on identified core domains.

**Parameters:**

- domains (str): A comma‑separated string of core domain names (e.g., "Users,Expenses,Categories") that the Reports table should reference.
**Returns:** str - A valid SQL CREATE TABLE statement defining the Reports table with appropriate columns and foreign‑key constraints to the supplied domains.

**Raises:**

- ValueError: If the domains string is empty or does not contain any recognizable core domain.
- TypeError: If the provided `domains` argument is not of type `str`.
**Examples:**

```python
>>> generate_reports_table('Users,Expenses,Categories')
"CREATE TABLE Reports (\n    report_id SERIAL PRIMARY KEY,\n    user_id INTEGER NOT NULL,\n    expense_id INTEGER NOT NULL,\n    category_id INTEGER NOT NULL,\n    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n    FOREIGN KEY (user_id) REFERENCES Users(user_id),\n    FOREIGN KEY (expense_id) REFERENCES Expenses(expense_id),\n    FOREIGN KEY (category_id) REFERENCES Categories(category_id)\n);"
```

```python
>>> generate_reports_table('Users')
"CREATE TABLE Reports (\n    report_id SERIAL PRIMARY KEY,\n    user_id INTEGER NOT NULL,\n    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n    FOREIGN KEY (user_id) REFERENCES Users(user_id)\n);"
```

