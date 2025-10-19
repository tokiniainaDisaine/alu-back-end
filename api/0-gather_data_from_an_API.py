#!/usr/bin/python3
"""
fgbvd
"""
import requests
from sys import argv


def get_info(url):
    data = requests.get(url)
    return data.json()


def main(employee_id):
    """
    fgbjfnd
    """
    employee_info_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/"
    employee_todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    employee_info = get_info(employee_info_url)
    employee_todo = get_info(employee_todo_url)

    employee_name = employee_info.get("name")
    tasks = {todo.get("title"): todo.get("completed") for todo in employee_todo}

    task_number = len(tasks)
    completed_tasks = [completed for completed in tasks.values() if completed]
    completed_tasks_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({completed_tasks_count}/{task_number}):")
    for title, completed in tasks.items():
        if completed:
            print(f"\t {title}")


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
