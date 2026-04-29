import json


def generate_ui_integration_code(ui_components: str, config: str) -> str:
    """
    Generate UI integration code for authentication.  This function receives a
    comma‑separated list of UI component names and a JSON‑encoded authentication
    configuration, validates the inputs, and returns a string containing Python
    code that imports the authentication module and inserts the necessary hooks
    into each UI component.

    Parameters
    ----------
    ui_components : str
        A comma‑separated string of UI component identifiers (e.g.,
        "login_screen,register_form,profile_page").
    config : str
        A JSON‑encoded string representing the authentication configuration
        produced by `generate_auth_configuration`.

    Returns
    -------
    str
        A multi‑line Python source code snippet that imports the auth module
        and injects authentication calls into each listed UI component.

    Raises
    ------
    ValueError
        If `ui_components` is empty or the JSON `config` cannot be parsed.
    TypeError
        If either argument is not of type `str`.

    Examples
    --------
    >>> code = generate_ui_integration_code(
    ...     ui_components='login_screen,register_form',
    ...     config='{"token_endpoint": "/api/token", "session_timeout": 3600}'
    >>> )
    >>> print(code[:80])  # show beginning of generated code
    "import auth_module\n\n# Integration for login_screen\nfrom login_screen
    import render as login_render\n..."

    >>> generate_ui_integration_code(
    ...     ui_components='',
    ...     config='{}'
    >>> )
    ValueError: ui_components must contain at least one component name.

    """
    
    if not isinstance(ui_components, str):
        raise TypeError("ui_components must be of type str")
    if not isinstance(config, str):
        raise TypeError("config must be of type str")
    
    ui_components = ui_components.strip()
    if not ui_components:
        raise ValueError("ui_components must contain at least one component name.")
    
    try:
        config_dict = json.loads(config)
    except json.JSONDecodeError as e:
        raise ValueError("config must be valid JSON") from e
    
    component_list = [comp.strip() for comp in ui_components.split(',') if comp.strip()]
    if not component_list:
        raise ValueError("ui_components must contain at least one component name.")
    
    code_lines = ["import auth_module", ""]
    
    for component in component_list:
        code_lines.append(f"# Integration for {component}")
        code_lines.append(f"from {component} import render as {component}_render")
        code_lines.append(f"")
        code_lines.append(f"def enhanced_{component}_render(*args, **kwargs):")
        code_lines.append(f"    # Initialize authentication for {component}")
        
        if 'token_endpoint' in config_dict:
            code_lines.append(f"    auth_module.set_token_endpoint('{config_dict['token_endpoint']}')")
        
        if 'session_timeout' in config_dict:
            code_lines.append(f"    auth_module.set_session_timeout({config_dict['session_timeout']})")
        
        code_lines.append(f"    # Add authentication hooks")
        code_lines.append(f"    auth_module.setup_auth_hooks()")
        code_lines.append(f"    # Call original render function")
        code_lines.append(f"    return {component}_render(*args, **kwargs)")
        code_lines.append(f"")
    
    return "\n".join(code_lines)