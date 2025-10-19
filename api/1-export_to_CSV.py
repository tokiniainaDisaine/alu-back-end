#!/usr/bin/python3
"""
fgbvd
"""
import requests
import csv
from sys import argv


def get_info(url):
    data = requests.get(url)
    return data.json()

def export_to_csv(employee_id, username, todos):
    filename = f'{employee_id}.csv'
    with open(filename, mode='w') as file:
        file_writer = (csv.writer(
                        file, 
                        delimiter=',', 
                        quoting=csv.QUOTE_ALL))
        for todo in todos:
            rowData = ([
                employee_id, 
                username, 
                todo['completed'], 
                todo['title']])
            file_writer.writerow(rowData)


def main(employee_id):
    """
    fgbjfnd
    """
    api_url = "https://jsonplaceholder.typicode.com/users"
    employee_info_url = f"{api_url}/{employee_id}/"

    employee_todo_url = f"{api_url}/{employee_id}/todos"

    employee_info = get_info(employee_info_url)
    employee_todo = get_info(employee_todo_url)

    username = employee_info.get("username")

    export_to_csv(employee_id, username, employee_todo)

if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
