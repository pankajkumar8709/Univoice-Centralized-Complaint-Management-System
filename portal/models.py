from portal import db,app

class acad(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    complaint=db.Column(db.String(500),nullable=False)
    semester=db.Column(db.String(4),nullable=False)
    course=db.Column(db.String(15),nullable=False)
    section=db.Column(db.String(3),nullable=True)
    date=db.Column(db.Date(),nullable=False)
    status = db.Column(db.String(20), default='Pending')
    response = db.Column(db.Text)
    date_resolved = db.Column(db.DateTime)

class hostel(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    complaint=db.Column(db.String(500),nullable=False)
    hostel_no=db.Column(db.Integer(),nullable=False)
    room_no=db.Column(db.Integer(),nullable=False)
    date=db.Column(db.Date(),nullable=False)
    status = db.Column(db.String(20), default='Pending')
    response = db.Column(db.Text)
    date_resolved = db.Column(db.DateTime)

class mess(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    complaint=db.Column(db.String(500),nullable=False)
    day=db.Column(db.String(15),nullable=False)
    meal=db.Column(db.String(20),nullable=False)
    date=db.Column(db.Date(),nullable=False)
    status = db.Column(db.String(20), default='Pending')
    response = db.Column(db.Text)
    date_resolved = db.Column(db.DateTime)


class sports(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    complaint=db.Column(db.String(500),nullable=False)
    type=db.Column(db.String(25),nullable=False)
    date=db.Column(db.Date(),nullable=False)
    status = db.Column(db.String(20), default='Pending')
    response = db.Column(db.Text)
    date_resolved = db.Column(db.DateTime)

class buses(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    complaint=db.Column(db.String(500),nullable=False)
    bus_no=db.Column(db.Integer(),nullable=False)
    date=db.Column(db.Date(),nullable=False)
    status = db.Column(db.String(20), default='Pending')
    response = db.Column(db.Text)
    date_resolved = db.Column(db.DateTime)

class s_suggest(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    suggestion=db.Column(db.String(500),nullable=False)
    date=db.Column(db.Date(),nullable=False)
    status = db.Column(db.String(20), default='Pending')
    response = db.Column(db.Text)
    date_resolved = db.Column(db.DateTime)

class  s_anonymous(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    complaint=db.Column(db.String(500),nullable=False)
    category=db.Column(db.String(25),nullable=False)
    date=db.Column(db.Date(),nullable=False)
    status = db.Column(db.String(20), default='Pending')
    response = db.Column(db.Text)
    date_resolved = db.Column(db.DateTime)

class basic(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    complaint=db.Column(db.String(500),nullable=False)
    category=db.Column(db.String(25),nullable=False)
    date=db.Column(db.Date(),nullable=False)
    status = db.Column(db.String(20), default='Pending')
    response = db.Column(db.Text)
    date_resolved = db.Column(db.DateTime)

class T_Complaints(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    title=db.Column(db.String(100),nullable=False)
    complaint=db.Column(db.String(500),nullable=False)
    category=db.Column(db.String(25),nullable=False)
    date=db.Column(db.Date(),nullable=False)
    others=db.Column(db.String(500),nullable=True)
    status = db.Column(db.String(20), default='Pending')
    response = db.Column(db.Text)
    date_resolved = db.Column(db.DateTime)

class T_Suggestion(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    title=db.Column(db.String(100),nullable=False)
    category=db.Column(db.String(55),nullable=False)
    complaint=db.Column(db.String(500),nullable=False)
    date=db.Column(db.Date(),nullable=False)
    status = db.Column(db.String(20), default='Pending')
    response = db.Column(db.Text)
    date_resolved = db.Column(db.DateTime)

class T_Anonymous(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(100),nullable=False)

    category=db.Column(db.String(55),nullable=False)
    complaint=db.Column(db.String(500),nullable=False)
    status = db.Column(db.String(20), default='Pending')
    response = db.Column(db.Text)
    date_resolved = db.Column(db.DateTime)