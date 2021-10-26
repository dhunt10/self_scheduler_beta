import requests
from auth import getToken
import datetime
import json

class appointmentMaker():

    def __init__(self):
        self.base_url = 'https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Appointment'
        auth = getToken()
        self.token = auth.getToken()
        self.headers = {'x-api-key': '5ca254dcc3ee6372d2513de1632e35c6fcae44a29240e3d100445c8d',
                       'Cache-Control': 'no-cache',
                       'Content-Type': 'application/json',
                       'Authorization': 'Bearer ' + self.token}

    def book_appointment(self, start, end, patient_id, practitioner_id, location_id, appointment_code, appointment_type, status, reason=None):
        
        self.appointment_type = appointment_code
        self.appointment_type_text = appointment_type
        self.patient_id = "{}".format(patient_id)
        self.start = start
        self.end = end
        self.duration = (datetime.datetime.strptime(end.replace('T', ' ').split('+')[0] , '%Y-%m-%d %H:%M:%S.%f') - datetime.datetime.strptime(start.replace('T', ' ').split('+')[0] , '%Y-%m-%d %H:%M:%S.%f'))
        self.duration = int((self.duration.total_seconds()/60))
        print(type(self.duration))
        #self.duration = 10
        self.location_id = 'Location/{}'.format(location_id)
        self.location_url = "https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Location/{}".format(location_id)
        self.practitioner = 'Practitioner/{}'.format(practitioner_id)
        self.practitioner_url = 'https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Practitioner/{}'.format(practitioner_id)
        self.patient_id = 'Patient/{}'.format(patient_id)
        self.patient_id_url = 'https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Patient/{}'.format(patient_id)        
        body = {"resourceType":"Appointment", "status":"booked", "appointmentType" : {"coding": [{"system": "https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/ValueSet/appointment-type", "code": self.appointment_type, "display": self.appointment_type_text}], "text": self.appointment_type_text}, "start": self.start, "end": self.end, "minutesDuration": self.duration, "participant": [{"actor": {"reference": self.location_id, "display": self.location_url}}, {"actor": {"reference": self.practitioner, "display": self.practitioner_url}},{"actor": {"reference":self.patient_id, "display": self.patient_id_url}}]}
        call = requests.post(url=self.base_url, data=json.dumps(body), headers=self.headers)
        print(call.text)
"""


SAMPLE POST


curl -X POST https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Appointment \
-H 'x-api-key: 5ca254dcc3ee6372d2513de1632e35c6fcae44a29240e3d100445c8d' \
-H 'Content-Type: application/json' \
-H 'Cache-Control: no-cache' \
-H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmaGlyX3V6YWFpIiwicG9sICAgICAgICAiOiJjaGFuZ2VtZSIsInVybFByZWZpeCI6ImVudHBtc2FuZGJveDI1OCIsInZlbmRvciI6ImZoaXJfdXphYWlAZW50cG1zYW5kYm94MjU4IiwiaXNzIjoibW9kbWVkIiwidG9rZW5UeXBlIjoiYWNjZXNzIiwianRpIjoiYWFjODJkNDFlNmI4NGQyNWI1MGE3MmI2NjdmZjAxMjkifQ.f10-AbGiJBeUmXBFjsxexfm9kW51nLsAhr-1hiabiro' \
-d '{"resourceType":"Appointment", "status":"booked", "appointmentType" : {"coding": [{"system": "https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/ValueSet/appointment-type", "code": "877", "display": "Follow Up"}], "text": "Follow Up"},"start": "2021-07-30T20:50:00.000+00:00", "end": "2021-07-30T21:00:00.000+00:00", "minutesDuration": 10, "participant": [{"actor": {"reference": "Location/381", "display": "https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Location/381"}}, {"actor": {"reference":"Practitioner/154960", "display": "https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Practitioner/154960"}},{"actor": {"reference":"Patient/155077", "display": "https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Patient/155077"}}]}'

"""


