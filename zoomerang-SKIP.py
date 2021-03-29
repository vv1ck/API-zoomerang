""" API SKIP ( zoomerang )"""


url = 'https://us-central1-zoomerang-dcf49.cloudfunctions.net/apiv2/v2/user/username/skip'

headers = {
	'Accept': 'application/json',
	'Accept-encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8',
	"Accept-Language": "ar-JO;q=1.0, en-JO;q=0.9",
	'Authorization': 'Bearer '+sis,
	'Content-Type':'application/json',
	'user-agent': 'Zoomerang/3.0.16 (com.yantech.zoomerang; build:3; iOS 13.5.0) Alamofire/5.2.2'}
	
data ={
		"status" : 'true',
		"result" : 'ZHkcReZTMFRnWW3GxuXjLz0wRlI3'
		}

requests.put()

""" By JOKER @t.uo """
