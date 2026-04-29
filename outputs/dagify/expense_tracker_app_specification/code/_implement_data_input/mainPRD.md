# _implement_data_input - Complete PRD Documentation

## Overview
PRDs for nodes in the '_implement_data_input' module.

## Table of Contents

- [validate_required_inputs](#validate_required_inputs)

- [synthesize_ui_and_backend_specs](#synthesize_ui_and_backend_specs)

- [derive_client_side_validation_rules](#derive_client_side_validation_rules)

- [generate_form_components_with_validation](#generate_form_components_with_validation)



---

## validate_required_inputs

### Description
Ensures that the provided UI components and database tables inputs are present, correctly typed, and non‑empty.

### Conceptual Info

This shim acts as a gatekeeper before synthesising UI and backend specifications, guaranteeing that the upstream nodes have produced meaningful UI component names and database table definitions.

### Docstring

**Summary:** Validate that required inputs `ui_components` and `db_tables` are present, are lists of strings, and contain at least one element each.

**Parameters:**

- ui_components (list[str]): List of UI component names derived from functional requirements.
- db_tables (list[str]): List of database table identifiers produced by the backend data‑structure node.
**Returns:** str - A short message such as "Validation successful." confirming that both inputs passed all checks.

**Raises:**

- TypeError: If either argument is not a list.
- ValueError: If a list is empty or contains non‑string elements.
**Examples:**

```python
>>> validate_required_inputs(['Dashboard', 'Settings'], ['User', 'Expense'])
'Validation successful.'
```

```python
>>> validate_required_inputs([], ['User'])
ValueError: ui_components must be a non‑empty list of strings
```



---

## synthesize_ui_and_backend_specs

### Description
Generates frontend form specifications and validation rules based on UI components and database schema to facilitate automated UI and backend configuration.

### Conceptual Info

This shim function synthesizes frontend UI form specifications and backend data structure definitions from provided UI components and database schema, enabling automated generation of form layouts and validation rules.

### Docstring

**Summary:** This function takes a list of UI component identifiers and database table definitions to produce a structured list of UI form specifications along with client-side validation rules, facilitating cohesive front-end and back-end implementation.

**Parameters:**

- ui_components (str): A string identifier or description representing the set of UI components and screens to be generated.
- db_tables (str): A string identifier or description representing the database tables and data structures relevant for backend integration.
**Returns:** list of dict - A list containing dictionaries that specify the UI form configurations and associated metadata, including validation rules tailored for each form component.

**Raises:**

- ValueError: Raised if input parameters are missing or contain invalid data formats.
- TypeError: Raised if input parameters are not of expected string type.
**Examples:**

```python
>>> synthesize_ui_and_backend_specs(ui_components='expense_ui', db_tables='ExpenseDB')
[{'form_name': 'ExpenseForm', 'fields': [{'name': 'amount', 'type': 'float', 'validation': {'required': True, 'min': 0}}, {'name': 'category', 'type': 'string', 'validation': {'required': True}}], 'submit_label': 'Add Expense'}, {'form_name': 'ReportFilter', 'fields': [{'name': 'date_range', 'type': 'date', 'validation': {'required': False}}], 'submit_label': 'Generate Report'}]
```

```python
>>> specs = synthesize_ui_and_backend_specs(ui_components='user_management', db_tables='UserDB')
[[{'form_name': 'UserRegistration', 'fields': [{'name': 'username', 'type': 'string', 'validation': {'required': True}}, {'name': 'password', 'type': 'string', 'validation': {'required': True, 'min_length': 8}}], 'submit_label': 'Register'}], [{'form_name': 'UserLogin', 'fields': [{'name': 'username', 'type': 'string', 'validation': {'required': True}}, {'name': 'password', 'type': 'string', 'validation': {'required': True}}], 'submit_label': 'Login'}]]
```



---

## derive_client_side_validation_rules

### Description
Generates client‑side validation rule definitions based on the provided database table specifications.

### Conceptual Info

This shim translates backend data‑model definitions into a set of client‑side validation constraints, enabling UI forms to enforce the same rules as the database without hard‑coding them.

### Docstring

**Summary:** Derive client‑side validation rules from a textual representation of database tables.

**Parameters:**

- db_tables (str): A string describing one or more database tables and their columns, e.g., "Users(id:int,name:str,email:str),Expenses(id:int,amount:float,date:date)".
**Returns:** str - A JSON‑encoded dictionary where each top‑level key is a table name and each value is a mapping of column names to validation rule dictionaries (e.g., type, required, max_length, format).

**Raises:**

- ValueError: If `db_tables` is empty or does not contain any parsable table definitions.
- TypeError: If `db_tables` is not a string.
**Examples:**

```python
>>> derive_client_side_validation_rules('Users(id:int,name:str,email:str)')
'{"Users": {"id": {"type": "int", "required": true}, "name": {"type": "str", "required": true, "max_length": 255}, "email": {"type": "str", "required": true, "format": "email"}}}'
```

```python
>>> derive_client_side_validation_rules('Expenses(id:int,amount:float,date:date)')
'{"Expenses": {"id": {"type": "int", "required": true}, "amount": {"type": "float", "required": true, "min": 0}, "date": {"type": "date", "required": true}}}'
```



---

## generate_form_components_with_validation

### Description
Generates a list of frontend form component code strings from JSON‑encoded form specifications and validation rules.

### Conceptual Info

This shim bridges the UI design and backend data models by turning abstract form specifications and derived validation constraints into concrete, ready‑to‑render form component snippets for the frontend.

### Docstring

**Summary:** Create frontend form component code strings from JSON‑encoded specifications and validation rules.

**Parameters:**

- form_specs (str): A JSON‑encoded list of dictionaries, each describing a form field (e.g., name, type, label, placeholder, options).
- validation_rules (str): A JSON‑encoded dictionary mapping field names to validation constraints such as required, min, max, pattern, etc.
**Returns:** list[str] - A list where each element is a string containing the rendered markup for a single form field, including any validation attributes derived from `validation_rules`.

**Raises:**

- ValueError: Raised when either JSON input cannot be parsed or required keys are missing from the specifications.
- TypeError: Raised when the provided arguments are not of type `str`.
**Examples:**

```python
>>> generate_form_components_with_validation(
...     form_specs='[{"name": "amount", "type": "number", "label": "Amount"}]',
...     validation_rules='{"amount": {"required": true, "min": 0}}'
>>> )
["<input type='number' name='amount' label='Amount' required min='0' />"]
```

```python
>>> generate_form_components_with_validation(
...     form_specs='[{"name": "category", "type": "select", "label": "Category", "options": ["Food", "Travel"]}]',
...     validation_rules='{"category": {"required": true}}'
>>> )
["<select name='category' label='Category' required><option>Food</option><option>Travel</option></select>"]
```

