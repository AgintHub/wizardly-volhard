from ._write_tests.validate_required_inputs import validate_required_inputs
from ._write_tests.generate_input_validation_tests import generate_input_validation_tests
from ._write_tests.generate_crud_operation_tests import generate_crud_operation_tests
from ._write_tests.generate_authentication_flow_tests import generate_authentication_flow_tests
from ._write_tests.generate_ui_rendering_tests import generate_ui_rendering_tests
from ._write_tests.generate_report_calculation_tests import generate_report_calculation_tests
from ._write_tests.compile_comprehensive_test_suite import compile_comprehensive_test_suite

from pydantic import BaseModel, Field
from typing import List


class ImplementDataInputOutput(BaseModel):
    """Pydantic model for implement_data_input node outputs."""
    frontend_forms: List[str] = (
        Field(..., description="Names of frontend form components for expense entry")
    )


class ImplementDataStorageOutput(BaseModel):
    """Pydantic model for implement_data_storage node outputs."""
    api_endpoints: List[str] = (
        Field(..., description="List of backend API endpoint definitions (e.g., /expenses, /users)")
    )


class CreateUserAuthenticationOutput(BaseModel):
    """Pydantic model for create_user_authentication node outputs."""
    auth_module: str = (
        Field(..., description="Identifier or filename of the authentication module/code")
    )


class DevelopExpenseViewOutput(BaseModel):
    """Pydantic model for develop_expense_view node outputs."""
    expense_view_component: str = (
        Field(..., description="Identifier or filename of the expense list UI component")
    )


class DevelopSummaryReportsOutput(BaseModel):
    """Pydantic model for develop_summary_reports node outputs."""
    report_dashboard_component: str = (
        Field(..., description="Identifier or filename of the report dashboard component")
    )


class WriteTestsOutput(BaseModel):
    """Pydantic model for write_tests node outputs."""
    test_suite: List[str] = (
        Field(..., description="List of test case identifiers or filenames covering the app")
    )


def write_tests(implement_data_input_input: ImplementDataInputOutput, implement_data_storage_input: ImplementDataStorageOutput, create_user_authentication_input: CreateUserAuthenticationOutput, develop_expense_view_input: DevelopExpenseViewOutput, develop_summary_reports_input: DevelopSummaryReportsOutput, **kwargs) -> WriteTestsOutput:
    """
    Generate a list of test case identifiers covering all functional components
    of the expense‑tracker app.

    Parameters
    ----------
    frontend_forms : List[str]
        Identifiers or filenames of the expense entry form components
        produced by `implement_data_input`.
    api_endpoints : List[str]
        Backend API endpoint paths (e.g., "/expenses", "/users") generated
        by `implement_data_storage`.
    auth_module : str
        Identifier or filename of the authentication module created by
        `create_user_authentication`.
    expense_view_component : str
        Identifier or filename of the UI component that displays the expense
        list, from `develop_expense_view`.
    report_dashboard_component : str
        Identifier or filename of the report/dashboard component generated
        by `develop_summary_reports`.

    Returns
    -------
    List[str]
        A list of test case identifiers or filenames that collectively
        validate the entire application.

    Raises
    ------
    ValueError
        If any required input collection is empty or None, indicating
        missing upstream artifacts.

    Examples
    --------
    >>> generate_test_suite(
    ...     frontend_forms=["expense_form.py"],
    ...     api_endpoints=["/expenses", "/users"],
    ...     auth_module="auth.py",
    ...     expense_view_component="expense_view.py",
    ...     report_dashboard_component="report_dashboard.py"
    >>> )
    ["test_input_validation.py", "test_crud_operations.py", "test_auth_flow.py",
    "test_ui_rendering.py", "test_report_calculations.py"]

    """
    validate_required_inputs(
        frontend_forms=implement_data_input_input.frontend_forms,
        api_endpoints=implement_data_storage_input.api_endpoints,
        auth_module=create_user_authentication_input.auth_module,
        expense_view_component=develop_expense_view_input.expense_view_component,
        report_dashboard_component=develop_summary_reports_input.report_dashboard_component
    )
    
    input_validation_tests: List[str] = generate_input_validation_tests(
        frontend_forms=implement_data_input_input.frontend_forms
    )
    
    crud_operation_tests: List[str] = generate_crud_operation_tests(
        api_endpoints=implement_data_storage_input.api_endpoints
    )
    
    auth_flow_tests: List[str] = generate_authentication_flow_tests(
        auth_module=create_user_authentication_input.auth_module
    )
    
    ui_rendering_tests: List[str] = generate_ui_rendering_tests(
        expense_view_component=develop_expense_view_input.expense_view_component
    )
    
    report_calculation_tests: List[str] = generate_report_calculation_tests(
        report_dashboard_component=develop_summary_reports_input.report_dashboard_component
    )
    
    comprehensive_test_suite: List[str] = compile_comprehensive_test_suite(
        input_tests=input_validation_tests,
        crud_tests=crud_operation_tests,
        auth_tests=auth_flow_tests,
        ui_tests=ui_rendering_tests,
        report_tests=report_calculation_tests
    )
    
    return WriteTestsOutput(test_suite=comprehensive_test_suite)