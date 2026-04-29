import json
import sqlite3


def create_database_tables(orm_models: str) -> str:
    """
    Create database tables from ORM model definitions.  The function parses the
    provided ORM models, issues the necessary DDL statements to the active
    database connection, and returns a human‑readable status message.

    Parameters
    ----------
    orm_models : str
        A string (e.g., JSON) describing the ORM models where each key is a
        model name and each value is a column‑definition string compatible
        with the target SQL dialect.

    Returns
    -------
    str
        A message summarising the outcome, such as "Database tables created
        successfully." or an error description.

    Raises
    ------
    ValueError
        If `orm_models` cannot be parsed as valid JSON or lacks required
        model definitions.
    TypeError
        If `orm_models` is not a string.
    RuntimeError
        If any underlying database operation fails (e.g., syntax error,
        connection loss).

    Examples
    --------
    >>> create_database_tables('{"User": "id INTEGER PRIMARY KEY, name TEXT",
    "Expense": "id INTEGER PRIMARY KEY, amount REAL, user_id INTEGER"}')
    "Database tables created successfully."

    >>> create_database_tables('invalid json')
    "ValueError: orm_models string is not valid JSON."

    """
    
    if not isinstance(orm_models, str):
        raise TypeError("orm_models must be a string")
    
    try:
        models_dict = json.loads(orm_models)
    except json.JSONDecodeError:
        raise ValueError("orm_models string is not valid JSON.")
    
    if not isinstance(models_dict, dict) or not models_dict:
        raise ValueError("orm_models must contain valid model definitions")
    
    try:
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        
        for table_name, column_definitions in models_dict.items():
            create_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
            cursor.execute(create_sql)
        
        conn.commit()
        conn.close()
        
        return "Database tables created successfully."
    except sqlite3.Error as e:
        raise RuntimeError(f"Database operation failed: {str(e)}") from e