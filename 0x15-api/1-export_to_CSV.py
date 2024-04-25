#!/usr/bin/python3
""" this is an API """
import requests
from sys import argv
import csv

if __name__ == "__main__":
    data = []

    user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos/?userId={argv[1]}')

    file_path = argv[1] + '.csv'
    with open(file_path, 'w', newline="") as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        for item in response.json():
            write.writerow([item['userId'], user.json()['username'],
                            item['completed'], item['title']])
