from typing import List

import json


def generate_component_names(mappings: str) -> List[str]:
    """
    Generate concise UI component names based on requirement‑to‑pattern
    mappings.

    Parameters
    ----------
    mappings : str
        A JSON‑encoded string representing a dictionary where each key is a
        functional requirement (str) and each value is the associated UI
        design pattern (str).

    Returns
    -------
    list[str]
        A list of component names derived from the mappings, preserving the
        order of the input requirements.

    Raises
    ------
    ValueError
        If the JSON string cannot be parsed or does not represent a
        dictionary of strings to strings.
    TypeError
        If any of the keys or values in the parsed dictionary are not
        strings.

    Examples
    --------
    >>> generate_component_names('{"Add expense": "Form", "View report":
    "Chart"}')
    ['AddExpenseForm', 'ViewReportChart']

    >>> generate_component_names('{"Settings": "Modal", "Help": "Drawer"}')
    ['SettingsModal', 'HelpDrawer']

    """
    
    try:
        parsed_mappings = json.loads(mappings)
    except json.JSONDecodeError:
        raise ValueError("JSON string cannot be parsed")
    
    if not isinstance(parsed_mappings, dict):
        raise ValueError("JSON does not represent a dictionary")
    
    for key, value in parsed_mappings.items():
        if not isinstance(key, str) or not isinstance(value, str):
            raise TypeError("Keys and values in the dictionary must be strings")
    
    component_names = []
    for requirement, pattern in parsed_mappings.items():
        requirement_words = requirement.replace(' ', '')
        component_name = requirement_words + pattern
        component_names.append(component_name)
    
    return component_names