import pyodbc

class DBUtil:
    @staticmethod
    def get_db_conn():
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=DESKTOP-NQM93MA\\SQLEXPRESS;'
                                  'Database=LOAN;'
                                  'Trusted_Connection=yes;')
            return conn
        except pyodbc.Error as ex:
            print(f"Error: {ex}")