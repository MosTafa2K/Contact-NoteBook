import sqlite3
from tkinter.constants import END


def convert(txt_desc):
    lst = []
    lst.append(str(txt_desc.get(1.0, END)).strip())
    return lst[0]


def connect():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    sql_command = '''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            contact_id INTEGER,
            name VARCHAR (60),
            family VARCHAR (60),
            email VARCHAR (60),
            phone INTEGER,
            fax INTEGER,
            addrress text,
            fact_phone INTEGER,
            home_phone INTEGER,
            work_phone INTEGER,
            description text
        );
    '''
    cursor.execute(sql_command)
    database.commit()
    database.close()


def insert(contact_id, name, family, email, phone, fax="", addr="", fact_phone="", home_phone="", work_phone="", desc=""):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    if len(contact_id) == 0 or\
            len(name) == 0 or\
            len(family) == 0 or\
            len(email) == 0 or\
            len(phone) == 0:
        raise ValueError(
            '{Id} or {Name} or {Family} or {Email} or {phone} can not be empty..!')
    else:
        sql_command = """
            INSERT INTO contacts VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        if len(fax) != 0 or len(addr) != 0 or len(fact_phone) != 0 or len(home_phone) != 0\
                or len(work_phone) != 0 or len(desc) != 0:
            cursor.execute(sql_command, (contact_id, name, family, email,
                                         phone, fax, addr, fact_phone, home_phone, work_phone, desc))
            database.commit()
            database.close()
            print('Done.')
        else:
            sql_command = """
            INSERT INTO contacts VALUES (NULL, ?, ?, ?, ?, ?)
            """
            cursor.execute(
                sql_command, (contact_id, name, family, email, phone))
            database.commit()
            database.close()
            print('Done.')


def view():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(contact_id="", name="", family="", phone=""):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE contact_id=? OR name=? OR family=? OR phone=?",
                (contact_id, name, family, phone))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(contact_id):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()


def update(contact_id, name, family, email, phone, fax, addr, fact_phone, home_phone, work_phone, desc):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET\
        name=?,\
        family=?,\
        email=?,\
        phone=?,\
        fax=?,\
        addrress=?,\
        fact_phone=?,\
        home_phone=?,\
        work_phone=?,\
        description=? WHERE contact_id=?",
                (name, family, email, phone, fax, addr, fact_phone, home_phone, work_phone, desc, contact_id))
    conn.commit()
    conn.close()


# contact_id INTEGER,
# name VARCHAR(60),
# family VARCHAR(60),
# email VARCHAR(60),
# phone INTEGER,
# fax INTEGER,
# addrress text,
# fact_phone INTEGER,
# home_phone INTEGER,
# work_phone INTEGER,
# description text
