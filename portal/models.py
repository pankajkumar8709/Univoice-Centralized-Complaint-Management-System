from portal import db,app

class acad(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    complaint=db.Column(db.String(500),nullable=False)
    semester=db.Column(db.String(4),nullable=False)
    course=db.Column(db.String(15),nullable=False)
    section=db.Column(db.String(3),nullable=False)
    date=db.Column(db.Date(),nullable=False)

class hostel(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    complaint=db.Column(db.String(500),nullable=False)
    hostel_no=db.Column(db.Integer(),nullable=False)
    room_no=db.Column(db.Integer(),nullable=False)
    date=db.Column(db.Date(),nullable=False)

class mess(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    complaint=db.Column(db.String(500),nullable=False)
    day=db.Column(db.String(15),nullable=False)
    meal=db.Column(db.String(20),nullable=False)
    date=db.Column(db.Date(),nullable=False)


class sports(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    complaint=db.Column(db.String(500),nullable=False)
    type=db.Column(db.String(25),nullable=False)
    date=db.Column(db.Date(),nullable=False)

class buses(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    complaint=db.Column(db.String(500),nullable=False)
    bus_no=db.Column(db.Integer(),nullable=False)
    date=db.Column(db.Date(),nullable=False)
class s_suggest(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    suggestion=db.Column(db.String(500),nullable=False)
    date=db.Column(db.Date(),nullable=False)

class  s_anonymous(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    complaint=db.Column(db.String(500),nullable=False)
    category=db.Column(db.String(25),nullable=False)
    date=db.Column(db.Date(),nullable=False)
class basic(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    complaint=db.Column(db.String(500),nullable=False)
    category=db.Column(db.String(25),nullable=False)
    date=db.Column(db.Date(),nullable=False)

class T_Complaints(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    complaint=db.Column(db.String(500),nullable=False)
    category=db.Column(db.String(25),nullable=False)
    date=db.Column(db.Date(),nullable=False)
    others=db.Column(db.String(500),nullable=True)

class T_Suggestion(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    category=db.Column(db.String(55),nullable=False)
    complaint=db.Column(db.String(500),nullable=False)
    date=db.Column(db.Date(),nullable=False)

class T_Anonymous(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    category=db.Column(db.String(55),nullable=False)
    complaint=db.Column(db.String(500),nullable=False)