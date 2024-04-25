#!/usr/bin/python3
""" this is an API """
import json
import requests

if __name__ == "__main__":
    js = {}

    with open('todo_all_employees.json', 'w', newline="") as f:
        for n in range(1, 3):
            lista = []
            response = requests.get(
                    f'https://jsonplaceholder.typicode.com/todos/?userId={n}')
            user = requests.get(
                    f'https://jsonplaceholder.typicode.com/users/{n}')
            for i in range(len(response.json())):
                di = {}
                di["username"] = user.json()['username']
                di["task"] = response.json()[i]['title']
                di["completed"] = response.json()[i]['completed']
                lista.append(di)

            js[f'{n}'] = lista
        json.dump(js, f)
