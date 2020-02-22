import sqlite3

class CoreSql(object):
    def __init__(self, name):
        self.name = name
        try:
            self.conn = sqlite3.connect(self.name, check_same_thread=False)
            self.conn.text_factory = lambda b: b.decode(errors='ignore')
            self.c = self.conn.cursor()
        except sqlite3.Error as e:
            print("Error connecting to database! ", e)

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.commit()
            self.c.close()
            self.conn.close()
    def get(self, sql_syntex, index = False):
        self.c.row_factory = None
        self.c.execute(sql_syntex)
        val = self.c.fetchall()
        for row in val:
            for v in row:
                yield v
                if(index):break
    def set(self, sql_syntex):
        self.c.execute(sql_syntex)

    def head(self, table):
        header_query = "SELECT * FROM %s" % table
        self.c.execute(header_query)
        header = [description[0] for description in self.c.description]
        return header





