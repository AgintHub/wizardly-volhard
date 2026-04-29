# _design_ui_components - Complete PRD Documentation

## Overview
PRDs for nodes in the '_design_ui_components' module.

## Table of Contents

- [validate_requirements_input](#validate_requirements_input)

- [map_requirements_to_ui_patterns](#map_requirements_to_ui_patterns)

- [generate_component_names](#generate_component_names)

- [create_wireframe_descriptions](#create_wireframe_descriptions)

- [finalize_ui_components](#finalize_ui_components)



---

## validate_requirements_input

### Description
Validates and normalizes a list of functional requirement strings, returning a cleaned list ready for downstream processing.

### Conceptual Info

This shim acts as a gatekeeper for the requirements pipeline, guaranteeing that the functional requirements passed from the DefineAppFunctionalityRequirements node are well‑formed, unique, and consistently formatted before they are mapped to UI patterns.

### Docstring

**Summary:** Validate and normalise a collection of functional requirement strings.

**Parameters:**

- requirements (list[str]): A list of raw requirement strings produced by the previous node. Each string may contain leading/trailing whitespace, inconsistent capitalisation, or duplicates.
**Returns:** list[str] - A cleaned list where each requirement is stripped of surrounding whitespace, capitalised, non‑empty, and unique while preserving the original order of first occurrence.

**Raises:**

- ValueError: If any element is not a string, is empty after stripping, or if duplicate requirements are detected.
- TypeError: If the supplied `requirements` argument is not iterable or not a list of strings.
**Examples:**

```python
>>> validate_requirements_input(['track expenses', 'view reports'])
['Track expenses', 'View reports']
```

```python
>>> validate_requirements_input(['  add expense  ', 'Add Expense', ''])
ValueError: Requirements must be non‑empty strings and unique.
```



---

## map_requirements_to_ui_patterns

### Description
Maps a list of validated functional requirements to appropriate UI design pattern names and returns the mapping as a JSON‑encoded string.

### Conceptual Info

This shim bridges the gap between high‑level functional specifications and concrete UI design patterns, enabling downstream components to generate component names, wireframes, and final UI artifacts.

### Docstring

**Summary:** Convert validated functional requirements into a mapping of UI design patterns, returning the result as a JSON‑encoded string.

**Parameters:**

- requirements (str): A JSON‑encoded list of validated requirement strings (e.g., '["Add expense", "View report"]').
**Returns:** str - A JSON‑encoded dictionary mapping each requirement to a list of UI pattern names (e.g., '{"Add expense": ["Form", "Button"], "View report": ["Chart", "Table"]}').

**Raises:**

- ValueError: If the input JSON cannot be parsed or does not represent a list of strings.
- TypeError: If the parsed object is not a list or contains non‑string elements.
**Examples:**

```python
>>> map_requirements_to_ui_patterns('["Add expense", "View report"]')
'{"Add expense": ["Form", "Button"], "View report": ["Chart", "Table"]}'
```

```python
>>> map_requirements_to_ui_patterns('["Sync data", "Export CSV"]')
'{"Sync data": ["Toggle", "ProgressBar"], "Export CSV": ["Button", "Dialog"]}'
```



---

## generate_component_names

### Description
Generates UI component names from requirement‑to‑pattern mappings.

### Conceptual Info

This shim translates the abstract relationship between high‑level functional requirements and their corresponding UI design patterns into concrete component identifiers that can be used downstream for wireframing and code generation.

### Docstring

**Summary:** Generate concise UI component names based on requirement‑to‑pattern mappings.

**Parameters:**

- mappings (str): A JSON‑encoded string representing a dictionary where each key is a functional requirement (str) and each value is the associated UI design pattern (str).
**Returns:** list[str] - A list of component names derived from the mappings, preserving the order of the input requirements.

**Raises:**

- ValueError: If the JSON string cannot be parsed or does not represent a dictionary of strings to strings.
- TypeError: If any of the keys or values in the parsed dictionary are not strings.
**Examples:**

```python
>>> generate_component_names('{"Add expense": "Form", "View report": "Chart"}')
['AddExpenseForm', 'ViewReportChart']
```

```python
>>> generate_component_names('{"Settings": "Modal", "Help": "Drawer"}')
['SettingsModal', 'HelpDrawer']
```



---

## create_wireframe_descriptions

### Description
Generates textual wireframe descriptions for UI components based on component names and functional requirements.

### Conceptual Info

This shim bridges the gap between abstract functional requirements and concrete UI design by producing short, descriptive wireframe snippets for each UI component, enabling downstream steps to render or refine visual mock‑ups.

### Docstring

**Summary:** Create wireframe description strings for UI components based on component identifiers and their associated functional requirements.

**Parameters:**

- components (List[str]): A list of UI component names (e.g., screen or widget identifiers) for which wireframes are to be generated.
- requirements (List[str]): A list of high‑level functional requirements that correspond to the UI components. The order should align with `components` when a direct mapping exists.
**Returns:** List[str] - Wireframe description strings, each summarising the visual layout and key interactions of the corresponding component.

**Raises:**

- ValueError: If `components` and `requirements` have differing lengths and a one‑to‑one mapping is expected.
- TypeError: If either argument is not a list of strings.
**Examples:**

```python
>>> components = ['LoginScreen', 'Dashboard']
>>> requirements = [
...     'User can enter credentials and tap Sign In',
...     'User sees an overview of recent activity after logging in'
>>> ]
>>> create_wireframe_descriptions(components, requirements)
["LoginScreen: A vertical form with fields for email and password, a prominent 'Sign In' button, and a link for password recovery.", "Dashboard: A top navigation bar, a summary card grid showing recent activity, and a side menu for navigation."]
```

```python
>>> create_wireframe_descriptions(['Settings'], ['User can toggle notification preferences'])
["Settings: A simple list with toggle switches for each notification type, positioned under a header labeled 'Notification Preferences'."]
```



---

## finalize_ui_components

### Description
Generates a finalized list of UI component names by integrating component identifiers with their wireframe descriptions.

### Conceptual Info

This shim consolidates raw UI component identifiers with their associated wireframe text, ensuring the two collections align and producing a user‑ready list of component specifications for downstream rendering steps.

### Docstring

**Summary:** Combine UI component names with wireframe descriptions to produce a finalized list of component specifications.

**Parameters:**

- components (str): A JSON‑encoded list of component names (e.g., '["LoginScreen", "Dashboard"]').
- wireframes (str): A JSON‑encoded list of wireframe description strings that correspond positionally to the component names.
**Returns:** list[str] - A list where each entry is "<ComponentName>: <WireframeDescription>", preserving the original order.

**Raises:**

- ValueError: If the two input lists have different lengths.
- TypeError: If either input cannot be parsed as a JSON list of strings.
**Examples:**

```python
>>> finalize_ui_components('["LoginScreen", "Dashboard"]', '["Login screen layout", "Dashboard layout"]')
["LoginScreen: Login screen layout", "Dashboard: Dashboard layout"]
```

```python
>>> finalize_ui_components('["Profile"]', '[]')
ValueError: Component and wireframe lists must have the same length.
```

