from ._set_backend_data_structure.validate_requirements import validate_requirements
from ._set_backend_data_structure.identify_core_domains import identify_core_domains
from ._set_backend_data_structure.generate_users_table import generate_users_table
from ._set_backend_data_structure.generate_categories_table import generate_categories_table
from ._set_backend_data_structure.generate_expenses_table import generate_expenses_table
from ._set_backend_data_structure.generate_reports_table import generate_reports_table

from pydantic import BaseModel, Field
from typing import List


class DefineAppFunctionalityRequirementsOutput(BaseModel):
    """Pydantic model for define_app_functionality_requirements node outputs."""
    requirements: List[str] = (
        Field(..., description="List of high\u2011level functional requirements for the expense tracker")
    )


class SetBackendDataStructureOutput(BaseModel):
    """Pydantic model for set_backend_data_structure node outputs."""
    db_tables: List[str] = (
        Field(..., description="List of database table definitions (e.g., Users, Expenses, Categories, Reports)")
    )


def set_backend_data_structure(define_app_functionality_requirements_input: DefineAppFunctionalityRequirementsOutput, **kwargs) -> SetBackendDataStructureOutput:
    """
    Generates SQL CREATE TABLE statements for the core data model of the
    expense‑tracker app from functional requirements.

    Parameters
    ----------
    requirements : List[str]
        High‑level functional requirements produced by the
        define_app_functionality_requirements node.

    Returns
    -------
    List[str]
        SQL CREATE TABLE statements (as strings) for Users, Expenses,
        Categories, and Reports.

    Raises
    ------
    ValueError
        If the requirements list is empty or lacks any core domain needed to
        infer the schema.

    Examples
    --------
    >>> generate_schema(['User authentication', 'Expense entry', 'Reporting'])
    ["CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT
    NOT NULL, password_hash TEXT NOT NULL);", "CREATE TABLE Categories (id
    INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);", "CREATE TABLE
    Expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL, amount REAL NOT NULL, date TEXT NOT NULL,
    description TEXT, FOREIGN KEY(user_id) REFERENCES Users(id), FOREIGN
    KEY(category_id) REFERENCES Categories(id));", "CREATE TABLE Reports (id
    INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, report_type
    TEXT NOT NULL, generated_at TEXT NOT NULL, FOREIGN KEY(user_id) REFERENCES
    Users(id));"]

    >>> generate_schema([])
    ValueError: Requirements list cannot be empty.

    """
    requirements = define_app_functionality_requirements_input.requirements
    
    validated_requirements: List[str] = validate_requirements(requirements=requirements)
    
    core_domains: List[str] = identify_core_domains(requirements=validated_requirements)
    
    users_table_sql: str = generate_users_table(domains=core_domains)
    
    categories_table_sql: str = generate_categories_table(domains=core_domains)
    
    expenses_table_sql: str = generate_expenses_table(domains=core_domains)
    
    reports_table_sql: str = generate_reports_table(domains=core_domains)
    
    db_tables = [users_table_sql, categories_table_sql, expenses_table_sql, reports_table_sql]
    
    return SetBackendDataStructureOutput(db_tables=db_tables)