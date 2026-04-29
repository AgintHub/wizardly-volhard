from ._implement_data_input.validate_required_inputs import validate_required_inputs
from ._implement_data_input.synthesize_ui_and_backend_specs import synthesize_ui_and_backend_specs
from ._implement_data_input.derive_client_side_validation_rules import derive_client_side_validation_rules
from ._implement_data_input.generate_form_components_with_validation import generate_form_components_with_validation

from pydantic import BaseModel, Field
from typing import List


class DesignUiComponentsOutput(BaseModel):
    """Pydantic model for design_ui_components node outputs."""
    ui_components: List[str] = (
        Field(..., description="Names of UI components and screens derived from the functional requirements")
    )


class SetBackendDataStructureOutput(BaseModel):
    """Pydantic model for set_backend_data_structure node outputs."""
    db_tables: List[str] = (
        Field(..., description="List of database table definitions (e.g., Users, Expenses, Categories, Reports)")
    )


class ImplementDataInputOutput(BaseModel):
    """Pydantic model for implement_data_input node outputs."""
    frontend_forms: List[str] = (
        Field(..., description="Names of frontend form components for expense entry")
    )


def implement_data_input(design_ui_components_input: DesignUiComponentsOutput, set_backend_data_structure_input: SetBackendDataStructureOutput, **kwargs) -> ImplementDataInputOutput:
    """
    Create expense‑entry form components with client‑side validation based on UI
    specs and backend schema.

    Parameters
    ----------
    ui_components : List[str]
        List of UI component names produced by the design_ui_components node
        (e.g., ['ExpenseForm', 'DatePicker']).
    db_tables : List[str]
        List of database table definitions from the
        set_backend_data_structure node (e.g., ['Users', 'Expenses',
        'Categories']).

    Returns
    -------
    List[str]
        Names of the generated frontend form components ready for
        integration (e.g., ['ExpenseFormComponent']).

    Raises
    ------
    ValueError
        If required UI components or database table definitions are missing,
        or if validation rules cannot be derived.

    Examples
    --------
    >>> ui = ['ExpenseForm', 'DatePicker', 'CategoryDropdown']
    >>> tables = ['Users', 'Expenses', 'Categories']
    >>> forms = generate_frontend_forms(ui, tables)
    ['ExpenseFormComponent']

    >>> generate_frontend_forms([], ['Expenses'])
    ValueError: UI component specifications are required to create forms.

    """
    ui_components: List[str] = design_ui_components_input.ui_components
    db_tables: List[str] = set_backend_data_structure_input.db_tables
    
    validate_required_inputs(ui_components=ui_components, db_tables=db_tables)
    
    form_specifications: List[dict] = synthesize_ui_and_backend_specs(ui_components=ui_components, db_tables=db_tables)
    
    validation_rules: dict = derive_client_side_validation_rules(db_tables=db_tables)
    
    frontend_form_components: List[str] = generate_form_components_with_validation(form_specs=form_specifications, validation_rules=validation_rules)
    
    return ImplementDataInputOutput(frontend_forms=frontend_form_components)