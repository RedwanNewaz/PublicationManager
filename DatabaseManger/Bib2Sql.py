from pybtex.database.input import bibtex
from .DatabaseWriter import DatabaseWriter

class obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, obj(b) if isinstance(b, dict) else b)

    def __call__(self, *args, **kwargs):
        #update the value of attributes
        self.cite, self.type, entries = args
        for item in entries:
            key = item.lower()
            setattr(self, key, entries[item])
        return self

def read_bibfile(file):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(file)
    return bib_data.entries

def get_columns(filename):
    entries = read_bibfile(filename)
    column = []
    for e in entries:
        keys = [k for k in entries[e].fields]
        for item in keys:
            candidate = item.lower()
            if(not candidate in column):
                column.append(candidate)
    return column

def make_sql_database(input, output):
    entries = read_bibfile(input)
    columns = ["cite", "type"]
    columns.extend(get_columns(input))
    sqlObj = obj({c : "" for c in columns})
    with DatabaseWriter(output, columns) as db:
        for e in entries:
            eObj = sqlObj(e, entries[e].type, entries[e].fields)
            db.write(vars(eObj))

