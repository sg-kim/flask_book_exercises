from werkzeug.datastructures import CallbackDict
from flask.sessions import SessionInterface, SessionMixin

import pickle
from uuid import uuid4
from appmain import app, db
from appmain.DBSession.models import DBSession
from sqlalchemy import create_engine

class SQLAlchemySession(CallbackDict, SessionMixin):
    def __init__(self, initial=None, sid=None, new=False):

        def on_update(self):
            self.modified = True

        CallbackDict.__init__(self, initial, on_update)
        self.sid = sid
        self.new = new
        self.modified = False

        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

        if not engine.dialect.has_table(engine, 'db_session'):
            db.create_all()
            print('table for session has been created.')

        engine.dispose()


class SQLAlchemySessionInterface(SessionInterface):
    session_class = SQLAlchemySession
    serializer = pickle

    def generate_sid(self):
        return str(uuid4())

    def open_session(self, app, request):
        sid = request.cookies.get(app.session_cookie_name)

        if not sid:
            sid = self.generate_sid()
            return self.session_class(sid=sid, new=True)

        rec = db.session.query(DBSession).filter(DBSession.sid == sid).first()

        if rec is not None:
            data = self.serializer.loads(rec.value)
            return self.session_class(data, sid=sid)

        return self.session_class(sid=sid, new=True)

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        if not session:
            rec = db.session.query(DBSession).filter(DBSession.sid == session.sid).first()
            db.session.delete(rec)
            db.session.commit()
            if session.modified:
                response.delete_cookie(app.session_cookie_name, domain=domain)
        val = self.serializer.dumps(dict(session))
        session_db = DBSession.change(session.sid, val)
        db.session.add(session_db)
        db.session.commit()

        httponly = self.get_cookie_httponly(app)
        secure = self.get_cookie_secure(app)
        expires = self.get_expiration_time(app, session)

        response.set_cookie(app.session_cookie_name, session.sid, expires=expires, httponly=httponly, domain=domain, secure=secure)
