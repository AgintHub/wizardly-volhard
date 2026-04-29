from typing import List


def consolidate_requirements(expense_ops: str, reporting: str, user_mgmt: str, settings: str, additional: str) -> List[str]:
    """
    Combine category‑specific requirement strings into a single list of
    high‑level functional requirements for the expense‑tracker app.

    Parameters
    ----------
    expense_ops : str
        A string representation (e.g., comma‑separated) of expense‑operation
        requirements such as creating, editing, and deleting expenses.
    reporting : str
        A string representation of reporting‑related requirements, e.g.,
        summary views, charts, export capabilities.
    user_mgmt : str
        A string representation of user‑management requirements, such as
        login, registration, and profile handling.
    settings : str
        A string representation of application‑settings requirements, like
        theme selection or notification preferences.
    additional : str
        A string representation of any extra functional requirements not
        covered by the other categories.

    Returns
    -------
    list[str]
        A list of consolidated, deduplicated, and logically ordered
        functional requirement statements.

    Raises
    ------
    TypeError
        If any of the inputs are not of type `str`.
    ValueError
        If an input string is empty or cannot be parsed into individual
        requirement items.

    Examples
    --------
    >>> consolidate_requirements(
    ...     expense_ops='Add expense,Edit expense,Delete expense',
    ...     reporting='Summary report,Expense chart',
    ...     user_mgmt='User login,User signup',
    ...     settings='Theme selection,Notification toggle',
    ...     additional='Data export')
    ["Add expense", "Edit expense", "Delete expense", "Generate summary report",
    "Generate expense chart", "User login", "User signup", "Configure theme
    selection", "Configure notification toggle", "Export data"]

    >>> consolidate_requirements(
    ...     expense_ops='Add,Edit',
    ...     reporting='Charts',
    ...     user_mgmt='Login',
    ...     settings='Dark mode',
    ...     additional='')
    ["Add expense", "Edit expense", "Generate charts", "User login", "Enable
    dark mode"]

    """
    if not all(isinstance(param, str) for param in [expense_ops, reporting, user_mgmt, settings, additional]):
        raise TypeError("All inputs must be of type str")
    
    consolidated = []
    
    categories = [
        (expense_ops, "expense"),
        (reporting, "reporting"),
        (user_mgmt, "user"),
        (settings, "settings"),
        (additional, "additional")
    ]
    
    for category_str, category_type in categories:
        if category_str.strip():
            if not category_str or category_str.isspace():
                raise ValueError("Input string cannot be empty or contain only whitespace")
            
            items = [item.strip() for item in category_str.split(',') if item.strip()]
            if not items:
                raise ValueError("Input string cannot be parsed into individual requirement items")
            
            for item in items:
                normalized_item = item.lower().strip()
                
                if category_type == "expense":
                    if "add" in normalized_item:
                        formatted_item = "Add expense"
                    elif "edit" in normalized_item:
                        formatted_item = "Edit expense"
                    elif "delete" in normalized_item:
                        formatted_item = "Delete expense"
                    else:
                        formatted_item = item.capitalize() + " expense"
                elif category_type == "reporting":
                    if "summary" in normalized_item or "report" in normalized_item:
                        formatted_item = "Generate summary report"
                    elif "chart" in normalized_item:
                        formatted_item = "Generate expense chart"
                    else:
                        formatted_item = "Generate " + item.lower()
                elif category_type == "user":
                    if "login" in normalized_item:
                        formatted_item = "User login"
                    elif "signup" in normalized_item or "registration" in normalized_item:
                        formatted_item = "User signup"
                    else:
                        formatted_item = "User " + item.lower()
                elif category_type == "settings":
                    if "theme" in normalized_item:
                        formatted_item = "Configure theme selection"
                    elif "notification" in normalized_item:
                        formatted_item = "Configure notification toggle"
                    elif "dark mode" in normalized_item:
                        formatted_item = "Enable dark mode"
                    else:
                        formatted_item = "Configure " + item.lower()
                elif category_type == "additional":
                    if "export" in normalized_item:
                        formatted_item = "Export data"
                    else:
                        formatted_item = item.capitalize()
                
                if formatted_item not in consolidated:
                    consolidated.append(formatted_item)
    
    return consolidated