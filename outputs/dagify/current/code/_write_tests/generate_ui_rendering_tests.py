from typing import List


def generate_ui_rendering_tests(expense_view_component: str) -> List[str]:
    """
    Generate UI rendering tests for a given expense view component.  The
    function validates the input component identifier, constructs a set of test
    case names (or code snippets) that exercise typical rendering scenarios, and
    returns them as a list of strings.

    Parameters
    ----------
    expense_view_component : str
        Identifier (e.g., module name, class name, or file path) of the
        expense view UI component to be tested.

    Returns
    -------
    List[str]
        A list containing descriptive test case identifiers (or code
        snippets) that verify the component renders correctly, handles empty
        states, and respects UI contracts.

    Raises
    ------
    ValueError
        Raised when `expense_view_component` is an empty string or only
        whitespace.
    TypeError
        Raised when `expense_view_component` is not of type `str`.

    Examples
    --------
    >>> generate_ui_rendering_tests('ExpenseListComponent')
    ['test_expense_list_renders_correctly',
    'test_expense_list_shows_no_items_message']

    >>> generate_ui_rendering_tests('MonthlySummaryWidget')
    ['test_monthly_summary_renders_header',
    'test_monthly_summary_displays_totals']

    """
    if not isinstance(expense_view_component, str):
        raise TypeError("expense_view_component must be of type str")
    
    if not expense_view_component or expense_view_component.isspace():
        raise ValueError("expense_view_component cannot be empty or only whitespace")
    
    component_name = expense_view_component.strip()
    
    test_cases = []
    
    if 'list' in component_name.lower() or 'expense' in component_name.lower():
        test_cases.extend([
            f"test_{component_name.lower().replace('component', '').replace('widget', '')}_renders_correctly",
            f"test_{component_name.lower().replace('component', '').replace('widget', '')}_shows_no_items_message",
            f"test_{component_name.lower().replace('component', '').replace('widget', '')}_handles_loading_state",
            f"test_{component_name.lower().replace('component', '').replace('widget', '')}_displays_expense_items"
        ])
    elif 'summary' in component_name.lower() or 'monthly' in component_name.lower():
        test_cases.extend([
            f"test_{component_name.lower().replace('component', '').replace('widget', '')}_renders_header",
            f"test_{component_name.lower().replace('component', '').replace('widget', '')}_displays_totals",
            f"test_{component_name.lower().replace('component', '').replace('widget', '')}_shows_period_info"
        ])
    else:
        test_cases.extend([
            f"test_{component_name.lower().replace('component', '').replace('widget', '')}_renders_correctly",
            f"test_{component_name.lower().replace('component', '').replace('widget', '')}_handles_empty_state",
            f"test_{component_name.lower().replace('component', '').replace('widget', '')}_displays_content"
        ])
    
    cleaned_test_cases = []
    for test_case in test_cases:
        cleaned_case = test_case.replace('__', '_').replace('  ', ' ').strip('_')
        while '__' in cleaned_case:
            cleaned_case = cleaned_case.replace('__', '_')
        cleaned_test_cases.append(cleaned_case)
    
    return cleaned_test_cases