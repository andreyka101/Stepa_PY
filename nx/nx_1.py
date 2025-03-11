import json

users = {}

def create_user():
    username = input()
    password = input()

    if username in users:
        print('your name had added')
    else:
        users[username] = password
        print(f"User {username} had added.")

def delete_user():
    username = input()
    if username in users:
        del users[username]

def display_users():
    for user in users:
        print("-", user)

while 0 == 0:
    command = input()

    if command == "new":
        create_user()
    elif command == "del":
        delete_user()
    elif command.lower() == "exit":
        break
    else:
        display_users()

with open('users.json', 'bw') as file:
    json.dump(users, file)
# sfdgfad