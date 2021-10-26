from patient import patient
import requests
import json

class newPatient(patient):

    def __init__(self, auth, first_name, last_name, sex, email,
                 monthDOB, dayDOB, yearDOB, phone, type, textBool, reason,
                 reference, street, city, state, zip, insurance_plan,
                 insurance_member_id, secondary_insurance_plan=None,
                 secondary_member_id=None):
        super().__init__(auth, first_name, last_name, sex,  email, monthDOB, dayDOB, yearDOB, phone, type, textBool, reason)
        self.reference =  reference # todo
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.insurance_plan = insurance_plan
        self.insurance_member_id = insurance_member_id
        self.secondary_insurance_plan = secondary_insurance_plan
        self.secondary_member_id = secondary_member_id
        self.patient_base_url = 'https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Patient'
        self.headers = {'x-api-key': '5ca254dcc3ee6372d2513de1632e35c6fcae44a29240e3d100445c8d',
                        'Cache-Control': 'no-cache',
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + auth}
        birthdate = str(self.yearDOB) + "-" + str(self.monthDOB) + "-" + str(self.dayDOB)
        self.body = {"resourceType":"Patient",
                     'birthDate':birthdate,
                     "name": [{"given":[self.first_name],
                     "family":self.last_name}],
                     "telecom": [{"system":"email", "value" : self.email},
                                 {"system":"phone", "value" : self.phone}],
                     "address" : [
                         {
                             "use":"home",
                             "type":"both",
                             "text":self.street,
                             "line": [
                                 self.street
                             ],
                             "city":self.city,
                             "state":self.state,
                             "postalCode":self.zip
                         }
                     ]
                     }
        self.patient_data = {"given": self.first_name, "family": self.last_name,
                             "birthdate": str(self.yearDOB) + "-" + str(self.monthDOB) + "-" + str(self.dayDOB)}
        self.patientID = None
#took out "gender":self.sex,

    def makePatient(self):
        requests.post(url=self.patient_base_url, data=json.dumps(self.body), headers=self.headers)

    def getOldPatientID(self):
        p = requests.get(url=self.patient_base_url, headers=self.headers, params=self.patient_data).json()
        return p['entry'][0]['resource']['id']