def generate_reports_table(domains: str) -> str:
    """
    Create the SQL statement for the Reports table based on identified core
    domains.

    Parameters
    ----------
    domains : str
        A comma‑separated string of core domain names (e.g.,
        "Users,Expenses,Categories") that the Reports table should
        reference.

    Returns
    -------
    str
        A valid SQL CREATE TABLE statement defining the Reports table with
        appropriate columns and foreign‑key constraints to the supplied
        domains.

    Raises
    ------
    ValueError
        If the domains string is empty or does not contain any recognizable
        core domain.
    TypeError
        If the provided `domains` argument is not of type `str`.

    Examples
    --------
    >>> generate_reports_table('Users,Expenses,Categories')
    "CREATE TABLE Reports (\n    report_id SERIAL PRIMARY KEY,\n    user_id
    INTEGER NOT NULL,\n    expense_id INTEGER NOT NULL,\n    category_id INTEGER
    NOT NULL,\n    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n
    FOREIGN KEY (user_id) REFERENCES Users(user_id),\n    FOREIGN KEY
    (expense_id) REFERENCES Expenses(expense_id),\n    FOREIGN KEY (category_id)
    REFERENCES Categories(category_id)\n);"

    >>> generate_reports_table('Users')
    "CREATE TABLE Reports (\n    report_id SERIAL PRIMARY KEY,\n    user_id
    INTEGER NOT NULL,\n    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n
    FOREIGN KEY (user_id) REFERENCES Users(user_id)\n);"

    """
    if not isinstance(domains, str):
        raise TypeError("The provided `domains` argument is not of type `str`.")
    
    if not domains or not domains.strip():
        raise ValueError("The domains string is empty or does not contain any recognizable core domain.")
    
    domain_list = [domain.strip() for domain in domains.split(',') if domain.strip()]
    
    if not domain_list:
        raise ValueError("The domains string is empty or does not contain any recognizable core domain.")
    
    sql_parts = ["CREATE TABLE Reports ("]
    sql_parts.append("    report_id SERIAL PRIMARY KEY,")
    
    for domain in domain_list:
        domain_lower = domain.lower()
        column_name = f"{domain_lower}_id"
        sql_parts.append(f"    {column_name} INTEGER NOT NULL,")
    
    sql_parts.append("    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,")
    
    for domain in domain_list:
        domain_lower = domain.lower()
        column_name = f"{domain_lower}_id"
        table_name = domain
        primary_key = f"{domain_lower}_id"
        sql_parts.append(f"    FOREIGN KEY ({column_name}) REFERENCES {table_name}({primary_key}),")
    
    sql_parts[-1] = sql_parts[-1].rstrip(',')
    sql_parts.append(");")
    
    return "\n".join(sql_parts)