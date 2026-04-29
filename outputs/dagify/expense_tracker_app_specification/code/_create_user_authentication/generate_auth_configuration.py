import json


def generate_auth_configuration(ui_components: str) -> str:
    """
    Generate a configuration dictionary for user authentication based on UI
    component names.

    Parameters
    ----------
    ui_components : List[str]
        A list of UI component identifiers (e.g., "LoginScreen",
        "RegistrationForm") that indicate which authentication features are
        needed.

    Returns
    -------
    str
        A JSON‑encoded string of a dictionary containing boolean flags and
        optional settings required to build the authentication module.

    Raises
    ------
    ValueError
        If the list does not contain any recognized authentication‑related
        components.
    TypeError
        If `ui_components` is not a list of strings.

    Examples
    --------
    >>> config_json = generate_auth_configuration(['LoginScreen',
    'RegistrationForm'])
    >>> print(config_json)
    '{"requires_login": true, "requires_registration": true,
    "password_reset_enabled": false}'

    >>> config_json = generate_auth_configuration(['PasswordResetScreen'])
    >>> print(config_json)
    '{"requires_login": false, "requires_registration": false,
    "password_reset_enabled": true}'

    """
    
    try:
        if isinstance(ui_components, str):
            component_list = json.loads(ui_components)
        else:
            component_list = ui_components
    except (json.JSONDecodeError, TypeError):
        raise TypeError("ui_components must be a list of strings or JSON string of a list")
    
    if not isinstance(component_list, list):
        raise TypeError("ui_components must be a list of strings")
    
    if not all(isinstance(item, str) for item in component_list):
        raise TypeError("ui_components must be a list of strings")
    
    config = {
        "requires_login": False,
        "requires_registration": False,
        "password_reset_enabled": False
    }
    
    auth_components_found = False
    
    for component in component_list:
        if 'login' in component.lower() or 'signin' in component.lower():
            config["requires_login"] = True
            auth_components_found = True
        elif 'registration' in component.lower() or 'register' in component.lower() or 'signup' in component.lower():
            config["requires_registration"] = True
            auth_components_found = True
        elif 'password' in component.lower() and 'reset' in component.lower():
            config["password_reset_enabled"] = True
            auth_components_found = True
    
    if not auth_components_found:
        raise ValueError("The list does not contain any recognized authentication-related components")
    
    return json.dumps(config)