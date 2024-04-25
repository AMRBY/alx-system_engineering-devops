#!/usr/bin/python3
""" this is an API """
import requests
from sys import argv

if __name__ == "__main__":
    number = 0
    done = []
    user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos/?userId={argv[1]}')
    # print(response.json())
    total = len(response.json())
    for i in range(len(response.json())):
        if response.json()[i]['completed'] is True:
            number += 1
            done.append(response.json()[i]['title'])
    print(f'Employee \
            {user.json()["name"]} is done with tasks ({number}/{total}):' end='')
    print(*done, sep="\n")
