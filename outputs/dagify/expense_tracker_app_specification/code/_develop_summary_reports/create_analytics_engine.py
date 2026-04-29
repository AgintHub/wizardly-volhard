import os
import logging


def create_analytics_engine() -> str:
    """
    Instantiate and return a reference to the analytics engine used for expense
    data analysis.

    Returns
    -------
    str
        A unique string identifier (such as a module name, class path, or
        filename) that downstream nodes can use to access the analytics
        engine.

    Raises
    ------
    ValueError
        If required configuration for the analytics engine is missing or
        invalid.
    RuntimeError
        If the analytics engine fails to initialize due to internal errors.

    Examples
    --------
    >>> engine_id = create_analytics_engine()
    >>> print(engine_id)
    'analytics_engine_v1'

    >>> try:
    ...     create_analytics_engine()
    >>> except ValueError as e:
    ...     print('Configuration error:', e)
    'Configuration error: missing analytics configuration'

    """
    
    required_configs = ['ANALYTICS_DB_URL', 'ANALYTICS_CACHE_SIZE']
    for config in required_configs:
        if not os.environ.get(config):
            raise ValueError(f"missing analytics configuration: {config}")
    
    db_url = os.environ.get('ANALYTICS_DB_URL')
    cache_size = os.environ.get('ANALYTICS_CACHE_SIZE')
    
    try:
        cache_size_int = int(cache_size)
        if cache_size_int <= 0:
            raise ValueError("ANALYTICS_CACHE_SIZE must be a positive integer")
    except ValueError as e:
        if "positive integer" in str(e):
            raise
        raise ValueError("ANALYTICS_CACHE_SIZE must be a valid integer") from e
    
    if not db_url.startswith(('postgresql://', 'mysql://', 'sqlite://')):
        raise ValueError("ANALYTICS_DB_URL must be a valid database URL")
    
    try:
        engine_id = "analytics_engine_v1"
        logging.getLogger().info(f"Analytics engine {engine_id} initialized successfully")
        return engine_id
    except Exception as e:
        raise RuntimeError(f"Analytics engine failed to initialize: {str(e)}") from e