from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    mysql.init_app(app)

class Student:
    def __init__(self, first_name, last_name, nshe_number, email, password, role):
        self.first_name = first_name
        self.last_name = last_name
        self.nshe_number = nshe_number
        self.email = email
        self.password = password
        self.role = role

class Exam:
    def __init__(self, exam_name, session_date, capacity, seats_booked=0):
        self.exam_name = exam_name
        self.session_date = session_date
        self.capacity = capacity
        self.seats_booked = seats_booked
