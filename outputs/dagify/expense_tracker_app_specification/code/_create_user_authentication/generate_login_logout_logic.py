import json


def generate_login_logout_logic(config: str) -> str:
    """
    Generate Python source code implementing login and logout functionality from
    a serialized authentication configuration.

    Parameters
    ----------
    config : str
        A serialized authentication configuration (e.g., JSON) that
        specifies required fields, validation rules, session handling
        strategy, and any third‑party auth integrations.

    Returns
    -------
    str
        A string containing the complete Python code for `login` and
        `logout` functions, ready to be inserted into the authentication
        module.

    Raises
    ------
    ValueError
        If the configuration is missing required keys such as
        `login_endpoint` or `session_cookie_name`.
    TypeError
        If `config` is not a string or cannot be parsed as valid JSON.
    KeyError
        If expected configuration fields are absent after parsing.

    Examples
    --------
    >>> config = '{"login_endpoint": "/login", "logout_endpoint": "/logout",
    "session_cookie_name": "session_id", "auth_method": "password"}'
    >>> code = generate_login_logout_logic(config)
    'def login(request):\n    # validate credentials\n    ...\n\ndef
    logout(request):\n    # clear session\n    ...'

    >>> invalid_cfg = 'not a json'
    >>> generate_login_logout_logic(invalid_cfg)
    ValueError: Configuration string is not valid JSON.

    """
    
    try:
        parsed_config = json.loads(config)
    except json.JSONDecodeError:
        raise ValueError("Configuration string is not valid JSON.")
    except TypeError:
        raise TypeError("Config must be a string.")
    
    required_keys = ['login_endpoint', 'logout_endpoint', 'session_cookie_name', 'auth_method']
    for key in required_keys:
        if key not in parsed_config:
            raise KeyError(f"Required configuration field '{key}' is missing.")
    
    login_endpoint = parsed_config['login_endpoint']
    logout_endpoint = parsed_config['logout_endpoint']
    session_cookie_name = parsed_config['session_cookie_name']
    auth_method = parsed_config['auth_method']
    
    login_code = f"""def login(request):
    if request.method != 'POST':
        return {{'error': 'Method not allowed'}}, 405
    
    credentials = request.get_json() or {{}}
    username = credentials.get('username')
    password = credentials.get('password')
    
    if not username or not password:
        return {{'error': 'Username and password required'}}, 400
    
    if auth_method == 'password':
        if validate_user_credentials(username, password):
            session_id = generate_session_id()
            response = make_response({{'message': 'Login successful'}})
            response.set_cookie('{session_cookie_name}', session_id, httponly=True, secure=True)
            return response
        else:
            return {{'error': 'Invalid credentials'}}, 401
    else:
        return {{'error': 'Unsupported auth method'}}, 400"""
    
    logout_code = f"""def logout(request):
    session_id = request.cookies.get('{session_cookie_name}')
    
    if session_id:
        invalidate_session(session_id)
    
    response = make_response({{'message': 'Logout successful'}})
    response.set_cookie('{session_cookie_name}', '', expires=0)
    return response"""
    
    return login_code + "\n\n" + logout_code