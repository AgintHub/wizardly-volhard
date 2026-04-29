from typing import List


def generate_crud_operation_tests(api_endpoints: str) -> List[str]:
    """
    Generate CRUD operation test identifiers from a string of API endpoint
    definitions.

    Parameters
    ----------
    api_endpoints : str
        A single string containing one or more API endpoint paths, separated
        by commas (e.g., "/expenses,/users").

    Returns
    -------
    List[str]
        A list of test case identifiers for create, read, update, and delete
        actions for each endpoint, formatted as "test_<action>_<resource>".

    Raises
    ------
    ValueError
        If the input string is empty or does not contain any valid endpoint
        paths.
    TypeError
        If the provided api_endpoints argument is not of type str.

    Examples
    --------
    >>> generate_crud_operation_tests('/expenses,/users')
    ['test_create_expense', 'test_read_expense', 'test_update_expense',
    'test_delete_expense', 'test_create_user', 'test_read_user',
    'test_update_user', 'test_delete_user']

    >>> generate_crud_operation_tests('/reports')
    ['test_create_report', 'test_read_report', 'test_update_report',
    'test_delete_report']

    """
    if not isinstance(api_endpoints, str):
        raise TypeError("If the provided api_endpoints argument is not of type str.")
    
    if not api_endpoints.strip():
        raise ValueError("If the input string is empty or does not contain any valid endpoint paths.")
    
    endpoints = [endpoint.strip() for endpoint in api_endpoints.split(',')]
    
    valid_endpoints = []
    for endpoint in endpoints:
        if endpoint and endpoint.startswith('/'):
            valid_endpoints.append(endpoint)
    
    if not valid_endpoints:
        raise ValueError("If the input string is empty or does not contain any valid endpoint paths.")
    
    test_identifiers = []
    actions = ['create', 'read', 'update', 'delete']
    
    for endpoint in valid_endpoints:
        resource_name = endpoint.lstrip('/')
        
        if resource_name.endswith('s'):
            singular_resource = resource_name[:-1]
        else:
            singular_resource = resource_name
        
        for action in actions:
            test_identifiers.append(f'test_{action}_{singular_resource}')
    
    return test_identifiers