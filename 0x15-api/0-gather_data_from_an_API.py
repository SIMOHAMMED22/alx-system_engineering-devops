#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    base_url = (
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    )
    user_url = (
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    )

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to fetch user info for ID {employee_id}")
        return

    user_data = user_response.json()
    employee_name = user_data['name']

    todos_response = requests.get(base_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch TODO list for ID {employee_id}")
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]
    num_completed_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks "
        f"({num_completed_tasks}/{total_tasks}):"
    )
    print(f"{employee_name}: {num_completed_tasks}/{total_tasks}")

    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_progress(employee_id)
