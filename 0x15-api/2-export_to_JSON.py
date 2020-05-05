#!/usr/bin/python3
""" Exports the data retrieved to a json file """
import json
import requests
import sys

if __name__ == "__main__":
    task_length = 0
    task_list = []
    task_completed = 0
    task_comp_list = []
    url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    r = requests.get(url)
    data = r.json()
    emp_name = data['name']
    emp_user = data['username']
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    r2 = requests.get(url_todo)
    for x in r2.json():
        if str(x.get('userId')) == sys.argv[1]:
            task_length += 1
            task_list.append(x.get('title'))
            if str(x.get('completed')) == "True":
                task_completed += 1
                task_comp_list.append(True)
            else:
                task_comp_list.append(False)

    json_list = []

    with open('{}.json'.format(sys.argv[1]), 'w', newline='') as jsfile:
        for x in range(0, task_length):
            json_list.append({"task": "{}".format(task_list[x]),
                              "completed": task_comp_list[x],
                              "username": "{}".format(emp_user)})
        json.dump({sys.argv[1]: json_list}, jsfile)
