import sqlite3

class StickyDB:
    def __init__(self, db_name="StickyLog.db"):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as con:
            con.execute("""CREATE TABLE IF NOT EXISTS sticky (
                            Window TEXT PRIMARY KEY,
                            StickyContent TEXT
                        );""")

    def save(self, window_name, text):
        with sqlite3.connect(self.db_name) as con:
            con.execute("INSERT OR REPLACE INTO sticky (Window, StickyContent) VALUES (?, ?)", (window_name, text))

    def read(self, window_name):
        with sqlite3.connect(self.db_name) as con:
            cursor = con.execute("SELECT StickyContent FROM sticky WHERE Window = ?", (window_name,))
            result = cursor.fetchone()
            return result[0] if result else None


