import json
import requests

class getToken():

	def __init__(self):
		URL = "https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/ws/oauth2/grant"

		PARAMS = {'x-api-key': '5ca254dcc3ee6372d2513de1632e35c6fcae44a29240e3d100445c8d',
			  'Cache-Control': 'no-cache',
	  		'Content-Type': 'application/x-www-form-urlencoded',
	  		'Content-Length': '59'}

		DATA = {'grant_type': 'password','username': 'fhir_uzaai', 'password': '5EQS71GChc'}

		r = requests.post(url = URL, data = DATA, headers = PARAMS)

		r = json.loads(r.text)

		self.token = r['access_token']
		self.refresh = r['refresh_token']

	def getToken(self):
		return self.token

	def getRefresh(self):
		return self.refresh
