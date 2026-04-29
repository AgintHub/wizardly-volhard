# create_restful_endpoints PRD

## Description
Generates a list of RESTful API endpoint definitions from required endpoint names and CRUD handler specifications.


## Conceptual Info

This shim translates high‑level UI‑driven endpoint requirements and CRUD handler mappings into concrete RESTful route definitions that can be registered with a web framework.

## Docstring

### Summary
Create RESTful endpoint strings from required endpoint names and CRUD handler definitions.

### Parameters

- **required_endpoints** (str): A JSON‑encoded string list of endpoint base paths (e.g., "[\"/users\", \"/expenses\"]").
- **crud_handlers** (str): A JSON‑encoded string mapping each resource name to its CRUD handler identifier (e.g., "{\"users\": \"UserModel\", \"expenses\": \"ExpenseModel\"}").

### Returns

list[str]: A list of fully qualified RESTful endpoint definitions (e.g., ["GET /users", "POST /users", "GET /expenses", "POST /expenses"]).

### Raises

- ValueError: If the JSON strings cannot be parsed or required endpoint entries are missing.
- TypeError: If the parsed structures are not of the expected types (list for required_endpoints, dict for crud_handlers).

### Examples

```python
>>> create_restful_endpoints('["/users","/expenses"]', '{"users":"UserModel","expenses":"ExpenseModel"}')
["GET /users", "POST /users", "GET /expenses", "POST /expenses"]
```

```python
>>> create_restful_endpoints('["/reports"]', '{"reports":"ReportModel"}')
["GET /reports", "POST /reports"]
```
