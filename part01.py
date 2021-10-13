import psycopg2
import sqlalchemy

class connection:
    def __init__(self):
        self.connect=psycopg2.connect(
            user="postgres",
            password="sumit",
            database="test",
            port="5432"
        )
        self.cursor=self.connect.cursor()
        self.engine=sqlalchemy.create_engine("postgresql://postgrey:sumit@localhost:5432/test")
    def disconnect(self):
        self.cursor.close()
        self.connect.close()
        self.engine.dispose()

database =connection()