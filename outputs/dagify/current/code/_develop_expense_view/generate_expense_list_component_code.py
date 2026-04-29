import json


def generate_expense_list_component_code(structure: str, filtering: str, sorting: str, crud_ops: str) -> str:
    """
    Generate the source code for the ExpenseList component using provided
    structure and logic fragments.

    Parameters
    ----------
    structure : str
        A JSON‑serialised or otherwise stringified representation of the
        component's UI layout (e.g., columns, rows, widget hierarchy).
    filtering : str
        A string containing the JavaScript/TypeScript (or equivalent) code
        that implements expense filtering based on user criteria.
    sorting : str
        A string containing the code that sorts the expense list (e.g., by
        date, amount) in the desired order.
    crud_ops : str
        A stringified object or code block defining inline Create, Read,
        Update, Delete operations that interact with the `/expenses` API
        endpoint.

    Returns
    -------
    str
        A single string representing the complete source code of the
        ExpenseList component, ready to be written to a file.

    Raises
    ------
    ValueError
        If any of the input strings are empty or missing required
        placeholders for integration.
    TypeError
        If any of the inputs are not of type `str`.

    Examples
    --------
    >>> generate_expense_list_component_code(
    ...     structure='{'layout':'table','columns':['Date','Amount','Status']}',
    ...     filtering='expense => expense.status === "Approved"',
    ...     sorting='(a,b) => new Date(b.date) - new Date(a.date)',
    ...     crud_ops='{'create':..., 'read':..., 'update':..., 'delete':...}'
    >>> )
    '<ComponentCode string containing the assembled ExpenseList component>'

    >>> generate_expense_list_component_code(
    ...     structure='{'layout':'list','itemTemplate':'<li>{name}</li'}',
    ...     filtering='exp => true',
    ...     sorting='(a,b)=>0',
    ...     crud_ops='{}'
    >>> )
    '<ComponentCode string for a minimal list component>'

    """
    
    if not isinstance(structure, str) or not isinstance(filtering, str) or not isinstance(sorting, str) or not isinstance(crud_ops, str):
        raise TypeError("All inputs must be of type str")
    
    if not structure.strip() or not filtering.strip() or not sorting.strip() or not crud_ops.strip():
        raise ValueError("Input strings cannot be empty or missing required placeholders for integration")
    
    try:
        structure_obj = json.loads(structure)
    except json.JSONDecodeError:
        structure_obj = structure
    
    try:
        crud_ops_obj = json.loads(crud_ops)
    except json.JSONDecodeError:
        crud_ops_obj = crud_ops
    
    component_template = '''
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ExpenseList = () => {
  const [expenses, setExpenses] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // CRUD Operations
  const crudOperations = {crud_operations};

  // Filtering logic
  const filterExpenses = (expenseList) => {
    return expenseList.filter({filtering_logic});
  };

  // Sorting logic
  const sortExpenses = (expenseList) => {
    return expenseList.sort({sorting_logic});
  };

  // Fetch expenses
  useEffect(() => {
    const fetchExpenses = async () => {
      setLoading(true);
      try {
        const response = await axios.get('/expenses');
        let fetchedExpenses = response.data;
        fetchedExpenses = filterExpenses(fetchedExpenses);
        fetchedExpenses = sortExpenses(fetchedExpenses);
        setExpenses(fetchedExpenses);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    fetchExpenses();
  }, []);

  // Create expense
  const createExpense = async (expenseData) => {
    try {
      const response = await axios.post('/expenses', expenseData);
      setExpenses(prev => [...prev, response.data]);
    } catch (err) {
      setError(err.message);
    }
  };

  // Update expense
  const updateExpense = async (id, expenseData) => {
    try {
      const response = await axios.put(`/expenses/${id}`, expenseData);
      setExpenses(prev => prev.map(exp => exp.id === id ? response.data : exp));
    } catch (err) {
      setError(err.message);
    }
  };

  // Delete expense
  const deleteExpense = async (id) => {
    try {
      await axios.delete(`/expenses/${id}`);
      setExpenses(prev => prev.filter(exp => exp.id !== id));
    } catch (err) {
      setError(err.message);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="expense-list">
      {component_structure}
    </div>
  );
};

export default ExpenseList;
'''
    
    if isinstance(structure_obj, dict) and 'layout' in structure_obj:
        if structure_obj['layout'] == 'table':
            columns = structure_obj.get('columns', ['Date', 'Amount', 'Status'])
            structure_html = f'''
      <table className="expense-table">
        <thead>
          <tr>
            {' '.join([f'<th key="{col}">{col}</th>' for col in columns])}
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {{expenses.map(expense => (
            <tr key={{expense.id}}>
              {' '.join([f'<td>{{expense.{col.lower()}}}</td>' for col in columns])}
              <td>
                <button onClick={{() => updateExpense(expense.id, expense)}}>Edit</button>
                <button onClick={{() => deleteExpense(expense.id)}}>Delete</button>
              </td>
            </tr>
          ))}}
        </tbody>
      </table>'''
        elif structure_obj['layout'] == 'list':
            item_template = structure_obj.get('itemTemplate', '<li>{name}</li>')
            structure_html = f'''
      <ul className="expense-list">
        {{expenses.map(expense => (
          <li key={{expense.id}}>
            {item_template.replace('{name}', '{expense.name}').replace('{', '{').replace('}', '}')}
            <button onClick={{() => updateExpense(expense.id, expense)}}>Edit</button>
            <button onClick={{() => deleteExpense(expense.id)}}>Delete</button>
          </li>
        ))}}
      </ul>'''
        else:
            structure_html = '<div>{JSON.stringify(expenses)}</div>'
    else:
        structure_html = '<div>{JSON.stringify(expenses)}</div>'
    
    crud_operations_str = json.dumps(crud_ops_obj) if isinstance(crud_ops_obj, dict) else str(crud_ops_obj)
    
    final_code = component_template.replace('{crud_operations}', crud_operations_str)
    final_code = final_code.replace('{filtering_logic}', filtering)
    final_code = final_code.replace('{sorting_logic}', sorting)
    final_code = final_code.replace('{component_structure}', structure_html)
    
    return final_code