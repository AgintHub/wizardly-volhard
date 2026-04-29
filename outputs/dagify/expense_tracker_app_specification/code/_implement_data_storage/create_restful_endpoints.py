from typing import List

import json


def create_restful_endpoints(required_endpoints: str, crud_handlers: str) -> List[str]:
    """
    Create RESTful endpoint strings from required endpoint names and CRUD
    handler definitions.

    Parameters
    ----------
    required_endpoints : str
        A JSON‑encoded string list of endpoint base paths (e.g.,
        "[\"/users\", \"/expenses\"]").
    crud_handlers : str
        A JSON‑encoded string mapping each resource name to its CRUD handler
        identifier (e.g., "{\"users\": \"UserModel\", \"expenses\":
        \"ExpenseModel\"}").

    Returns
    -------
    list[str]
        A list of fully qualified RESTful endpoint definitions (e.g., ["GET
        /users", "POST /users", "GET /expenses", "POST /expenses"]).

    Raises
    ------
    ValueError
        If the JSON strings cannot be parsed or required endpoint entries
        are missing.
    TypeError
        If the parsed structures are not of the expected types (list for
        required_endpoints, dict for crud_handlers).

    Examples
    --------
    >>> create_restful_endpoints('["/users","/expenses"]',
    '{"users":"UserModel","expenses":"ExpenseModel"}')
    ["GET /users", "POST /users", "GET /expenses", "POST /expenses"]

    >>> create_restful_endpoints('["/reports"]', '{"reports":"ReportModel"}')
    ["GET /reports", "POST /reports"]

    """
    
    try:
        endpoints_list = json.loads(required_endpoints)
    except json.JSONDecodeError as e:
        raise ValueError(f"Could not parse required_endpoints JSON: {e}")
    
    try:
        handlers_dict = json.loads(crud_handlers)
    except json.JSONDecodeError as e:
        raise ValueError(f"Could not parse crud_handlers JSON: {e}")
    
    if not isinstance(endpoints_list, list):
        raise TypeError("Parsed required_endpoints must be a list")
    
    if not isinstance(handlers_dict, dict):
        raise TypeError("Parsed crud_handlers must be a dict")
    
    result = []
    
    for endpoint in endpoints_list:
        endpoint_clean = endpoint.strip('/')
        if endpoint_clean not in handlers_dict:
            raise ValueError(f"Required endpoint '{endpoint_clean}' not found in crud_handlers")
        
        result.append(f"GET /{endpoint_clean}")
        result.append(f"POST /{endpoint_clean}")
    
    return result