import requests

class getLocations():

    def __init__(self, auth):
        self.base_url = 'https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Location'
        self.headers = {'x-api-key': '5ca254dcc3ee6372d2513de1632e35c6fcae44a29240e3d100445c8d',
                        'Cache-Control': 'no-cache',
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + auth}

    def getLocation(self):
        locations = []
        call = requests.get(url = self.base_url, headers = self.headers)
        for i in range(call.json()['total']):
            locations.append(call.json()['entry'][i]['resource']['name'])
        return locations


