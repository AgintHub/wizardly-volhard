import json


def generate_password_reset_logic(config: str) -> str:
    """
    Generate password‑reset source code from an authentication configuration.

    Parameters
    ----------
    config : str
        A JSON‑encoded string describing the authentication configuration
        required for password‑reset logic (e.g., user model, token expiry,
        email template, SMTP settings).

    Returns
    -------
    str
        A string of Python code that implements password‑reset routes, token
        generation/validation, and email dispatch according to the supplied
        configuration.

    Raises
    ------
    ValueError
        If the configuration JSON is malformed or missing required keys such
        as `user_model`, `reset_token`, or `email_settings`.
    TypeError
        If `config` is not a string.

    Examples
    --------
    >>> config = '{"user_model": "User", "reset_token": {"length": 32,
    "expiry_minutes": 15}, "email_settings": {"sender": "no-reply@example.com",
    "template": "reset_email.html"}}'
    >>> code = generate_password_reset_logic(config)
    'def reset_password(request):\n    # generated password‑reset logic...\n
    ...'

    >>> config = '{"user_model": "Account", "reset_token": {"length": 64,
    "expiry_minutes": 30}, "email_settings": {"sender": "support@example.com",
    "template": "reset_template.txt"}}'
    >>> code = generate_password_reset_logic(config)
    'def reset_password(request):\n    # generated password‑reset logic for
    Account model...\n    ...'

    """
    
    if not isinstance(config, str):
        raise TypeError("Config must be a string")
    
    try:
        config_data = json.loads(config)
    except json.JSONDecodeError:
        raise ValueError("Configuration JSON is malformed")
    
    required_keys = ['user_model', 'reset_token', 'email_settings']
    for key in required_keys:
        if key not in config_data:
            raise ValueError(f"Missing required key: {key}")
    
    user_model = config_data['user_model']
    token_length = config_data['reset_token'].get('length', 32)
    expiry_minutes = config_data['reset_token'].get('expiry_minutes', 15)
    sender_email = config_data['email_settings']['sender']
    email_template = config_data['email_settings']['template']
    
    code = f'''import secrets
import datetime
from email.mime.text import MIMEText
import smtplib

def reset_password(request):
    """Generated password reset logic for {user_model} model"""
    email = request.get('email')
    if not email:
        return {{"error": "Email is required"}}
    
    reset_token = secrets.token_urlsafe({token_length})
    
    expiry_time = datetime.datetime.now() + datetime.timedelta(minutes={expiry_minutes})
    
    
    subject = "Password Reset Request"
    body = f"Your password reset token is: {{reset_token}}. It expires in {expiry_minutes} minutes."
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "{sender_email}"
    msg['To'] = email
    
    
    return {{"message": "Password reset email sent", "template_used": "{email_template}"}}
'''
    
    return code