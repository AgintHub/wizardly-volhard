# generate_form_components_with_validation PRD

## Description
Generates a list of frontend form component code strings from JSON‑encoded form specifications and validation rules.


## Conceptual Info

This shim bridges the UI design and backend data models by turning abstract form specifications and derived validation constraints into concrete, ready‑to‑render form component snippets for the frontend.

## Docstring

### Summary
Create frontend form component code strings from JSON‑encoded specifications and validation rules.

### Parameters

- **form_specs** (str): A JSON‑encoded list of dictionaries, each describing a form field (e.g., name, type, label, placeholder, options).
- **validation_rules** (str): A JSON‑encoded dictionary mapping field names to validation constraints such as required, min, max, pattern, etc.

### Returns

list[str]: A list where each element is a string containing the rendered markup for a single form field, including any validation attributes derived from `validation_rules`.

### Raises

- ValueError: Raised when either JSON input cannot be parsed or required keys are missing from the specifications.
- TypeError: Raised when the provided arguments are not of type `str`.

### Examples

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
