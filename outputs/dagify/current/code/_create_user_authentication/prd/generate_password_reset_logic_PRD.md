# generate_password_reset_logic PRD

## Description
Generates the source code for password reset functionality based on the provided authentication configuration.


## Conceptual Info

This shim creates the password‑reset module for the authentication system. It consumes a serialized authentication configuration (e.g., JSON) that describes how users are stored, what reset token strategy is used, and email settings, and it outputs ready‑to‑use source code that can be inserted into the compiled authentication package.

## Docstring

### Summary
Generate password‑reset source code from an authentication configuration.

### Parameters

- **config** (str): A JSON‑encoded string describing the authentication configuration required for password‑reset logic (e.g., user model, token expiry, email template, SMTP settings).

### Returns

str: A string of Python code that implements password‑reset routes, token generation/validation, and email dispatch according to the supplied configuration.

### Raises

- ValueError: If the configuration JSON is malformed or missing required keys such as `user_model`, `reset_token`, or `email_settings`.
- TypeError: If `config` is not a string.

### Examples

```python
>>> config = '{"user_model": "User", "reset_token": {"length": 32, "expiry_minutes": 15}, "email_settings": {"sender": "no-reply@example.com", "template": "reset_email.html"}}'
>>> code = generate_password_reset_logic(config)
'def reset_password(request):\n    # generated password‑reset logic...\n    ...'
```

```python
>>> config = '{"user_model": "Account", "reset_token": {"length": 64, "expiry_minutes": 30}, "email_settings": {"sender": "support@example.com", "template": "reset_template.txt"}}'
>>> code = generate_password_reset_logic(config)
'def reset_password(request):\n    # generated password‑reset logic for Account model...\n    ...'
```
