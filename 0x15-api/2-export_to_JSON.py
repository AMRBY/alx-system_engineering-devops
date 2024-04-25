#!/usr/bin/python3
""" this is an API """
import json
import requests
from sys import argv

if __name__ == "__main__":
    di = {}
    js = {}

    user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos/?userId={argv[1]}')

    file_path = argv[1] + '.json'
    with open(file_path, 'w', newline="") as f:

        for i in range(len(response.json())):
            di["task"] = response.json()[i]['title']
            di["completed"] = response.json()[i]['completed']
            di["username"] = user.json()['username']
            js[argv[1]] = di
            json.dump(js, f)
            print(js)
