import sqlite3


class Sql:
    def __init__(self, list_bases):
        self.list_bases = list_bases

    def get_users_id(self):
        list_id = []

        for db in self.list_bases:
            conn = sqlite3.connect(db)
            c = conn.cursor()

            for id in c.execute("SELECT id FROM id"):
                list_id.append(id[0])

        return list_id


sql = Sql(['id.db'])
print(sql.get_users_id())