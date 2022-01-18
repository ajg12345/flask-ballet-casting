from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class locations(db.Model):
    location_id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.Text, nullable=False)
    building = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Integer, primary_key=False)
    
    def __repr__(self):
        return f'<Location {self.building}, {self.room}>'

class dancers(db.Model):
    dancer_id = db.Column(db.Integer, primary_key=True)
    dancer_fullname = db.Column(db.Text, nullable=False)
    dancer_email = db.Column(db.Text, nullable=False)
    dancer_phone = db.Column(db.Text, nullable=False)
    dancer_email_or_phone = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Integer, primary_key=False)
    
    def __repr__(self):
        return f'<dancer {self.dancer_fullname}>'        

class productions(db.Model):
    prod_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Integer, nullable=False)
    create_dt = db.Column(db.Date, nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return f'<production {self.description}>'        

class rehearsals(db.Model):
    re_id = db.Column(db.Integer, primary_key=True)
    prod_id = db.Column(db.Integer, db.ForeignKey('productions.prod_id'), nullable=False)
    perf_dt = db.Column(db.Date, nullable=False)
    is_performance = db.Column(db.Integer, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'), primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    
    def __repr__(self):
        return f'<rehearsal {self.re_id}>'       

class roles(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    prod_id = db.Column(db.Integer, db.ForeignKey('productions.prod_id'), nullable=False)
    role_count = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<role {self.description}>'    

class users(db.Model):
    user_uid = db.Column(db.Integer, primary_key=True)
    user_first = db.Column(db.Text, nullable=False)
    user_last = db.Column(db.Text, nullable=False)
    user_email = db.Column(db.Text, nullable=False)
    user_pwd = db.Column(db.Text, nullable=False)
    can_create = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<user {self.user_email}>'  

class role_conflicts(db.Model):
    """select  rc.conflict_id as rc_id, 
        p.description as production,
        ro1.description as role1,
        ro2.description as role2
        from role_conflicts as rc
        join productions as p on rc.prod_id = p.prod_id
        join roles as ro1 on rc.role_id1 = ro1.role_id
        join roles as ro2 on rc.role_id2 = ro2.role_id;"""
    conflict_id = db.Column(db.Integer, primary_key=True)
    prod_id = db.Column(db.Integer, db.ForeignKey('productions.prod_id'), nullable=False)
    conflict_pair_id = db.Column(db.Integer, nullable=False)
    role_id1 = db.Column(db.Integer, nullable=False)
    role_id2 = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<role_conflict {self.conflict_id}>'   

class castings(db.Model):
    """
    select  ro.description as role, 
            p.description as production,
            d.dancer_fullname as dancer_name,
            c.update_dt as last_updated
        from castings as c
        join roles as ro on c.role_id = ro.role_id
        join rehearsals as r on c.re_id = r.re_id
        join dancers as d on c.dancer_id = d.dancer_id
        join productions as p on r.prod_id = p.prod_id
        where d.is_active=1;
    """
    casting_id = db.Column(db.Integer, primary_key=True)
    re_id = db.Column(db.Integer, db.ForeignKey('rehearsals.re_id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'), nullable=False)
    dancer_id = db.Column(db.Integer, nullable=False)
    update_dt = db.Column(db.Date, nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return f'<casting {self.casting_id}>'       