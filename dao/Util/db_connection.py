import pyodbc
class DBConnutil:
    @staticmethod
    def get_connectionOBJ(con_string):
        connectionstring=(f"Driver={con_string['Driver']};" 
              f"Server={con_string["server_name"]};"
    f"Database={con_string["database_name"]};"
    f"Trusted_Connection=Yes;")
        connection=pyodbc.connect(connectionstring)
        print("connections success")

        return connection
        # conn=pyodbc.connect();

