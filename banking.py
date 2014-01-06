#!/usr/bin/env python

import db_manager
import sqlite3

def main():
    db = db_manager.DatabaseManager()
    db.connect()
    db.insert(3000.0, "10/03/2013")
    db.insert(-10.0, "11/03/2013")
    db.print_db()
    sum = db.sum()
    print sum
    db.close()

if __name__ == "__main__":
    main()
