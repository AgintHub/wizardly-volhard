from typing import List

import json


def generate_form_components_with_validation(form_specs: str, validation_rules: str) -> List[str]:
    """
    Create frontend form component code strings from JSON‑encoded specifications
    and validation rules.

    Parameters
    ----------
    form_specs : str
        A JSON‑encoded list of dictionaries, each describing a form field
        (e.g., name, type, label, placeholder, options).
    validation_rules : str
        A JSON‑encoded dictionary mapping field names to validation
        constraints such as required, min, max, pattern, etc.

    Returns
    -------
    list[str]
        A list where each element is a string containing the rendered markup
        for a single form field, including any validation attributes derived
        from `validation_rules`.

    Raises
    ------
    ValueError
        Raised when either JSON input cannot be parsed or required keys are
        missing from the specifications.
    TypeError
        Raised when the provided arguments are not of type `str`.

    Examples
    --------
    >>> generate_form_components_with_validation(
    ...     form_specs='[{"name": "amount", "type": "number", "label":
    "Amount"}]',
    ...     validation_rules='{"amount": {"required": true, "min": 0}}'
    >>> )
    ["<input type='number' name='amount' label='Amount' required min='0' />"]

    >>> generate_form_components_with_validation(
    ...     form_specs='[{"name": "category", "type": "select", "label":
    "Category", "options": ["Food", "Travel"]}]',
    ...     validation_rules='{"category": {"required": true}}'
    >>> )
    ["<select name='category' label='Category'
    required><option>Food</option><option>Travel</option></select>"]

    """
    
    if not isinstance(form_specs, str):
        raise TypeError("form_specs must be of type str")
    if not isinstance(validation_rules, str):
        raise TypeError("validation_rules must be of type str")
    
    try:
        specs_list = json.loads(form_specs)
        rules_dict = json.loads(validation_rules)
    except json.JSONDecodeError:
        raise ValueError("JSON input cannot be parsed")
    
    components = []
    
    for spec in specs_list:
        if 'name' not in spec or 'type' not in spec:
            raise ValueError("Required keys are missing from the specifications")
        
        field_name = spec['name']
        field_type = spec['type']
        field_label = spec.get('label', '')
        field_placeholder = spec.get('placeholder', '')
        field_options = spec.get('options', [])
        
        validation = rules_dict.get(field_name, {})
        
        if field_type == 'select':
            attrs = [f"name='{field_name}'"]
            if field_label:
                attrs.append(f"label='{field_label}'")
            if validation.get('required', False):
                attrs.append('required')
            
            options_html = ''.join(f'<option>{option}</option>' for option in field_options)
            component = f"<select {' '.join(attrs)}>{options_html}</select>"
        else:
            attrs = [f"type='{field_type}'", f"name='{field_name}'"]
            if field_label:
                attrs.append(f"label='{field_label}'")
            if field_placeholder:
                attrs.append(f"placeholder='{field_placeholder}'")
            if validation.get('required', False):
                attrs.append('required')
            if 'min' in validation:
                attrs.append(f"min='{validation['min']}'")
            if 'max' in validation:
                attrs.append(f"max='{validation['max']}'")
            if 'pattern' in validation:
                attrs.append(f"pattern='{validation['pattern']}'")
            
            component = f"<input {' '.join(attrs)} />"
        
        components.append(component)
    
    return components