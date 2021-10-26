import mysql.connector
import datetime

class getDates():
    def __init__(self, location_name):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Familyguy10',
            database='onspot_scheduler_locations',
            auth_plugin='mysql_native_password'
        )
        self.location_name = location_name

    def getDates(self, location_id):

        dates = []
        mycursor = self.mydb.cursor()
        mycursor.execute('select dd.date_of_derma_drive from location '
                         'join derma_drive_has_location loc using (location_id) '
                         'join derma_drive_date dd using (derma_drive_date_id) '
                         'where loc.location_id = \'{}\';'.format(location_id))
        li = mycursor.fetchall()
        for i in range(len(li)):
            print(li[i][0])
            dates.append(datetime.datetime.strftime(li[i][0], '%Y-%m-%d'))
        return dates

    def getLocationID(self):
        mycursor = self.mydb.cursor()
        mycursor.execute('SELECT location_id from location where location_name = \'{}\''.format(self.location_name))
        return mycursor.fetchall()[0][0]

