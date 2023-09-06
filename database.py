import psycopg2
import datetime


class Database:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        self.cur = self.conn.cursor

    def get_user(self, _id):
        with self.cur() as cur:
            cur.execute("SELECT * FROM users WHERE telegram_id = %s", (_id,))
            return cur.fetchone()

    def get_timetable(self, _id, day=datetime.date.today().weekday()):
        with self.cur() as cur:
            user = self.get_user(_id)
            if len(user):
                cur.execute(
                    "SELECT * FROM lessons WHERE (group_id=%s OR group_id=%s "
                    "OR group_id IS NULL) AND day=%s ORDER BY order_id",
                    (user[2], user[3], day)
                )
                return cur.fetchall()

    def get_tomorrow(self, _id):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        return self.get_timetable(_id, tomorrow.weekday())

    def get_subject(self, sub_id):
        with self.cur() as cur:
            cur.execute("SELECT id, name, url FROM subjects WHERE id=%s", (sub_id,))
            return cur.fetchone()
