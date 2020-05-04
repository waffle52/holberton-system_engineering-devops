#!/usr/bin/python3
""" Given an employee ID, looks up and displays after their TODO list """
import requests
import sys

if __name__ == "__main__":
    task_length = 0
    task_list = []
    task_completed = 0
    url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    r = requests.get(url)
    data = r.json()
    emp_name = data['name']
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    r2 = requests.get(url_todo)
    for x in r2.json():
        if str(x.get('userId')) == sys.argv[1]:
            task_length += 1
            if str(x.get('completed')) == "True":
                task_completed += 1
                task_list.append(x.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, task_completed, task_length))
    for x in task_list:
        print("\t {}".format(x))
