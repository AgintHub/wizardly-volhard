# generate_component_names PRD

## Description
Generates UI component names from requirement‑to‑pattern mappings.


## Conceptual Info

This shim translates the abstract relationship between high‑level functional requirements and their corresponding UI design patterns into concrete component identifiers that can be used downstream for wireframing and code generation.

## Docstring

### Summary
Generate concise UI component names based on requirement‑to‑pattern mappings.

### Parameters

- **mappings** (str): A JSON‑encoded string representing a dictionary where each key is a functional requirement (str) and each value is the associated UI design pattern (str).

### Returns

list[str]: A list of component names derived from the mappings, preserving the order of the input requirements.

### Raises

- ValueError: If the JSON string cannot be parsed or does not represent a dictionary of strings to strings.
- TypeError: If any of the keys or values in the parsed dictionary are not strings.

### Examples

```python
>>> generate_component_names('{"Add expense": "Form", "View report": "Chart"}')
['AddExpenseForm', 'ViewReportChart']
```

```python
>>> generate_component_names('{"Settings": "Modal", "Help": "Drawer"}')
['SettingsModal', 'HelpDrawer']
```
