import json
import uuid


def create_expense_data_service(api_endpoints: str) -> str:
    """
    Create and register an expense data service based on provided API endpoint
    definitions.

    Parameters
    ----------
    api_endpoints : str
        A string representation (e.g., JSON or comma‑separated list) of the
        API endpoints required for the expense service, such as "/expenses".

    Returns
    -------
    str
        A unique service identifier (e.g., UUID or logical name) that
        downstream nodes can use to reference the provisioned expense data
        service.

    Raises
    ------
    ValueError
        If `api_endpoints` does not contain the required "/expenses"
        endpoint or is otherwise malformed.
    TypeError
        If `api_endpoints` is not of type `str`.

    Examples
    --------
    >>> service_id = create_expense_data_service('/expenses')
    >>> print(service_id)
    'expense_service_1'

    >>> service_id = create_expense_data_service('{"endpoints": ["/expenses",
    "/users"]}')
    >>> print(service_id)
    'expense_service_2'

    """
    
    if not isinstance(api_endpoints, str):
        raise TypeError("api_endpoints is not of type str")
    
    endpoints = []
    
    try:
        parsed = json.loads(api_endpoints)
        if isinstance(parsed, dict) and "endpoints" in parsed:
            endpoints = parsed["endpoints"]
        else:
            endpoints = [api_endpoints]
    except json.JSONDecodeError:
        if "," in api_endpoints:
            endpoints = [endpoint.strip() for endpoint in api_endpoints.split(",")]
        else:
            endpoints = [api_endpoints.strip()]
    
    if "/expenses" not in endpoints:
        raise ValueError('api_endpoints does not contain the required "/expenses" endpoint or is otherwise malformed')
    
    service_id = f"expense_service_{str(uuid.uuid4()).replace('-', '')[:8]}"
    
    return service_id