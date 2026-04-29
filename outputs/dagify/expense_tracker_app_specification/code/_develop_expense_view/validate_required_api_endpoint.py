def validate_required_api_endpoint(api_endpoints: str, required_endpoint: str) -> str:
    """
    Checks if the specified required API endpoint exists within the list of
    provided API endpoints, raising an error if it is missing.

    Parameters
    ----------
    api_endpoints : str
        A comma-separated string of API endpoint paths (e.g.,
        "/expenses,/users") representing available backend endpoints.
    required_endpoint : str
        The specific API endpoint path that must be present in the list
        (e.g., "/expenses").

    Returns
    -------
    str
        A confirmation message or status indicating successful validation,
        or raises an error if validation fails.

    Raises
    ------
    ValueError
        Raised if the required_endpoint is not found within the
        api_endpoints list, indicating a missing or misconfigured API
        endpoint.
    TypeError
        Raised if the input parameters are not of the expected string types.

    Examples
    --------
    >>> validate_required_api_endpoint('/expenses,/users', '/expenses')
    'API endpoint /expenses is available.'

    >>> validate_required_api_endpoint('/users,/payments', '/expenses')
    ValueError: Required API endpoint '/expenses' not found in available
    endpoints.

    """
    if not isinstance(api_endpoints, str):
        raise TypeError("api_endpoints must be a string")
    if not isinstance(required_endpoint, str):
        raise ValueError("required_endpoint must be a string")
    
    endpoint_list = [endpoint.strip() for endpoint in api_endpoints.split(',') if endpoint.strip()]
    
    if required_endpoint in endpoint_list:
        return f"API endpoint {required_endpoint} is available."
    else:
        raise ValueError(f"Required API endpoint '{required_endpoint}' not found in available endpoints.")