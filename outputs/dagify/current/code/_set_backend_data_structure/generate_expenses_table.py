def generate_expenses_table(domains: str) -> str:
    """
    Generate the SQL CREATE TABLE statement for the Expenses table using core
    domain information.

    Parameters
    ----------
    domains : str
        A comma‑separated string of core domain identifiers (e.g.,
        "finance,user,category") that influence column selection and naming
        conventions for the Expenses table.

    Returns
    -------
    str
        A single string containing a valid SQL CREATE TABLE statement for
        the Expenses table, including appropriate columns, data types,
        primary keys, foreign keys, and any domain‑driven constraints.

    Raises
    ------
    ValueError
        If the `domains` string is empty or does not contain any recognized
        domain keywords required to build the table.
    TypeError
        If `domains` is not of type `str`.

    Examples
    --------
    >>> generate_expenses_table('finance,user,category')
    'CREATE TABLE Expenses (expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL, category_id INTEGER NOT NULL, amount REAL NOT
    NULL, expense_date DATE NOT NULL, description TEXT, FOREIGN KEY(user_id)
    REFERENCES Users(user_id), FOREIGN KEY(category_id) REFERENCES
    Categories(category_id));'

    >>> generate_expenses_table('finance')
    'CREATE TABLE Expenses (expense_id INTEGER PRIMARY KEY AUTOINCREMENT, amount
    REAL NOT NULL, expense_date DATE NOT NULL, description TEXT);'

    """
    if not isinstance(domains, str):
        raise TypeError("domains must be of type str")
    
    if not domains or not domains.strip():
        raise ValueError("domains string is empty or does not contain any recognized domain keywords")
    
    domain_list = [domain.strip().lower() for domain in domains.split(',')]
    
    table_name = "Expenses"
    columns = []
    foreign_keys = []
    
    columns.append("expense_id INTEGER PRIMARY KEY AUTOINCREMENT")
    
    if "user" in domain_list:
        columns.append("user_id INTEGER NOT NULL")
        foreign_keys.append("FOREIGN KEY(user_id) REFERENCES Users(user_id)")
    
    if "category" in domain_list:
        columns.append("category_id INTEGER NOT NULL")
        foreign_keys.append("FOREIGN KEY(category_id) REFERENCES Categories(category_id)")
    
    if "finance" in domain_list or any(domain in domain_list for domain in ["finance", "user", "category"]):
        columns.append("amount REAL NOT NULL")
        columns.append("expense_date DATE NOT NULL")
        columns.append("description TEXT")
    
    recognized_domains = {"finance", "user", "category"}
    if not any(domain in recognized_domains for domain in domain_list):
        raise ValueError("domains string does not contain any recognized domain keywords required to build the table")
    
    columns_str = ", ".join(columns)
    
    if foreign_keys:
        all_constraints = columns + foreign_keys
        constraints_str = ", ".join(all_constraints)
    else:
        constraints_str = columns_str
    
    sql_statement = f"CREATE TABLE {table_name} ({constraints_str});"
    
    return sql_statement