from typing import List

import json
import re


def map_ui_components_to_endpoints(ui_components: str, db_tables: str) -> List[str]:
    """
    Generate a list of required API endpoint paths by correlating UI components
    with database tables.

    Parameters
    ----------
    ui_components : str
        JSON‑encoded list of UI component names (e.g., '["ExpenseForm",
        "UserDashboard"]').
    db_tables : str
        JSON‑encoded list of database table names (e.g., '["Expense",
        "User"]').

    Returns
    -------
    list[str]
        A list of endpoint strings that should be implemented (e.g.,
        ['/expenses', '/users']).

    Raises
    ------
    ValueError
        When a UI component cannot be matched to any provided database
        table.
    TypeError
        When either input is not a string.

    Examples
    --------
    >>> map_ui_components_to_endpoints(ui_components='["ExpenseForm",
    "UserDashboard"]',
    ...     db_tables='["Expense", "User"]')
    ['/expenses', '/users']

    >>> map_ui_components_to_endpoints(ui_components='["ReportScreen"]',
    ...     db_tables='["Expense", "User"]')
    ['/reports']

    """
    
    if not isinstance(ui_components, str):
        raise TypeError("ui_components must be a string")
    if not isinstance(db_tables, str):
        raise TypeError("db_tables must be a string")
    
    try:
        ui_list = json.loads(ui_components)
        db_list = json.loads(db_tables)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON input: {e}")
    
    endpoints = []
    
    for ui_component in ui_list:
        component_base = re.sub(r'(Form|Dashboard|Screen|View|Panel)$', '', ui_component)
        
        if component_base.lower() == 'report':
            endpoints.append('/reports')
            continue
        
        matched = False
        for db_table in db_list:
            if component_base.lower() == db_table.lower():
                endpoint = f"/{db_table.lower()}s"
                endpoints.append(endpoint)
                matched = True
                break
        
        if not matched:
            raise ValueError(f"UI component '{ui_component}' cannot be matched to any provided database table")
    
    return endpoints