#!/usr/bin/python3
""" Records all tasks from employees to json file """
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    url_user = "https://jsonplaceholder.typicode.com/users/"

    todo_r = requests.get(url)
    user_r = requests.get(url_user)

    task_length = len(todo_r.json())
    task_user = todo_r.json()
    task_test = user_r.json()

    json_list = []
    overall_list = {}
    for x in range(1, len(task_test)):
        overall_list[x] = None
    track = 1

    for x in range(0, task_length):
        """ loops through data and saves it to each key in overall_list """
        if (track != int(task_user[x].get('userId'))):
            overall_list[track] = json_list
            json_list = []
            track += 1
        num = task_user[x].get('userId')
        usernm = task_test[num - 1].get('username')
        if (str(task_user[x].get('completed')) == 'False'):
            status = False
        else:
            status = True
        json_list.append({"username": "{}".format(usernm),
                          "task": "{}".format(task_user[x].get('title')),
                          "completed": status})

    overall_list[track] = json_list
    json_list = []

    with open('todo_all_employees.json', 'w', newline='') as jsfile:
        json.dump(overall_list, jsfile)
