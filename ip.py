import sys
import requests
import re
import socket
from multiprocessing.dummy import Pool
from colorama import Fore, init

init(autoreset=True)

fr = Fore.RED
fg = Fore.GREEN

print("""
[#] Created By ::

                                              
     _____   ______  _     _     _______  _____   
    (_____) (______)(_)   (_)   (_______)(_____)  
    (_)__(_)(_)__   (_)   (_)      (_)   (_)__(_) 
    (_____) (____)  (_)   (_)      (_)   (_____)  
    ( ) ( ) (_)____  (_)_(_)     __(_)__ (_)      
    (_)  (_)(______)  (___)     (_______)(_)      
                                              
                                              
                          Garsec Rev  https://t.me/garudasec4    
                       Get IPs From Domains Faster And Any Type
                       
                    menggunakan nya jangan pakai http maupun https hapus
                            http/https di dalam list website mu
""")

requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    sys.exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')


def domain(site):
    site = re.sub(r'^https?://|www\.|\/.*$', '', site)
    return site


def getIP(url):
    try:
        dom = domain(url)
        try:
            ip = socket.gethostbyname(dom)
            print(' -| ' + url + ' --> {}[{}]'.format(fg, ip))
            with open('IPs.txt', 'a') as f:
                f.write(ip + '\n')
        except socket.error:
            print(' -| ' + url + ' --> {}[DomainNotWork]'.format(fr))
    except Exception as e:
        print(' -| ' + url + ' --> {}[DomainNotWork] - {}'.format(fr, str(e)))


mp = Pool(150)
mp.map(getIP, target)
mp.close()
mp.join()
