from patient_type import patientType
from auth import getToken
import requests
import json

class patientAppointment():
    def __init__(self, auth):

        self.base_url = 'https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Appointment'
        self.headers = {'x-api-key': '5ca254dcc3ee6372d2513de1632e35c6fcae44a29240e3d100445c8d',
                        'Cache-Control': 'no-cache',
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + auth}

        self.patient = None
        self.patientID = None
        self.patientURL = None
        self.location = None
        self.locationURL = None
        self.provider = None
        self.providerURL = None
        self.appointmentTypeID = None
        self.appointmentTypeText = None
        self.start = None
        self.end = None
        self.duration = None
        self.status = 'booked'

    def make_appointment(self):

        body = {"resourceType":"Appointment",
                "status":"booked",
                "appointmentType" :
                    {"coding":
                         [{"system":
                               "https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/ValueSet/appointment-type",
                           "code": self.appointmentTypeID,
                           "display": self.appointmentTypeText}],
                     "text": self.appointmentTypeText},
                "start": self.start, "end": self.end,
                "minutesDuration": self.duration,
                "participant":
                    [{"actor": {"reference": "Location/" + str(self.location),
                                "display": self.locationURL}},
                     {"actor": {"reference": "Practitioner/" + str(self.provider),
                                "display": self.providerURL}},
                     {"actor": {"reference": "Patient/" + str(self.patientID),
                                "display": self.patientURL}}]}

        print(self.location, self.patientID, self.provider)

        call = requests.post(url=self.base_url, data=json.dumps(body), headers=self.headers)

        return call

    def setPatient(self, patient):
        self.patient = patient
        self.patientID = patient.getNewPatientID()
        self.patientURL = 'https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Patient/{}'.format(
            self.patientID)

    def setLocation(self, location):
        self.location = location
        self.locationURL = "https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Location/{}".format(
            self.location)

    def setSlot(self, slot, provider):
        self.start = slot[0]
        self.end = slot[1]
        self.duration = 10 #self.start - self.end
        self.provider = provider
        self.providerURL = 'https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Practitioner/{}'.format(
            self.provider)

    def setAppointmentType(self, apptTypeID, apptTypeText):
        self.appointmentTypeID = apptTypeID
        self.appointmentTypeText = apptTypeText





