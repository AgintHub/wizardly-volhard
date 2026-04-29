import json


def map_requirements_to_ui_patterns(requirements: str) -> str:
    """
    Convert validated functional requirements into a mapping of UI design
    patterns, returning the result as a JSON‑encoded string.

    Parameters
    ----------
    requirements : str
        A JSON‑encoded list of validated requirement strings (e.g., '["Add
        expense", "View report"]').

    Returns
    -------
    str
        A JSON‑encoded dictionary mapping each requirement to a list of UI
        pattern names (e.g., '{"Add expense": ["Form", "Button"], "View
        report": ["Chart", "Table"]}').

    Raises
    ------
    ValueError
        If the input JSON cannot be parsed or does not represent a list of
        strings.
    TypeError
        If the parsed object is not a list or contains non‑string elements.

    Examples
    --------
    >>> map_requirements_to_ui_patterns('["Add expense", "View report"]')
    '{"Add expense": ["Form", "Button"], "View report": ["Chart", "Table"]}'

    >>> map_requirements_to_ui_patterns('["Sync data", "Export CSV"]')
    '{"Sync data": ["Toggle", "ProgressBar"], "Export CSV": ["Button",
    "Dialog"]}'

    """
    
    try:
        parsed_requirements = json.loads(requirements)
    except json.JSONDecodeError:
        raise ValueError("Input JSON cannot be parsed")
    
    if not isinstance(parsed_requirements, list):
        raise TypeError("Parsed object is not a list")
    
    for item in parsed_requirements:
        if not isinstance(item, str):
            raise TypeError("List contains non-string elements")
    
    ui_pattern_mapping = {
        "add": ["Form", "Button"],
        "create": ["Form", "Button"],
        "new": ["Form", "Button"],
        "view": ["Chart", "Table"],
        "show": ["Chart", "Table"],
        "display": ["Chart", "Table"],
        "report": ["Chart", "Table"],
        "sync": ["Toggle", "ProgressBar"],
        "synchronize": ["Toggle", "ProgressBar"],
        "update": ["Toggle", "ProgressBar"],
        "export": ["Button", "Dialog"],
        "download": ["Button", "Dialog"],
        "save": ["Button", "Dialog"],
        "edit": ["Form", "Input"],
        "modify": ["Form", "Input"],
        "change": ["Form", "Input"],
        "delete": ["Button", "Confirmation"],
        "remove": ["Button", "Confirmation"],
        "search": ["Input", "List"],
        "find": ["Input", "List"],
        "filter": ["Dropdown", "List"],
        "sort": ["Dropdown", "Table"],
        "login": ["Form", "Input"],
        "logout": ["Button"],
        "upload": ["Button", "FileInput"],
        "import": ["Button", "FileInput"]
    }
    
    result = {}
    for requirement in parsed_requirements:
        requirement_lower = requirement.lower()
        patterns = ["Form", "Button"]
        
        for keyword, ui_patterns in ui_pattern_mapping.items():
            if keyword in requirement_lower:
                patterns = ui_patterns
                break
        
        result[requirement] = patterns
    
    return json.dumps(result)