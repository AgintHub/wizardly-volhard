from typing import List

import re


def identify_core_domains(requirements: str) -> List[str]:
    """
    Identify core domain names from a textual description of functional
    requirements.

    Parameters
    ----------
    requirements : str
        A single string containing high‑level functional requirements; items
        may be separated by commas, semicolons, newlines, or the word "and".

    Returns
    -------
    list[str]
        A list of distinct core domain identifiers (lower‑case,
        whitespace‑trimmed) that were recognized in the input.

    Raises
    ------
    ValueError
        If the input string is empty or does not contain any recognizable
        domain keywords.
    TypeError
        If the supplied `requirements` argument is not of type `str`.

    Examples
    --------
    >>> identify_core_domains('Users can register, create expenses, and view
    reports')
    ['users', 'expenses', 'reports']

    >>> identify_core_domains('Manage categories; track expenses; generate
    summary reports')
    ['categories', 'expenses', 'reports']

    """
    
    if not isinstance(requirements, str):
        raise TypeError("If the supplied `requirements` argument is not of type `str`.")
    
    if not requirements.strip():
        raise ValueError("If the input string is empty or does not contain any recognizable domain keywords.")
    
    text = re.sub(r'\band\b', ',', requirements, flags=re.IGNORECASE)
    parts = re.split(r'[,;\n]+', text)
    
    domains = []
    domain_keywords = [
        'user', 'users', 'account', 'accounts', 'profile', 'profiles',
        'expense', 'expenses', 'cost', 'costs', 'spending',
        'report', 'reports', 'summary', 'summaries', 'analytics',
        'category', 'categories', 'classification', 'classifications',
        'product', 'products', 'item', 'items',
        'order', 'orders', 'purchase', 'purchases',
        'payment', 'payments', 'transaction', 'transactions',
        'customer', 'customers', 'client', 'clients',
        'invoice', 'invoices', 'bill', 'bills',
        'inventory', 'stock', 'warehouse',
        'employee', 'employees', 'staff',
        'project', 'projects', 'task', 'tasks'
    ]
    
    for part in parts:
        words = re.findall(r'\b\w+\b', part.lower())
        for word in words:
            if word in domain_keywords:
                normalized = word
                if word.endswith('s') and word[:-1] in domain_keywords:
                    normalized = word
                elif word + 's' in domain_keywords:
                    normalized = word + 's' if word + 's' in ['users', 'expenses', 'reports', 'categories', 'products', 'orders', 'payments', 'customers', 'invoices', 'employees', 'projects'] else word
                
                if normalized not in domains:
                    domains.append(normalized)
    
    if not domains:
        raise ValueError("If the input string is empty or does not contain any recognizable domain keywords.")
    
    return domains