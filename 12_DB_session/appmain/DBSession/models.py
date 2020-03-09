from appmain import db


class DBSession(db.Model):

    sid = db.Column(db.String(36), primary_key=True)
    value = db.Column(db.LargeBinary)

    @classmethod
    def change(cls, sid, value):
        rec = db.session.query(cls).filter(cls.sid == sid).first()
        if not rec:
            rec = cls()
            rec.sid = sid
        rec.value = value

        return rec
