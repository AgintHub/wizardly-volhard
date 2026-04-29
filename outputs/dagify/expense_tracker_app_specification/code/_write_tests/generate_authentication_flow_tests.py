from typing import List


def generate_authentication_flow_tests(auth_module: str) -> List[str]:
    """
    Generate authentication‑flow test identifiers for a given authentication
    module.  The function inspects the supplied module identifier (e.g.,
    filename or package name) and returns a deterministic list of test case
    names that cover typical auth scenarios such as successful login, failed
    login, token refresh, logout, and password reset.

    Parameters
    ----------
    auth_module : str
        Identifier, path, or filename of the authentication module whose
        flow is to be tested.

    Returns
    -------
    list[str]
        A list of test case identifiers (or filenames) that validate the
        authentication workflow.

    Raises
    ------
    ValueError
        Raised when `auth_module` is an empty string or only whitespace.
    TypeError
        Raised when `auth_module` is not of type `str`.

    Examples
    --------
    >>> generate_authentication_flow_tests('auth.py')
    ['test_login_success', 'test_login_failure', 'test_token_refresh',
    'test_logout', 'test_password_reset']

    >>> generate_authentication_flow_tests('myapp.security.auth')
    ['test_login_success', 'test_login_failure', 'test_token_refresh',
    'test_logout', 'test_password_reset']

    """
    if not isinstance(auth_module, str):
        raise TypeError("auth_module must be of type str")
    
    if not auth_module or auth_module.isspace():
        raise ValueError("auth_module cannot be empty or only whitespace")
    
    return [
        'test_login_success',
        'test_login_failure', 
        'test_token_refresh',
        'test_logout',
        'test_password_reset'
    ]