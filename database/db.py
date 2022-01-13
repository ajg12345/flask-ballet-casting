from sqlalchemy import create_engine, text


class localdb():
    def __init__(self):
        self.engine = None
        try:
            self.engine = create_engine('mysql+pymysql://root:root@localhost:3307/flaskballetcasting')
            self.engine.connect() 
        except Exception as e: 
            print('not running in local development environment, so using other server name')
            self.engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/flaskballetcasting')

    def get_locations(self) -> tuple:
        """
        Get data from the locations table, the column names and the rows in a tuple of 2 lists
        """
        with self.engine.connect() as conn:
            rows = conn.execute(text("select * from locations;")) 
            column_table = conn.execute(text("show columns in locations;")) 
            columns = [i[0] for i in column_table] 
        return columns, rows


