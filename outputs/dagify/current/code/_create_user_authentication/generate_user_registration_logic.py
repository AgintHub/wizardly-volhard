import json


def generate_user_registration_logic(config: str) -> str:
    """
    Generate user registration logic code from a JSON‑encoded authentication
    configuration.

    Parameters
    ----------
    config : str
        A JSON‑encoded string describing the authentication setup (e.g.,
        user model name, password hashing algorithm, required fields, email
        verification flow).

    Returns
    -------
    str
        A string containing the full source code for the registration
        component, ready to be written to a file or concatenated with other
        auth code.

    Raises
    ------
    ValueError
        If the JSON in `config` cannot be parsed or required configuration
        keys are missing.
    TypeError
        If `config` is not a string.

    Examples
    --------
    >>> config = '{"user_model": "User", "password_hash": "bcrypt",
    "email_verification": true}'
    >>> registration_code = generate_user_registration_logic(config)
    >>> print(registration_code[:60])  # preview first part of generated code
    'def register_user(...):\n    # Validate input\n    ...'  # truncated
    preview of the generated source

    >>> bad_config = 'not a json'
    >>> generate_user_registration_logic(bad_config)
    ValueError: Invalid JSON configuration supplied to
    generate_user_registration_logic.

    """
    
    if not isinstance(config, str):
        raise TypeError("Config must be a string")
    
    try:
        config_data = json.loads(config)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON configuration supplied to generate_user_registration_logic.")
    
    required_keys = ['user_model', 'password_hash']
    for key in required_keys:
        if key not in config_data:
            raise ValueError(f"Required configuration key '{key}' is missing.")
    
    user_model = config_data['user_model']
    password_hash = config_data['password_hash']
    email_verification = config_data.get('email_verification', False)
    required_fields = config_data.get('required_fields', ['username', 'email', 'password'])
    
    code_lines = []
    code_lines.append("def register_user(user_data):")
    code_lines.append("    # Validate input")
    code_lines.append("    if not isinstance(user_data, dict):")
    code_lines.append("        raise ValueError('User data must be a dictionary')")
    code_lines.append("")
    
    for field in required_fields:
        code_lines.append(f"    if '{field}' not in user_data or not user_data['{field}']:")
        code_lines.append(f"        raise ValueError('{field} is required')")
    code_lines.append("")
    
    if password_hash == 'bcrypt':
        code_lines.append("    import bcrypt")
        code_lines.append("    password = user_data['password'].encode('utf-8')")
        code_lines.append("    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())")
    elif password_hash == 'sha256':
        code_lines.append("    import hashlib")
        code_lines.append("    password = user_data['password']")
        code_lines.append("    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()")
    else:
        code_lines.append("    hashed_password = user_data['password']  # No hashing")
    code_lines.append("")
    
    code_lines.append(f"    user = {user_model}()")
    for field in required_fields:
        if field == 'password':
            code_lines.append(f"    user.{field} = hashed_password")
        else:
            code_lines.append(f"    user.{field} = user_data['{field}']")
    code_lines.append("")
    
    if email_verification:
        code_lines.append("    # Send email verification")
        code_lines.append("    import uuid")
        code_lines.append("    verification_token = str(uuid.uuid4())")
        code_lines.append("    user.email_verified = False")
        code_lines.append("    user.verification_token = verification_token")
        code_lines.append("    # TODO: Send verification email with token")
        code_lines.append("")
    
    code_lines.append("    # Save user to database")
    code_lines.append("    user.save()")
    code_lines.append("    return user")
    
    return "\n".join(code_lines)