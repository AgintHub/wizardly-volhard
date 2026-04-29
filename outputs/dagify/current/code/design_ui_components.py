from ._design_ui_components.validate_requirements_input import validate_requirements_input
from ._design_ui_components.map_requirements_to_ui_patterns import map_requirements_to_ui_patterns
from ._design_ui_components.generate_component_names import generate_component_names
from ._design_ui_components.create_wireframe_descriptions import create_wireframe_descriptions
from ._design_ui_components.finalize_ui_components import finalize_ui_components

from pydantic import BaseModel, Field
from typing import List


class DefineAppFunctionalityRequirementsOutput(BaseModel):
    """Pydantic model for define_app_functionality_requirements node outputs."""
    requirements: List[str] = (
        Field(..., description="List of high\u2011level functional requirements for the expense tracker")
    )


class DesignUiComponentsOutput(BaseModel):
    """Pydantic model for design_ui_components node outputs."""
    ui_components: List[str] = (
        Field(..., description="Names of UI components and screens derived from the functional requirements")
    )


def design_ui_components(define_app_functionality_requirements_input: DefineAppFunctionalityRequirementsOutput, **kwargs) -> DesignUiComponentsOutput:
    """
    Create wireframes and enumerate UI component names for the expense‑tracker
    app.

    Parameters
    ----------
    requirements : List[str]
        High‑level functional requirements produced by
        `define_app_functionality_requirements`.

    Returns
    -------
    List[str]
        Names of UI components and screens derived from the functional
        requirements.

    Raises
    ------
    ValueError
        If `requirements` is empty or None.
    KeyError
        If a required functional requirement cannot be mapped to a UI
        component.

    Examples
    --------
    >>> requirements = [
    ...     "User authentication and login",
    ...     "Create, edit, and delete expense entries",
    ...     "View expense list with filtering",
    ...     "Generate expense summary reports",
    ...     "Configure user settings"
    >>> ]
    >>> ui_components = design_ui_components(requirements)
    ['LoginScreen', 'ExpenseEntryForm', 'ExpenseListView', 'ReportDashboard',
    'SettingsScreen']

    >>> design_ui_components([])
    ValueError: requirements list cannot be empty.

    """
    requirements: List[str] = define_app_functionality_requirements_input.requirements
    
    validated_requirements: List[str] = validate_requirements_input(requirements=requirements)
    
    requirement_mappings: dict = map_requirements_to_ui_patterns(requirements=validated_requirements)
    
    ui_component_names: List[str] = generate_component_names(mappings=requirement_mappings)
    
    wireframe_descriptions: List[str] = create_wireframe_descriptions(components=ui_component_names, requirements=validated_requirements)
    
    final_components: List[str] = finalize_ui_components(components=ui_component_names, wireframes=wireframe_descriptions)
    
    return DesignUiComponentsOutput(ui_components=final_components)