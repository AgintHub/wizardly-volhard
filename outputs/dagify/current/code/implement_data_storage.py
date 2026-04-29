from ._implement_data_storage.validate_required_tables import validate_required_tables
from ._implement_data_storage.initialize_database_connection import initialize_database_connection
from ._implement_data_storage.create_orm_models import create_orm_models
from ._implement_data_storage.create_database_tables import create_database_tables
from ._implement_data_storage.map_ui_components_to_endpoints import map_ui_components_to_endpoints
from ._implement_data_storage.generate_crud_handlers import generate_crud_handlers
from ._implement_data_storage.create_restful_endpoints import create_restful_endpoints
from ._implement_data_storage.register_endpoints_with_framework import register_endpoints_with_framework

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


class ImplementDataStorageOutput(BaseModel):
    """Pydantic model for implement_data_storage node outputs."""
    api_endpoints: List[str] = (
        Field(..., description="List of backend API endpoint definitions (e.g., /expenses, /users)")
    )


def implement_data_storage(design_ui_components_input: DesignUiComponentsOutput, set_backend_data_structure_input: SetBackendDataStructureOutput, **kwargs) -> ImplementDataStorageOutput:
    """
    Creates database tables and RESTful API endpoints for user and expense
    management, returning the list of exposed endpoint paths.

    Parameters
    ----------
    db_tables : List[str]
        Table definitions supplied by the parent node
        "set_backend_data_structure" (e.g., ['Users', 'Expenses',
        'Categories', 'Reports']).
    ui_components : List[str]
        UI component identifiers from "design_ui_components" that dictate
        which resources need corresponding endpoints (e.g., ['login_screen',
        'expense_form', 'report_dashboard']).

    Returns
    -------
    List[str]
        List of generated API endpoint paths, ready to be registered with
        the web framework (e.g., ['/users', '/expenses']).

    Raises
    ------
    ValueError
        If `db_tables` is empty or does not contain required tables such as
        'Users' or 'Expenses'.
    ConnectionError
        If the underlying database cannot be initialized or connected during
        the setup phase.

    Examples
    --------
    >>> api_endpoints = create_api_endpoints(
    ...     db_tables=['Users', 'Expenses', 'Categories', 'Reports'],
    ...     ui_components=['login_screen', 'expense_form', 'report_dashboard']
    >>> )
    ['/users', '/expenses', '/categories', '/reports']

    >>> create_api_endpoints(db_tables=[], ui_components=['login_screen'])
    ValueError: No database tables defined.

    """
    db_tables: List[str] = set_backend_data_structure_input.db_tables
    ui_components: List[str] = design_ui_components_input.ui_components
    
    validate_required_tables(db_tables=db_tables)
    
    initialize_database_connection()
    
    orm_models: dict = create_orm_models(db_tables=db_tables)
    
    create_database_tables(orm_models=orm_models)
    
    required_endpoints: List[str] = map_ui_components_to_endpoints(ui_components=ui_components, db_tables=db_tables)
    
    crud_handlers: dict = generate_crud_handlers(orm_models=orm_models)
    
    api_endpoints: List[str] = create_restful_endpoints(required_endpoints=required_endpoints, crud_handlers=crud_handlers)
    
    register_endpoints_with_framework(endpoints=api_endpoints)
    
    return ImplementDataStorageOutput(api_endpoints=api_endpoints)