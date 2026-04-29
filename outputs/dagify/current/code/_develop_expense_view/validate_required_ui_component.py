def validate_required_ui_component(ui_components: str, required_component: str) -> str:
    """
    Check that a required UI component is included in the list of UI components
    and return a success message or raise an error.

    Parameters
    ----------
    ui_components : list of str
        A collection of UI component names generated from the functional
        requirements.
    required_component : str
        The name of the UI component that must be present (e.g.,
        "ExpenseList").

    Returns
    -------
    str
        A message confirming that the required component was found, e.g.,
        "UI component 'ExpenseList' is present."

    Raises
    ------
    ValueError
        Raised when `required_component` is not found in `ui_components`.
    TypeError
        Raised when `ui_components` is not a list of strings or
        `required_component` is not a string.

    Examples
    --------
    >>> validate_required_ui_component(ui_components=['Dashboard',
    'ExpenseList', 'Settings'], required_component='ExpenseList')
    "UI component 'ExpenseList' is present."

    >>> validate_required_ui_component(ui_components=['Dashboard', 'Settings'],
    required_component='ExpenseList')
    ValueError: Required UI component 'ExpenseList' not found in the provided
    list.

    """
    if not isinstance(ui_components, list):
        raise TypeError("ui_components must be a list of strings")
    if not isinstance(required_component, str):
        raise TypeError("required_component must be a string")
    if not all(isinstance(component, str) for component in ui_components):
        raise TypeError("ui_components must be a list of strings")
    if required_component not in ui_components:
        raise ValueError(f"Required UI component '{required_component}' not found in the provided list.")
    return f"UI component '{required_component}' is present."