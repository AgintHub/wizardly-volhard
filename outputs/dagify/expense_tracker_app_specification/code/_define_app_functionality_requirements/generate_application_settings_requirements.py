from typing import List


def generate_application_settings_requirements() -> List[str]:
    """
    Return high‑level functional requirements for the application‑settings
    component of the expense‑tracker system.

    Returns
    -------
    List[str]
        A list where each element is a short, declarative sentence
        describing a required settings feature (e.g., theme selection,
        currency configuration).

    Raises
    ------
    ValueError
        If internal generation logic fails to produce any requirement
        strings.
    TypeError
        If the function is called with unexpected positional or keyword
        arguments.

    Examples
    --------
    >>> generate_application_settings_requirements()
    ['User can select dark or light theme', 'Currency display can be set per
    user', 'Notification preferences are configurable', 'Settings are persisted
    across sessions']

    >>> generate_application_settings_requirements()
    ['App supports multiple language selections', 'User can enable or disable
    automatic backups', 'Privacy settings allow data export control']

    """
    requirements = [
        "User can select dark or light theme",
        "Currency display can be set per user",
        "Notification preferences are configurable",
        "Settings are persisted across sessions",
        "App supports multiple language selections",
        "User can enable or disable automatic backups",
        "Privacy settings allow data export control",
        "Default expense categories can be customized",
        "Date and time format preferences are configurable",
        "User can set spending limit alerts",
        "Export format preferences can be specified",
        "Authentication settings support biometric options"
    ]
    
    if not requirements:
        raise ValueError("Failed to generate any requirement strings")
    
    return requirements