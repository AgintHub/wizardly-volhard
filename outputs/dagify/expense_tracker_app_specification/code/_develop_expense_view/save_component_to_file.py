import os
import tempfile
import re


def save_component_to_file(component_code: str, component_name: str) -> str:
    """
    Save a UI component's source code to a file and return the file path.

    Parameters
    ----------
    component_code : str
        The source code of the UI component to be written to disk.
    component_name : str
        Logical name of the component; used to derive the filename (e.g.,
        "ExpenseList" → "ExpenseList.py").

    Returns
    -------
    str
        Absolute path of the written file (e.g., "/tmp/ExpenseList.py").

    Raises
    ------
    TypeError
        If either argument is not a string.
    ValueError
        If component_code is empty or component_name contains invalid
        filesystem characters.
    IOError
        If the file cannot be created or written due to permission or disk
        issues.

    Examples
    --------
    >>> save_component_to_file('def render():\n    return "<div>Expense
    List</div>"', 'ExpenseList')
    '/your/output/directory/ExpenseList.py'

    >>> save_component_to_file('class Foo: pass', 'FooComponent')
    '/your/output/directory/FooComponent.py'

    """
    
    if not isinstance(component_code, str):
        raise TypeError("component_code must be a string")
    if not isinstance(component_name, str):
        raise TypeError("component_name must be a string")
    
    if not component_code.strip():
        raise ValueError("component_code cannot be empty")
    
    if not re.match(r'^[a-zA-Z0-9_-]+$', component_name):
        raise ValueError("component_name contains invalid filesystem characters")
    
    filename = f"{component_name}.py"
    file_path = os.path.join(tempfile.gettempdir(), filename)
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(component_code)
    except (IOError, OSError) as e:
        raise IOError(f"File cannot be created or written: {e}") from e
    
    return os.path.abspath(file_path)