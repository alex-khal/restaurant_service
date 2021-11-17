from config import config
import psycopg2

class DB_singelton:
    """
    This class represents a singelton DB for the app.
    """
    __instance = None

    @staticmethod
    def create_DB():
        if DB_singelton.__instance == None:
            DB_singelton()
        return DB_singelton.__instance

    def __init__(self):
        if DB_singelton.__instance != None:
            raise Exception("There already exists one instance of this class")
        else:
            DB_singelton.__instance = self
            self.create_table()

    def create_table(self):
        """
        this method creates a new table of dishes
        :return:
        """
        command = """
                    CREATE TABLE dishes
                    (
                    category_id int,
                    category_name varchar(100),
                    dish_id int,
                    dish_name varchar(100),
                    dish_description varchar(250),
                    dish_price int
                    )
                    """

        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(command)
            cur.close()
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
