from typing import List


def validate_requirements_input(requirements: str) -> List[str]:
    """
    Validate and normalise a collection of functional requirement strings.

    Parameters
    ----------
    requirements : list[str]
        A list of raw requirement strings produced by the previous node.
        Each string may contain leading/trailing whitespace, inconsistent
        capitalisation, or duplicates.

    Returns
    -------
    list[str]
        A cleaned list where each requirement is stripped of surrounding
        whitespace, capitalised, non‑empty, and unique while preserving the
        original order of first occurrence.

    Raises
    ------
    ValueError
        If any element is not a string, is empty after stripping, or if
        duplicate requirements are detected.
    TypeError
        If the supplied `requirements` argument is not iterable or not a
        list of strings.

    Examples
    --------
    >>> validate_requirements_input(['track expenses', 'view reports'])
    ['Track expenses', 'View reports']

    >>> validate_requirements_input(['  add expense  ', 'Add Expense', ''])
    ValueError: Requirements must be non‑empty strings and unique.

    """
    if not isinstance(requirements, list):
        raise TypeError("Requirements must be a list")
    
    cleaned_requirements = []
    seen = set()
    
    for req in requirements:
        if not isinstance(req, str):
            raise TypeError("If the supplied `requirements` argument is not iterable or not a list of strings.")
        
        stripped = req.strip()
        if not stripped:
            raise ValueError("Requirements must be non‑empty strings and unique.")
        
        capitalized = stripped.capitalize()
        
        if capitalized in seen:
            raise ValueError("Requirements must be non‑empty strings and unique.")
        
        seen.add(capitalized)
        cleaned_requirements.append(capitalized)
    
    return cleaned_requirements