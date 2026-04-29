import re
from typing import List


def generate_additional_functionality_requirements(context: str) -> List[str]:
    """
    Generate additional high‑level functional requirements for the
    expense‑tracker app based on a free‑form context string.

    Parameters
    ----------
    context : str
        A free‑form description of any extra features, constraints, or
        stakeholder wishes that should be reflected in the requirement list.

    Returns
    -------
    list[str]
        A list of requirement statements, each a short sentence suitable for
        inclusion in the overall functional specification.

    Raises
    ------
    ValueError
        When the provided context string is empty or does not contain any
        recognizable feature information.
    TypeError
        When the input `context` is not of type `str`.

    Examples
    --------
    >>> generate_additional_functionality_requirements(context='Allow users to
    set recurring monthly budgets')
    ['Support recurring monthly budget creation for each user']

    >>> generate_additional_functionality_requirements(context='Integrate with
    Google Calendar for expense reminders')
    ['Sync expense due dates with Google Calendar and send reminder
    notifications']

    """
    if not isinstance(context, str):
        raise TypeError("The input `context` is not of type `str`.")
    
    if not context or not context.strip():
        raise ValueError("The provided context string is empty or does not contain any recognizable feature information.")
    
    
    context = context.strip().lower()
    requirements = []
    
    if re.search(r'budget|spending limit|financial limit', context):
        if 'recurring' in context or 'monthly' in context:
            requirements.append('Support recurring monthly budget creation for each user')
        else:
            requirements.append('Enable users to set and manage spending budgets')
    
    if re.search(r'calendar|google calendar|reminder|notification', context):
        requirements.append('Sync expense due dates with Google Calendar and send reminder notifications')
    
    if re.search(r'report|analytics|chart|graph|visualization', context):
        requirements.append('Generate detailed expense reports with visual analytics')
    
    if re.search(r'share|collaborate|team|group|family', context):
        requirements.append('Allow expense sharing and collaboration between multiple users')
    
    if re.search(r'receipt|photo|scan|image|attachment', context):
        requirements.append('Support receipt photo capture and automatic expense extraction')
    
    if re.search(r'export|import|csv|excel|backup', context):
        requirements.append('Provide data export and import functionality for expense records')
    
    if re.search(r'tax|deduction|business expense|irs', context):
        requirements.append('Categorize expenses for tax deduction tracking and reporting')
    
    if re.search(r'mobile|offline|sync|cloud', context):
        requirements.append('Support offline expense entry with cloud synchronization')
    
    if re.search(r'currency|international|exchange rate|multi.currency', context):
        requirements.append('Handle multiple currencies with automatic exchange rate conversion')
    
    if re.search(r'security|encryption|privacy|authentication', context):
        requirements.append('Implement secure user authentication and data encryption')
    
    if not requirements:
        requirements.append('Implement additional user-requested functionality based on provided specifications')
    
    return requirements