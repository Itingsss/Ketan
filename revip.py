import requests , sys , time , random
from multiprocessing.dummy import Pool


def ii( ip ):
	for bolo in range(10):
		try:
			
			return requests.get( "https://api.webscan.cc/?action=query&ip={}".format( str(ip).strip() ) )
			
		except:
			time.sleep( random.randint( 4 , 7 ) )
			

def action( iphada ):
	iphada = str(iphada).strip()
	
	def saveIT( saveTEXT , saveOn ):
		
		while True:
			try:
				with open( saveOn , "a" , encoding="utf-8" , errors="ignore" ) as p:
					p.write( "{}\n".format( saveTEXT ) )
					
				break
			except:
				pass

	allrst = ii(  iphada  )
	
	try:
		allrst = allrst.json()
	except:
		allrst = False
		
		
	if allrst:
		for res in allrst:
			
			try:
				domains = res["domain"]
			except:
				domains = False
			
			if domains :
				saveIT( "https://" + domains , "domains.txt"  )
				print( domains )
			else:
				pass
				
		saveIT( iphada , "ip_YES_domains.txt"  )
		print( ">>>>>>>>>> {} >>> {} ".format( iphada , len(allrst) )  )

	else:
		saveIT( iphada , "ip_No_DOMAINS.txt"  )
		print( ">>>>> {} >>> 0 ".format( iphada )  )



def main():
	try:
		ips = open( sys.argv[1] , "r"  , encoding="utf-8" , errors="ignore" ).read().splitlines()
	except:
		print( "Usage >>> revip list.txt ")
		exit()
		
		
	print(  "<<<< List reaad and splited . Script Started >>>>" )
	mp = Pool( 200 )
	mp.map( action , ips )
	mp.close()
	mp.join()


if __name__  == "__main__":
	main()
