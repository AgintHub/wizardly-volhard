from typing import List

import json


def compile_comprehensive_test_suite(input_tests: str, crud_tests: str, auth_tests: str, ui_tests: str, report_tests: str) -> List[str]:
    """
    Compile a comprehensive test suite from distinct test case groups.  The
    function receives five pre‑generated test lists (as strings containing
    serialized representations) and returns a single list of test identifiers
    that can be executed together.

    Parameters
    ----------
    input_tests : str
        Serialized representation (e.g., JSON or CSV string) of
        input‑validation test identifiers.
    crud_tests : str
        Serialized representation of CRUD operation test identifiers.
    auth_tests : str
        Serialized representation of authentication‑flow test identifiers.
    ui_tests : str
        Serialized representation of UI‑rendering test identifiers.
    report_tests : str
        Serialized representation of report‑calculation test identifiers.

    Returns
    -------
    list[str]
        A combined, ordered list of test case identifiers (or filenames)
        ready for execution.

    Raises
    ------
    ValueError
        If any of the input strings are empty or cannot be parsed into a
        list of test identifiers.
    TypeError
        If any of the provided arguments are not of type `str`.

    Examples
    --------
    >>> input_tests = "['test_input_1', 'test_input_2']"
    >>> crud_tests = "['test_create', 'test_read', 'test_update',
    'test_delete']"
    >>> auth_tests = "['test_login', 'test_logout']"
    >>> ui_tests = "['test_expense_view', 'test_form_render']"
    >>> report_tests = "['test_monthly_summary', 'test_yearly_total']"
    >>> suite = compile_comprehensive_test_suite(input_tests, crud_tests,
    auth_tests, ui_tests, report_tests)
    ['test_input_1', 'test_input_2', 'test_create', 'test_read', 'test_update',
    'test_delete', 'test_login', 'test_logout', 'test_expense_view',
    'test_form_render', 'test_monthly_summary', 'test_yearly_total']

    >>> # Passing an empty string raises a ValueError
    >>> compile_comprehensive_test_suite('', crud_tests, auth_tests, ui_tests,
    report_tests)
    ValueError: input_tests cannot be empty or unparsable

    """
    
    test_groups = [input_tests, crud_tests, auth_tests, ui_tests, report_tests]
    group_names = ['input_tests', 'crud_tests', 'auth_tests', 'ui_tests', 'report_tests']
    
    for i, test_group in enumerate(test_groups):
        if not isinstance(test_group, str):
            raise TypeError(f"All arguments must be of type str, but {group_names[i]} is {type(test_group).__name__}")
    
    combined_tests = []
    
    for i, test_group in enumerate(test_groups):
        if not test_group.strip():
            raise ValueError(f"{group_names[i]} cannot be empty or unparsable")
        
        try:
            parsed_tests = json.loads(test_group)
            if not isinstance(parsed_tests, list):
                raise ValueError(f"{group_names[i]} cannot be empty or unparsable")
            combined_tests.extend(parsed_tests)
        except (json.JSONDecodeError, ValueError) as e:
            if "cannot be empty or unparsable" in str(e):
                raise e
            raise ValueError(f"{group_names[i]} cannot be empty or unparsable") from e
    
    return combined_tests