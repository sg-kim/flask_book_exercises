from appmain import db, loginManager, app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@loginManager.user_loader
def load_user(userId):
        return Userdata.query.get(int(userId))

class Userdata(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(30), unique=True, nullable=False)
        email = db.Column(db.String(60), unique=True, nullable=False)
        picture = db.Column(db.String(20), nullable=False, default="default.png")
        password = db.Column(db.String(60), nullable=False)

        def getResetToken(self, expires_sec = 1800):
                s = Serializer(app.config['SECRET_KEY'], expires_sec)
                return s.dumps({'userId': self.id}).decode('utf-8')

        @staticmethod
        def verifyResetToken(token):
                s = Serializer(app.config['SECRET_KEY'])
                try:
                        userId = s.loads(token)['userId']
                except:
                        return None
                return Userdata.query.get(userId)
