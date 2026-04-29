import json


def design_dashboard_layout(chart_components: str) -> str:
    """
    Designs the overall dashboard layout for the summary reports based on
    provided chart component identifiers.

    Parameters
    ----------
    chart_components : List[str]
        A list of identifiers (e.g., filenames or component names) for the
        chart components that should be placed on the dashboard.

    Returns
    -------
    str
        A serialized representation (e.g., JSON or DSL) describing the
        positioned chart components and overall layout of the dashboard.

    Raises
    ------
    ValueError
        If `chart_components` is empty, because a dashboard must contain at
        least one chart.
    TypeError
        If `chart_components` is not a list of strings.

    Examples
    --------
    >>> layout = design_dashboard_layout(['sales_chart', 'expense_chart'])
    '{"layout": [{"id": "sales_chart", "position": "top-left"}, {"id":
    "expense_chart", "position": "top-right"}]}'

    >>> layout = design_dashboard_layout(['revenue_trend'])
    '{"layout": [{"id": "revenue_trend", "position": "full-width"}]}'

    """
    
    if not isinstance(chart_components, list):
        raise TypeError("chart_components must be a list of strings")
    
    if not chart_components:
        raise ValueError("chart_components cannot be empty, dashboard must contain at least one chart")
    
    for component in chart_components:
        if not isinstance(component, str):
            raise TypeError("chart_components must be a list of strings")
    
    layout = []
    
    if len(chart_components) == 1:
        layout.append({
            "id": chart_components[0],
            "position": "full-width"
        })
    elif len(chart_components) == 2:
        layout.append({
            "id": chart_components[0],
            "position": "top-left"
        })
        layout.append({
            "id": chart_components[1],
            "position": "top-right"
        })
    else:
        positions = ["top-left", "top-right", "bottom-left", "bottom-right"]
        for i, component in enumerate(chart_components):
            if i < 4:
                position = positions[i]
            else:
                position = f"grid-{i+1}"
            layout.append({
                "id": component,
                "position": position
            })
    
    return json.dumps({"layout": layout})