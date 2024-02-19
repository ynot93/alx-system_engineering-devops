#!/usr/bin/python3
"""
Gathers data about an employee from a RESTful API

"""
import requests
import sys
import csv


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

    """Export data to csv"""
    csv_file = f"{employee_id}.csv"
    with open(csv_file, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for todo in todo_data:
            csv_writer.writerow([
                employee_id,
                employee_name,
                todo.get('completed'),
                todo.get('title')
            ])


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_progress_data(employee_id)
