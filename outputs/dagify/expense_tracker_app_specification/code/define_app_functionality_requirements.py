from ._define_app_functionality_requirements.generate_expense_crud_requirements import generate_expense_crud_requirements
from ._define_app_functionality_requirements.generate_reporting_requirements import generate_reporting_requirements
from ._define_app_functionality_requirements.generate_user_account_requirements import generate_user_account_requirements
from ._define_app_functionality_requirements.generate_application_settings_requirements import generate_application_settings_requirements
from ._define_app_functionality_requirements.generate_additional_functionality_requirements import generate_additional_functionality_requirements
from ._define_app_functionality_requirements.consolidate_requirements import consolidate_requirements
from ._define_app_functionality_requirements.validate_requirements_completeness import validate_requirements_completeness

from pydantic import BaseModel, Field
from typing import List


class DefineAppFunctionalityRequirementsOutput(BaseModel):
    """Pydantic model for define_app_functionality_requirements node outputs."""
    requirements: List[str] = (
        Field(..., description="List of high\u2011level functional requirements for the expense tracker")
    )


def define_app_functionality_requirements(general_input: str, **kwargs) -> DefineAppFunctionalityRequirementsOutput:
    """
    Generate a list of core functional requirements for an expense‑tracker
    application.

    Returns
    -------
    List[str]
        A list of high‑level functional requirements covering expense
        management, reporting, user accounts, and settings.

    Raises
    ------
    RuntimeError
        If the requirement generation process fails unexpectedly.

    Examples
    --------
    >>> define_app_functionality_requirements()
    ['Expense entry', 'Expense editing', 'Expense deletion', 'Expense viewing',
    'Expense reports', 'User account management', 'Application settings']

    >>> requirements = define_app_functionality_requirements()
    >>> len(requirements)
    7

    """
    expense_operations: List[str] = generate_expense_crud_requirements()
    reporting_features: List[str] = generate_reporting_requirements()
    user_management: List[str] = generate_user_account_requirements()
    app_settings: List[str] = generate_application_settings_requirements()
    additional_features: List[str] = generate_additional_functionality_requirements(context=general_input)
    all_requirements: List[str] = consolidate_requirements(
        expense_ops=expense_operations,
        reporting=reporting_features, 
        user_mgmt=user_management,
        settings=app_settings,
        additional=additional_features
    )
    validated_requirements: List[str] = validate_requirements_completeness(requirements=all_requirements)
    return DefineAppFunctionalityRequirementsOutput(requirements=validated_requirements)