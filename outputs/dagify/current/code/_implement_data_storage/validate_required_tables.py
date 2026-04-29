def validate_required_tables(db_tables: str) -> str:
    """
    Validate that the required database tables are present in the provided table
    list.

    Parameters
    ----------
    db_tables : str
        A comma‑separated string of table names supplied by the
        `set_backend_data_structure` node (e.g.,
        `'Users,Expenses,Categories,Reports'`).

    Returns
    -------
    str
        A confirmation message such as `'All required tables are present.'`
        when validation succeeds.

    Raises
    ------
    ValueError
        Raised when one or more of the mandatory tables (`Users`,
        `Expenses`, `Categories`, `Reports`) are missing from `db_tables`.
        The error message lists the absent tables.
    TypeError
        Raised when `db_tables` is not of type `str`.

    Examples
    --------
    >>> validate_required_tables('Users,Expenses,Categories,Reports')
    'All required tables are present.'

    >>> validate_required_tables('Users,Expenses')
    ValueError: Missing required tables: Categories, Reports

    """
    if not isinstance(db_tables, str):
        raise TypeError("db_tables must be of type str")
    
    required_tables = {'Users', 'Expenses', 'Categories', 'Reports'}
    
    if not db_tables.strip():
        provided_tables = set()
    else:
        provided_tables = {table.strip() for table in db_tables.split(',') if table.strip()}
    
    missing_tables = required_tables - provided_tables
    
    if missing_tables:
        missing_list = sorted(list(missing_tables))
        raise ValueError(f"Missing required tables: {', '.join(missing_list)}")
    
    return "All required tables are present."