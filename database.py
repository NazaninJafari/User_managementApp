import sqlite3

con = sqlite3.connect('users_database.db')
my_cursor = con.cursor()

def getAll():
    my_cursor.execute("SELECT * FROM user")
    result = my_cursor.fetchall()
    return result

def add(name ,family ,icode, date):
    my_cursor.execute(f'INSERT INTO user(Name, Family, Identitycode, Birthday) VALUES("{name}", "{family}", "{icode}", "{date}")')
    con.commit()     

#for change info and update
def update_info(icode,name,family,date):
    my_cursor.execute(f'UPDATE user SET Name= "{name}", Family= "{family}", Identitycode= {icode}, Birthday= "{date}" WHERE Identitycode= {icode}')
    con.commit()

