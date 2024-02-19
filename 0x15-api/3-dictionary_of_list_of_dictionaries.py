#!/usr/bin/python3
"""
Gathers data about an employee from a RESTful API

"""
import json
import requests
import sys


def get_employees_data():
    """
    Returns info about todo list progress.

    """
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos"
    users_url = f"{base_url}/users"

    """Get employee's data"""
    employee_response = requests.get(users_url)
    employee_data = employee_response.json()

    """Store all tasks for all employees"""
    all_tasks = {}

    """Loop throuh all users to get their tasks"""
    for employee in employee_data:
        employee_username = employee.get('username')
        user_id = employee.get('id')

        """Get employees todo list"""
        todo_response = requests.get(todos_url, params={'userId': user_id})
        todo_data = todo_response.json()

        """Order tasks in a dictionary"""
        tasks = []
        for todo in todo_data:
            task = {
                    'username': employee_username,
                    'task': todo.get('title'),
                    'completed': todo.get('completed')
            }
            tasks.append(task)
        all_tasks[user_id] = tasks

    """Write JSON data to file"""
    json_file = "todo_all_employees.json"
    with open(json_file, 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    get_employees_data()
