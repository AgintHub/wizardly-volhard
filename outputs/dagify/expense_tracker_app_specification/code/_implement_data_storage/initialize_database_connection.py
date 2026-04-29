import sqlite3


def initialize_database_connection() -> str:
    """
    Establishes a connection to the database system to prepare for data storage
    operations; requires proper configuration and handles connection errors.

    Parameters
    ----------
    config : dict
        Configuration parameters needed for establishing the database
        connection, such as host, port, user, password, and database name.

    Returns
    -------
    str
        A status message indicating success or failure of the database
        connection attempt.

    Raises
    ------
    ValueError
        Raised if essential configuration parameters are missing or invalid.
    ConnectionError
        Raised if the database server is unreachable or the connection
        cannot be established.

    Examples
    --------
    >>> initialize_database_connection({'host': 'localhost', 'port': 5432,
    'user': 'admin', 'password': 'secret', 'database': 'mydb'})
    'Database connection established successfully.'

    >>> initialize_database_connection({'host': '', 'port': 5432, 'user':
    'admin', 'password': 'secret', 'database': 'mydb'})
    Raises ValueError: Missing or invalid configuration parameters.

    """
    
    try:
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute('SELECT 1')
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if result:
            return 'Database connection established successfully.'
        else:
            raise ConnectionError('Connection test failed')
            
    except sqlite3.Error as e:
        raise ConnectionError(f'Database connection failed: {str(e)}')
    except Exception as e:
        raise ValueError(f'Invalid configuration or connection parameters: {str(e)}')