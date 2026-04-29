def compile_auth_module(registration: str, login: str, password_reset: str, session_management: str, ui_integration: str) -> str:
    """
    Compile the authentication module from individual code fragments and write
    it to a file.

    Parameters
    ----------
    registration : str
        Source code implementing user registration functionality.
    login : str
        Source code implementing login and logout functionality.
    password_reset : str
        Source code implementing password‑reset workflow.
    session_management : str
        Source code handling session creation, validation, and termination.
    ui_integration : str
        Source code that connects the authentication backend to the
        generated UI components.

    Returns
    -------
    str
        Path to the generated authentication module file (e.g.,
        "auth_module.py").

    Raises
    ------
    ValueError
        If any of the required code fragments are empty strings or contain
        only whitespace.
    TypeError
        If any argument is not of type str.

    Examples
    --------
    >>> module_path = compile_auth_module(
    ...     registration='def register_user(...): ...',
    ...     login='def login_user(...): ...',
    ...     password_reset='def reset_password(...): ...',
    ...     session_management='def manage_session(...): ...',
    ...     ui_integration='def integrate_ui(...): ...'
    >>> )
    >>> print(module_path)
    'auth_module.py'

    >>> # Trigger a validation error
    >>> compile_auth_module(
    ...     registration='',
    ...     login='def login_user(...): ...',
    ...     password_reset='def reset_password(...): ...',
    ...     session_management='def manage_session(...): ...',
    ...     ui_integration='def integrate_ui(...): ...'
    >>> )
    ValueError: registration code cannot be empty

    """
    for param_name, param_value in [('registration', registration), ('login', login), ('password_reset', password_reset), ('session_management', session_management), ('ui_integration', ui_integration)]:
        if not isinstance(param_value, str):
            raise TypeError(f"{param_name} must be of type str")
        if not param_value.strip():
            raise ValueError(f"{param_name} code cannot be empty")
    
    module_content = f"""# Generated Authentication Module

{registration}

{login}

{password_reset}

{session_management}

{ui_integration}
"""
    
    output_file = "auth_module.py"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(module_content)
    
    return output_file