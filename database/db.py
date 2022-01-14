from sqlalchemy import create_engine, text, insert



class localdb():
    def __init__(self):
        self.engine = None
        try:
            self.engine = create_engine('mysql+pymysql://root:root@localhost:3307/flaskballetcasting')
            self.engine.connect() 
        except Exception as e: 
            print('not running in local development environment, so using other server name')
            self.engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/flaskballetcasting')

    def get_table(self, tablename) -> tuple:
        """
        Get data from most of the more reference like table, the column names and the rows in a tuple of 2 lists
        """
        with self.engine.connect() as conn:
            rows = conn.execute(text(f"select * from {tablename};")) 
            column_table = conn.execute(text(f"show columns in {tablename};")) 
            columns = [i[0] for i in column_table] 
        return columns, rows

    def create_location(self, room, building):
        """
        Create a location in the table, automatically creating a primary key.
        """
        with self.engine.connect() as conn:
            conn.execute(text(f"insert into flaskballetcasting.locations (room, building, is_active) VALUES('{room}', '{building}', 1);"))
            

    def get_performances(self) -> tuple:

        with self.engine.connect() as conn:
            rows = conn.execute(text("""select  p.description as performance, 
                                                r.perf_dt as date, 
                                                r.start_time as start_time, 
                                                r.end_time as end_time,
                                                l.building as building,
                                                l.room as room
                                         from rehearsals as r 
                                         join productions as p on r.prod_id = p.prod_id
                                         join locations as l on r.location_id = l.location_id
                                         where r.is_performance=1 and p.is_active=1;""")) 
            
            columns = ['performance', 'date', 'start @', 'end @', 'building', 'room'] 
        return columns, rows

    
    def get_rehearsals(self) -> tuple:

        with self.engine.connect() as conn:
            rows = conn.execute(text("""select  p.description as rehearsal, 
                                                r.perf_dt as date, 
                                                r.start_time as start_time, 
                                                r.end_time as end_time,
                                                l.building as building,
                                                l.room as room
                                         from rehearsals as r 
                                         join productions as p on r.prod_id = p.prod_id
                                         join locations as l on r.location_id = l.location_id
                                         where r.is_performance=0 and p.is_active=1;""")) 
            columns = ['rehearsal', 'date', 'start @', 'end @', 'building', 'room'] 
        return columns, rows

    def get_roles(self) -> tuple:

        with self.engine.connect() as conn:
            rows = conn.execute(text("""select  r.description as role, 
                                                p.description as production,
                                                r.role_count as role_count
                                         from roles as r 
                                         join productions as p on r.prod_id = p.prod_id
                                         where p.is_active=1;""")) 
            columns = ['role', 'production', 'role count'] 
        return columns, rows

    def get_castings(self) -> tuple:

        with self.engine.connect() as conn:
            rows = conn.execute(text("""select  ro.description as role, 
                                                p.description as production,
                                                d.dancer_fullname as dancer_name,
                                                c.update_dt as last_updated
                                         from castings as c
                                         join roles as ro on c.role_id = ro.role_id
                                         join rehearsals as r on c.re_id = r.re_id
                                         join dancers as d on c.dancer_id = d.dancer_id
                                         join productions as p on r.prod_id = p.prod_id
                                         where d.is_active=1;""")) 
            columns = ['role', 'production', 'dancer', 'updated'] 
        return columns, rows

    def get_role_conflicts(self) -> tuple:

        with self.engine.connect() as conn:
            rows = conn.execute(text("""select  rc.conflict_id as rc_id, 
                                                p.description as production,
                                                ro1.description as role1,
                                                ro2.description as role2
                                         from role_conflicts as rc
                                         join productions as p on rc.prod_id = p.prod_id
                                         join roles as ro1 on rc.role_id1 = ro1.role_id
                                         join roles as ro2 on rc.role_id2 = ro2.role_id;""")) 
            columns = ['rc_id', 'production', 'role 1', 'role 2'] 
        return columns, rows
