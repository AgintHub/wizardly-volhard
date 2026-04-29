def register_endpoints_with_framework(endpoints: str) -> str:
    """
    Register a collection of API endpoint definitions with the web framework and
    return a success confirmation.

    Parameters
    ----------
    endpoints : List[str]
        A list of endpoint strings (e.g., ['/users', '/expenses']) to be
        added to the framework's routing table.

    Returns
    -------
    str
        A human‑readable message confirming successful registration, e.g.,
        "Endpoints registered successfully".

    Raises
    ------
    ValueError
        If the `endpoints` list is empty or contains non‑string items.
    RuntimeError
        If the underlying framework raises an exception while attempting to
        register the endpoints.

    Examples
    --------
    >>> register_endpoints_with_framework(['GET /users', 'POST /expenses'])
    'Endpoints registered successfully'

    >>> register_endpoints_with_framework([])
    ValueError: 'endpoints' list must contain at least one endpoint definition

    """
    if not endpoints:
        raise ValueError("'endpoints' list must contain at least one endpoint definition")
    
    if not isinstance(endpoints, str):
        raise ValueError("'endpoints' list must contain at least one endpoint definition")
    
    try:
        endpoint_list = [ep.strip() for ep in endpoints.split(',') if ep.strip()]
        
        if not endpoint_list:
            raise ValueError("'endpoints' list must contain at least one endpoint definition")
        
        for endpoint in endpoint_list:
            if not isinstance(endpoint, str) or not endpoint:
                raise ValueError("'endpoints' list must contain at least one endpoint definition")
        
        registered_count = len(endpoint_list)
        
        if registered_count == 0:
            raise RuntimeError("Framework failed to register endpoints")
        
        return "Endpoints registered successfully"
    
    except Exception as e:
        if isinstance(e, (ValueError, RuntimeError)):
            raise
        raise RuntimeError("Framework failed to register endpoints") from e