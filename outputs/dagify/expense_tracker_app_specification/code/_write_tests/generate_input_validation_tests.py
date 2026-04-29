from typing import List

import json
import re


def generate_input_validation_tests(frontend_forms: str) -> List[str]:
    """
    Generate input‑validation test case identifiers from a string describing
    frontend form components.

    Parameters
    ----------
    frontend_forms : str
        A comma‑separated (or JSON‑array) string containing the names of
        frontend form components for which input‑validation tests should be
        produced.

    Returns
    -------
    list[str]
        A list where each element is a unique, human‑readable test
        identifier (e.g., "test_<form_name>_input_validation") corresponding
        to a form in `frontend_forms`.

    Raises
    ------
    ValueError
        If `frontend_forms` is empty or does not contain any parsable form
        names.
    TypeError
        If `frontend_forms` is not of type `str`.

    Examples
    --------
    >>> generate_input_validation_tests('login_form, expense_form')
    ['test_login_form_input_validation', 'test_expense_form_input_validation']

    >>> generate_input_validation_tests('["signup", "profile_edit"]')
    ['test_signup_input_validation', 'test_profile_edit_input_validation']

    """
    
    if not isinstance(frontend_forms, str):
        raise TypeError("frontend_forms must be of type str")
    
    if not frontend_forms or not frontend_forms.strip():
        raise ValueError("frontend_forms is empty or does not contain any parsable form names")
    
    form_names = []
    
    frontend_forms = frontend_forms.strip()
    
    if frontend_forms.startswith('[') and frontend_forms.endswith(']'):
        try:
            parsed_forms = json.loads(frontend_forms)
            if isinstance(parsed_forms, list):
                form_names = [str(form).strip() for form in parsed_forms if str(form).strip()]
        except (json.JSONDecodeError, ValueError):
            pass
    
    if not form_names:
        form_names = [form.strip() for form in frontend_forms.split(',') if form.strip()]
    
    if not form_names:
        raise ValueError("frontend_forms is empty or does not contain any parsable form names")
    
    test_identifiers = []
    for form_name in form_names:
        clean_name = re.sub(r'[^a-zA-Z0-9_]', '_', form_name)
        clean_name = re.sub(r'_+', '_', clean_name).strip('_')
        if clean_name:
            test_identifiers.append(f"test_{clean_name}_input_validation")
    
    if not test_identifiers:
        raise ValueError("frontend_forms is empty or does not contain any parsable form names")
    
    return test_identifiers