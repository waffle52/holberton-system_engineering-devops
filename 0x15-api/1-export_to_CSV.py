#!/usr/bin/python3
""" Records all tasks of the employee ID passed to a CSV file """
import csv
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
    emp_name = data.get('name')
    emp_user = data.get('username')
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    r2 = requests.get(url_todo)
    for x in r2.json():
        if str(x.get('userId')) == sys.argv[1]:
            task_length += 1
            task_list.append(x.get('title'))
            if str(x.get('completed')) == "True":
                task_completed += 1
                task_comp_list.append("True")
            else:
                task_comp_list.append("False")
    with open('{}.csv'.format(sys.argv[1]), 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for x in range(0, len(task_list)):
            spamwriter.writerow([sys.argv[1], emp_user, task_comp_list[x],
                                 task_list[x]])
