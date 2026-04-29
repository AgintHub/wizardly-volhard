def validate_required_ui_component(ui_components: str, required_component: str) -> str:
    """
    Validate that a required UI component is included in the provided UI
    components list.

    Parameters
    ----------
    ui_components : str
        A comma‑separated string of UI component names produced by the
        design step (e.g., "Login, Dashboard, ReportDashboard").
    required_component : str
        The name of the UI component that must be present (e.g.,
        "ReportDashboard").

    Returns
    -------
    str
        A message confirming the presence of `required_component`, e.g.,
        "Component 'ReportDashboard' is present."

    Raises
    ------
    ValueError
        Raised when `required_component` is not found in `ui_components`.
    TypeError
        Raised when either argument is not of type `str`.

    Examples
    --------
    >>> validate_required_ui_component('Login, Dashboard, ReportDashboard',
    'ReportDashboard')
    'Component \'ReportDashboard\' is present.'

    >>> try:
    ...     validate_required_ui_component('Login, Dashboard',
    'ReportDashboard')
    >>> except ValueError as e:
    ...     print(e)
    'Required UI component \'ReportDashboard\' is missing from the provided
    list.'

    """
    if not isinstance(ui_components, str):
        raise TypeError(f"Expected ui_components to be of type str, got {type(ui_components).__name__}")
    if not isinstance(required_component, str):
        raise TypeError(f"Expected required_component to be of type str, got {type(required_component).__name__}")
    
    component_list = [component.strip() for component in ui_components.split(',')]
    
    if required_component not in component_list:
        raise ValueError(f"Required UI component '{required_component}' is missing from the provided list.")
    
    return f"Component '{required_component}' is present."