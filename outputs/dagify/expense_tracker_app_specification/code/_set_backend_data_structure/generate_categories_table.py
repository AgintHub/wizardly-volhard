def generate_categories_table(domains: str) -> str:
    """
    Generates an SQL command string for creating a categories table based on
    specified core domains.

    Parameters
    ----------
    domains : str
        A comma-separated string of core domain names that influence the
        table structure.

    Returns
    -------
    str
        An SQL command string for creating the categories table, customized
        for the provided core domains.

    Raises
    ------
    ValueError
        Raised if 'domains' is empty or not a valid string representing core
        domains.
    TypeError
        Raised if 'domains' is not of type str.

    Examples
    --------
    >>> generate_categories_table('finance,budget')
    'CREATE TABLE IF NOT EXISTS Categories (id INTEGER PRIMARY KEY, name TEXT,
    domain TEXT);'

    >>> generate_categories_table('personal,work')
    'CREATE TABLE IF NOT EXISTS Categories (id INTEGER PRIMARY KEY, name TEXT,
    domain TEXT);'

    """
    if not isinstance(domains, str):
        raise TypeError("'domains' is not of type str.")
    
    if not domains or not domains.strip():
        raise ValueError("'domains' is empty or not a valid string representing core domains.")
    
    domain_list = [domain.strip() for domain in domains.split(',')]
    if not any(domain_list) or any(not domain for domain in domain_list):
        raise ValueError("'domains' is empty or not a valid string representing core domains.")
    
    return "CREATE TABLE IF NOT EXISTS Categories (id INTEGER PRIMARY KEY, name TEXT, domain TEXT);"