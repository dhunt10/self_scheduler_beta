from enum import Enum

class patientType(Enum):
    NEW_PATIENT = 'New Patient'
    NEW_PATIENT_ID = 878
    RETURNING_PATIENT = 'Follow Up'
    RETURNING_PATIENT_ID = 877
    BOTOX = 'Botox Consult/Treatment'
    BOTOX_ID = 879