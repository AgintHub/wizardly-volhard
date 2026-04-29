from typing import List


def generate_report_calculation_tests(report_dashboard_component: str) -> List[str]:
    """
    Generate a suite of test case identifiers that validate the calculation
    logic of a report dashboard component.

    Parameters
    ----------
    report_dashboard_component : str
        The filename, module path, or unique identifier of the report
        dashboard component whose calculations need to be tested.

    Returns
    -------
    List[str]
        A list of strings, each representing a distinct test case name
        (e.g., 'test_report_total', 'test_report_breakdown_by_category').

    Raises
    ------
    ValueError
        If `report_dashboard_component` is an empty string or only
        whitespace.
    TypeError
        If `report_dashboard_component` is not of type `str`.

    Examples
    --------
    >>> tests = generate_report_calculation_tests('report_dashboard.py')
    >>> print(tests)
    ['test_report_total', 'test_report_breakdown_by_category',
    'test_report_filter_by_date']

    >>> generate_report_calculation_tests('')
    ValueError: report_dashboard_component must be a non‑empty string.

    """
    if not isinstance(report_dashboard_component, str):
        raise TypeError("report_dashboard_component must be of type str")
    
    if not report_dashboard_component or report_dashboard_component.isspace():
        raise ValueError("report_dashboard_component must be a non-empty string.")
    
    test_cases = [
        "test_report_total",
        "test_report_breakdown_by_category",
        "test_report_filter_by_date",
        "test_report_percentage_calculations",
        "test_report_sum_aggregations",
        "test_report_average_calculations",
        "test_report_filter_by_amount",
        "test_report_sort_functionality",
        "test_report_grouping_logic",
        "test_report_data_validation"
    ]
    
    return test_cases