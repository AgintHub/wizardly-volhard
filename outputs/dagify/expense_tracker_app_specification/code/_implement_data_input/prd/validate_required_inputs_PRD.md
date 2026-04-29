# validate_required_inputs PRD

## Description
Ensures that the provided UI components and database tables inputs are present, correctly typed, and non‑empty.


## Conceptual Info

This shim acts as a gatekeeper before synthesising UI and backend specifications, guaranteeing that the upstream nodes have produced meaningful UI component names and database table definitions.

## Docstring

### Summary
Validate that required inputs `ui_components` and `db_tables` are present, are lists of strings, and contain at least one element each.

### Parameters

- **ui_components** (list[str]): List of UI component names derived from functional requirements.
- **db_tables** (list[str]): List of database table identifiers produced by the backend data‑structure node.

### Returns

str: A short message such as "Validation successful." confirming that both inputs passed all checks.

### Raises

- TypeError: If either argument is not a list.
- ValueError: If a list is empty or contains non‑string elements.

### Examples

```python
>>> validate_required_inputs(['Dashboard', 'Settings'], ['User', 'Expense'])
'Validation successful.'
```

```python
>>> validate_required_inputs([], ['User'])
ValueError: ui_components must be a non‑empty list of strings
```
