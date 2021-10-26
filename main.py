from auth import getToken
from locationGetter import getLocations
from getDates import getDates
from getSlots import getSlots
from patient_type import patientType
from appointment import patientAppointment
from patient import patient
from newPatient import newPatient
from twilio.rest import Client


# for now things like appointment type, date, location will just be
# strings, when we create a front end we will replace these strings with enums


if __name__ == "__main__":

    account_sid = 'AC0b05fedb690adfe083e62b44a42ffa33'
    auth = '31bbf426eddf51a9fc34078877be3fdb'
    twilio_number = '+19412057836'
    client = Client(account_sid, auth)

    token = getToken().getToken()

    appt = patientAppointment(token)

    choice = input('What kind of patient are you?: 1,2,3')

    appointment_type = patientType.RETURNING_PATIENT_ID.value
    appointment_type_text = patientType.RETURNING_PATIENT.value

    locations = getLocations(token).getLocation() #api

    print('Location options: {}'.format(locations))

    chosen_location = input('Enter name of location: ')

    appt.setLocation(381) # hardcoded
    appt.setAppointmentType(appointment_type, appointment_type_text)

    dates = getDates(chosen_location) # db

    print('Available dates: {}'.format(dates))

    location_id = dates.getLocationID()
    available_dates = dates.getDates(location_id) #db
    chosen_date = available_dates[0]

    slots = getSlots(token, available_dates[0], 381, 877).getSlots() # 877 hard coded cause there are no available slots for new patients

    print('Available Slots: {}'.format(slots))

    chosen_slot = slots[0]
    day = (str(chosen_slot[0][0]).split('T')[0])
    time = (str(chosen_slot[0][0]).split('T')[1].split('.')[0])

    appt.setSlot(chosen_slot[0], chosen_slot[1])

    # todo make an new patient or grab the info for a
    #  returning patient, then make an appointment given the correct
    #  information, need to get the provider id first
    # make one class for both new and retunring patients and just polymorhpisize the init methods,
    # causing confusion between getPatientID method

    if appointment_type == 877:
        #patient = patient(token, first_name, last_name, sex, email, monthDOB, dayDOB, yearDOB, phone, type, textBool, reason)
        patient = patient(token, 'Mary', 'Doyle', 'sex', 'email', 11, 14, 1987, 'phone', 'Mobile', True, 'reason')
        patient.getPatientData()
    elif appointment_type == 878:
        patient = newPatient(token, 'darin', 'hunt', 'Male', 'dhunt@gmail.com', 10, 10, 1998, '9788065045', 'Mobile', True, 'reason',
                 'other', 'street', 'city', 'state', 'zip', 'insurance_plan',
                 'insurance_member_id', secondary_insurance_plan=None,
                 secondary_member_id=None)
        patient.makePatient()
        patient.getPatientID()

    appt.setPatient(patient)
    call = appt.make_appointment()

    if call.status_code == 200 or call.status_code == 201:
        sms_body = "{} thank you for booking with OnSpot Dermatology, you are confirmed for your appointment on {}" \
                   " at {} at {}".format('darin', day, time, chosen_location)
        client.messages \
            .create(
            body=sms_body,
            from_=twilio_number,
            status_callback='http://postb.in/1234abcd',
            to='+19788065045'
        )

    else:
        print('not successful')