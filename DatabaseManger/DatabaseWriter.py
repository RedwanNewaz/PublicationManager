from .CoreSql import CoreSql

class DatabaseWriter(CoreSql):
    def __init__(self, name, fields, table = 'kavrakilab'):
        self.table = table
        self.scope = fields
        super().__init__(name)
        sql_create = 'CREATE TABLE IF NOT EXISTS {}({})'.format(table, self.fields)
        # print(sql_create)
        self.set(sql_create)
        self.__log = 'database initialized'
    def write(self, data):
        columns = ', '.join(data.keys())
        placeholders = ':' + ', :'.join(data.keys())
        sql = 'INSERT INTO %s (%s) VALUES (%s)' % ( self.table, columns, placeholders)
        self.c.execute(sql, data)
        # self.__log = "NEW DATA ADDED"

    @property
    def fields(self):
        rules = {'cite': 'TEXT PRIMARY KEY', 'type': 'TEXT NOT NULL'}
        param = [rules.get(item, 'TEXT') for item in self.scope ]
        sqlFieldArray = [ " ".join([s, p]) for s, p in zip(self.scope, param)]
        return ", ".join(sqlFieldArray)

    def get_header(self):
        return self.head(self.table)
