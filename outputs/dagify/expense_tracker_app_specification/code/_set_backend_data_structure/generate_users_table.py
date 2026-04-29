def generate_users_table(domains: str) -> str:
    """
    Generate a SQL `CREATE TABLE` statement for the Users table based on a
    comma‑separated list of core domains.

    Parameters
    ----------
    domains : str
        Comma‑separated list of core domain names (e.g.,
        "users,expenses,categories") derived from the requirements analysis.

    Returns
    -------
    str
        A valid SQL `CREATE TABLE` statement for the Users table, including
        an integer primary key `id`, columns `username`, `email`,
        `created_at`, and any additional columns inferred from the provided
        domains.

    Raises
    ------
    ValueError
        If the `domains` string is empty or does not contain the required
        "users" domain.
    TypeError
        If `domains` is not of type `str`.

    Examples
    --------
    >>> generate_users_table('users,expenses,categories')
    "CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT
    NULL, email TEXT UNIQUE NOT NULL, created_at TIMESTAMP DEFAULT
    CURRENT_TIMESTAMP);"

    >>> generate_users_table('users')
    "CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT
    NULL, email TEXT UNIQUE NOT NULL, created_at TIMESTAMP DEFAULT
    CURRENT_TIMESTAMP);"

    """
    if not isinstance(domains, str):
        raise TypeError("domains must be of type str")
    
    if not domains.strip():
        raise ValueError("domains string cannot be empty")
    
    domain_list = [domain.strip().lower() for domain in domains.split(',')]
    
    if 'users' not in domain_list:
        raise ValueError('domains must contain the required "users" domain')
    
    sql_statement = "CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, email TEXT UNIQUE NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
    
    return sql_statement