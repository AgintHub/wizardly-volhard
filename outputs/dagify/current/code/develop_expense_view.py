from ._develop_expense_view.validate_required_ui_component import validate_required_ui_component
from ._develop_expense_view.validate_required_api_endpoint import validate_required_api_endpoint
from ._develop_expense_view.define_expense_list_component_structure import define_expense_list_component_structure
from ._develop_expense_view.implement_expense_filtering_functionality import implement_expense_filtering_functionality
from ._develop_expense_view.implement_expense_sorting_functionality import implement_expense_sorting_functionality
from ._develop_expense_view.implement_inline_crud_operations import implement_inline_crud_operations
from ._develop_expense_view.generate_expense_list_component_code import generate_expense_list_component_code
from ._develop_expense_view.save_component_to_file import save_component_to_file

from pydantic import BaseModel, Field
from typing import List


class DesignUiComponentsOutput(BaseModel):
    """Pydantic model for design_ui_components node outputs."""
    ui_components: List[str] = (
        Field(..., description="Names of UI components and screens derived from the functional requirements")
    )


class ImplementDataStorageOutput(BaseModel):
    """Pydantic model for implement_data_storage node outputs."""
    api_endpoints: List[str] = (
        Field(..., description="List of backend API endpoint definitions (e.g., /expenses, /users)")
    )


class DevelopExpenseViewOutput(BaseModel):
    """Pydantic model for develop_expense_view node outputs."""
    expense_view_component: str = (
        Field(..., description="Identifier or filename of the expense list UI component")
    )


def develop_expense_view(design_ui_components_input: DesignUiComponentsOutput, implement_data_storage_input: ImplementDataStorageOutput, **kwargs) -> DevelopExpenseViewOutput:
    """
    Creates the expense‑list UI component with full CRUD capabilities and
    returns its identifier.

    Parameters
    ----------
    ui_components : List[str]
        List of UI component names produced by the design_ui_components node
        (e.g., ['LoginScreen', 'ExpenseEntryForm', 'ExpenseList']).
    api_endpoints : List[str]
        List of backend API endpoint paths produced by the
        implement_data_storage node (e.g., ['/expenses', '/users']).

    Returns
    -------
    str
        The filename or identifier of the generated expense‑list component
        (e.g., 'ExpenseList.jsx').

    Raises
    ------
    ValueError
        If the required UI component name for the expense list is missing
        from ui_components.
    RuntimeError
        If the necessary '/expenses' API endpoint is not present in
        api_endpoints.

    Examples
    --------
    >>> component_id = develop_expense_view(
    ...     ui_components=['LoginScreen', 'ExpenseEntryForm', 'ExpenseList'],
    ...     api_endpoints=['/expenses', '/users']
    >>> )
    'ExpenseList.jsx'

    >>> develop_expense_view(
    ...     ui_components=['LoginScreen', 'ExpenseEntryForm'],
    ...     api_endpoints=['/expenses']
    >>> )
    ValueError: Required UI component 'ExpenseList' not found.

    """
    ui_components: List[str] = design_ui_components_input.ui_components
    api_endpoints: List[str] = implement_data_storage_input.api_endpoints
    
    validate_required_ui_component(ui_components=ui_components, required_component="ExpenseList")
    validate_required_api_endpoint(api_endpoints=api_endpoints, required_endpoint="/expenses")
    
    component_structure: dict = define_expense_list_component_structure()
    filtering_logic: str = implement_expense_filtering_functionality()
    sorting_logic: str = implement_expense_sorting_functionality()
    crud_operations: dict = implement_inline_crud_operations(api_endpoints=api_endpoints)
    
    component_code: str = generate_expense_list_component_code(
        structure=component_structure,
        filtering=filtering_logic,
        sorting=sorting_logic,
        crud_ops=crud_operations
    )
    
    component_filename: str = save_component_to_file(component_code=component_code, component_name="ExpenseList")
    
    return DevelopExpenseViewOutput(expense_view_component=component_filename)