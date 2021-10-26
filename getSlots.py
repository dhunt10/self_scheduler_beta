import requests

class getSlots():
    def __init__(self, auth, date, location_id, appointment_type):
        self.date = date
        self.location_id = location_id
        self.appointment_type = appointment_type
        self.base_url = 'https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Slot'
        self.headers = {'x-api-key': '5ca254dcc3ee6372d2513de1632e35c6fcae44a29240e3d100445c8d',
                        'Cache-Control': 'no-cache',
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + auth}

        self.data = {"date" : "eq" + self.date, "appointment-type" : self.appointment_type}

        # todo should be this:
        # self.data = {"date" : "eq" + self.date, "appointment-type" : self.appointment_type,
        #               "identifier" : "identifier\=https://www.hl7.org/fhir/v2/0203/index.html\#v2-0203-FI\|{}"
        #               .format(self.location_id)"}


    def getSlots(self):
        call = requests.get(url=self.base_url, headers=self.headers, params=self.data)
        slots = call.json()
        time_slots = []
        print(slots['total'])
        for i in range(slots['total']):
            time_slots.append(((slots['entry'][i]['resource']['start'], slots['entry'][i]['resource']['end']), slots['entry'][i]['resource']['identifier'][2]['value']))
        return time_slots

