import json

class Config:
    def __init__(self):
        with open('./appmain/config.json') as cf:
            self.config = json.load(cf)

        self.SECRET_KEY = self.config.get('SECRET_KEY')
        self.DB_USERNAME = self.config.get('DB_USERNAME')
        self.DB_PASSWORD = self.config.get('DB_PASSWORD')
        self.MAIL_USERNAME = self.config.get('MAIL_USERNAME')
        self.MAIL_PASSWORD = self.config.get('MAIL_PASSWORD')
