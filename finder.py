import requests,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from multiprocessing import Pool


def logo():
	print("""
	
	[ telegram ] @SukaJanda01
	[ cannel  ] @garudasec4
	
	""")

def finde_it(domain):
	try:
		domain = domain.strip()
		headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language": "en-us,en;q=0.5",
		"Accept-Encoding": "gzip,deflate",
		"Connection": "keep-alive",
		"Cookie": "PHPSESSID=demo;",
		"Cache-Control": "no-cache"}
		for name in open('privat/name.txt','r',encoding="utf-8").readlines():
			name=name.strip()
			to_domain = requests.get(f"http://{domain}{name}",headers=headers,timeout=3).text
			# ~ print(name,to_domain)
			if ">public_html" in to_domain:
				open("result/shell.txt","a").write(f"http://{domain}{name}\n")
				print(f"[x] http://{domain}{name} >> \033[33mshells")
				break
			elif "<span>Upload file:" in to_domain:
				open("result/random.txt","a").write(f"http://{domain}{name}\n")
				print(f"[x] http://{domain}{name} >> \033[33mrandom")
				break
			elif 'type="submit" id="_upl" value="Upload">'  in to_domain:
				open("result/Config.txt","a").write(f"http://{domain}{name}\n")
				print(f"[x] http://{domain}{name}  >> \033[33mconfig")
				break
			elif 'Leaf PHPMailer' in to_domain or '>alexusMailer 2.0<' in to_domain:
				open("result/Mailer.txt","a").write(f"http://{domain}{name}\n")
				print(f"[x] http://{domain}{name}  >> \033[33mmailer")
				break
			elif 'method=post>Password:' in to_domain or '<input type=password name=pass' in to_domain:
				open("result/passwod.txt","a").write(f"http://{domain}{name}\n")
				print(f"[x] http://{domain}{name}  >> \033[33mshell password")
				break
			elif 'name="uploader" id="uploader">' in to_domain:
				open("result/result.txt","a").write(f"http://{domain}{name}\n")
				print(f"[x] http://{domain}{name}  >> \033[33muploader")
				break
			else:
				print(f"[-] {domain}  >> \033[38mNO")
				pass
	except:pass


def check_num(path):
	try:
		return len(open(path).readlines())
	except:
		return 0


def index():
	domain = open(input("[X] WebSite : ")).readlines()
	ThreadPool = Pool(60)
	ThreadPool.map(finde_it, domain)
	print(f'''[x] Shell- {check_num("result/shell.txt")} | Mailer- {check_num("result/Mailer.txt")} | Password- {check_num("result/passwod.txt")}| Config- {check_num("result/Config.txt")} | result- {check_num("result/result.txt")}''')


if __name__ == "__main__":
	logo();
	index();

