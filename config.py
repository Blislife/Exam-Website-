import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'exam_user'
    MYSQL_PASSWORD = 'yourpassword'
    MYSQL_DB = 'exam_registration'
