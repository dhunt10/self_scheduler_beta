import requests

class patient():
    def __init__(self, auth, first_name, last_name, sex, email, monthDOB, dayDOB, yearDOB, phone, type, textBool, reason):
        self.first_name = first_name
        self.sex = sex
        self.last_name = last_name
        self.email = email
        self.monthDOB = monthDOB
        self.dayDOB = dayDOB
        self.yearDOB = yearDOB
        self.phone = phone
        self.type = type
        self.textBool = textBool
        self.reason = reason
        self.token = auth
        self.patient_base_url = 'https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Patient'
        self.coverage_base_url = 'https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Patient'
        self.headers = {'x-api-key': '5ca254dcc3ee6372d2513de1632e35c6fcae44a29240e3d100445c8d',
                        'Cache-Control': 'no-cache',
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + auth}
        self.patient_data = {"given":self.first_name, "family":self.last_name,
                     "birthdate":str(self.yearDOB) + "-" +str(self.monthDOB) + "-" + str(self.dayDOB)}

    def getNewPatientID(self):
        p = requests.get(url=self.patient_base_url, headers=self.headers, params=self.patient_data).json()
        return p['entry'][0]['resource']['id']

    def getPatientData(self):
        patient = requests.get(url=self.patient_base_url, headers=self.headers, params=self.patient_data).json()
        self.id = patient['entry'][0]['resource']['id']
        self.reference = 'hello'#todo
        address = patient['entry'][0]['resource']['address'][0]
        self.street = address['line'][0]
        self.city = address['city']
        self.state = address['state']
        self.zip = address['postalCode']
        coverage = self.getCoverage()
        #print(coverage)
        #self.insurance_plan = coverage['entry'][0]['resource']['payor'][0]['display']
        #self.insurance_member_id = coverage['entry'][0]['resource']['class'][0]['value']
        try:
            print('')
            ##self.secondary_insurance_plan = coverage['entry'][0]['resource']['payor'][1]['display']
            #self.secondary_member_id = ['entry'][0]['resource']['class'][1]['value'] # check logic on that
        except:
            pass #no secondary insurnace


    def getCoverage(self):
        coverage_data = {"patient": self.id}
        return requests.get(url=self.coverage_base_url, headers=self.headers, params=coverage_data).json()
