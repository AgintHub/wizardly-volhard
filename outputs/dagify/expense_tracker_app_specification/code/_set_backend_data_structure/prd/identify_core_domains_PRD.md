# identify_core_domains PRD

## Description
Extracts the core domain names from a high‑level functional requirements string.


## Conceptual Info

This shim isolates the business‑level concepts that drive the data model, allowing downstream nodes to generate appropriate database tables based on the identified core domains.

## Docstring

### Summary
Identify core domain names from a textual description of functional requirements.

### Parameters

- **requirements** (str): A single string containing high‑level functional requirements; items may be separated by commas, semicolons, newlines, or the word "and".

### Returns

list[str]: A list of distinct core domain identifiers (lower‑case, whitespace‑trimmed) that were recognized in the input.

### Raises

- ValueError: If the input string is empty or does not contain any recognizable domain keywords.
- TypeError: If the supplied `requirements` argument is not of type `str`.

### Examples

```python
>>> identify_core_domains('Users can register, create expenses, and view reports')
['users', 'expenses', 'reports']
```

```python
>>> identify_core_domains('Manage categories; track expenses; generate summary reports')
['categories', 'expenses', 'reports']
```
