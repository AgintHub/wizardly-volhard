import re
import json


def derive_client_side_validation_rules(db_tables: str) -> str:
    """
    Derive client‑side validation rules from a textual representation of
    database tables.

    Parameters
    ----------
    db_tables : str
        A string describing one or more database tables and their columns,
        e.g., "Users(id:int,name:str,email:str),Expenses(id:int,amount:float
        ,date:date)".

    Returns
    -------
    str
        A JSON‑encoded dictionary where each top‑level key is a table name
        and each value is a mapping of column names to validation rule
        dictionaries (e.g., type, required, max_length, format).

    Raises
    ------
    ValueError
        If `db_tables` is empty or does not contain any parsable table
        definitions.
    TypeError
        If `db_tables` is not a string.

    Examples
    --------
    >>> derive_client_side_validation_rules('Users(id:int,name:str,email:str)')
    '{"Users": {"id": {"type": "int", "required": true}, "name": {"type": "str",
    "required": true, "max_length": 255}, "email": {"type": "str", "required":
    true, "format": "email"}}}'

    >>> derive_client_side_validation_rules('Expenses(id:int,amount:float,date:d
    ate)')
    '{"Expenses": {"id": {"type": "int", "required": true}, "amount": {"type":
    "float", "required": true, "min": 0}, "date": {"type": "date", "required":
    true}}}'

    """
    
    if not isinstance(db_tables, str):
        raise TypeError("db_tables must be a string")
    
    if not db_tables.strip():
        raise ValueError("db_tables cannot be empty")
    
    table_pattern = r'(\w+)\(([^)]+)\)'
    matches = re.findall(table_pattern, db_tables)
    
    if not matches:
        raise ValueError("No parsable table definitions found")
    
    result = {}
    
    for table_name, columns_str in matches:
        columns = {}
        column_specs = [col.strip() for col in columns_str.split(',')]
        
        for col_spec in column_specs:
            if ':' not in col_spec:
                continue
            
            col_name, col_type = col_spec.split(':', 1)
            col_name = col_name.strip()
            col_type = col_type.strip()
            
            validation_rule = {
                "type": col_type,
                "required": True
            }
            
            if col_type == "str":
                validation_rule["max_length"] = 255
                if "email" in col_name.lower():
                    validation_rule["format"] = "email"
            elif col_type == "float":
                if "amount" in col_name.lower():
                    validation_rule["min"] = 0
            
            columns[col_name] = validation_rule
        
        result[table_name] = columns
    
    return json.dumps(result)