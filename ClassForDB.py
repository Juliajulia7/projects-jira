from contextlib import closing

import pymysql
from pymysql.cursors import DictCursor
from pymysql import Error

# conn = pymysql.connect(host='localhost',
#                        database='python_mysql',
#                        user='root',
#                        password='secret')

class ClassForDB(object):
    def __init__(self, host, database, user,  password):  # добавить login, pass
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def insertfordb(self, userId):
        with closing(pymysql.connect(self.host,
                                     self.user,
                                     self.password,
                                     self.database,
                                     charset='utf8mb4',
                                     cursorclass=DictCursor)) as connection:
            with connection.cursor() as cursor:
                query = "INSERT INTO users value (" + userId + ");"   #нужна таблица

                cursor.execute(query)
                connection.commit()

    def selectfordb(self, userId):
        with closing(pymysql.connect(self.host,
                                     self.user,
                                     self.password,
                                     self.database,
                                     charset='utf8mb4',
                                     cursorclass=DictCursor)) as connection:
            with connection.cursor() as cursor:
                query = "SELECT COUNT(USERID) as count FROM PYSHA.USERS WHERE USERID = (" + userId + ");"
                cursor.execute(query)
                for row in cursor:
                    if(row['count']==0):
                        return False
                    else:
                        return True
