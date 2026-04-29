import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.define_app_functionality_requirements import define_app_functionality_requirements
from code.design_ui_components import design_ui_components
from code.set_backend_data_structure import set_backend_data_structure
from code.implement_data_storage import implement_data_storage
from code.create_user_authentication import create_user_authentication
from code.implement_data_input import implement_data_input
from code.develop_expense_view import develop_expense_view
from code.develop_summary_reports import develop_summary_reports
from code.write_tests import write_tests

# Get async mode from environment variable or default to False
ASYNC_MODE = os.environ.get('ASYNC_MODE', '').lower() in ('true', '1', 'yes', 'y')

def make_async(func):
    """Convert a synchronous function to an asynchronous function.

    If the function is already asynchronous, return it unchanged.
    If the function is synchronous, wrap it in an async function.
    """
    # If it's already a coroutine function, return it as is
    if inspect.iscoroutinefunction(func):
        return func

    # Otherwise, wrap it as an async function
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return async_wrapper

define_app_functionality_requirements_async = make_async(define_app_functionality_requirements)
design_ui_components_async = make_async(design_ui_components)
set_backend_data_structure_async = make_async(set_backend_data_structure)
implement_data_storage_async = make_async(implement_data_storage)
create_user_authentication_async = make_async(create_user_authentication)
implement_data_input_async = make_async(implement_data_input)
develop_expense_view_async = make_async(develop_expense_view)
develop_summary_reports_async = make_async(develop_summary_reports)
write_tests_async = make_async(write_tests)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: define_app_functionality_requirements
    async def run_define_app_functionality_requirements():
        # Call the async version of define_app_functionality_requirements with results from dependencies
        return await define_app_functionality_requirements_async(user_input)

    # Run level 0 nodes in parallel
    results['define_app_functionality_requirements'] = await run_define_app_functionality_requirements()

    # Level 1: design_ui_components, set_backend_data_structure
    async def run_design_ui_components():
        # Call the async version of design_ui_components with results from dependencies
        return await design_ui_components_async(results['define_app_functionality_requirements'])

    async def run_set_backend_data_structure():
        # Call the async version of set_backend_data_structure with results from dependencies
        return await set_backend_data_structure_async(results['define_app_functionality_requirements'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_design_ui_components(), run_set_backend_data_structure())
    results['design_ui_components'] = level_1_results[0]
    results['set_backend_data_structure'] = level_1_results[1]

    # Level 2: create_user_authentication, implement_data_input, implement_data_storage
    async def run_create_user_authentication():
        # Call the async version of create_user_authentication with results from dependencies
        return await create_user_authentication_async(results['design_ui_components'])

    async def run_implement_data_input():
        # Call the async version of implement_data_input with results from dependencies
        return await implement_data_input_async(results['design_ui_components'], results['set_backend_data_structure'])

    async def run_implement_data_storage():
        # Call the async version of implement_data_storage with results from dependencies
        return await implement_data_storage_async(results['design_ui_components'], results['set_backend_data_structure'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_create_user_authentication(), run_implement_data_input(), run_implement_data_storage())
    results['create_user_authentication'] = level_2_results[0]
    results['implement_data_input'] = level_2_results[1]
    results['implement_data_storage'] = level_2_results[2]

    # Level 3: develop_expense_view, develop_summary_reports
    async def run_develop_expense_view():
        # Call the async version of develop_expense_view with results from dependencies
        return await develop_expense_view_async(results['design_ui_components'], results['implement_data_storage'])

    async def run_develop_summary_reports():
        # Call the async version of develop_summary_reports with results from dependencies
        return await develop_summary_reports_async(results['design_ui_components'], results['implement_data_storage'])

    # Run level 3 nodes in parallel
    level_3_results = await asyncio.gather(run_develop_expense_view(), run_develop_summary_reports())
    results['develop_expense_view'] = level_3_results[0]
    results['develop_summary_reports'] = level_3_results[1]

    # Level 4: write_tests
    async def run_write_tests():
        # Call the async version of write_tests with results from dependencies
        return await write_tests_async(results['implement_data_input'], results['implement_data_storage'], results['create_user_authentication'], results['develop_expense_view'], results['develop_summary_reports'])

    # Run level 4 nodes in parallel
    results['write_tests'] = await run_write_tests()

    # Return all results
    return results

def run_workflow_sync(user_input: str) -> Dict[str, Any]:
    """Synchronous wrapper around the async workflow execution."""
    return asyncio.run(run_workflow(user_input))

def main():
    """Main entry point.

    Handles arguments in the following priority:
    1. Command-line argument (sys.argv[1])
    2. If no argument, uses empty string as input but displays a warning.
    """
    # Get user input from command line or use empty string
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # No input provided - display help message but continue with empty string
        print('Warning: No input provided. Using empty string as input.')
        print('For better results, provide an input argument:')
        print(f'  python {os.path.basename(__file__)} "your input text here"')
        print('Or use a file as input:')
        print(f'  python {os.path.basename(__file__)} "$(cat input.txt)"')
        user_input = ""

    print(f'Running workflow with input: {user_input}')

    # Run the workflow
    results = run_workflow_sync(user_input)

    # Print results
    try:
        # Convert results to JSON
        json_results = json.dumps(results, indent=2, default=str)
        print(json_results)
    except (TypeError, ValueError) as e:
        print(f'Results could not be converted to JSON: {e}')
        print(f'Raw results: {results}')

    return results

if __name__ == '__main__':
    main()
