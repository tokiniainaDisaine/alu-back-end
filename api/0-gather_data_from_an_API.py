#!/usr/bin/python3
"""
fgbvd
"""
import requests
from sys import argv


def main(employee_id):
    """
    fgbjfnd
    """
    api_url = "https://jsonplaceholder.typicode.com/users"

    employee_info_url = f"{api_url}/{employee_id}/"
    employee_todo_url = f"{api_url}/{employee_id}/todos"

    employee_info = requests.get(employee_info_url).json()
    employee_todo = requests.get(employee_todo_url)

    employee_name = employee_info.get("name")
    tasks = ({todo.get("title"):
              todo.get("completed")
              for todo in employee_todo})

    task_number = len(tasks)
    completed_tasks = ([completed
                        for completed in tasks.values()
                        if completed])
    completed_tasks_count = len(completed_tasks)

    message_1 = "Employee {} is done with tasks".format(employee_name) 
    message_2 = "({}/{}):".format(completed_tasks_count, task_number)

    print(message_1 + message_2)

    for title, completed in tasks.items():
        if completed:
            print("\t {}".format(title))


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
