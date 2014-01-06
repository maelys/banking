#!/usr/bin/env python

import sqlite3

class DatabaseManager:
    
    CREATE_TABLE = "CREATE TABLE IF NOT EXISTS boi (id integer PRIMARY KEY AUTOINCREMENT, amount float, time_stamp text);"

    INSERT_QUERY = "INSERT INTO boi (amount, time_stamp) VALUES (?, ?);"

    conn = ''
    c= ''

    def connect(self):
        self.conn = sqlite3.connect('banking.sqlite')
        self.c = self.conn.cursor()
        # Create table
        self.c.execute(self.CREATE_TABLE)
        self.conn.commit()

    def insert(self,a,ts):
        self.c.execute(self.INSERT_QUERY, (a,ts))
        self.conn.commit()

    def sum(self):
        self.c.execute('SELECT SUM(amount) FROM boi')
        s = self.c.fetchone()
        return s

    def print_db(self):
        # Select all
        self.c.execute('SELECT* FROM boi')
        for row in self.c:
            print row

    def close(self):
        # Close the cursor
        self.conn.close()
