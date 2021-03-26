""" API LOGIN ( zoomerang )"""

url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyAZyyldZdaECkbp9vEr0IkFFfghSgtv20U'
	
headers = {
	'accept': '*/*',
	'accept-language': 'en',
	'accept-encoding': 'gzip, deflate, br',
	'content-length': '87',
	'content-type': 'application/json',
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
	'x-clint-version': 'iOS/FirebaseSDK/6.9.2/FirebaseCore-iOS',
	'x-ios-bundle-identifier': 'com.yantech.zoomerang'}
	
data = {
	"email": email,
	"password": password,
	"returnSecureToken": "true"}

requests.post()

""" By JOKER @t.uo """
