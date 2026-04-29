import json


def validate_required_api_endpoints(api_endpoints: str, required_endpoints: str) -> str:
    """
    Validate that the supplied API endpoint list includes all required
    endpoints.

    Parameters
    ----------
    api_endpoints : str
        A JSON‑encoded string representing a list of available API endpoint
        paths (e.g., "[\"/expenses\", \"/users\"]").
    required_endpoints : str
        A JSON‑encoded string representing the list of endpoint paths that
        must be present (e.g., "[\"/expenses\"]").

    Returns
    -------
    str
        An empty string if validation succeeds; otherwise a human‑readable
        message listing missing endpoints.

    Raises
    ------
    ValueError
        Raised when any of the required endpoints are absent from the
        provided list.
    TypeError
        Raised when either argument cannot be parsed as a JSON list of
        strings.

    Examples
    --------
    >>> validate_required_api_endpoints(
    ...     api_endpoints='["/expenses", "/users"]',
    ...     required_endpoints='["/expenses"]'
    >>> )
    ""

    >>> validate_required_api_endpoints(
    ...     api_endpoints='["/users"]',
    ...     required_endpoints='["/expenses"]'
    >>> )
    "Missing required endpoint(s): /expenses"

    """
    
    try:
        api_list = json.loads(api_endpoints)
        required_list = json.loads(required_endpoints)
    except json.JSONDecodeError as e:
        raise TypeError(f"Cannot parse JSON input: {e}")
    
    if not isinstance(api_list, list) or not isinstance(required_list, list):
        raise TypeError("Input must be JSON lists")
    
    if not all(isinstance(item, str) for item in api_list):
        raise TypeError("API endpoints must be a list of strings")
    
    if not all(isinstance(item, str) for item in required_list):
        raise TypeError("Required endpoints must be a list of strings")
    
    api_set = set(api_list)
    required_set = set(required_list)
    
    missing_endpoints = required_set - api_set
    
    if missing_endpoints:
        missing_list = sorted(list(missing_endpoints))
        if len(missing_list) == 1:
            message = f"Missing required endpoint(s): {missing_list[0]}"
        else:
            message = f"Missing required endpoint(s): {', '.join(missing_list)}"
        raise ValueError(message)
    
    return ""