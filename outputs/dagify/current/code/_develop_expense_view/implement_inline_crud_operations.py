import json


def implement_inline_crud_operations(api_endpoints: str) -> str:
    """
    Generate inline CRUD operation specifications for a set of API endpoints.
    The function maps each supplied endpoint to a dictionary containing the four
    standard CRUD operations, expressed as HTTP method and URL pattern strings.
    The resulting mapping is returned as a JSON‑encoded string suitable for
    templating into generated UI component code.

    Parameters
    ----------
    api_endpoints : list[str]
        A list of backend API endpoint paths (e.g., ['/expenses',
        '/users']). Each endpoint must start with a leading '/'.

    Returns
    -------
    str
        A JSON‑encoded string representing a dictionary of CRUD
        specifications. Example format: ```json {   "/expenses": {
        "create": "POST /expenses",     "read": "GET /expenses",
        "update": "PUT /expenses/{id}",     "delete": "DELETE
        /expenses/{id}"   } } ```

    Raises
    ------
    ValueError
        If `api_endpoints` is empty or any endpoint does not start with a
        leading '/'.
    TypeError
        If `api_endpoints` is not a list or its elements are not strings.

    Examples
    --------
    >>> crud_json = implement_inline_crud_operations(['/expenses'])
    >>> print(crud_json)
    {"/expenses": {"create": "POST /expenses", "read": "GET /expenses",
    "update": "PUT /expenses/{id}", "delete": "DELETE /expenses/{id}"}}

    >>> endpoints = ['/expenses', '/users']
    >>> result = implement_inline_crud_operations(endpoints)
    >>> print(result)
    {"/expenses": {"create": "POST /expenses", "read": "GET /expenses",
    "update": "PUT /expenses/{id}", "delete": "DELETE /expenses/{id}"},
    "/users": {"create": "POST /users", "read": "GET /users", "update": "PUT
    /users/{id}", "delete": "DELETE /users/{id}"}}

    """
    
    if not isinstance(api_endpoints, list):
        raise TypeError("api_endpoints must be a list")
    
    if not api_endpoints:
        raise ValueError("api_endpoints cannot be empty")
    
    for endpoint in api_endpoints:
        if not isinstance(endpoint, str):
            raise TypeError("All elements in api_endpoints must be strings")
        if not endpoint.startswith('/'):
            raise ValueError("All endpoints must start with a leading '/'")
    
    crud_dict = {}
    
    for endpoint in api_endpoints:
        crud_dict[endpoint] = {
            "create": f"POST {endpoint}",
            "read": f"GET {endpoint}",
            "update": f"PUT {endpoint}/{{id}}",
            "delete": f"DELETE {endpoint}/{{id}}"
        }
    
    return json.dumps(crud_dict)