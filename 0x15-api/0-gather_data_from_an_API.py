#!/usr/bin/python3
"""
Gathers data about an employee from a RESTful API

"""
import requests
import sys


def get_employee_progress_data(employee_id):
    """
    Returns info about todo list progress.

    """
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    user_url = f"{base_url}/users/{employee_id}"

    """Get employee's data"""
    employee_response = requests.get(user_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get('name')

    """Get TODO list data of the employee"""
    todo_response = requests.get(todos_url)
    todo_data = todo_response.json()

    """Perform calculations"""
    total_tasks = len(todo_data)
    completed_tasks = 0
    for todo in todo_data:
        if todo.get('completed') is True:
            completed_tasks += 1

    """Print data"""
    print(
            f"Employee {employee_name} is done with tasks"
            f"({completed_tasks}/{total_tasks}):"
    )
    for todo in todo_data:
        if todo.get('completed') is True:
            print(f"\t {todo.get('title')}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_progress_data(employee_id)
