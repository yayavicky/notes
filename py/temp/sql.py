# https://dev.mysql.com/doc/connector-j/5.1/en/connector-j-versions.html
# https://github.com/mkleehammer/pyodbc/wiki
# pip install pyodbc

import pyodbc 

class SqlSummary:
    def __init__(self,device_id, status, start_date, end_date, scene_type, operator) -> None:
        self.DeviceID = device_id
        self.Status = status
        self.StartDate = start_date
        self.EndDate = end_date
        self.SceneType = scene_type
        self.OperatorUser = operator
class EpdsMysqlOdbc(object):

    def __init__(self, driver="{MySQL ODBC 5.1 Driver}", 
    # {MySQL ODBC 5.1 Driver}
                user="root", pwd="@epds", 
                server="127.0.0.1", port="3306",
                database="jxfactory",charset="utf8mb4") -> None:
        super().__init__()
        driver = "ODBC Driver 17 for SQL Server"
        self._connect_str = (
            f'DRIVER={driver};'
            f'SERVER={server};'
            f'UID={user};'
            f'PWD={pwd};'
            f'PORT={port};'
            f'DATABASE={database};'
        )
        # f'charset={charset};'
        print(self._connect_str)
        
                
    
    def insert_summary_row(self, data:SqlSummary):
        cnxn = pyodbc.connect('DSN=sqlInhe;PWD=@epds')
        # cnxn = pyodbc.connect(self._connect_str)
        cursor = cnxn.cursor()
        insert_str = (
            "INSERT INTO meteroutfactory "
            " (DeviceID, Status, StartDate, EndDate, SceneType, OperatorUser) "
            " VALUES "
            f"('{data.DeviceID}', '{data.Status}', {data.StartDate}, {data.EndDate}, '{data.SceneType}', '{data.OperatorUser}')"
        )   
        cursor.execute(insert_str) 
        cnxn.commit()
        cursor.close() 
        cnxn.close()


if __name__ == "__main__":
    odbc = EpdsMysqlOdbc()
    data = SqlSummary(device_id="255",
                      status="S", 
                      start_date="2021-07-22 12:00:00",
                      end_date="2021-07-22 12:00:01",scene_type="23",operator="oper123")
    odbc.insert_summary_row(data)
    # print(pyodbc.drivers())



