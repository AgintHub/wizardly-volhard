def create_orm_models(db_tables: str) -> str:
    """
    Generate ORM model specifications from a textual table definition.  The
    function parses `db_tables`, validates its format, and returns a stringified
    Python dictionary where each key is a table name and each value is a mapping
    of field names to generic ORM types (e.g., Integer, String, Float). The
    output can be fed directly to code generators that produce SQLAlchemy or
    similar ORM classes.

    Parameters
    ----------
    db_tables : str
        Newline‑separated table definitions. Each line must follow the
        pattern `TableName:field1:type1,field2:type2,...` where `type` is
        one of `int`, `str`, `float`, or `bool`.

    Returns
    -------
    str
        A string representation of a dictionary `{table_name: {field_name:
        orm_type, ...}, ...}` where `orm_type` is a generic ORM type name
        (e.g., "Integer", "String", "Float", "Boolean").

    Raises
    ------
    ValueError
        If any line in `db_tables` does not conform to the required
        `TableName:field:type` syntax or contains an unsupported field type.
    TypeError
        If `db_tables` is not a string.

    Examples
    --------
    >>> create_orm_models('User:id:int,name:str,email:str\nExpense:id:int,amount
    :float,user_id:int')
    '{'User': {'id': 'Integer', 'name': 'String', 'email': 'String'}, 'Expense':
    {'id': 'Integer', 'amount': 'Float', 'user_id': 'Integer'}}'

    >>> create_orm_models('Category:id:int,title:str')
    '{'Category': {'id': 'Integer', 'title': 'String'}}'

    """
    if not isinstance(db_tables, str):
        raise TypeError("db_tables must be a string")
    
    if not db_tables.strip():
        return "{}"
    
    type_mapping = {
        'int': 'Integer',
        'str': 'String', 
        'float': 'Float',
        'bool': 'Boolean'
    }
    
    result = {}
    
    lines = db_tables.strip().split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if ':' not in line:
            raise ValueError(f"Line does not conform to required TableName:field:type syntax: {line}")
        
        parts = line.split(':', 1)
        if len(parts) != 2:
            raise ValueError(f"Line does not conform to required TableName:field:type syntax: {line}")
            
        table_name = parts[0].strip()
        fields_part = parts[1].strip()
        
        if not table_name:
            raise ValueError(f"Table name cannot be empty: {line}")
            
        if not fields_part:
            raise ValueError(f"Fields part cannot be empty: {line}")
        
        fields = {}
        field_definitions = fields_part.split(',')
        
        for field_def in field_definitions:
            field_def = field_def.strip()
            if not field_def:
                continue
                
            field_parts = field_def.split(':')
            if len(field_parts) != 2:
                raise ValueError(f"Field definition does not conform to field:type syntax: {field_def}")
                
            field_name = field_parts[0].strip()
            field_type = field_parts[1].strip()
            
            if not field_name:
                raise ValueError(f"Field name cannot be empty in: {field_def}")
                
            if field_type not in type_mapping:
                raise ValueError(f"Unsupported field type: {field_type}")
                
            fields[field_name] = type_mapping[field_type]
        
        if not fields:
            raise ValueError(f"No valid fields found for table: {table_name}")
            
        result[table_name] = fields
    
    return str(result)