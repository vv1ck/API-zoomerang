""" API new account ( zoomerang )"""


url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=AIzaSyAZyyldZdaECkbp9vEr0IkFFfghSgtv20U'
	
headers = {
	'Accept': '*/*',
	'Accept-encoding':'gzip, deflate, br',
	"Accept-Language": "en",
	'Content-Type':'application/json',
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
	'X-Client-Version':'iOS/FirebaseSDK/6.9.2/FirebaseCore-iOS',
	'X-Ios-Bundle-Identifier':'com.yantech.zoomerang'}
	
data = {
		"email": email,
		"password": password,
		"returnSecureToken": "true"}
	
requests.post()


""" By JOKER @t.uo """
