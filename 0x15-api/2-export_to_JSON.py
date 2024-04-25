#!/usr/bin/python3
""" this is an API """
import json
import requests
from sys import argv

if __name__ == "__main__":
    js = {}
    lista = []

    user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos/?userId={argv[1]}')

    file_path = argv[1] + '.json'
    with open(file_path, 'w', newline="") as f:

        for i in range(len(response.json())):
            di = {}
            di["task"] = response.json()[i]['title']
            di["completed"] = response.json()[i]['completed']
            di["username"] = user.json()['username']
            lista.append(di)

        js[argv[1]] = lista
        json.dump(js, f)
