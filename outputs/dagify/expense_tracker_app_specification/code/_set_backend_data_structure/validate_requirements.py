from typing import List


def validate_requirements(requirements: str) -> List[str]:
    """
    Validate and normalize a list of functional requirement strings.

    Parameters
    ----------
    requirements : List[str]
        A list of high‑level functional requirement strings produced by the
        previous node.

    Returns
    -------
    List[str]
        A cleaned list of requirement strings with leading/trailing
        whitespace removed and duplicates eliminated.

    Raises
    ------
    TypeError
        If `requirements` is not a list or contains non‑string elements.
    ValueError
        If any requirement string is empty after stripping whitespace.

    Examples
    --------
    >>> validate_requirements(['Track expenses', '  Track expenses ', 'Generate
    reports'])
    ['Track expenses', 'Generate reports']

    >>> validate_requirements('Track expenses')
    TypeError: requirements must be a list of strings

    """
    if not isinstance(requirements, list):
        raise TypeError("requirements must be a list of strings")
    
    cleaned_requirements = []
    for req in requirements:
        if not isinstance(req, str):
            raise TypeError("requirements must be a list of strings")
        
        stripped_req = req.strip()
        if not stripped_req:
            raise ValueError("requirement string cannot be empty after stripping whitespace")
        
        if stripped_req not in cleaned_requirements:
            cleaned_requirements.append(stripped_req)
    
    return cleaned_requirements