def validate_required_inputs(ui_components: str, db_tables: str) -> str:
    """
    Validate that required inputs `ui_components` and `db_tables` are present,
    are lists of strings, and contain at least one element each.

    Parameters
    ----------
    ui_components : list[str]
        List of UI component names derived from functional requirements.
    db_tables : list[str]
        List of database table identifiers produced by the backend
        data‑structure node.

    Returns
    -------
    str
        A short message such as "Validation successful." confirming that
        both inputs passed all checks.

    Raises
    ------
    TypeError
        If either argument is not a list.
    ValueError
        If a list is empty or contains non‑string elements.

    Examples
    --------
    >>> validate_required_inputs(['Dashboard', 'Settings'], ['User', 'Expense'])
    'Validation successful.'

    >>> validate_required_inputs([], ['User'])
    ValueError: ui_components must be a non‑empty list of strings

    """
    if not isinstance(ui_components, list):
        raise TypeError("ui_components must be a list")
    if not isinstance(db_tables, list):
        raise TypeError("db_tables must be a list")
    
    if len(ui_components) == 0:
        raise ValueError("ui_components must be a non‑empty list of strings")
    if len(db_tables) == 0:
        raise ValueError("db_tables must be a non‑empty list of strings")
    
    for component in ui_components:
        if not isinstance(component, str):
            raise ValueError("ui_components must be a non‑empty list of strings")
    
    for table in db_tables:
        if not isinstance(table, str):
            raise ValueError("db_tables must be a non‑empty list of strings")
    
    return "Validation successful."