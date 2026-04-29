from typing import List

import json


def finalize_ui_components(components: str, wireframes: str) -> List[str]:
    """
    Combine UI component names with wireframe descriptions to produce a
    finalized list of component specifications.

    Parameters
    ----------
    components : str
        A JSON‑encoded list of component names (e.g., '["LoginScreen",
        "Dashboard"]').
    wireframes : str
        A JSON‑encoded list of wireframe description strings that correspond
        positionally to the component names.

    Returns
    -------
    list[str]
        A list where each entry is "<ComponentName>:
        <WireframeDescription>", preserving the original order.

    Raises
    ------
    ValueError
        If the two input lists have different lengths.
    TypeError
        If either input cannot be parsed as a JSON list of strings.

    Examples
    --------
    >>> finalize_ui_components('["LoginScreen", "Dashboard"]', '["Login screen
    layout", "Dashboard layout"]')
    ["LoginScreen: Login screen layout", "Dashboard: Dashboard layout"]

    >>> finalize_ui_components('["Profile"]', '[]')
    ValueError: Component and wireframe lists must have the same length.

    """
    
    try:
        components_list = json.loads(components)
        wireframes_list = json.loads(wireframes)
    except json.JSONDecodeError as e:
        raise TypeError("Input cannot be parsed as a JSON list of strings") from e
    
    if not isinstance(components_list, list) or not isinstance(wireframes_list, list):
        raise TypeError("Input cannot be parsed as a JSON list of strings")
    
    if not all(isinstance(item, str) for item in components_list) or not all(isinstance(item, str) for item in wireframes_list):
        raise TypeError("Input cannot be parsed as a JSON list of strings")
    
    if len(components_list) != len(wireframes_list):
        raise ValueError("Component and wireframe lists must have the same length.")
    
    result = []
    for component, wireframe in zip(components_list, wireframes_list):
        result.append(f"{component}: {wireframe}")
    
    return result