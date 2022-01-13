from sqlalchemy import create_engine, text


class localdb():
    def __init__(self):
        self.engine = None
        try:
            self.engine = create_engine('mysql+pymysql://root:root@localhost:3307/flaskballetcasting')
        except Exception as e: 
            self.engine = create_engine('mysql+pymysql://root:root@localhost:3306/flaskballetcasting')
            print('could not connect to localhost database because bad port' + str(e))

    def get_locations(self) -> tuple:
        """
        Get data from the locations table, the column names and the rows in a tuple of 2 lists
        """
        with self.engine.connect() as conn:
            rows = conn.execute(text("select * from locations;")) 
            column_table = conn.execute(text("show columns in locations;")) 
            columns = [i[0] for i in column_table] 
        return columns, rows


