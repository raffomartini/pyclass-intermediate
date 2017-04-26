''' sqldict.py
dict-like, backed by a SQLite database.
- persistency
- concurrency
- sheareably with other languages
- instrospectable
'''

from collections import MutableMapping
import sqlite3, json

class SqlDict(MutableMapping):
    'dict-like, backed by an SQLite database.'
    # Dict
    # ==========
    # key   text    <-- unique index
    # value text

    # Values will be stored in JASON-format

    def __init__(self, dbname, *args, **kwargs):
        self.dbname = dbname
        # opens a connection to the DB
        self.connection = sqlite3.connect(dbname)
        c = self.connection.cursor()
        try:
            c.execute('CREATE TABLE Dict (key text, value text)')
            c.execute('CREATE UNIQUE INDEX KeyIndex ON Dict (key)')
        except sqlite3.OperationalError:
            pass #table already exsist
        self.update(*args, **kwargs)

    def __repr__(self):
        return '{}({!r}, {!r})'.format(type(self).__name__, self.dbname,self.items())

    def __getitem__(self, key):
        c = self.connection.cursor()
        c.execute('SELECT value FROM Dict WHERE key=?', (key,))
        # run a query on the DB
        # the '?' keyword is going to sanitize the inputs, requires a tuple as a second argument
        row = c.fetchone()
        # fetch one row
        if row is None:
            raise KeyError(key)
        # extracting from json
        return json.loads(row[0])

    def __delitem__(self, key):
        if key not in self:
            raise KeyError(key)
        c = self.connection.cursor()
        c.execute('DELETE FROM Dict WHERE key=?', (key,))
        self.connection.commit()

    def __setitem__(self,key, value):
        # I will store in json format
        value = json.dumps(value)
        if key in self:     # LBYL creates a race condition
            del self[key]   # TODO: use a transaction
        c = self.connection.cursor()
        c.execute('INSERT INTO Dict VALUES (?, ?)', (key, value))
        self.connection.commit()

    def __len__(self):
        c = self.connection.cursor()
        c.execute('SELECT count(key) FROM Dict')
        row = c.fetchone()
        return row[0]

    def __iter__(self):
        c = self.connection.cursor()
        c.execute('SELECT key FROM Dict')
        rows = c.fetchall()
        # rows is a list of tuples with a single value
        keys = [key for (key,) in rows]
        # this upacks the tuple from
        return iter(keys)

if __name__ == '__main__':
    d = SqlDict('starwars.db')
    d['hero'] = 'Luke'
    d['villain'] = 'Darth Vader'
    print d

    del d['villain']
    d['hero'] = ('Rey', 'Finn')
    print d