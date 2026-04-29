from typing import List

import json


def create_wireframe_descriptions(components: str, requirements: str) -> List[str]:
    """
    Create wireframe description strings for UI components based on component
    identifiers and their associated functional requirements.

    Parameters
    ----------
    components : List[str]
        A list of UI component names (e.g., screen or widget identifiers)
        for which wireframes are to be generated.
    requirements : List[str]
        A list of high‑level functional requirements that correspond to the
        UI components. The order should align with `components` when a
        direct mapping exists.

    Returns
    -------
    List[str]
        Wireframe description strings, each summarising the visual layout
        and key interactions of the corresponding component.

    Raises
    ------
    ValueError
        If `components` and `requirements` have differing lengths and a
        one‑to‑one mapping is expected.
    TypeError
        If either argument is not a list of strings.

    Examples
    --------
    >>> components = ['LoginScreen', 'Dashboard']
    >>> requirements = [
    ...     'User can enter credentials and tap Sign In',
    ...     'User sees an overview of recent activity after logging in'
    >>> ]
    >>> create_wireframe_descriptions(components, requirements)
    ["LoginScreen: A vertical form with fields for email and password, a
    prominent 'Sign In' button, and a link for password recovery.", "Dashboard:
    A top navigation bar, a summary card grid showing recent activity, and a
    side menu for navigation."]

    >>> create_wireframe_descriptions(['Settings'], ['User can toggle
    notification preferences'])
    ["Settings: A simple list with toggle switches for each notification type,
    positioned under a header labeled 'Notification Preferences'."]

    """
    
    try:
        components_list = json.loads(components)
        requirements_list = json.loads(requirements)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format for components or requirements")
    
    if not isinstance(components_list, list) or not isinstance(requirements_list, list):
        raise TypeError("Both arguments must be lists of strings")
    
    if not all(isinstance(comp, str) for comp in components_list):
        raise TypeError("Components must be a list of strings")
    
    if not all(isinstance(req, str) for req in requirements_list):
        raise TypeError("Requirements must be a list of strings")
    
    if len(components_list) != len(requirements_list):
        raise ValueError("Components and requirements must have the same length")
    
    wireframes = []
    
    for component, requirement in zip(components_list, requirements_list):
        wireframe_desc = f"{component}: "
        
        if 'login' in component.lower() or 'sign in' in requirement.lower():
            wireframe_desc += "A vertical form with fields for email and password, a prominent 'Sign In' button, and a link for password recovery."
        elif 'dashboard' in component.lower() or 'overview' in requirement.lower() or 'activity' in requirement.lower():
            wireframe_desc += "A top navigation bar, a summary card grid showing recent activity, and a side menu for navigation."
        elif 'settings' in component.lower() or 'preferences' in requirement.lower() or 'toggle' in requirement.lower():
            wireframe_desc += "A simple list with toggle switches for each notification type, positioned under a header labeled 'Notification Preferences'."
        else:
            wireframe_desc += f"A clean interface layout designed to accommodate: {requirement.lower()}."
        
        wireframes.append(wireframe_desc)
    
    return wireframes