from ._create_user_authentication.validate_required_auth_components import validate_required_auth_components
from ._create_user_authentication.generate_auth_configuration import generate_auth_configuration
from ._create_user_authentication.generate_user_registration_logic import generate_user_registration_logic
from ._create_user_authentication.generate_login_logout_logic import generate_login_logout_logic
from ._create_user_authentication.generate_password_reset_logic import generate_password_reset_logic
from ._create_user_authentication.generate_session_management_logic import generate_session_management_logic
from ._create_user_authentication.generate_ui_integration_code import generate_ui_integration_code
from ._create_user_authentication.compile_auth_module import compile_auth_module

from pydantic import BaseModel, Field
from typing import List


class DesignUiComponentsOutput(BaseModel):
    """Pydantic model for design_ui_components node outputs."""
    ui_components: List[str] = (
        Field(..., description="Names of UI components and screens derived from the functional requirements")
    )


class CreateUserAuthenticationOutput(BaseModel):
    """Pydantic model for create_user_authentication node outputs."""
    auth_module: str = (
        Field(..., description="Identifier or filename of the authentication module/code")
    )


def create_user_authentication(design_ui_components_input: DesignUiComponentsOutput, **kwargs) -> CreateUserAuthenticationOutput:
    """
    Create an authentication module based on UI component specifications.

    Parameters
    ----------
    ui_components : list[str]
        List of UI component names produced by the design_ui_components node
        (e.g., ['login_screen', 'signup_form']).

    Returns
    -------
    str
        Path or identifier of the generated authentication module (e.g.,
        'auth.py').

    Raises
    ------
    ValueError
        If required UI components for authentication (e.g., 'login_screen')
        are missing from ui_components.
    RuntimeError
        If the authentication module cannot be generated due to internal
        errors.

    Examples
    --------
    >>> ui = ['login_screen', 'signup_form', 'settings_page']
    >>> auth_path = create_auth_module(ui)
    'auth.py'

    >>> ui = ['dashboard', 'expense_list']
    >>> create_auth_module(ui)
    ValueError: Missing required authentication UI components: login_screen

    """
    ui_components: List[str] = design_ui_components_input.ui_components
    
    required_components: List[str] = validate_required_auth_components(ui_components=ui_components)
    
    auth_config: dict = generate_auth_configuration(ui_components=ui_components)
    
    registration_code: str = generate_user_registration_logic(config=auth_config)
    
    login_code: str = generate_login_logout_logic(config=auth_config)
    
    password_reset_code: str = generate_password_reset_logic(config=auth_config)
    
    session_management_code: str = generate_session_management_logic(config=auth_config)
    
    ui_integration_code: str = generate_ui_integration_code(ui_components=ui_components, config=auth_config)
    
    auth_module_path: str = compile_auth_module(registration=registration_code, login=login_code, password_reset=password_reset_code, session_management=session_management_code, ui_integration=ui_integration_code)
    
    return CreateUserAuthenticationOutput(auth_module=auth_module_path)